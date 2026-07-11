let searchIndex = [];
let searchInput = null;
let resultsContainer = null;

async function initSearch() {
    try {
        const response = await fetch('/search-index.json');
        searchIndex = await response.json();
        setupSearchUI();
    } catch (error) {
        console.error('Failed to load search index:', error);
    }
}

function setupSearchUI() {
    searchInput = document.getElementById('search-input');
    resultsContainer = document.getElementById('search-results');

    if (searchInput && resultsContainer) {
        searchInput.addEventListener('input', debounce(performSearch, 150));
        searchInput.focus();
    }
}

function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

function performSearch() {
    const query = searchInput.value.toLowerCase().trim();

    if (!query || query.length < 2) {
        resultsContainer.innerHTML = '';
        return;
    }

    const queryTerms = query.split(/\s+/).filter(t => t.length > 0);
    const isMultiWord = queryTerms.length > 1;

    const results = searchIndex
        .filter(page => {
            const titleLower = page.title.toLowerCase();
            const descLower = page.description.toLowerCase();

            if (isMultiWord) {
                return queryTerms.every(term =>
                    titleLower.includes(term) ||
                    descLower.includes(term) ||
                    page.words.some(word => word.includes(term))
                );
            } else {
                const singleTerm = queryTerms[0];
                return titleLower.includes(singleTerm) ||
                       descLower.includes(singleTerm) ||
                       page.words.some(word => word.includes(singleTerm));
            }
        })
        .slice(0, 20);

    displayResults(results, query);
}

function displayResults(results, query) {
    if (results.length === 0) {
        resultsContainer.innerHTML = '<div class="search-empty">No results found for "' + escapeHtml(query) + '"</div>';
        return;
    }

    const html = results.map(page => {
        const excerpt = extractExcerpt(page.description || page.words.join(' '), query);
        return `
            <a href="${escapeHtml(page.url)}" class="search-result">
                <div class="search-result-title">${highlightMatch(page.title, query)}</div>
                <div class="search-result-excerpt">${excerpt}</div>
                <div class="search-result-url">${escapeHtml(page.url)}</div>
            </a>
        `;
    }).join('');

    resultsContainer.innerHTML = html;
}

function highlightMatch(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function extractExcerpt(text, query) {
    const lowerText = text.toLowerCase();
    const queryIndex = lowerText.indexOf(query);

    if (queryIndex === -1) {
        return text.substring(0, 120) + '...';
    }

    const start = Math.max(0, queryIndex - 40);
    const end = Math.min(text.length, queryIndex + query.length + 80);
    let excerpt = text.substring(start, end);

    if (start > 0) excerpt = '...' + excerpt;
    if (end < text.length) excerpt = excerpt + '...';

    return highlightMatch(excerpt, query);
}

function escapeHtml(text) {
    const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Initialize on load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSearch);
} else {
    initSearch();
}
