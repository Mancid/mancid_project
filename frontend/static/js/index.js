const btnparking = document.getElementById('button_parking');
const btntram = document.getElementById('button_tram');
const btnbus = document.getElementById('button_bus');
const btnvelo = document.getElementById('button_velo');
const btnverdict = document.getElementById('button_verdict');


const green = btn => {
    console.log(btn)
    btn.style.backgroundColor = "green"
    btn.style.color = "white"
    if (btn == btnparking) {
        btntram.style.backgroundColor = "white"
        btntram.style.color = "grey"
        btnbus.style.backgroundColor = "white"
        btnbus.style.color = "grey"
        btnvelo.style.backgroundColor = "white"
        btnvelo.style.color = "grey"
        btnverdict.style.backgroundColor = "white"
        btnverdict.style.color = "grey"
    }
    else if (btn == btntram) {
        btnparking.style.backgroundColor = "white"
        btnparking.style.color = "grey"
        btnbus.style.backgroundColor = "white"
        btnbus.style.color = "grey"
        btnvelo.style.backgroundColor = "white"
        btnvelo.style.color = "grey"
        btnverdict.style.backgroundColor = "white"
        btnverdict.style.color = "grey"
    }
    else if (btn == btnbus) {
        btnparking.style.backgroundColor = "white"
        btnparking.style.color = "grey"
        btntram.style.backgroundColor = "white"
        btntram.style.color = "grey"
        btnvelo.style.backgroundColor = "white"
        btnvelo.style.color = "grey"
        btnverdict.style.backgroundColor = "white"
        btnverdict.style.color = "grey"
    }
    else if (btn == btnvelo) {
        btnparking.style.backgroundColor = "white"
        btnparking.style.color = "grey"
        btntram.style.backgroundColor = "white"
        btntram.style.color = "grey"
        btnbus.style.backgroundColor = "white"
        btnbus.style.color = "grey"
        btnverdict.style.backgroundColor = "white"
        btnverdict.style.color = "grey"
    }
    else if (btn == btnverdict) {
        btnparking.style.backgroundColor = "white"
        btnparking.style.color = "grey"
        btntram.style.backgroundColor = "white"
        btntram.style.color = "grey"
        btnbus.style.backgroundColor = "white"
        btnbus.style.color = "grey"
        btnvelo.style.backgroundColor = "white"
        btnvelo.style.color = "grey"
    }
    };

btnparking.addEventListener('click', () => green(btnparking));
btntram.addEventListener('click', () => green(btntram));
btnbus.addEventListener('click', () => green(btnbus));
btnvelo.addEventListener('click', () => green(btnvelo));
btnverdict.addEventListener('click', () => green(btnverdict));

document.getElementById("button_parking").addEventListener("click", parking);
document.getElementById("button_tram").addEventListener("click", tram);
document.getElementById("button_bus").addEventListener("click", bus);
document.getElementById("button_velo").addEventListener("click", velo);

$(document).ready(function(){     
    $("#button_parking").click(function(){
        $("#ParkingsList").show();
        $("#StationsList").hide();
        $("#ArretsList").hide();
        $("#VelosList").hide();
    });
    $("#button_tram").click(function(){
        $("#ParkingsList").hide();
        $("#StationsList").show();
        $("#ArretsList").hide();
        $("#VelosList").hide();
    });
    $("#button_bus").click(function(){
        $("#ParkingsList").hide();
        $("#StationsList").hide();
        $("#ArretsList").show();
        $("#VelosList").hide();
    });
    $("#button_velo").click(function(){
        $("#ParkingsList").hide();
        $("#StationsList").hide();
        $("#ArretsList").hide();
        $("#VelosList").show();
    });
});

function parking() {
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
            </br><div class="progress-bar bg-success" role="progressbar" style="width:${((result.Free) / result.Total) * 100}%;" aria-valuenow=${(result.Total - result.Free)} aria-valuemin="0" aria-valuemax=${result.Total}></div>
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
            const res = await fetch('https://mancid.herokuapp.com/api/parking');
            // const res = await fetch('http://localhost:5000/api/parking');
            ResultList = await res.json();
            displayResults(ResultList);
        } 
        catch (err) {
            console.error(err);
        }
    };
    loadresults();
}

function tram() {
    const StationsList = document.getElementById('StationsList');
    const searchBar = document.getElementById('searchBar');
    let ResultList = [];
    searchBar.addEventListener('keyup', (e) => {
        const searchString = e.target.value.toLowerCase();
        const filteredStation = ResultList.filter((result) => {
            return (
                result.Station.toLowerCase().includes(searchString) ||
                result.Ligne.toLowerCase().includes(searchString)
            );
        });
        displayResults(filteredStation);
    });
    const displayResults = (results) => {
        const htmlString = results
        .map((result) => {
            return `
            <li class="result">
            <h2>${result.Station}</h2>
            <p>Ligne: ${result.Ligne}
            </br>Direction: ${result.Direction}
            </br>&#9201; Délai: ${result.Delai} min
            </p>
            <a href="https://www.google.com/maps/dir//${result.Adresse}" target="_blank"><img id="google-maps"  src="./static/images/google_maps.png"></a>
            </li>
            `;
        })
        .join('');
        StationsList.innerHTML = htmlString;
    };
    const loadresults = async () => {
        try {
            const res = await fetch('https://mancid.herokuapp.com/api/tram');
            // const res = await fetch('http://localhost:5000/api/tram');
            ResultList = await res.json();
            displayResults(ResultList);
        } 
        catch (err) {
            console.error(err);
        }
    };
    loadresults();
}

function bus() {
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
            const res = await fetch('https://mancid.herokuapp.com/api/bus');
            // const res = await fetch('http://localhost:5000/api/bus');
            ResultList = await res.json();
            displayResults(ResultList);
        } 
        catch (err) {
            console.error(err);
        }
    };
    loadresults();
}

function velo() {
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
            const res = await fetch('https://mancid.herokuapp.com/api/velo');
            // const res = await fetch('http://localhost:5000/api/velo');
            ResultList = await res.json();
            displayResults(ResultList);
        } 
        catch (err) {
            console.error(err);
        }
    };
    loadresults();
}
