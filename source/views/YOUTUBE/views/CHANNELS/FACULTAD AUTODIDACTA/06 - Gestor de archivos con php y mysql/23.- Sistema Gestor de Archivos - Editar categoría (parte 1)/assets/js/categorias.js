function agregarCategoria() {
    var categoria = $('#nombreCategoria').val();
    if(categoria == "") {
        swal("Advertencia", "Debes agregar una categoria", "warning");
        return false;
    } else {
        $.ajax({
            type: "POST",
            data:'categoria=' + categoria,
            url:"../../source/procesos/categorias/agregar.php",
            success: function(respuesta) {
                respuesta = respuesta.trim();
                if (respuesta == 1) {
                    $('#tablaCategorias').load("ajax/tabla.php");
                    $('#nombreCategoria').val("");
                    swal(":D", "Agregado con éxito!", "success");
                } else {
                    swal(":(", "Falló al agregar!", "error");
                }
            }
        });
    }
}

function eliminarCategorias(idCategoria) {
    idCategoria = parseInt(idCategoria);
    if(idCategoria < 1) {
        swal(":(", "No tienes 'id' de categoria!", "error");
        return false;
    } else {
        //****************************************
        swal({
            title: "Estas seguro de eliminar esta categoria?",
            text: "Una vez eliminada, no podrá recuperarse!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
          })
          .then((willDelete) => {
              if (willDelete) {
                /**
                 * AJAX
                 */
                  $.ajax({
                      type: "POST",
                      data: "idCategoria=" + idCategoria,
                      url:"../../source/procesos/categorias/eliminar.php",
                      success: function (respuesta) {
                          respuesta = respuesta.trim();
                          if (respuesta == 1) {
                            $('#tablaCategorias').load("ajax/tabla.php");
                            swal("Eliminado con éxito!", { icon: "success", });
                          } else {
                            swal(":(", "Falló al eliminar!", "error");
                        }
                      }
                  });
                
            }
          });
        //****************************************
    }
}

function obtenerDatosCategoria(idCategoria) {
    $.ajax({
        type: "POST",
        data: "idCategoria=" + idCategoria,
        url: "../../source/procesos/categorias/editar.php",
        success: function(respuesta) {
            respuesta = jQuery.parseJSON(respuesta);
            console.log(respuesta);
            $('#idCategoria').val(respuesta['idCategoria']);
            $('#categoriaU').val(respuesta['nombreCategoria']);
        }
    });
}

function actualizarCategoria() {
    if($('#categoriaU').val() == "") {
        swal(":(", "No hay categoria!!", "error");
        return false;
    } else {
        $.ajax({
            type: "POST",
            data:$('#frmActualizarCategoria').serialize(),
            url:"../../source/procesos/categorias/actualizar.php",
            success: function(respuesta) {
                respuesta = respuesta.trim();
                if(respuesta == 1) {
                    $('#tablaCategorias').load("ajax/tabla.php");
                    swal(":D", "Actualizado con éxito!", "success");
                } else {
                    swal(":(", "Falló al actualizar!", "error");
                }
            }
        });
    }
}