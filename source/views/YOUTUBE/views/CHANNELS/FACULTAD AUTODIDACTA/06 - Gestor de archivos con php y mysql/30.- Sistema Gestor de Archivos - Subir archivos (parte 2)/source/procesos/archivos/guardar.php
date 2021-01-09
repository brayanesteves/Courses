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
        $carpeta = "../../documents/";
        /**
         * Contatenamos el ID del usuario
         */
        $carpetaUsuario = "../../documents/" . $_SESSION['idUsuario'];
        /**
         * Si no existe $carpeta que es la carpeta 'documents' más el nombre del usuario del
         * que se encuentra ubicada en 'source', creamos la carpeta 'documents' y la carpeta del
         * nombre del usuario que sube los archivos
         */
        if(!file_exists($carpetaUsuario)) {
            /**
             * 0777
             */
            mkdir($carpetaUsuario, 0777, true);
        }
        $totalArchivos = count($_FILES['archivos']['name']);        
        for($i = 0; $i < $totalArchivos; $i++) {
            //echo $_FILES['archivos']['name'][$i];
            /**
             * Extensión del archivo
             */
            $nombreArchivo      = $_FILES['archivos']['name'][$i];
            $explode            = explode(".", $nombreArchivo);
            $tipoArchivo        = array_pop($explode);
            $rutaAlmacenamiento = $_FILES['archivos']['tmp_name'][$i];

            switch($tipoArchivo) {
                case "xlsx":
                    if(!file_exists($carpetaUsuario . "/" . "office/" . $tipoArchivo)) {
                        mkdir($carpetaUsuario . "/" . "office/" . $tipoArchivo, 0777, true);
                        $datosRegistroArchivo = array("idUsuario" => $idUsuario, "idCategoria" => $idCategoria, "nombreArchivo" => $nombreArchivo, "tipo" => $tipoArchivo, "ruta" => $carpetaUsuario . "/" . "office/" . $tipoArchivo);
                        if(move_uploaded_file($rutaAlmacenamiento, $carpetaUsuario . "/" . "office/" . $tipoArchivo . "/" . $nombreArchivo)) {
                            $respuesta = $Gestor->agregarRegistroArchivo($datosRegistroArchivo);
                            echo $respuesta;
                        }
                    }
                    break;
                
                case "xls":
                    if(!file_exists($carpetaUsuario . "/" . "office/" . $tipoArchivo)) { 
                        mkdir($carpetaUsuario . "/" . "office/" . $tipoArchivo, 0777, true);
                        $datosRegistroArchivo = array("idUsuario" => $idUsuario, "idCategoria" => $idCategoria, "nombreArchivo" => $nombreArchivo, "tipo" => $tipoArchivo, "ruta" => $carpetaUsuario . "/" . "office/" . $tipoArchivo);
                        if(move_uploaded_file($rutaAlmacenamiento, $carpetaUsuario . "/" . "office/" . $tipoArchivo . "/" . $nombreArchivo)) {
                            $respuesta = $Gestor->agregarRegistroArchivo($datosRegistroArchivo);
                            echo $respuesta;
                        }
                    }
                    break;
                
                case "csv":
                    if(!file_exists($carpetaUsuario . "/" . "office/" . $tipoArchivo)) {
                        mkdir($carpetaUsuario . "/" . "office/" . $tipoArchivo, 0777, true);
                        $datosRegistroArchivo = array("idUsuario" => $idUsuario, "idCategoria" => $idCategoria, "nombreArchivo" => $nombreArchivo, "tipo" => $tipoArchivo, "ruta" => $carpetaUsuario . "/" . "office/" . $tipoArchivo);
                        if(move_uploaded_file($rutaAlmacenamiento, $carpetaUsuario . "/" . "office/" . $tipoArchivo . "/" . $nombreArchivo)) {
                            $respuesta = $Gestor->agregarRegistroArchivo($datosRegistroArchivo);
                            echo $respuesta;
                        }
                    }
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