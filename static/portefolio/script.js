function updateClock() {
        const clockElement = document.getElementById('clock');
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        clockElement.textContent = `${hours}:${minutes}:${seconds}`;
    }

    setInterval(updateClock, 1000);
    updateClock();

    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const menuImage = document.querySelector('.menu-content img');

    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        if (document.body.classList.contains('dark-mode')) {
            darkModeToggle.textContent = 'Toggle Light Mode';
            darkModeToggle.style.backgroundColor = '#fff';
            darkModeToggle.style.color = '#333';
            menuImage.src = '/static/portefolio/imgs/1.png';
        } else {
            darkModeToggle.textContent = 'Toggle Dark Mode';
            darkModeToggle.style.backgroundColor = '#333';
            darkModeToggle.style.color = '#fff';
            menuImage.src = '/static/portefolio/imgs/0.png';
        }
    });

async function fetchWeatherImage() {
    try {
        const response = await fetch('https://a22205897.pythonanywhere.com/meteo/previsao/img/');
        const data = await response.json();

        // Verifica se a resposta contém o atributo 'src'
        if (data.src) {
            const imgSrc = data.src;
            document.getElementById('weatherIcon').src = imgSrc;
        } else {
            console.error('A resposta da API não contém o atributo "src" esperado.');
        }
    } catch (error) {
        console.error('Ocorreu um erro ao buscar a imagem do clima:', error);
    }
}

window.onload = fetchWeatherImage;
