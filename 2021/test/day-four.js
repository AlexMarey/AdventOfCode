const { partOne, partTwo, isWinningBoard, getWinningProduct, getIndexBoards } = require('../4/giant-squid');
const assert = require('assert');
const { it } = require('mocha');

const input = {
    pullOrder: [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1],
    boards: [
        [22,13,17,11,0,8,2,23,4,24,21,9,14,16,7,6,10,3,18,5,1,12,20,15,19],
        [3,15,0,2,22,9,18,13,17,5,19,8,7,25,23,20,11,10,24,4,14,21,16,12,6],
        [14,21,17,24,4,10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7]
    ]
};

describe('Day Four', function() {
    it('part one should be 4512', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partOne(testInput), 4512);
    });

    it('getWinningMultiplier should return -1 when no winner is found', () => {
        let pulledIndexes = [1, 3, 9];

        let result = isWinningBoard(pulledIndexes);

        assert.equal(result, false);
    });

    it('isWinningBoard should return true when a winning row is found', () => {
        let pulledIndexes = [0, 3, 6, 10, 12, 18, 22, 24];

        let result = isWinningBoard(pulledIndexes);

        assert.equal(result, true);
    });

    it('getWinningPorduct should return 15', () => {
        let board = Array(25);
        board.fill(1,0,25);
        let selectedNums = [3,5,9,12,14,20,4,2,17,22];

        let result = getWinningProduct(board, selectedNums);

        assert.equal(result, 15);
    });

    it('part two should be 1924', () => {
        let testInput = JSON.parse(JSON.stringify(input));
        assert.equal(partTwo(testInput), 1924);
    });

    // it('getIndexBoards should return 2D array of length 3', () => {

    //     let result = getIndexBoards(input.boards.length);

    //     assert.equal(result.length, 3);
    //     assert(Array.isArray(result[0]));
    //     assert(Array.isArray(result[1]));
    //     assert(Array.isArray(result[2]));
    // });
});