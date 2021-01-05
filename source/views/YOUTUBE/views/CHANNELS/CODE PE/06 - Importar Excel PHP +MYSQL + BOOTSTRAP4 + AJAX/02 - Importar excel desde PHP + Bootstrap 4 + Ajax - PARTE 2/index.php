<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="source/libs/HTML, CSS & JS/bootstrap/version/4.4.1/css/bootstrap.min.css">

    <title>Subir archivos</title>
  </head>
  <body>
    <div class="col-lg-12">
        <div class="card">
            <div class="card-header" style="padding-top:20px;">
                <b>Importar Excel</b>
            </div>
            <div class="card-body">                

                <form action="#" enctype="multipart/form-data">
                        
                    <div class="row">

                        <div class="col-lg-8">
                            <input type="file" name="" id="txt_archivo" class="form-control" accept=".csv, .xlsx, .xls">
                            <br>
                        </div>

                        <div class="col-lg-2">
                            <button class="btn btn-danger" style="width:100%;" onclick="CargarExcel()">Cargar Excel</button>
                            <br>
                        </div>

                        <div class="col-lg-2">
                            <button class="btn btn-primary" style="width:100%;" onclick="Registrar_Excel()" disabled id="btn_registrar">Registrar Excel</Guardar Datos</button>
                            <br>
                        </div>

                        <div class="col-lg-12" id="div_table">
                            <br>
                        </div>
                    </div>

                </form>            

            </div>
        </div>
    </div>
    
    <script src="source/libs/HTML, CSS & JS/jquery/version/3.4.1/js/jquery-3.4.1.min.js"></script>
    <script src="source/libs/HTML, CSS & JS/popper/version/1.16.0/js/popper.min.js"></script>
    <script src="source/libs/HTML, CSS & JS/bootstrap/version/4.4.1/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>