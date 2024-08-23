const ctx = document.getElementById('trendsChart').getContext('2d');
const trendsChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Keyword1', 'Keyword2'],
        datasets: [{
            label: 'Search Volume',
            data: [12, 19],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            fill: false,
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        return `Volume: ${tooltipItem.raw}`;
                    }
                }
            }
        }
    }
});
