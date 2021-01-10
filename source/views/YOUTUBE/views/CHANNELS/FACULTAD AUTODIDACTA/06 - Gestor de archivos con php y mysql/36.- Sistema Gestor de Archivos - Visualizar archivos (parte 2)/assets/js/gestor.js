function agregarArchivosGestor() {
    var formData = new FormData(document.getElementById('frmArchivos'));
        $.ajax({
            url:"../../source/procesos/archivos/guardar.php",
            type:"POST",
            datatype: "html",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function(respuesta) {
                console.log(respuesta);
                /**
                 * print_r($_FILES); "procesos/archivos/guardar.php"
                 * Array
                 *  (
                 *      [archivos] => Array
                 *          (
                 *              [name] => producto.xlsx
                 *              [type] => application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
                 *              [tmp_name] => C:\wamp\tmp\phpC101.tmp
                 *              [error] => 0
                 *              [size] => 9900
                 *          )
                 *
                 *  )
                 * 
                 * print_r($_POST); "procesos/archivos/guardar.php"
                 * Array
                 *  (
                 *      [categoriasArchivos] => 2
                 *  )
                 */
                respuesta = respuesta.trim();
                if (respuesta == 1) {
                    $('#frmArchivos')[0].reset();
                    $('#tablaGestorArchivos').load("ajax/tabla.php");
                    swal(":D", "Agregado con éxito!", "success");
                } else if(respuesta == 2) { 
                    swal("Advertencia", "Tipo de archivo no permitido", "warning");
                }
                else {
                    swal(":(", "Falló al agregar !", "error");
                }
            }
        });
}

function eliminarArchivo(idArchivo) {
    swal({
        title: "Estas seguro de eliminar este archivo?",
        text: "Una vez eliminado, no podrá recuperarse!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
          if (willDelete) {
              $.ajax({
                  type: "POST",
                  data:"idArchivo=" + idArchivo,
                  url:"../../source/procesos/archivos/eliminar.php",
                  success: function (respuesta) {
                      respuesta = respuesta.trim();
                      if (respuesta == 1) {                            
                            $('#tablaGestorArchivos').load("ajax/tabla.php");
                            swal("Eliminado con éxito!", {
                                icon: "success",
                            });                          
                      } else {
                        swal("Error al eliminar!", {
                            icon: "error",
                        });
                      }
                  }
              });
        }        
      });
}

function obtenerArchivoPorId(idArchivo) {
    //alert(idArchivo);
    $.ajax({
        type: "POST",
        data:"idArchivo=" + idArchivo,
        url:"../../source/procesos/archivos/obtener.php",
        success: function(respuesta) {
            //alert(respuesta);
            $('#archivoObtenido').html(respuesta);
        }
    });
}