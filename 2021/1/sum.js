function calculate(input) {
    let count = 0;
    let isFirstInput = true;
    let previousInput = 0;
    
    for(let i of input) {
        if(!isFirstInput) {
            if (i > previousInput) {
                count++;
            }
            previousInput = i;
        } else {
            isFirstInput = false;
            previousInput = i;
        }
    }
    return count;    
}

function calculateThrees(input) {
    let isFirstInput = true;
    let previousSum = 0;
    let total = 0;

    for(let i=2; i<input.length; i++) {
        let currentSum = input[i] + input[i-1] + input[i-2];
        if(!isFirstInput) {
            if (currentSum > previousSum) {
                total++;
            }
        } else {
            isFirstInput = false;
        }
        previousSum = currentSum;
    }
    return total;
}

module.exports = {
    calculate,
    calculateThrees
}