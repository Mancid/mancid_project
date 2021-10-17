const ArretsList = document.getElementById('ArretsList');
const searchBar = document.getElementById('searchBar');
let ResultList = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
    const filteredArret = ResultList.filter((result) => {
        return (
            result.Arret.toLowerCase().includes(searchString) ||
            result.Ligne.toLowerCase().includes(searchString)
        );
    });
    displayResults(filteredArret);
});

const displayResults = (results) => {
    const htmlString = results
    .map((result) => {
        return `
        <li class="result">
        <h2>${result.Arret}</h2>
        <p>Ligne: ${result.Ligne}
        </br>Direction: ${result.Direction}
        </br>&#9201; Délai: ${result.Delai} min
        </p>
        <a href="https://www.google.com/maps/dir//${result.Adresse}" target="_blank"><img id="google-maps"  src="./static/images/google_maps.png"></a>
        </li>
        `;
    })
    .join('');
    ArretsList.innerHTML = htmlString;
};

const loadresults = async () => {
    try {
        // const res = await fetch('https://mancid.herokuapp.com/api/bus');
        const res = await fetch('http://localhost:5000/api/bus');
        ResultList = await res.json();
        displayResults(ResultList);
    } 
    catch (err) {
        console.error(err);
    }
};

loadresults();
