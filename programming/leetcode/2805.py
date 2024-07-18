/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.arr = nums
};

ArrayWrapper.prototype.valueOf = function() {
    var sum = 0;
    for(num of this.arr)
        sum += num
    return sum
}

ArrayWrapper.prototype.toString = function() {
    if(this.arr.length == 0)
        return "[]"
    var s = "["
    for(num of this.arr)
        s += num.toString() + ","
    return s.substring(0, s.length-1) + "]"
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */