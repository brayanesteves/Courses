<?php
    //print_r($_FILES);
    /**
     * Array
     *  (
     *      [archivos] => Array
     *          (
     *              [name] => producto.xlsx
     *              [type] => application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
     *              [tmp_name] => C:\wamp\tmp\phpC101.tmp
     *              [error] => 0
     *              [size] => 9900
     *          )
     *
     *  )
     */
    //print_r($_POST);
    /**
     * 
     */
    session_start();
    require_once "../../clases/Gestor.php";
    $Gestor      = new Gestor();

    $idCategoria = $_POST['categoriasArchivos'];
    $idUsuario   = $_SESSION['idUsuario'];

    if($_FILES['archivos']['size'] > 0) {
        $totalArchivos = count($_FILES['archivos']['name']);        
        for($i = 0; $i < $totalArchivos; $i++) {
            //echo $_FILES['archivos']['name'][$i];
            /**
             * Extensión del archivo
             */
            $nombreArchivo = $_FILES['archivos']['name'][$i];
            $explode = explode(".", $nombreArchivo);
            $tipoArchivo = array_pop($explode);
            $rutaAlmacenamiento = $_FILES['archivos']['tmp_name'][$i];
            $carpeta = "../../documents/";
            switch($tipoArchivo) {
                case "xlsx":
                    echo move_uploaded_file($rutaAlmacenamiento, $carpeta . "office/" . $tipoArchivo . "/" . $nombreArchivo);
                    break;
                
                case "xls":
                    echo move_uploaded_file($rutaAlmacenamiento, $carpeta . "office/" . $tipoArchivo . "/" . $nombreArchivo);
                    break;
                
                case "csv":
                    echo move_uploaded_file($rutaAlmacenamiento, $carpeta . "office/" . $tipoArchivo . "/" . $nombreArchivo);
                    break;

                default:
                    echo 2;
                    break;
            }
        } 
    } else {
        echo 0;
    }

?>