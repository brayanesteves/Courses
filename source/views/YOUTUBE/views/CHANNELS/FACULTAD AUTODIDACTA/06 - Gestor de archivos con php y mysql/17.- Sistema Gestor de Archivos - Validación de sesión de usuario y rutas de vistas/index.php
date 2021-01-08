<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="assets/css/login.css">
    <link href="source/libs/css&js/bootstrap/version/4.4.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link href="source/libs/css&js/jquery/plugins/ui/version/1.12.1/js/jquery-ui.css" rel="stylesheet">
    <link href="source/libs/css&js/jquery/plugins/ui/version/1.12.1/js/jquery-ui.theme.min.css" rel="stylesheet">
</head>
<body>
    <div class="wrapper fadeInDown">
        <div id="formContent">
            <!-- Tabs Titles -->

            <!-- Icon -->
            <div class="fadeIn first">
            <img src="assets/img/png/300x296.png" id="icon" alt="User Icon" />
            <h1>Gestor de archivos</h1>
            </div>

            <!-- Login Form -->
            <form method="POST" id="frmLogin" action="" onsubmit="return logear()">
                <input type="text" id="login" class="fadeIn second" name="login" placeholder="username" required="">
                <input type="password" id="password" class="fadeIn third" name="password" placeholder="password" required="">
                <input type="submit" class="fadeIn fourth" value="Entrar">
            </form>

            <!-- Remind Passowrd -->
            <div id="formFooter">
            <a class="underlineHover" href="registro.php">Registrar</a>
            </div>

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