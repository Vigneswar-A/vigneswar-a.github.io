async function getListing() {
    try {
        const response = await fetch(`https://api.github.com/repos/vigneswar-a/vigneswar-a.github.io/contents/${document.location.pathname.replace('.html', '')}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return [];
    }
}

async function makeCard(name, path) {
    let card = document.createElement('a');
    card.innerText = name;
    card.href = `programming/view_code.html?code_path=${path}`;
    return card;
}

async function getSlugs() {
    try {
        let slugs = {};
        const response = await fetch('programming/lc.json');
        const res = await response.json();

        let questions = res.stat_status_pairs;
        for (let question of questions) {
            slugs[question.stat.question_id] = question.stat.question__title;
        }

        return slugs;
    } catch (error) {
        console.error('Error fetching slugs:', error);
        return {}; // Return empty object or handle error appropriately
    }
}

async function renderCards(prefix = '') {
    let content = document.getElementById("content");
    let loading = document.getElementById("loading");
    loading.style.display = 'block';

    try {
        let slugs = await getSlugs();
        let list = await getListing();

        content.innerHTML = '';
        for (let item of list) {
            let { name, path } = item;
            let question_id = name.replace('.py', '');
            let question_title = slugs[Number.parseInt(question_id)];
            if (prefix === '' || question_title.toLowerCase().startsWith(prefix.toLowerCase())) {
                let card = await makeCard(question_title, path);
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

let search_bar = document.getElementById("search_bar");
search_bar.addEventListener('input', () => {
    renderCards(search_bar.value);
});
