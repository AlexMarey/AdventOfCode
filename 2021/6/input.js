const path = require('path');
const fs = require('fs');
const { parse } = require('path');

const input = fs
	.readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
	.toString()
	.trim()
	.split('\n')[0]
	.split(',')
	.map(val => parseInt(val));
	
module.exports = {
	input,
};