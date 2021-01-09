<?php
    session_start();
    if(isset($_SESSION['idUsuario'])):
        require_once "../../../source/clases/Conexion.php";
        $c         = new Conectar();
        $conexion  = $c->conexion();
        $idUsuario = $_SESSION['idUsuario'];
        $sql       = "SELECT `archivos`.`id_archivo` AS `idArchivo`, `archivos`.`id_usuario` AS `idUsuario`, `archivos`.`nombre` AS `nombreArchivo`, `archivos`.`tipo` AS `tipoArchivo`, `archivos`.`ruta` AS `rutaArchivo`, `archivos`.`fecha` AS `fecha`, `usuarios`.`nombre` AS `nombreUsuario`, `categorias`.`nombre` AS `categorias` FROM `t_archivos` AS `archivos` INNER JOIN `t_usuarios` AS `usuarios` ON `archivos`.`id_usuario` = `usuarios`.`id_usuario` INNER JOIN `t_categorias` AS `categorias` ON `archivos`.`id_categoria` = `categorias`.`id_categoria` WHERE `archivos`.`id_usuario` = '$idUsuario';";
        $result    = mysqli_query($conexion, $sql);
?>
<div class="row">

    <div class="col-sm-12">
        <div class="table-responsive">
            <table class="table table-hover table-dark" id="tablaGestorDataTable">

                <thead>
                    <tr>
                        <th scope="col">Nombre</th>
                        <th scope="col">Tipo de archivo</th>
                        <th scope="col">Descargar</th>
                        <th scope="col">Visualizar</th>
                        <th scope="col">Eliminar</th>
                    </tr>
                </thead>

                <tbody>
                <?php 
                    while ($mostrar = mysqli_fetch_array($result)):
                        $rutaDescarga = "../../source/documents/" . $idUsuario . "/office/" . $mostrar['tipoArchivo'] . "/" . $mostrar['nombreArchivo'];
                        $nombreArchivo = $mostrar['nombreArchivo'];
                ?>
                    <tr>
                        <td><?php echo $mostrar['nombreArchivo']; ?></td>
                        <td><?php echo $mostrar['tipoArchivo']; ?></td>
                        <td>
                            <a href="<?php echo $rutaDescarga; ?>" download="<?php echo $nombreArchivo; ?>" class="btn btn-success btn-sm"><span class="fas fa-download"></span></a>
                        </td>
                        <td></td>
                        <td>
                            <span class="btn btn-danger btn-sm"><span class="fas fa-trash-alt"></span></span>
                        </td>
                    </tr>
                <?php endwhile; ?>
                </tbody>

            </table>
        </div>
    </div>

</div>

<?php
    include '../layout/default/footer.php'; 
?>
<script type="text/javascript">
    $(document).ready(function() {    
        $('#tablaGestorDataTable').DataTable();
    });
</script>
<?php
    endif; 
?>
