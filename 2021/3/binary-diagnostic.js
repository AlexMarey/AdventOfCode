function partOne(input) {
    let tranMatrix = transpose(input);
    let gamma = '';
    let epsilon ='';
    
    for(let row of tranMatrix) {
        let oneCount = 0;
        let zeroCount = 0;

        for(let bit of row) {
            if (bit == '1') {
                oneCount++;
            } else if (bit =='0') {
                zeroCount++;
            }
        }

        if (oneCount > zeroCount) {
            gamma += '1';
            epsilon += '0';
        } else if (zeroCount > oneCount) {
            gamma += '0';
            epsilon += '1';
        }
    }
    gamma = parseInt(gamma, 2);
    epsilon = parseInt(epsilon, 2);

    return gamma * epsilon;
}

function partTwo(input) {
    let oxygenInput = input;
    let scrubInput = [...input];
    let oxygenRating = getOxygenRating(oxygenInput);
    let scrubRating = getScrubberRating(scrubInput);
    return oxygenRating * scrubRating;
}

function transpose(matrix) {
    let rows = matrix.length;
    let cols = matrix[0].length;
    let transposedMatrix = [];

    for(let i=0; i<cols; i++) {
        transposedMatrix[i] = Array(rows); 
    }

    for(let i=0; i<rows;i++) {
        for(let j=0; j<cols;j++) {
            transposedMatrix[j][i] = matrix[i][j];
        }
    }

    return transposedMatrix;
}

function getOxygenRating(matrix) {
    let col = 0;
    
    while(matrix.length != 1) {
        let oneCount = 0;
        let zeroCount = 0;
        let removalBit = '-1';

        for(let row of matrix) {            
            if(row[col]=='1'){
                oneCount++;
            } else if(row[col]=='0'){
                zeroCount++;
            }
        }

        if (oneCount >= zeroCount) {
            removalBit = '0';
        } else if (oneCount < zeroCount) {
            removalBit = '1';
        } 

        // Remove the rows
        let toRemoveIndexes = [];
        for(let row of matrix){
            if (row[col] == removalBit){
                let i = matrix.indexOf(row);
                if(i !== -1) {
                    toRemoveIndexes.push(i);
                }
            }
        }

        toRemoveIndexes = toRemoveIndexes.reverse();

        for(let i=0; i<toRemoveIndexes.length; i++) {
            matrix.splice(toRemoveIndexes[i], 1);
        }
        
        col++;
    }
    let oxygenRating = matrix[0].join('');
    return parseInt(oxygenRating, 2);
}

function getScrubberRating(matrix) {
    let col = 0;
    
    while(matrix.length != 1) {
        let oneCount = 0;
        let zeroCount = 0;
        let removalBit = '-1';

        for(let row of matrix) {            
            if(row[col]=='1'){
                oneCount++;
            } else if(row[col]=='0'){
                zeroCount++;
            }
        }

        if (zeroCount <= oneCount ) {
            removalBit = '1';
        } else if ( zeroCount > oneCount ) {
            removalBit = '0';
        }

        // Remove the rows
        let toRemoveIndexes = [];
        for(let row of matrix){
            if (row[col] == removalBit){
                let i = matrix.indexOf(row);
                if(i !== -1) {
                    toRemoveIndexes.push(i);
                }
            }
        }
        toRemoveIndexes = toRemoveIndexes.reverse();
        for(let i=0; i<toRemoveIndexes.length; i++) {
            matrix.splice(toRemoveIndexes[i], 1);
        }
        col++;
    }
    let scrubberRating = matrix[0].join('');
    return parseInt(scrubberRating, 2);
}

function removeMatrixCol(matrix, colIndex) {
    let rows = matrix.length;
    for(let i=0; i<rows; i++){
        matrix[i].splice(colIndex, 1);
    }
    return matrix;
}


module.exports = {
    partOne,
    partTwo,
    transpose, 
    getOxygenRating,
    getScrubberRating,
    removeMatrixCol,
}