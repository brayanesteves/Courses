<?php
    session_start();

    require_once "../../clases/categorias.php";
    $Categorias = new Categorias();
    $datos      = array("idUsuario" => $_SESSION['idUsuario'], "categoria" => $_POST['categoria']);
    
    echo $Categorias->agregarCategorias($datos);
?>