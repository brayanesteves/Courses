<?php
    session_start();
    if(isset($_SESSION['usuario'])):
        require_once "../../../source/clases/Conexion.php";
        $idUsuario = $_SESSION['idUsuario'];
        $conexion  = new Conectar();
        $conexion  = $conexion->conexion();
?>
<div class="table-responsive">

    <table class="table table-hover table-dark" id="tablaCategoriasDataTable">
        <thead>
            <th>Nombre</th>
            <th>Fecha</th>
            <th>Editar</th>
            <th>Eliminar</th>
        </thead>

        <tbody>
        <?php
            $sql             = "SELECT `id_categoria`, `nombre`, `fechaInsert` FROM `t_categorias` WHERE `id_usuario` = '$idUsuario';";
            $result          = mysqli_query($conexion, $sql);
            while($mostrar   = mysqli_fetch_array($result)):  
                $idCategoria = $mostrar['id_categoria'];              
        ?>
            <tr>
                <td><?php echo $mostrar['nombre']; ?></td>
                <td><?php echo $mostrar['fechaInsert']; ?></td>
                <td>
                    <span class="btn btn-warning btn-sm" style="text-align:center;">
                        <span class="fas fa-edit"></span>
                    </span>
                </td>
                <td>
                    <span class="btn btn-primary btn-sm" style="text-align:center;">
                        <span class="fas fa-trash-alt"></span>
                    </span>
                </td>
            </tr>
            <?php endwhile; ?>
        </tbody>
    </table>

</div>

<?php
    include '../layout/default/footer.php'; 
?>
<script type="text/javascript">
    $(document).ready(function() {    
        $('#tablaCategoriasDataTable').DataTable();
    });
</script>
<?php 
    endif; 
?>