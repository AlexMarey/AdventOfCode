function calcHorizontalDepth(input) {
    horizontalDistance = 0;
    depth = 0;

    for(let {direction, amount} of input) {
        if(direction == "forward") {
            horizontalDistance += amount;
        } else if (direction == "down") {
            depth += amount;
        } else if (direction == "up" ) {
            depth -= amount;
        }
    }

    return horizontalDistance * depth;
}

function calcHorizontalAim(input) {
    horizontalDistance = 0;
    depth = 0;
    aim = 0;

    for(let {direction, amount} of input) {
        if(direction == "forward") {
            horizontalDistance += amount;
            depth += amount * aim;
        } else if (direction == "down") {
            aim += amount;
        } else if (direction == "up" ) {
            aim -= amount;
        }
    }
    return horizontalDistance * depth;
}

module.exports = {
    calcHorizontalAim,
    calcHorizontalDepth
}