let list = [];

async function getListing() {
    try {
        const response = await fetch(`https://api.github.com/repos/vigneswar-a/vigneswar-a.github.io/contents/${document.location.pathname.replace('.html', '')}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        list = data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

async function makeCard(name, path) {
    let card = document.createElement('a');
    card.innerText = name;
    card.href = path;
    return card;
}

async function renderCards(prefix = '') {
    let content = document.getElementById("content");
    loading.style.display = 'block';
    try {
        await getListing();
        content.innerHTML = '';
        for (let item of list) {
            let { name, path } = item;
            name = name.replace('.pdf', '').replace(/_/g, ' ');
            if (prefix === '' || name.toLowerCase().startsWith(prefix.toLowerCase())) {
                let card = await makeCard(name, path);
                content.appendChild(card);
            }
        }
    } catch (error) {
        console.error('Error rendering cards:', error);
    } finally {
        loading.style.display = 'none';
    }
}


renderCards();

let search_bar = document.getElementById("search_bar")

search_bar.addEventListener('input', (e) => {
    renderCards(search_bar.value);
})
