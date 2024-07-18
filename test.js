const fs = require('fs');

let i = 0;
let flag = true;

function fetchSubmissions() {
    fetch(`https://leetcode.com/api/submissions/?offset=${i}&limit=${20}&lastkey=`, {
        "headers": {
            "cookie": "gr_user_id=ef27ef09-4b11-4472-9280-d5bd1a91318a; 87b5a3c3f1a55520_gr_last_sent_cs1=Vigneswar_A; __stripe_mid=3eb1457d-60aa-42a3-837f-2b1836f67b7fd2d0c6; _ga_CDRWKZTDEX=deleted; csrftoken=RPVrCuLTKhpeqlykhes69ZgnDpO8HxtzFOR3J9F23gDXoi3jJtnJLw9h3CsC6p6E; cf_clearance=vTpcAfSle6eR7HbbnRX2mujhIj4wphJXZ0NmxnTpM2Y-1717646768-1.0.1.1-JtzV_aMcSAOGgNV6MslXRVcwvNQUXrc2UvYv5XYbTpTSlpVkLjMEXPwqc0pgpUt3tG_B1ESoUKaFJAj68IN.tw; _gid=GA1.2.56735713.1720700083; ip_check=(false, \"2409:408d:3480:1a8c:b4ff:eea0:fcf5:a81f\"); LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTI5MDg5OSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjVmNjg3ZGRkM2Y3OTE2YzU5MGI3NzljZWNkNDMwNGNlYzQyZjNjMTA2ZGQyZGM4YmQyZjVjMmY1OGJmOTdmNCIsImlkIjo1MjkwODk5LCJlbWFpbCI6InZpZ3UudmlnbmVzd2FyQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiVmlnbmVzd2FyX0EiLCJ1c2VyX3NsdWciOiJWaWduZXN3YXJfQSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9hdmF0YXJzL2F2YXRhcl8xNjQ5NjExMDE4LnBuZyIsInJlZnJlc2hlZF9hdCI6MTcyMTIyNTE3NCwiaXAiOiIyNDA5OjQwOGQ6MzA5ZToxYjVjOmFjOWQ6YWQ0ODpmZmQ1OmRiNTEiLCJpZGVudGl0eSI6ImExNmRkYWFiOTA5ZDJjZjI3ZmNlMzUzZjI2ZGQyZmYyIiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwLCJzZXNzaW9uX2lkIjo2MTU1ODk5MCwiZGV2aWNlX3dpdGhfaXAiOlsiZGE5YTZhNDAyZTExYjZiMTQ0MTc0M2JiYjQ3MDc4ZDEiLCIyNDA5OjQwOGQ6MzA5ZToxYjVjOmFjOWQ6YWQ0ODpmZmQ1OmRiNTEiXX0.W6F3mxhmtDhczEKED1BcpFF-pMbSOz-tcnZXcnq9DxM; 87b5a3c3f1a55520_gr_session_id=5c91c7e2-c0b3-4c29-96bf-dede04fbd855; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=5c91c7e2-c0b3-4c29-96bf-dede04fbd855; 87b5a3c3f1a55520_gr_session_id_sent_vst=5c91c7e2-c0b3-4c29-96bf-dede04fbd855; INGRESSCOOKIE=62343b89313e4cd4b65b30cac30440db|8e0876c7c1464cc0ac96bc2edceabd27; __stripe_sid=d25f2130-3d57-43a2-b705-150656a7a82ab84a5f; __cf_bm=ihVC0zpA4EoNRcs8Uf21qqqSbqfBVGxkxXBSAEgeavk-1721306650-1.0.1.1-zjnZBz0afufDqMGjwCc8i20rBecXP1x_tnZdo8dPs2eTnTBQfZhmDCBXTKS4lHVEb6NbMx4WmQ5pSHax7VwHcQ; __gads=ID=f64b33b4ceb2fbb4-2294af7bd9e70012:T=1698891362:RT=1721306966:S=ALNI_MZrvCq5ZtLMfoXjiI_ZJQOieMRb-Q; __gpi=UID=00000c7e27de99fb:T=1698891362:RT=1721306966:S=ALNI_MZrNFBH3bDkgCYJTDb3M3lmVSSBWg; __eoi=ID=4304d5f876dc0b5c:T=1707667720:RT=1721306966:S=AA-AfjZ7BRLqIdObI0SetmivTndn; FCNEC=%5B%5B%22AKsRol9kfF7dg055_xgdq2hzxLZT4uATxGT2N5sB3SrFwu9kMVPMVqChVt-nVHCf8j7SZHQER0wqP8Vd3DECxzZ53jxYKvZtHJFJG5QA_fqbSyCxFz_ZxxguV_pWpJKkHgYZKTFJXB2kb-GBG8ZVwAzSpxIOF06gig%3D%3D%22%5D%5D; _gat=1; 87b5a3c3f1a55520_gr_cs1=Vigneswar_A; _dd_s=rum=0&expire=1721307957604; _ga=GA1.1.1662290726.1686023940; _ga_CDRWKZTDEX=GS1.1.1721305750.868.1.1721307061.39.0.0"
        },
        "body": null,
        "method": "GET"
    }).then(res => res.json())
        .then(res => {
            if (!res.has_next) {
                flag = false;
            }

            try {
                for (let question of res.submissions_dump) {
                    if (question.status_display === 'Accepted') {
                        let fileName = `programming/leetcode/${question.question_id}.py`;
                        if (!fs.existsSync(fileName)) {
                            fs.writeFileSync(fileName, question.code);
                            console.log(fileName);
                        }
                    }
                }
            } catch (e) {
                console.log(e);
            }

            // Schedule next fetch or terminate
            if (flag) {
                i += 20;
                setTimeout(fetchSubmissions, 3000); // Delay of 3 seconds
            }
        })
        .catch(error => {
            console.error('Error fetching submissions:', error);
            flag = false; // Stop on error
        });
}

// Initial call to start fetching
fetchSubmissions();
