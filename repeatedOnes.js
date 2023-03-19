const numbers = [1, 2, 2, 5, 4, 6, 7, 8, 8, 8];
let maxNum = 0;
let counter = 0;
let mostRepeated = numbers[0];

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] === numbers[i - 1]) {
    counter += 1;
  } else {
    if (counter > maxNum) {
      maxNum = counter;
      mostRepeated = numbers[i - 1];
    }
    counter = 1;
  }
}
if (counter > maxNum) {
    maxNum = counter;
    mostRepeated = numbers[numbers.length - 1];
}

console.log(mostRepeated)
console.log(counter)
