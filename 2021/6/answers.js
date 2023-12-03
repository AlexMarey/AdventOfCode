const { input } = require('./input');
const { partOne, partTwo } = require('./lanternfish');

let partOneInput = JSON.parse(JSON.stringify(input));
let partTwoInput = JSON.parse(JSON.stringify(input));

console.log(`Part One: ${partOne(partOneInput, 80)}`);
console.log(`Part Two: ${partTwo(partTwoInput, 256)}`);