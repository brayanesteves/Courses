<?php
    class Modelo_Persona {
        private $conexion;
        function __construct() {
            require_once '../controller/conexion.php';
            $this->conexion = new conexion();
            $this->conexion->conectar();
        }

        function Registrar_Persona($nombres, $apellidos, $nombrearchivo){
            $sql = "call SP_REGISTRAR_PERSONA('$nombres', '$apellidos', '$nombrearchivo')";
            if($resultado = $this->conexion->conexion->query($sql)) {
                $id_retornado = mysqli_insert_id($this->conexion->conexion);
                return 1;
            } else {
                return 0;
            }
            $this->conexion->cerrar();
        }
    }
?>