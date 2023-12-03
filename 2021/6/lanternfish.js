function partOne(input, timePeriod) {
    for(let i=0; i<timePeriod; i++) {
        let toAddCounter = 0;
        for(let index in input) {
            if(input[index] == 0) {
                input[index] = 6;
                toAddCounter++;
            } else {
                input[index]--;
            }
        }
        while(toAddCounter > 0) {
            input.push(8);
            toAddCounter--;
        }
    }
    return input.length;
}

function partTwo(input, timePeriod) {
    let fishTotals = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    for(let value of input) {
        fishTotals[value]++; 
    }

    while(timePeriod > 0) {
        let newFish = 0;

        for(let i=0;i<fishTotals.length; i++) {
            // console.log(i);
            if(i==0) {
                newFish = fishTotals[i];
                fishTotals[i] = fishTotals[i+1];
            } else if( i == 8 ) {
                fishTotals[i] = newFish;
            } else if( i == 6 ) {
                fishTotals[i] = fishTotals[i+1] + newFish;
            } else {
                fishTotals[i] = fishTotals[i+1];
            }

        }
        timePeriod--;
        // console.log(`Day ${256 - timePeriod}: ${fishTotals}`);
    }

    // Get the totals
    let total = 0;
    for(let value of fishTotals) {
        total += value;
    }
    return total;
}

module.exports = {
    partOne,
    partTwo,
}