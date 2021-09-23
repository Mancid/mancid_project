const matchList = document.getElementById('result');
const searchBar = document.getElementById('searchBar');
let StationsList = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredStations = StationsList.filter((station) => {
        return (
            station.Station.toLowerCase().includes(searchString) ||
            station.Direction.toLowerCase().includes(searchString)
        );
    });
    displayStations(filteredStations);
});

const loadStations = async () => {
    try {
        const res = await fetch('http://localhost:5000/api/tram');
        // const res = await fetch('https://hp-api.herokuapp.com/api/characters');
        StationsList = await res.json();
        displayStations(StationsList);
    } catch (err) {
        console.error(err);
    }
};

const outputHtml = matches => {
    if(matches.length > 0){
        const html = matches.map(match =>`
        <table class="table">
        <tbody>
          <tr class="table-active">
            <th scope="row">${match.Ligne}</th>
            <td>${match.Station}</td>
            <td>${match.Direction}</td>
            <td>${match.Delai} min</td>
          </tr>  </tbody>
          </table>

                `
                ).join('');
            matchList.innerHTML = html;
    }
};

loadStations();
