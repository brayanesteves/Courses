<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="source/libs/bootstrap/version/4.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.css">

    <title>Graficos Estadisticos - PHP+JQuery+ChartJS+MySQL (PARTE 1)</title>
  </head>
  <body>

    <div class="col-lg-12" style="padding-top:20px;">

        <!--       <SIN PARAMETROS>       -->
        <div class="card">
            <div class="card-header">
                GRÁFICO CON CHART.JS - SUSCRIBE A CODEPE
            </div>
            <div class="card-body"> 
                <div class="row">

                    <div class="col-lg-4">
                        <canvas id="graficobar" width="400" height="400"></canvas>                        
                    </div>

                    <div class="col-lg-4">
                        <canvas id="graficobarHorizontal" width="400" height="400"></canvas>                        
                    </div>

                    <div class="col-lg-4">
                        <canvas id="graficopie" width="400" height="400"></canvas>
                    </div>
                    
                    
                </div>             
                
            </div>
        </div>
        <!--       <.SIN PARAMETROS>       -->

        <!--       <CON PARAMETROS>       -->
        <div class="card">
            <div class="card-header">
                GRÁFICO CON CHART.JS CON PARAMETROS - SUSCRIBE A CODEPE
            </div>
            <div class="card-body"> 
                <div class="row">

                    <div class="col-lg-5">
                        <label for="">Fecha de inicio</label>
                        <select name="" id="select_fininicio" class="form-control"></select>
                    </div>

                    <div class="col-lg-5">
                        <label for="">Fecha fin</label>
                        <select name="" id="select_ffin" class="form-control"></select>
                    </div>

                    <div class="col-lg-2">
                        <label for="">&nbsp;</label>
                        <br>
                        <button class="btn btn-danger" onclick="CargarGraficoParametro()">BUSCAR</button>
                    </div>

                    <div class="col-lg-4">
                        <canvas id="graficodoughnut_parametro" width="400" height="400"></canvas>                        
                    </div>

                    <div class="col-lg-4">
                        <canvas id="graficopolararea_parametro" width="400" height="400"></canvas>                        
                    </div>

                    <div class="col-lg-4">
                        <canvas id="graficoline_parametro" width="400" height="400"></canvas>
                    </div>
                    
                    
                </div>             
                
            </div>
        </div>
        <!--       <.CON PARAMETROS>       -->

    </div>
    
    <script src="source/libs/jquery/version/3.4.1/js/jquery-3.4.1.min.js"></script>
    <script src="source/libs/popper/version/1.16.0/js/popper.min.js"></script>
    <script src="source/libs/bootstrap/version/4.4.1/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>