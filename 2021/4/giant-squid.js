const winningIndexes = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24],
    [0, 6, 12, 18, 24],
    [4, 6, 12, 16, 20],
]

function partOne(input) {
    let isWinner = false;
    let pullOrder = input.pullOrder;
    let boards = input.boards;
    let answer;
    let index = 0;

    let selectedIndexOnBoards = Array(boards.length);
    for(let i=0; i<selectedIndexOnBoards.length; i++) {
        selectedIndexOnBoards[i] = Array();
    }

    while(!isWinner) {
        let currentNumber = pullOrder[index];
        for(let board of boards) {
            if(board.includes(currentNumber)) {
                let boardIndex = boards.indexOf(board);
                let numIndex = board.indexOf(currentNumber);
                
                selectedIndexOnBoards[boardIndex].push(numIndex);
                
                if(isWinningBoard(selectedIndexOnBoards[boardIndex]))
                {
                    answer = getWinningProduct(board, selectedIndexOnBoards[boardIndex]) * currentNumber;
                    isWinner = true;
                }
            }
        }
        index++;
    }
    return answer;
}

function partTwo(input) {
    let isLastBoard = false;
    let pullOrder = input.pullOrder;
    let boards = input.boards;
    let answer;
    let index = 0;

    let selectedIndexOnBoards = Array(boards.length);
    for(let i=0; i<selectedIndexOnBoards.length; i++) {
        selectedIndexOnBoards[i] = Array();
    }

    while(!isLastBoard) {
        let currentNumber = pullOrder[index];
        for(let i=0; i<boards.length; i++) {
            if(boards[i].includes(currentNumber)) {
                let boardIndex = boards.indexOf(boards[i]);
                let numIndex = boards[i].indexOf(currentNumber);
                
                selectedIndexOnBoards[boardIndex].push(numIndex);
                let isWinner = isWinningBoard(selectedIndexOnBoards[boardIndex]);
                if(isWinner)
                {
                    if(boards.length == 1){
                        answer = getWinningProduct(boards[i], selectedIndexOnBoards[boardIndex]) * currentNumber;
                        isLastBoard = true;
                    } else {
                        boards.splice(boardIndex,1);
                        selectedIndexOnBoards.splice(boardIndex,1);
                        i--;
                    }
                }
            }
        }
        index++;
    }
    return answer;
}

function isWinningBoard(selectedIndexes){
    for( let indexes of winningIndexes) {
        if( indexes.every(val => selectedIndexes.includes(val)) ) {
            return true;
        }
    }
    return false;
}

function getWinningProduct(board, selectedIndexes) {
    let product = 0;
    selectedIndexes.sort((a,b) => (a-b)).reverse();

    for(let index of selectedIndexes) {
        board.splice(index, 1);
    }

    for(let num of board) {
        product += num;
    }

    return product;
    
}

function getIndexBoards(length){
    let selectedIndexOnBoards = Array(length);
    for(let i=0; i<length; i++) {
        selectedIndexOnBoards[i] = Array();
    }
    return selectedIndexOnBoards;
}

module.exports = {
    partOne,
    partTwo,
    isWinningBoard,
    getWinningProduct,
    getIndexBoards,
}