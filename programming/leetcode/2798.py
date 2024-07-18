/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    arrays = []
    let k = 0
    temp = []
    for(let i = 0; i < arr.length; i++){
        temp.push(arr[i])
        k++;
        if(k%size == 0){
            arrays.push(temp)
            temp = []
        }  
    }
    if(k%size)
    arrays.push(temp)
    return arrays
};
