var throttle = function(fn, t) {
  let interval = null
  let args = null
  
  const intervalFunction = () => {
    if (args === null) {
      clearInterval(interval)
      interval = null
    } else {
      fn(...args)
      args = null
    }
  };

  return function throttled(...arg) {
    if (interval) {
      args = arg
    } else {
      fn(...arg)
      interval = setInterval(intervalFunction, t)
    }
  }
};