<?php
    session_start();
    require_once "../../clases/Categorias.php";
    $c = new Conectar();
    $conexion = $c->conexion();
?>