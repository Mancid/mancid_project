const ParkingsList = document.getElementById('ParkingsList');
const searchBar = document.getElementById('searchBar');
let ResultList = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
    const filteredParking = ResultList.filter((result) => {
        return (
            result.Parking.toLowerCase().includes(searchString)
        );
    });
    displayResults(filteredParking);
});

const displayResults = (results) => {
    const htmlString = results
    .map((result) => {
        return `
        <li class="result">
        <h2>${result.Parking}</h2>
        <p>
        </br>Status: <span class="badge bg-info">${result.Status}</span>
        </br>Dispo: ${result.Free}
        </br><div class="progress">
        </br><div class="progress-bar bg-success" role="progressbar" style="width:${((result.Total - result.Free) / result.Total) * 100}%;" aria-valuenow=${result.Free} aria-valuemin="0" aria-valuemax=${result.Total}></div>
        </div>
        </p>
        <a href="https://www.google.com/maps/dir//${result.Adresse}" target="_blank"><img id="google-maps"  src="./static/images/google_maps.png"></a>
        </li>
        `;
    })
    .join('');
    ParkingsList.innerHTML = htmlString;
};

const loadresults = async () => {
    try {
        const res = await fetch('http://0.0.0.0:9375/api/parking');
        ResultList = await res.json();
        displayResults(ResultList);
    } 
    catch (err) {
        console.error(err);
    }
};

loadresults();
