const { input } = require('./input');
const { partOne, partTwo } = require('./hydrothermal');

let partOneInput = JSON.parse(JSON.stringify(input));
let partTwoInput = JSON.parse(JSON.stringify(input));

console.log(`Part One: ${partOne(partOneInput)}`);
console.log(`Part Two: ${partTwo(partTwoInput)}`);