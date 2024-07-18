/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

var createCounter = function(init) {
    var counter = init;
    var increment = function(){
        return ++counter;
    }
    var decrement = function(){

        return --counter;
    }
    var reset = function(){
        return counter = init;
    }
    return {increment, decrement, reset}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */