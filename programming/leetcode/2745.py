/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if(object === null)
        return 'null'
    
    if (Array.isArray(object))
        return `[${object.map((element) => jsonStringify(element))}]`
    
    if(typeof object === 'object'){
        const keys = Object.keys(object)
        const keyValuePairs = keys.map((key) => `"${key}":${jsonStringify(object[key])}`)
        return `{${keyValuePairs.join(',')}}`
    }

    if (typeof object === 'string') 
        return `"${object}"`
  
    return String(object)
};