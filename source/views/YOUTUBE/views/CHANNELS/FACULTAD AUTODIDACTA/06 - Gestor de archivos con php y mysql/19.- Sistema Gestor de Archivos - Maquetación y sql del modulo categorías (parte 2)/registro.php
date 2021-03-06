<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro</title>
    <link href="source/libs/css&js/bootstrap/version/4.4.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link href="source/libs/css&js/jquery/plugins/ui/version/1.12.1/js/jquery-ui.css" rel="stylesheet">
    <link href="source/libs/css&js/jquery/plugins/ui/version/1.12.1/js/jquery-ui.theme.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="text-center">Registro de usuario</h1>
        <hr>
        <div class="row">
            
            <div class="col-sm-4"></div>

            <div class="col-sm-4">

                <form action="" id="frmRegistro" method="POST" onsubmit="return agregarUsuarioNuevo()" autocomplete="off">                    
                    <label>Nombre personal</label>
                    <input type="text" name="nombre" id="nombre" class="form-control" required="">
    
                    <label>Fecha de nacimiento</label>
                    <input type="text" name="fechaNacimiento" id="fechaNacimiento" class="form-control" required="" readonly="">
    
                    <label>Email o correo</label>
                    <input type="email" name="correo" id="correo" class="form-control" required="">
    
                    <label>Nombre de usuario</label>
                    <input type="text" name="usuario" id="usuario" class="form-control" required="">
    
                    <label>Password o contraseña</label>
                    <input type="password" name="password" id="password" class="form-control" required="">

                    <br>
                    
                    <div class="row">
                        
                        <div class="col-sm-6 text-left">
                            <button class="btn btn-primary">Registrar</button>                            
                        </div>
                        
                        <div class="col-sm-6 text-right">
                            <a href="index.php" class="btn btn-success">Login</a>
                        </div>                        
                        
                    </div>
                </form>
            </div>

            <div class="col-sm-4"></div>

        </div>
    </div>

    <script src="source/libs/css&js/jquery/version/3.2.1/js/jquery.min.js"></script>
    <script src="source/libs/css&js/jquery/plugins/ui/version/1.12.1/js/jquery-ui.min.js"></script>
    <script src="source/libs/css&js/popper/version/1.12.9/js/popper.min.js"></script>
    <script src="source/libs/css&js/bootstrap/version/4.4.1/js/bootstrap.min.js"></script>
    <script src="source/libs/css&js/sweetalert/version/2.1.2/js/sweetalert.min.js"></script>
    <script src="assets/js/main.js"></script>
</body>
</html>