/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    called = 0
    return function(...args){
        if (called) return
        called = 1
        return fn(...args)
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
