async function getListing() {
    try {
        const response = await fetch(`https://api.github.com/repos/vigneswar-a/vigneswar-a.github.io/contents/${document.location.pathname.replace('.html', '')}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return [];
    }
}

async function makeCard(name, path) {
    let card = document.createElement('a');
    card.innerText = name;
    card.href = path;
    return card;
}

async function renderCards() {
    let content = document.getElementById("content");
    loading.style.display = 'block';
    try {
        const list = await getListing();
        content.innerHTML = '';
        for (let item of list) {
            let { name, path } = item;
            let card = await makeCard(name.replace('.pdf', '').replace(/_/g, ' '), path);
            content.appendChild(card);
        }
    } catch (error) {
        console.error('Error rendering cards:', error);
    } finally {
        // Hide loading indicator after rendering cards or on error
        loading.style.display = 'none';
    }
}

renderCards();