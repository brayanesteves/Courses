<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="source/libs/bootstrap/version/4.4.1/css/bootstrap.min.css">

    <title>Subir archivos</title>
  </head>
  <body>
  
    <div class="col-lg-12" style="padding-top:10px;">
      <div class="row">
      
        <!--       <COLUMN Nº0>       -->
        <div class="col-lg-4">        
        </div>
        <!--       <.COLUMN Nº0>       -->

        <!--       <COLUMN Nº1>       -->
        <div class="col-lg-4">
          <div class="card">
              <img src="..." id="mostrarimagen" class="card-img-top" alt="...">
              <div class="card-body">
                  <h5 class="card-title">Vista del archivo</h5>
                  <!--       <FORM>       -->
                  <form action="POST" action="#" enctype="multipart/form-data" onsubmit="return false">

                    <div class="row">

                      <div class="col-lg-6">
                        <label for="">Nombres:</label>
                        <input type="text" name="" id="txt_nombres" class="form-control">
                      </div>

                      <div class="col-lg-6">
                        <label for="">Apellidos:</label>
                        <input type="text" name="" id="txt_apellidos" class="form-control">
                      </div>

                      <div class="col-lg-12">
                        <br>
                        <input type="file" name="" id="seleccionararchivo" class="form-control-file" accept="image/x-png, image/gif, image/jpeg">
                      </div>

                      <div class="col-lg-12" style="text-align:center;">
                        <button class="btn btn-primary" onclick="Registrar()">Guardar Datos</button>
                      </div>

                    </div>

                  </form>
                  <!--       <.FORM>       -->
              </div>
          </div>
        </div>
        <!--       <.COLUMN Nº1>       -->

        <!--       <COLUMN Nº2>       -->
        <div class="col-lg-4">        
        </div>
        <!--       <.COLUMN Nº2>       -->

      </div>
    </div>
    
    <script src="source/libs/jquery/version/3.4.1/js/jquery-3.4.1.min.js"></script>
    <script src="source/libs/popper/version/1.16.0/js/popper.min.js"></script>
    <script src="source/libs/bootstrap/version/4.4.1/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>
    <script src="assets/js/main.js"></script>
  </body>
</html>