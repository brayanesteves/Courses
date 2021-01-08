<?php
    session_start();
    if(isset($_SESSION['usuario'])):           
?>
<div class="table table-responsive table-hover">

    <table class="table table-hover table-dark" id="tablaCategoriasDataTable">
        <thead>
            <th>Nombre</th>
            <th>Fecha</th>
            <th>Editar</th>
            <th>Eliminar</th>
        </thead>

        <tbody>
            <tr>
                <td></td>
                <td></td>
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