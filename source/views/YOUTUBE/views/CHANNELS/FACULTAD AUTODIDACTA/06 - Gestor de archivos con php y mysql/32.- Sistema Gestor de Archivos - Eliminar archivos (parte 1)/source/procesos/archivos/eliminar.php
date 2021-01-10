<?php
    session_start();
    require_once "../../clases/Gestor.php";
    $Gestor      = new Gestor();
    /**
     * gestor.js ubicado en assets/js/
     * function eliminarArchivo(idArchivo)
     * data:"idArchivo=" + idArchivo, => idArchivo
     */
    $idArchivo = $_POST['idArchivo'];


    echo $Gestor->eliminarRegistroArchivo($idArchivo);
?>