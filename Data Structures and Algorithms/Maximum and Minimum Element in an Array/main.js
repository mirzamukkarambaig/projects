const myList = [5, 15, 50, 3, 67, 100];

// Initialize minimum and maximum to opposite extremes
minimum = Number.MAX_SAFE_INTEGER;
maximum = Number.MIN_SAFE_INTEGER;

for (const element of myList) {
  if (minimum > element) {
    minimum = element;
  }
  if (maximum < element) {
    maximum = element;
  }
}

console.log(`Maximum: ${maximum}, Minimum: ${minimum}`);  // Use backticks for string interpolation
