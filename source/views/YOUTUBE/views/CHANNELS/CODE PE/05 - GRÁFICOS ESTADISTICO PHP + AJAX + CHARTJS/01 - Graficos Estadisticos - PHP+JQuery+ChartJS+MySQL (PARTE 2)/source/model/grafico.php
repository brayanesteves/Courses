<?php
    class Modelo_Grafico {
        private $conexion;
        function __construct() {
            require_once('../controller/conexion.php');
            $this->conexion = new conexion();
            $this->conexion->conectar();
        }

        function TraerDatosGraficoBar() {
            $sql = "CALL `SP_DATOSGRAFICOS_BAR`();";
            $arreglo = array();
            if($consulta = $this->conexion->conexion->query($sql)) {
                while($consulta_VU = mysqli_fetch_array($consulta)) {
                    $arreglo[] = $consulta_VU;                    
                }
                
                return $arreglo;
                $this->conexion->cerrar();
            }
        }

        function TraerDatosGraficoParametro($fechainicio, $fechafin) {
            $sql = "CALL `SP_DATOSGRAFICOS_PARAMETRO`('$fechainicio', '$fechafin');";
            $arreglo = array();
            if($consulta = $this->conexion->conexion->query($sql)) {
                while($consulta_VU = mysqli_fetch_array($consulta)) {
                    $arreglo[] = $consulta_VU;                    
                }
                
                return $arreglo;
                $this->conexion->cerrar();
            }
        }
    }
?>