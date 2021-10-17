const VelosList = document.getElementById('VelosList');
const searchBar = document.getElementById('searchBar');
let ResultList = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
    const filteredVelo = ResultList.filter((result) => {
        return (
            result.name.toLowerCase().includes(searchString)
        );
    });
    displayResults(filteredVelo);
});

const displayResults = (results) => {
    const htmlString = results
    .map((result) => {
        return `
        <li class="result">
        <h2>${result.name}</h2>
        <p>
        </br>Dispo: ${result.dispo}
        </br><div class="progress">
        </br><div class="progress-bar bg-success" role="progressbar" style="width:${(result.dispo / (result.dispo + result.free)) * 100}%;" aria-valuenow=${result.dispo} aria-valuemin="0" aria-valuemax=${(result.dispo + result.free)}></div>
        </div>
        </p>
        <a href="https://www.google.com/maps/dir//${result.pos}" target="_blank"><img id="google-maps"  src="./static/images/google_maps.png"></a>
        </li>
        `;
    })
    .join('');
    VelosList.innerHTML = htmlString;
};

const loadresults = async () => {
    try {
        // const res = await fetch('https://mancid.herokuapp.com/api/velo');
        const res = await fetch('http://localhost:5000/api/velo');
        ResultList = await res.json();
        displayResults(ResultList);
    } 
    catch (err) {
        console.error(err);
    }
};

loadresults();
