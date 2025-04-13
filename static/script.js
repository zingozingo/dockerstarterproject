document.getElementById("weather-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const city = document.getElementById("city").value;
    const country = document.getElementById("country").value;
    console.log("Form submitted, city:", city, "country:", country);
    const body = country ? `city=${encodeURIComponent(city)},${encodeURIComponent(country)}` : `city=${encodeURIComponent(city)}`;
    const response = await fetch("/weather", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body
    });
    const data = await response.json();
    console.log("Response data:", data);
    const resultDiv = document.getElementById("weather-result");
    if (data.error) {
        resultDiv.innerHTML = `<p class="error">${data.error}</p>`;
    } else {
        resultDiv.innerHTML = `
            <h2>${data.name}</h2>
            <p>${data.main.temp}°C, ${data.weather[0].description}</p>
        `;
    }
});