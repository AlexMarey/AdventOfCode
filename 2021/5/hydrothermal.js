function partOne(input) {
    let pointCounter = {};
    for(let line of input) {
        let x0 = line[0];
        let y0 = line[1];
        let x1 = line[2];
        let y1 = line[3];

        if(x0 == x1 || y0 == y1) {
            // Create list of points
            let points = []
            let axisRange = []
            if(x0 == x1) {
                axisRange = y0 > y1 ? range(y0 - y1 + 1, y1) : range(y1 - y0 + 1, y0);
                points = axisRange.map(val => `(${x0},${val})`);
            }
            if(y0 == y1){
                axisRange = x0 > x1 ? range(x0 - x1 + 1, x1) : range(x1 - x0 + 1, x0);
                points = axisRange.map(val => `(${val},${y0})`);
            }
            // Increase count or add to dictionary
            for(let point of points) {
                if(pointCounter[point] == undefined ) {
                    pointCounter[point] = 1;
                } else {
                    pointCounter[point]++;
                }
            } 

        }
    }

    // return amount of keys with value 2
    return findValueCountAtAndAbove(pointCounter, 2);
}

function partTwo(input) {
    let pointCounter = {};
    for(let line of input) {
        let x0 = line[0];
        let y0 = line[1];
        let x1 = line[2];
        let y1 = line[3];
        let points = [];

        if(isSlopeOneToOne(x0, y0, x1, y1)) {
            let xRange = x0 > x1 ? range(x0 - x1 + 1, x1) : range(x1 - x0 + 1, x0);
            let yRange = y0 > y1 ? range(y0 - y1 + 1, y1) : range(y1 - y0 + 1, y0);
            if(isSlopeNegtive(x0,y0,x1,y1)) {
                yRange.reverse();
            }
            for(let i = 0; i<xRange.length; i++) {
                points.push(`(${xRange[i]},${yRange[i]})`)
            }
            // console.log(`1: (${x0}, ${y0}) 2: (${x1}, ${y1})`)
            // console.log(points);
        } else if(x0 == x1 || y0 == y1) {
            let axisRange = [];
            if(x0 == x1) {
                axisRange = y0 > y1 ? range(y0 - y1 + 1, y1) : range(y1 - y0 + 1, y0);
                points = axisRange.map(val => `(${x0},${val})`);
            }
            if(y0 == y1){
                axisRange = x0 > x1 ? range(x0 - x1 + 1, x1) : range(x1 - x0 + 1, x0);
                points = axisRange.map(val => `(${val},${y0})`);
            }
        }

        // Increase count or add to dictionary
        for(let point of points) {
            if(pointCounter[point] == undefined ) {
                pointCounter[point] = 1;
            } else {
                pointCounter[point]++;
            }
        } 
    }
    // return amount of keys with value 2
    return findValueCountAtAndAbove(pointCounter, 2);
}

function range(size, startAt = 0) {
    return [...Array(size).keys()].map(i => i + startAt);
}

function findValueCountAtAndAbove(obj, value) {
    let count = 0;
    for(let i in obj) {
        // console.log(`Obj Value: ${o}, Value: ${value}`)
        if(obj[i] >= value) {
            count++; 
        }
    }
    return count;
}

function isSlopeOneToOne(x0, y0, x1, y1) {
    xSlope = x1 - x0;
    ySlope = y1 - y0;

    return xSlope == ySlope || xSlope == -ySlope;
}

function isSlopeNegtive(x0, y0, x1, y1) {
    xSlope = x1 - x0;
    ySlope = y1 - y0;

    return xSlope == -ySlope;
}

module.exports = {
    partOne,
    partTwo,
    isSlopeOneToOne,
    isSlopeNegtive,
}