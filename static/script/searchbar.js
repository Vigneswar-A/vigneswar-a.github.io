async function addSearchBar() {
    let searchbar = document.createElement('input');
    searchbar.type = 'text';
    searchbar.id = "search_bar";
    document.getElementById('content').insertAdjacentElement('beforebegin', searchbar);
}

addSearchBar();