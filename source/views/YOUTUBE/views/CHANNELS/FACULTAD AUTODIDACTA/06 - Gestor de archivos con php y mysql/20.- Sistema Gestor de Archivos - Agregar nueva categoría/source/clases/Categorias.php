<?php
    require_once "Conexion.php";
    class Categorias extends Conectar {
        public function agregarCategorias($datos) {
            $conexion  = Conectar::conexion();

            $sql       = "INSERT INTO `t_categorias`(`id_usuario`, `nombre`) VALUES (?, ?);";
            $query     = $conexion->prepare($sql);
            $query->bind_param('is', $datos['idUsuario'], $datos['categoria']);
            $respuesta = $query->execute();
            $query->close();

            return $respuesta;
        }
    }
?>