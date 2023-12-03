const { calculate, calculateThrees } = require('../1/sum');
const assert = require('assert');

const input = [199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263];

describe('Day One', function() {
    it('part one should increase 7 times', () => {
        assert.equal(calculate(input), 7);
    });

    it('part two should increase 5 times', () => {
        assert.equal(calculateThrees(input), 5);
    });
});