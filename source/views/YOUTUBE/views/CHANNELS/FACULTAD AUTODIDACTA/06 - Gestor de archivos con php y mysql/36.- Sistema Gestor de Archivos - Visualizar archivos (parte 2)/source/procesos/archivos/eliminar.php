<?php
    session_start();
    require_once "../../clases/Gestor.php";
    $Gestor      = new Gestor();
    
    /**
     * gestor.js ubicado en assets/js/
     * function eliminarArchivo(idArchivo)
     * data:"idArchivo=" + idArchivo, => idArchivo
     */
    $idArchivo     = $_POST['idArchivo'];
    $idUsuario     = $_SESSION['idUsuario'];

    $nombreArchivo = $Gestor->obtenNombreArchivo($idArchivo);
    $tipoArchivo   = $Gestor->obtenTipoArchivo($idArchivo);
    if($nombreArchivo == "") {
        echo 1;
    } else {
        $rutaEliminar = "../../documents/" . $idUsuario . "/office/" . $tipoArchivo . "/" . $nombreArchivo;
        if(unlink($rutaEliminar)) {
            echo $Gestor->eliminarRegistroArchivo($idArchivo);
        } else {
            echo 0;
        }
    }


    
?>