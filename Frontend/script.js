async function getQuote() {
    try {
        const response = await fetch("https://<your-backend-route>/quote");
        const data = await response.json();
        document.getElementById("quoteText").innerText = data.quote;
    } catch (error) {
        document.getElementById("quoteText").innerText = "Error fetching quote.";
    }
}
