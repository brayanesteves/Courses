
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
            //console.log(respuesta);
            respuesta = respuesta.trim();
            if(respuesta == 1) {
                $("#frmRegistro")[0].reset();  
                swal(":D", "Agregado con exito!", "success");
            } else if(respuesta == 2) {
                swal("Advertencia", "Este usuario ya existe, por favor escribe otro !!!", "warning");
             }else {
                swal(":D", "Fallo al agregar!", "error");
            }
        }
    });
    return false;
}