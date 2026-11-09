
import os
import sys
import argparse
import requests
from urllib.parse import quote

JENKINS_URL = os.getenv("JENKINS_URL", "http://localhost:8080").rstrip("/")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")

session = requests.Session()

if JENKINS_USER and JENKINS_TOKEN:
    session.auth = (JENKINS_USER, JENKINS_TOKEN)


def api_request(method, endpoint, **kwargs):
    url = f"{JENKINS_URL}/{endpoint.lstrip('/')}"

    try:
        response = session.request(
            method,
            url,
            timeout=15,
            **kwargs
        )
        response.raise_for_status()
        return response

    except requests.exceptions.HTTPError as error:
        print(f"Blad HTTP: {error}")
    except requests.exceptions.ConnectionError:
        print("Nie mozna polaczyc sie z serwerem Jenkins.")
    except requests.exceptions.Timeout:
        print("Przekroczono czas oczekiwania na odpowiedz.")
    except requests.exceptions.RequestException as error:
        print(f"Blad zapytania: {error}")

    return None


def get_jobs():
    response = api_request("GET", "api/json?tree=jobs[name,color]")

    if response is None:
        return

    jobs = response.json().get("jobs", [])

    if not jobs:
        print("Brak zadan Jenkins.")
        return

    print("Lista zadan Jenkins:")

    for job in jobs:
        print(f"- {job['name']} (status: {job.get('color', 'unknown')})")


def get_last_build(job_name):
    encoded_name = quote(job_name, safe="")
    endpoint = (
        f"job/{encoded_name}/api/json"
        "?tree=name,lastBuild[number,result,building,url]"
    )

    response = api_request("GET", endpoint)

    if response is None:
        return

    job = response.json()
    last_build = job.get("lastBuild")

    if not last_build:
        print(f"Zadanie {job_name} nie ma jeszcze buildow.")
        return

    print(f"Zadanie: {job_name}")
    print(f"Numer buildu: {last_build.get('number')}")
    print(f"Wynik: {last_build.get('result') or 'W TRAKCIE'}")
    print(f"Czy trwa: {last_build.get('building')}")
    print(f"URL: {last_build.get('url')}")


def run_job(job_name):
    encoded_name = quote(job_name, safe="")
    endpoint = f"job/{encoded_name}/build"

    response = api_request("POST", endpoint)

    if response is not None:
        print(f"Zlecono uruchomienie zadania: {job_name}")


def main():
    parser = argparse.ArgumentParser(
        description="Prosty manager zadan Jenkins"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    subparsers.add_parser("list", help="Lista zadan")

    status_parser = subparsers.add_parser(
        "status",
        help="Status ostatniego buildu"
    )
    status_parser.add_argument("job_name")

    run_parser = subparsers.add_parser(
        "run",
        help="Uruchom zadanie"
    )
    run_parser.add_argument("job_name")

    args = parser.parse_args()

    if not JENKINS_USER or not JENKINS_TOKEN:
        print("Brak JENKINS_USER lub JENKINS_TOKEN.")
        sys.exit(1)

    if args.command == "list":
        get_jobs()
    elif args.command == "status":
        get_last_build(args.job_name)
    elif args.command == "run":
        run_job(args.job_name)


if __name__ == "__main__":
    main()
