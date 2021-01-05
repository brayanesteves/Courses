<?php
    // Importar la ruta del PHPExcel
    require_once 'source/libs/PHP/PHPExcel/version/1.8/Classes/PHPExcel.php';
    require_once 'source/controller/conexion.php';

    $archivos = 'source/files/documents/office/excel/producto.xlsx';

    // Cargar nuestra hoja de Excel
    $excel = PHPExcel_IOFactory::load($archivos);

    // Cargar la hoja de calculo que queremos
    $excel->setActiveSheetIndex(0);

    // Obtener el número de filas de nuestro archivo excel
    $numerofila = $excel->setActiveSheetIndex(0)->getHighestRow();
    //echo $numerofila;
    /**
     * $i = 2, es para que no me muestre la cabecera
     */
    for($i = 2; $i <= $numerofila; $i++) {
        /**
         * getCell('A') - Es la columna A del Excel
         */
        $idproducto = $excel->getActiveSheet()->getCell('A' . $i)->getCalculatedValue();
        if($idproducto != "") {
            $producto = $excel->getActiveSheet()->getCell('B' . $i)->getCalculatedValue();
            //echo $idproducto . " - ";
            //echo $producto . " - ";
            $CONSULTA = "INSERT INTO producto(`producto_id`, `producto_nombre`) VALUE('$idproducto', '$producto');";
            $resultado = $mysqli->query($CONSULTA);
        }
    }
?>