var promisePool = async function(functions, n) {
    return new Promise((resolve) => {
    let count = 0
        let idx = 0
        function helper() {
            if (idx >= functions.length) {
                if (count === 0) resolve()
                return
            }

            while (count < n && idx < functions.length) {
                count++
                const promise = functions[idx]()
                idx++
                promise.then(() => {
                    count--
                    helper()
            })
            }
        }
        helper();
    });
};