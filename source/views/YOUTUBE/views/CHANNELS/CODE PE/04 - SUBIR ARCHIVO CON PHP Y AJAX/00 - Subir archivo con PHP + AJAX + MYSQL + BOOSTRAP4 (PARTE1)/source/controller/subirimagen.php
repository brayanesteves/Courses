<?php
    $nombres = $_POST['n'];
    $apellidos = $_POST['a'];
    if(is_array($_FILES) && count($_FILES) > 0) {
        /**
         * Mover el archivo al servidor
        */
        if(move_uploaded_file($_FILES["f"]["tmp_name"], "../files/img/" . $_FILES["f"]["name"])) {
            echo 1;
        } else {
            echo 0;
        }
    } else {
        echo 0;
    }
?>