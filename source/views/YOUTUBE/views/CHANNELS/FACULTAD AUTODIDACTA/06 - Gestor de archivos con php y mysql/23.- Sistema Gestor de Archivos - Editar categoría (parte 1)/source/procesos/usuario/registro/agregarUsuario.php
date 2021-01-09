<?php
    require_once "../../../clases/Usuarios.php";
    //echo "si paso";
    //print_r($_POST);
    $password = sha1($_POST['password']);
    $fechaNacimiento = explode("-", $_POST['fechaNacimiento']);
    /**
     * $fechaNacimiento[2] = Año
     * $fechaNacimiento[1] = Mes
     * $fechaNacimiento[0] = Día
     */
    $fechaNacimiento = $fechaNacimiento[2] . "-" . $fechaNacimiento[1] . "-" . $fechaNacimiento[0];
    $datos = array("nombre" => $_POST['nombre'], "fechaNacimiento" => $fechaNacimiento, "correo" => $_POST['correo'], "usuario" => $_POST['usuario'], "password" => $password);
    $usuario = new Usuarios();
    echo $usuario->agregarUsuario($datos);
?>