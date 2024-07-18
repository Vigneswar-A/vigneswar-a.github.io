/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const res = {}
    for(const obj of this){
        const k = fn(obj)
        if(!(k in res))
            res[k] = []
        res[k].push(obj)
    }
    return res
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */