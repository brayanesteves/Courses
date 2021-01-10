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

        public function obtenNombreArchivo($idArchivo) {
            $conexion  = Conectar::conexion();
            $sql       = "SELECT `nombre` FROM `t_archivos` WHERE `id_archivo` = '$idArchivo';";
            $result    = mysqli_query($conexion, $sql);
            return mysqli_fetch_array($result)['nombre'];
        }
        public function obtenTipoArchivo($idArchivo) {
            $conexion  = Conectar::conexion();
            $sql       = "SELECT `tipo` FROM `t_archivos` WHERE `id_archivo` = '$idArchivo';";
            $result    = mysqli_query($conexion, $sql);
            return mysqli_fetch_array($result)['tipo'];
        }

        public function eliminarRegistroArchivo($idArchivo) {
            $conexion  = Conectar::conexion();
            $sql       = "DELETE FROM `t_archivos` WHERE `id_archivo` = ?;";
            $query     = $conexion->prepare($sql);
            $query->bind_param('i', $idArchivo);
            $respuesta = $query->execute();
            $query->close();
            return $respuesta;  
        }

        public function obtenerRutaArchivo($idArchivo) {
            $conexion      = Conectar::conexion();
            
            $sql           = "SELECT `nombre`, `tipo` FROM `t_archivos` WHERE `id_archivo` = '$idArchivo';";
            $result        = mysqli_query($conexion, $sql);
            $datos         = mysqli_fetch_array($result);
            $nombreArchivo = $datos['nombre'];
            $extension     = $datos['tipo'];

            return self::tipoArchivo($nombreArchivo, $extension);
        }

        public function tipoArchivo($nombre, $extension) {
            $idUsuario = $_SESSION['idUsuario'];
            $ruta = "../documents/" . $idUsuario . "/";
            switch ($extension) {
                case 'xlsx':
                    break;

                case 'xls':
                    break;

                case 'csv':
                    break;

                case 'png':
                    return '<img src="' . $ruta . 'img/' . $extension . '/' . $nombre . '"';
                    break;

                default:
                    break;
            }
        }
    }
?>