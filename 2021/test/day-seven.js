const { partOne, partTwo} = require('../7/crabattack');
const assert = require('assert');
const { it } = require('mocha');

const input = [16,1,2,0,4,2,7,1,2,14];

describe('Day Six', function() {
    it('part one should be ', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partOne(testInput), 26);
    });

    it('part one should be 5934 after 80 days', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partTwo(testInput), 5934);
    });
});