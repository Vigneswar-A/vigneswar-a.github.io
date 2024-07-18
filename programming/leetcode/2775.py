/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    var x = 0
    var y = 1
    yield x
    yield y
    while (1){
        const temp = y
        y = x+y
        yield y
        x = temp
        
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */