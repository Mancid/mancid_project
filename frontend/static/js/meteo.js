let ville = 'Montpellier';
recevoirTemperature(ville);

let button = document.querySelector('#changer');
button.addEventListener('click', () => {
  ville = prompt('Choisissez une ville :');
  recevoirTemperature(ville);
});

function recevoirTemperature(ville) {
  const url = 'https://api.openweathermap.org/data/2.5/weather?q=' + ville + '&lang=fr&appid=eb3e55ca0093756f2541d5ad27c5021c&units=metric';
  
  let requete = new XMLHttpRequest();
  requete.open('GET', url);
  requete.responseType = 'json';
  requete.send();

  requete.onload = function() {
    if (requete.readyState === XMLHttpRequest.DONE) {
      if (requete.status === 200) {
        let reponse = requete.response;
        let display = reponse.name + " - " + reponse.main.temp + "°C - " + reponse.weather[0].description;
        document.querySelector('#display').textContent = display;

      } else {
        alert('Un problème est intervenu, merci de revenir plus tard.');
      }
    }
  }
}
