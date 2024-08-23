const ctx = document.getElementById('trendsChart').getContext('2d');

const trendsChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Keyword1', 'Keyword2'], // Placeholder for dynamic labels
        datasets: [{
            label: 'Search Volume',
            data: [12, 19], // Placeholder for dynamic data
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 7,
            fill: true,
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Search Volume'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Keywords'
                }
            }
        },
        plugins: {
            legend: {
                display: true,
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `${context.dataset.label}: ${context.raw}`;
                    }
                }
            }
        }
    }
});
