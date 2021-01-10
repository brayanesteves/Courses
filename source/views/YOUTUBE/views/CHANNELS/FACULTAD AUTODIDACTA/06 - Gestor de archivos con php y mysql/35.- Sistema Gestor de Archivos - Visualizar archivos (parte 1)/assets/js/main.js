
$(document).ready(function() {
    $('#tablaGestorArchivos').load("ajax/tabla.php");
    $('#categoriasLoad').load("../categorias/ajax/select.php");
    $('#btnGuardarArchivos').click(function () { 
        agregarArchivosGestor();
    });

    $('#tablaCategorias').load("ajax/tabla.php");

    $('#btnGuardarCategoria').click(function() {
        agregarCategoria();
    });
});

$('#btnActualizarCategoria').click(function() {
    actualizarCategoria();
});

//                       <REGISTRAR USUARIO>                       //
$(function() {
    var fechaA = new Date();
    var yyyy = fechaA.getFullYear();

    $("#fechaNacimiento").datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: '1990:' + true,
        dateFormat: 'dd-mm-yy'
    });
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
//                       <.REGISTRAR USUARIO>                       //

//                       <LOGIN>                       //
function logear() {
    $.ajax({
        type: "POST",
        data: $('#frmLogin').serialize(),
        url:'source/procesos/usuario/login/login.php',
        success: function (respuesta) {
            //alert(respuesta);
            respuesta = respuesta.trim();
            if(respuesta == 1) {
                window.location = "views/inicio/inicio.php";
            } else {
                swal(":(", "Fallo al entrar!", "error");
            }
        }
    });
    return false;
}
//                       <.LOGIN>                       //