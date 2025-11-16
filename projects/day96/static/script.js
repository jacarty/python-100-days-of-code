// DOM Elements
const stockInput = document.getElementById('stockInput');
const searchBtn = document.getElementById('searchBtn');
const loading = document.getElementById('loading');
const error = document.getElementById('error');
const stockData = document.getElementById('stockData');
const popularList = document.getElementById('popularList');

// Load popular stocks on page load
loadPopularStocks();

// Event Listeners
searchBtn.addEventListener('click', searchStock);
stockInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        searchStock();
    }
});

/**
 * Load and display popular stocks
 */
async function loadPopularStocks() {
    try {
        const response = await fetch('/popular');
        const stocks = await response.json();

        popularList.innerHTML = '';
        stocks.forEach(stock => {
            const chip = document.createElement('div');
            chip.className = 'stock-chip';
            chip.innerHTML = `<strong>${stock.symbol}</strong> - ${stock.name}`;
            chip.onclick = () => {
                stockInput.value = stock.symbol;
                searchStock();
            };
            popularList.appendChild(chip);
        });
    } catch (err) {
        console.error('Failed to load popular stocks:', err);
    }
}

/**
 * Search for a stock
 */
async function searchStock() {
    const symbol = stockInput.value.trim().toUpperCase();

    if (!symbol) {
        showError('Please enter a stock symbol');
        return;
    }

    // Show loading state
    hideAll();
    loading.style.display = 'block';

    try {
        const response = await fetch(`/stock/${symbol}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch stock data');
        }

        displayStockData(data);
    } catch (err) {
        showError(err.message);
    } finally {
        loading.style.display = 'none';
    }
}

/**
 * Display stock data
 */
function displayStockData(data) {
    hideAll();

    // Update header
    document.getElementById('stockSymbol').textContent = data.symbol;
    document.getElementById('stockPrice').textContent = `$${data.close.toFixed(2)}`;

    // Update change
    const changeElement = document.getElementById('stockChange');
    if (data.change !== null) {
        const arrow = data.change > 0 ? '▲' : '▼';
        const sign = data.change > 0 ? '+' : '';
        changeElement.textContent = `${arrow} ${sign}$${data.change.toFixed(2)} (${sign}${data.change_percent.toFixed(2)}%)`;
        changeElement.className = `change ${data.change > 0 ? 'positive' : 'negative'}`;
    } else {
        changeElement.textContent = 'N/A';
        changeElement.className = 'change';
    }

    // Update details
    document.getElementById('stockOpen').textContent = `$${data.open.toFixed(2)}`;
    document.getElementById('stockHigh').textContent = `$${data.high.toFixed(2)}`;
    document.getElementById('stockLow').textContent = `$${data.low.toFixed(2)}`;
    document.getElementById('stockVolume').textContent = data.volume.toLocaleString();
    document.getElementById('stockDate').textContent = new Date(data.date).toLocaleDateString();

    // Update history
    displayHistory(data.history);

    stockData.style.display = 'block';
}

/**
 * Display stock history table
 */
function displayHistory(history) {
    const historyElement = document.getElementById('stockHistory');

    let tableHTML = `
        <table>
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Open</th>
                    <th>High</th>
                    <th>Low</th>
                    <th>Close</th>
                    <th>Volume</th>
                </tr>
            </thead>
            <tbody>
    `;

    history.forEach(day => {
        const date = new Date(day.date).toLocaleDateString();
        tableHTML += `
            <tr>
                <td>${date}</td>
                <td>$${day.open.toFixed(2)}</td>
                <td>$${day.high.toFixed(2)}</td>
                <td>$${day.low.toFixed(2)}</td>
                <td>$${day.close.toFixed(2)}</td>
                <td>${day.volume.toLocaleString()}</td>
            </tr>
        `;
    });

    tableHTML += `
            </tbody>
        </table>
    `;

    historyElement.innerHTML = tableHTML;
}

/**
 * Show error message
 */
function showError(message) {
    hideAll();
    error.textContent = message;
    error.style.display = 'block';
}

/**
 * Hide all content sections
 */
function hideAll() {
    loading.style.display = 'none';
    error.style.display = 'none';
    stockData.style.display = 'none';
}