const { partOne, partTwo} = require('../6/lanternfish');
const assert = require('assert');
const { it } = require('mocha');

const input = [3,4,3,1,2];

describe('Day Six', function() {
    it('part one should be 26 after 18 days', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partOne(testInput, 18), 26);
    });

    it('part one should be 5934 after 80 days', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partOne(testInput, 80), 5934);
    });

    it('part two should be 26984457539 after 256 days', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partTwo(testInput, 256), 26984457539);
    });
});