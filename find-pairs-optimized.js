
function findPairs(arr, targetSum) {
    const pairs = [];
    const seen = new Map();
  
    for (const num of arr) {
      const complement = targetSum - num;
  
      const count = seen.get(complement) || 0;
  
      for (let i = 0; i < count; i++) {
        pairs.push([complement, num]);
      }
  
      seen.set(num, (seen.get(num) || 0) + 1);
    }
  
    return pairs;
  }
  
  // Przykład użycia
  const numbers = [2, 4, 3, 5, 7, 8];
  const targetSum = 10;
  
  console.log(findPairs(numbers, targetSum));
  