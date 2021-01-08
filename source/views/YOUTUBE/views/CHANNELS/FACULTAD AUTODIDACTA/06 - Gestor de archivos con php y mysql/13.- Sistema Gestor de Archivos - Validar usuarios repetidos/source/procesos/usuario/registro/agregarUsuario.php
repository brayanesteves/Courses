<?php
    require_once "../../../clases/Usuarios.php";
    //echo "si paso";
    //print_r($_POST);
    $password = sha1($_POST['password']);
    $datos = array("nombre" => $_POST['nombre'], "fechaNacimiento" => $_POST['fechaNacimiento'], "correo" => $_POST['correo'], "usuario" => $_POST['usuario'], "password" => $password);
    $usuario = new Usuarios();
    echo $usuario->agregarUsuario($datos);
?>