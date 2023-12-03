const { partOne, partTwo, isSlopeOneToOne, isSlopeNegtive } = require('../5/hydrothermal');
const assert = require('assert');
const { it } = require('mocha');

const input = [
    [0,9,5,9],
    [8,0,0,8],
    [9,4,3,4],
    [2,2,2,1],
    [7,0,7,4],
    [6,4,2,0],
    [0,9,2,9],
    [3,4,1,4],
    [0,0,8,8],
    [5,5,8,2],
];

describe('Day Four', function() {
    it('part one should be 5', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partOne(testInput), 5);
    });

    it('part two should be 12', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partTwo(testInput), 12);
    });

    it('isSlopeOneToOne should be True when given 9,7 and 7,9', () => {
        assert(isSlopeOneToOne(9, 7, 7, 9));
    });

    it('isSlopeOneToOne should be False when given 9,8 and 7,9', () => {
        assert.equal(isSlopeOneToOne(9, 8, 7, 9), false);
    });

    it('isSlopeNegative should be True when given 8,0 and 0,8', () => {
        assert(isSlopeNegtive(8, 0, 0, 8));
    });

    it('isSlopeNegative should be False when given 0,0 and 8,8', () => {
        assert.equal(isSlopeNegtive(0, 0, 8, 8), false);
    });

});