<?php
    if(is_array($_FILES['archivoexcel']) && count($_FILES['archivoexcel'] > 0)) {
        // Llamamos a nuestra libreria PHPExcel
        require_once '../libs/PHP/PHPExcel/version/1.8/Classes/PHPExcel.php';
        require_once 'conexion.php';

        /**
         * Es un archivo temporal
         */
        $tmpfname  = $_FILES['archivoexcel']['tmp_name'];
        // CREAR EL EXCEL PARA LUEGO LEERLO
        $leerexcel = PHPExcel_IOFactory::createReaderForFile($tmpfname);

        // CARGAR NUESTRO EXCEL
        $excelobj  = $leerexcel->load($tmpfname);

        // CARGAR EN QUE HOJA TRABAJAREMOS
        $hoja      = $excelobj->getSheet(0);
        // Cuenta las filas que se estan ocupando con datos en el Excel
        $filas     = $hoja->getHighestRow();
        //echo $filas;
        echo "<table id='tabla_detalle' class='table-responsive' style='width:100%; table-layout:fixed;'><thead><tr><td>ID</td><td>PRODUCTO</td></tr></thead><tbody id='tbody_tabla_detalle'>";
        for($row = 2; $row <= $filas; $row++) {
            $ID = $hoja->getCell('A' . $row)->getValue();
            $PRODUCTO = $hoja->getCell('B' . $row)->getValue();
            echo "<tr>";
            echo "<td>" . $ID . "</td>";
            echo "<td>" . $PRODUCTO . "</td>";
            echo "</tr>";
        }        
        echo "</tbody></table>";

    }
?>