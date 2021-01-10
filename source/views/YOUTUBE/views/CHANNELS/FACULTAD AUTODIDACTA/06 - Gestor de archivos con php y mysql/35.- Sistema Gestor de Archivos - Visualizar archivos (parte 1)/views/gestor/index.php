<?php
    session_start();
    if(isset($_SESSION['usuario'])):
        include '../layout/default/header.php';        
?>
<div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">Gestor de archivos</h1>
    <span class="btn btn-primary" data-toggle="modal" data-target="#modalAgregarArchivos"><span class="fas fa-plus-circle"></span> Agregar archivos</span>
    <hr>
    <div id="tablaGestorArchivos"></div>
  </div>
</div>

<!-- Modal para agregar archivos-->
<div class="modal fade" id="modalAgregarArchivos" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="" id="frmArchivos" enctype="multipart/form-data" method="POST">
            <label>Categoria</label>
            <div id="categoriasLoad"></div>
            <label>Selecciona archivos</label>
            <input type="file" name="archivos[]" id="archivos[]" class="form-control" multiple="">
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
        <button type="button" class="btn btn-primary" id="btnGuardarArchivos">Guardar</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal -->
<div class="modal fade" id="visualizarArchivo" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Archivo</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
      </div>
    </div>
  </div>
</div>
<?php
      include '../layout/default/footer.php';
    else:
        header("location:../../index.php");
    endif; 
?>