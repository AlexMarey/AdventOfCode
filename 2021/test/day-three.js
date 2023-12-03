const { partOne , partTwo, transpose, removeMatrixCol, getOxygenRating, getScrubberRating } = require('../3/binary-diagnostic');
const assert = require('assert');
const { it } = require('mocha');

const input = ['00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
];

describe('Day Three', function() {
    it('transpose should transpose NxM matrix', () => {
        let matrix = [
            ['1', '1', '1', '1'],
            ['2', '2', '2', '2'],
            ['3', '3', '3', '3'],
        ];
        let expectedResult = [
            ['1', '2', '3'],
            ['1', '2', '3'],
            ['1', '2', '3'],
            ['1', '2', '3'],
        ]

        let result = transpose(matrix);

        assert.equal(result.length, expectedResult.length);
        assert.equal(result[0].length, expectedResult[0].length);
        assert.equal(result[0][0], expectedResult[0][0]);
        assert.equal(result[0][1], expectedResult[0][1]);
        assert.equal(result[0][2], expectedResult[0][2]);

        assert.equal(result[1].length, expectedResult[1].length);
        assert.equal(result[1][0], expectedResult[1][0]);
        assert.equal(result[1][1], expectedResult[1][1]);
        assert.equal(result[1][2], expectedResult[1][2]);

        assert.equal(result[2].length, expectedResult[2].length);
        assert.equal(result[2][0], expectedResult[2][0]);
        assert.equal(result[2][1], expectedResult[2][1]);
        assert.equal(result[2][2], expectedResult[2][2]);
    });

    it('part one should be 198 ', () => {
        let parsedInput = input.map((line) => line.split(''));
        assert.equal(partOne(parsedInput), 198);
    });

    it('removeMatrixCol should remove 2nd column given index 1', () => {
        let input = [
            ['1','0','1'],
            ['0','1','1'],
        ];
        let expectedResult = [
            ['1','1'],
            ['0','1'],
        ];

        let result = removeMatrixCol(input, 1);

        assert.equal(result.length, expectedResult.length);
        assert.equal(result[0].length, expectedResult[0].length);
        assert.equal(result[0][0], expectedResult[0][0]);
        assert.equal(result[0][1], expectedResult[0][1]);
        assert.equal(result[1].length, expectedResult[1].length);
        assert.equal(result[1][0], expectedResult[1][0]);
        assert.equal(result[1][1], expectedResult[1][1]);
    });

    it('getOxygenRating should return 23 (10111)', () => {
        let parsedInput = input.map((line) => line.split(''));
        let expectedResult = 23;

        assert.equal(getOxygenRating(parsedInput), expectedResult);
    });

    it('getScrubber should return 10 (01010)', () => {
        let parsedInput = input.map((line) => line.split(''));
        let expectedResult = 10;

        assert.equal(getScrubberRating(parsedInput), expectedResult);
    });

    it('part two should be 230', () => {
        let parsedInput = input.map((line) => line.split(''));

        assert.equal(partTwo(parsedInput), 230);
    });
});