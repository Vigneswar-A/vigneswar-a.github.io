let slugs = {}; // Cached object for slugs
let list = []; // Cached array for listing

async function getSlugs() {
    if (Object.keys(slugs).length === 0) { // Check if slugs are already fetched
        try {
            const response = await fetch('programming/lc.json');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const res = await response.json();
            let questions = res.stat_status_pairs;
            for (let question of questions) {
                slugs[question.stat.question_id] = question.stat.question__title;
            }
        } catch (error) {
            console.error('Error fetching slugs:', error);
        }
    }
    return slugs;
}

async function getListing() {
    if (list.length === 0) { // Check if listing is already fetched
        try {
            const response = await fetch('programming/solved.json');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            list = await response.json();
        } catch (error) {
            console.error('Error fetching listing:', error);
        }
    }
    return list;
}

async function makeCard(name, path) {
    let card = document.createElement('a');
    card.innerText = name;
    card.href = `programming/view_code.html?code_path=${path}`;
    return card;
}

async function renderCards(prefix = '') {
    let content = document.getElementById("content");
    loading.style.display = 'block';

    // Fetch slugs and listing if not already cached
    if (Object.keys(slugs).length === 0 || list.length === 0) {
        await Promise.all([getSlugs(), getListing()]);
    }

    try {
        content.innerHTML = '';
        for (let item of list) {
            let name = item;
            let path = `programming/leetcode/${name}`;
            let question_id = name.replace('.py', '');
            name = slugs[Number.parseInt(question_id)];
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

// Initial rendering
renderCards();

// Event listener for search bar input
let search_bar = document.getElementById("search_bar");
search_bar.addEventListener('input', (e) => {
    renderCards(search_bar.value);
});
