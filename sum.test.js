
const sum = require('./sum');

test('dodaje 2 + 3 i zwraca 5', () => {
  expect(sum(2, 3)).toBe(5);
});

test('dodaje dwie liczby ujemne', () => {
  expect(sum(-2, -3)).toBe(-5);
});

test('dodaje zero do liczby', () => {
  expect(sum(5, 0)).toBe(5);
});
