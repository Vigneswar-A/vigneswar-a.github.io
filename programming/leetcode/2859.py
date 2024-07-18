/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return new Promise(function(res, rej){
        var ans = 0;
        
        promise2.then((data) => {
            ans += data;
            promise1.then((data) => {
                ans += data;
                res(ans)
            })
        }) 
    })
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */