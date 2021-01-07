CargarDatosGraficosBar();
CargarDatosGraficosBarHorizontal();
CargarDatosGraficosPie();

function CargarDatosGraficosBar() {
    $.ajax({
        url: 'source/controller/grafico.php',
        type: 'POST',

    }).done(function (resp) {
        if(resp.length > 0) {
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            var colores = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][1]);
                cantidad.push(data[i][2]);
                colores.push(colorRGB());
            }
            CrearGrafico(titulo, cantidad, colores, 'bar', 'GRÁFICO EN BARRAS DE PRODUCTOS', 'graficobar');
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
            var colores = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][1]);
                cantidad.push(data[i][2]);
                colores.push(colorRGB());
            } 
            CrearGrafico(titulo, cantidad, colores, 'horizontalBar', 'GRÁFICO EN BARRAS HORIZONTAL DE PRODUCTOS', 'graficobarHorizontal');            
        }
    });
}
function CargarDatosGraficosPie() {
    $.ajax({
        url: 'source/controller/grafico.php',
        type: 'POST',

    }).done(function (resp) {
        if(resp.length > 0) {            
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            var colores = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][1]);
                cantidad.push(data[i][2]);
                colores.push(colorRGB());
            } 
            CrearGrafico(titulo, cantidad, colores, 'pie', 'GRÁFICO PIE DE PRODUCTOS', 'graficopie');            
        }
    });
}

function generarNumero(numero) {
    return (Math.random() * numero.toFixed(0));
}

function colorRGB() {
    var color = "(" + generarNumero(255) + "," + generarNumero(255) + "," + generarNumero(255) + ")";
    return "rgb" + color;
}

//////////////////////////////////////////////////////////////////////////////////////
////////////// FUNCIONES PARA REPORTES CON PARAMETROS ///////////////////////////////
TraerAnio();

function CargarGraficoParametro() {
    CargarDatosGraficosDoughnut();
    CargarDatosGraficosPolar();
    CargarDatosGraficosLine();
}
function TraerAnio() {
    var mifecha = new Date();
    var anio    = mifecha.getFullYear();
    var cadena = "";
    /**
     * 2015 es el año inicial
     * anio + 1 = 
     */
    for(var i = 2015; i < anio + 1; i++) {
        cadena += "<option value=" + i +">" + i + "</option>";
    }
    $("#select_fininicio").html(cadena);
    $("#select_ffin").html(cadena);
}

function CargarDatosGraficosDoughnut() {
    var fechainicio = $("#select_fininicio").val();
    var fechafin    = $("#select_ffin").val();
    $.ajax({
        url: 'source/controller/parametro.php',
        type: 'POST',
        data: {
            inicio: fechainicio,
            fin: fechafin,
        }
    }).done(function (resp) {
        if(resp.length > 0) {
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            var colores = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][0]);
                cantidad.push(data[i][1]);
                colores.push(colorRGB());
            }
            CrearGrafico(titulo, cantidad, colores, 'doughnut', 'GRÁFICO DOUGHNUT PRODUCTOS', 'graficodoughnut_parametro');
        }
    });
}

function CargarDatosGraficosPolar() {
    var fechainicio = $("#select_fininicio").val();
    var fechafin    = $("#select_ffin").val();
    $.ajax({
        url: 'source/controller/parametro.php',
        type: 'POST',
        data: {
            inicio: fechainicio,
            fin: fechafin,
        }
    }).done(function (resp) {
        if(resp.length > 0) {
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            var colores = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][0]);
                cantidad.push(data[i][1]);
                colores.push(colorRGB());
            }
            CrearGrafico(titulo, cantidad, colores, 'polarArea', 'GRÁFICO POLAR AREA DE PRODUCTOS', 'graficopolararea_parametro');
        }
    });
}

function CargarDatosGraficosLine() {
    var fechainicio = $("#select_fininicio").val();
    var fechafin    = $("#select_ffin").val();
    $.ajax({
        url: 'source/controller/parametro.php',
        type: 'POST',
        data: {
            inicio: fechainicio,
            fin: fechafin,
        }
    }).done(function (resp) {
        if(resp.length > 0) {
            var data = JSON.parse(resp);
            var titulo = [];
            var cantidad = [];
            var colores = [];
            for (var i = 0; i < data.length; i++) {
                titulo.push(data[i][0]);
                cantidad.push(data[i][1]);
                colores.push(colorRGB());
            }
            CrearGrafico(titulo, cantidad, colores, 'line', 'GRÁFICO LINE DE PRODUCTOS', 'graficoline_parametro');
        }
    });
}

//////////////////////////////////////////////////////////////////////////////////////

function CrearGrafico(titulo, cantidad, colores, tipo, encabezado, id) {
    var ctx = document.getElementById(id);
        var myChart = new Chart(ctx, {
            type: tipo,
            data: {
                labels: titulo,
                datasets: [{
                    label: encabezado,
                    data: cantidad,
                    backgroundColor: colores,
                    borderColor: colores,
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