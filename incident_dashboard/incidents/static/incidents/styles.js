document.getElementById('year-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const year = document.getElementById('year').value;

    fetch(`/incidents/get_incidents_data?year=${year}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const months = Object.keys(data.monthlyData);
            const monthlyIncidents = Object.values(data.monthlyData);

            generateChart('yearly-chart', 'Incidents annuels', [year], [data.yearlyTotal]);
            generateChart('monthly-chart', 'Incidents mensuels', months, monthlyIncidents);
        })
        .catch(error => console.error('Error:', error));
});

function generateChart(chartId, label, labels, data) {
    const ctx = document.getElementById(chartId).getContext('2d');
   
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: '#FFAF61',
                borderColor: '#ff923c',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1 
                    }
                }
            }
        }
    });
}
