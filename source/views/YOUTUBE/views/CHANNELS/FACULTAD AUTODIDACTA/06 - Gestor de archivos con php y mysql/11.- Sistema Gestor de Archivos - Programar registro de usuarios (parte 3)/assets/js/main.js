
$(document).ready(function() {
    $('#tablaGestorArchivos').load("ajax/tabla.php");
});

function agregarUsuarioNuevo() {
    $.ajax({
        method: "POST",
        data: $('#frmRegistro').serialize(),
        url: "source/procesos/usuario/registro/agregarUsuario.php",
        success: function(respuesta) {
            //alert(respuesta);
            console.log(respuesta);
        }
    });
    return false;
}