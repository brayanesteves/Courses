<?php
    require_once '../model/excel.php';
    $ME = new Modelo_Excel();

    $idproducto = htmlspecialchars($_POST['id'], ENT_QUOTES, 'UTF-8');
    $producto   = htmlspecialchars($_POST['p'],  ENT_QUOTES, 'UTF-8');

    // Cuando encuentra una coma ',' lo separa y lo convierte en un arreglo
    $array_id       = explode(',', $idproducto);
    // Cuando encuentra una coma ',' lo separa y lo convierte en un arreglo
    $array_producto = explode(',', $producto);

    for($i = 0; $i < count($array_id); $i++) {
        $consulta = $ME->Registrar_Excel($array_id[$i], $array_producto[$i]);
    }
    echo $consulta;
?>