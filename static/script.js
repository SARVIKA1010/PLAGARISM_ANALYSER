document.getElementById('plagiarismForm').addEventListener('submit', function(e) {
    e.preventDefault();

    let textInput = document.getElementById('textInput').value;

    let formData = new FormData();
    formData.append('text', textInput);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('plagiarismPercentage').innerText = data.plagiarismPercentage + '%';

        let reportHTML = '<ul>';
        data.detailedReport.forEach(item => {
            reportHTML += `<li>${item.source}: ${item.similarity}</li>`;
        });
        reportHTML += '</ul>';
        document.getElementById('detailedReport').innerHTML = reportHTML;

        const ctx = document.getElementById('plagiarismChart').getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Plagiarized', 'Unique'],
                datasets: [{
                    data: [data.plagiarismPercentage, 100 - data.plagiarismPercentage],
                    backgroundColor: ['#dc3545', '#28a745'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error:', error));
});
