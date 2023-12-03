const { calcHorizontalDepth, calcHorizontalAim } = require('../2/dive');
const assert = require('assert');

const input = [
    {direction: 'forward', amount: 5},
    {direction: 'down', amount: 5},
    {direction: 'forward', amount: 8},
    {direction: 'up', amount: 3},
    {direction: 'down', amount: 8},
    {direction: 'forward', amount: 2},
];

describe('Day Two', function() {
    it('part one horizontal and depth is 150', () => {
        assert.equal(calcHorizontalDepth(input), 150);
    });

    it('part two horiontal and depth with aim is 900', () => {
        assert.equal(calcHorizontalAim(input), 900);
    });
});