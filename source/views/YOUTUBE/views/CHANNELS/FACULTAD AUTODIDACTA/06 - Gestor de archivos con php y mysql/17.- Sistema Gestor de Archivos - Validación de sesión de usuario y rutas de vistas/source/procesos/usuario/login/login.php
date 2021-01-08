<?php
    session_start();
    //print_r($_POST);
    require_once "../../../clases/Usuarios.php";

    $usuario  = $_POST['login'];
    $password = sha1($_POST['password']);

    $usuarioObj  = new Usuarios();

    echo $usuarioObj->login($usuario, $password);
?>