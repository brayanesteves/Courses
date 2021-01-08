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
                    $('#nombreCategoria').val("");
                    swal(":D", "Agregado con éxito!", "success");
                } else {
                    swal(":(", "Falló al agregar!", "error");
                }
            }
        });
    }
}