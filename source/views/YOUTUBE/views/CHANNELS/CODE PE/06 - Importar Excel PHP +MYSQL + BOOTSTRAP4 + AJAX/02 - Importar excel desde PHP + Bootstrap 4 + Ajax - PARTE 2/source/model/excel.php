<?php
    class Modelo_Excel {
        private $conexion;
        function __construct() {
            require_once '../model/conexion.php';
            $this->conexion = new conexion();
            $this->conexion->conectar();
        }

        function Registrar_Excel($id, $producto) {
            $sql = "call PA_REGISTRAR_PRODUCTO_EXCEL('$id', '$producto')";
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