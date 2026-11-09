
function isValidIPv4(ip) {
    const regex = /^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$/;
  
    return regex.test(ip);
  }
  
  // Przykłady testów
  const addresses = [
    '192.168.1.1',
    '8.8.8.8',
    '255.255.255.255',
    '0.0.0.0',
    '256.100.50.25',
    '192.168.1',
    '192.168.1.999',
    '192.168.01.1',
    'abc.def.ghi.jkl'
  ];
  
  addresses.forEach(ip => {
    console.log(`${ip}: ${isValidIPv4(ip)}`);
  });
  