<?php
    require_once "Conexion.php";
    class Gestor extends Conectar {
        /**
         * Esto va a agregar un registro a la base de datos que va relacionado al 
         * archivo que voy a subir en el formulario, por eso es necesario
         */
        public function agregarRegistroArchivo($datos) {
            $conexion  = Conectar::conexion();

            $sql       = "INSERT INTO `t_archivos`(`id_usuario` ,`id_categoria`, `nombre`, `tipo`, `ruta`) VALUES(?, ?, ?, ?, ?);";
            $query     = $conexion->prepare($sql);
            $query->bind_param("iisss", $datos['idUsuario'], $datos['idCategoria'], $datos['nombreArchivo'], $datos['tipo'], $datos['ruta']);
            $respuesta = $query->execute();
            $query->close();
            return $respuesta;
        }
    }
?>