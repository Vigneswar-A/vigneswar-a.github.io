/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    if (n === 0) return arr
    let res = [];
    for (const subarr of arr)
        if (Array.isArray(subarr)) res.push(...flat(subarr, n-1))
        else res.push(subarr)

    return res
};