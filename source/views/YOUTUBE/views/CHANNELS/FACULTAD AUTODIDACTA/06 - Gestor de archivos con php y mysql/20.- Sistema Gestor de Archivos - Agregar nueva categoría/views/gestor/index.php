<?php
    session_start();
    if(isset($_SESSION['usuario'])):
        include '../layout/default/header.php';        
?>
<div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">Gestor de archivos</h1>
    <div id="tablaGestorArchivos"></div>
  </div>
</div>
<?php
        include '../layout/default/footer.php';
    else:
        header("location:../../index.php");
    endif; 
?>