document.addEventListener('DOMContentLoaded', function() {
    fetch('/platform-chart/?json=true')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('platformChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.platform_names,
                    datasets: [{
                        label: 'Nombre des incidents',
                        data: data.incident_counts,
                        backgroundColor: '#FFC374',
                        borderColor: 'rgba(54, 162, 235, 1)',
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
        })
        .catch(error => console.error('Error:', error));
});


