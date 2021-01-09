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
            }
        });
}