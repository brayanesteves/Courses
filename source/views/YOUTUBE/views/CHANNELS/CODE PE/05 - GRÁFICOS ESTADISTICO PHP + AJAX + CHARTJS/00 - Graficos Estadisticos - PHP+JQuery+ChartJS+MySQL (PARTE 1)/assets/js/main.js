

function CargarDatosGraficosBar() {
    $.ajax({
        url: 'source/controller/grafico.php',
        type: 'POST',

    }).done(function (resp) {
        if(resp.length > 0) {
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][1]);
                cantidad.push(data[i][2]);
            }
            CrearGrafico(titulo, cantidad, 'bar', 'GRÁFICO EN BARRAS DE PRODUCTOS', 'graficobar');
            document.getElementById("graficobarHorizontal").style.display = "none";
            document.getElementById("graficobar").style.display = "block";
        }
    });
}
function CargarDatosGraficosBarHorizontal() {
    $.ajax({
        url: 'source/controller/grafico.php',
        type: 'POST',

    }).done(function (resp) {
        if(resp.length > 0) {            
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][1]);
                cantidad.push(data[i][2]);
            } 
            CrearGrafico(titulo, cantidad, 'horizontalBar', 'GRÁFICO EN BARRAS HORIZONTAL DE PRODUCTOS', 'graficobarHorizontal');
            document.getElementById("graficobar").style.display = "none";
            document.getElementById("graficobarHorizontal").style.display = "block";
        }
    });
}

function CrearGrafico(titulo, cantidad, tipo, encabezado, id) {
    var ctx = document.getElementById(id);
        var myChart = new Chart(ctx, {
            type: tipo,
            data: {
                labels: titulo,
                datasets: [{
                    label: encabezado,
                    data: cantidad,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
}