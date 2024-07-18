let code_path = new URLSearchParams(document.location.search).get('code_path');
if (code_path === null) {
    document.location = 'programming/leetcode.html';
}

fetch(code_path).then(res => res.text())
    .then(res => {
        res = res.trimEnd()
        document.getElementById("code").innerHTML = res;
        let lines = '';
        for (let i = 1; i <= res.match(/[\n]/g)?.length + 1; i++) {
            lines += `${i}\n`;
        }
        document.getElementById("line-numbers").innerHTML = lines;
    })
    .catch((e) => {
    })
