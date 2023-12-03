const path = require('path');
const fs = require('fs');
const { parse } = require('path');

let isFirstLine = true;
let pullOrder = [];
let boards = [];
let setupBoard = [];

let file = fs
	.readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
	.toString()
	.trim()
	.split('\n');

for(let line of file) {
	if(isFirstLine) {
		pullOrder = line.split(',').map((digit) => parseInt(digit, 10));
		isFirstLine = false;
	} else {
		let newLine = line.replace("\r","").split(' ');
		for(let digit of newLine) {
			if(digit == '') {
				let index = newLine.indexOf(digit);
				newLine.splice(index,1);
			}
		}
		if (newLine.length == 1) {
			break;
		} else {
			setupBoard = setupBoard.concat(newLine);
			if(setupBoard.length == 25){
				setupBoard = setupBoard.map((val) => parseInt(val,10))
				boards.push(setupBoard);
				setupBoard = [];
			}
		}
	}
}

const input = {
	pullOrder,
	boards
}

module.exports = {
	input,
};