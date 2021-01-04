<?php
    require_once '../model/persona.php';
    $MP = new Modelo_Persona();
    $nombres = htmlspecialchars($_POST['n'], ENT_QUOTES, 'UTF-8');
    $apellidos = htmlspecialchars($_POST['a'], ENT_QUOTES, 'UTF-8');
    $nombrearchivo = htmlspecialchars($_POST['nombrearchivo'], ENT_QUOTES, 'UTF-8');

    if(is_array($_FILES) && count($_FILES) > 0) {
        /**
         * Mover el archivo al servidor
        */
        if(move_uploaded_file($_FILES["f"]["tmp_name"], "../files/img/" . $nombrearchivo)) {
            $nombrearchivo = "files/img/" . $nombrearchivo;
            $consulta = $MP->Registrar_Persona($nombres, $apellidos, $nombrearchivo);
            echo $consulta;
        } else {
            echo 0;
        }
    } else {
        echo 0;
    }
?>