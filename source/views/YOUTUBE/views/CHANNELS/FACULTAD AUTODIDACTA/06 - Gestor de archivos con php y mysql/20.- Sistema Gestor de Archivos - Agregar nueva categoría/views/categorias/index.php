<?php
    session_start();
    if(isset($_SESSION['usuario'])):
        include '../layout/default/header.php';        
?>
    <div class="jumbotron jumbotron-fluid">
        <div class="container">
            <h1 class="display-4">Categorías</h1>

            <div class="row">
                <div class="col-sm-4">
                    <span class="btn btn-primary" data-toggle="modal" data-target="#modalAgregaCategoria"><span class="fas fa-plus circle"></span> Agregar nueva categoria</span>
                </div>
            </div>
            <hr>
            <div class="row">

                <div class="col-sm-12">
                    <div id="tablaCategorias"></div>
                </div>

            </div>            
        </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="modalAgregaCategoria" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-sm" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Agregar nueva categoria</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="" id="frmCategorias">
                    
                    <label>Nombre de la categoria</label>
                    <input type="text" name="nombreCategoria" id="nombreCategoria" class="form-control">

                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                <button type="button" class="btn btn-primary" id="btnGuardarCategoria">Guardar</button>
            </div>
            </div>
        </div>
    </div>
<?php
    include '../layout/default/footer.php';
?>
<?php
    else:
        header("location:../../index.php");
    endif; 
?>