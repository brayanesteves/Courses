document.getElementById("seleccionararchivo").addEventListener("change", () => {
    var archivoseleccionado = document.querySelector("#seleccionararchivo");
    var archivos = archivoseleccionado.files;
    var imagenPrevisualizacion = document.querySelector("#mostrarimagen");

    // Si no hay archivos salimos de la función y quitamos la imágen
    if(!archivos || !archivos.length) {
        imagenPrevisualizacion.src = "";
        return;
    }

    // Ahora tomamos el primer archivo, el cual vamos a previsualizar
    var primerArchivo = archivos[0];
    // Lo convertimos a un objeto de tipo objectURL
    var objectURL = URL.createObjectURL(primerArchivo);
    // Y a la fuente de la imagen le ponemos el objectURL
    imagenPrevisualizacion.src = objectURL;
});

function Registrar() {
    var nombres = $("#txt_nombres").val();
    var apellidos = $("#txt_apellidos").val();
    var archivo = $("#seleccionararchivo").val();
    if (nombres.length == 0 || apellidos.length == 0) {
        // Libs 'sweetalert2'
        return Swal.fire('Mensaje De Advertencia', "Los campos no pueden quedar vacios", "warning");
    }

    if(archivo.length == 0) {
        // Libs 'sweetalert2'
        return Swal.fire('Mensaje De Advertencia', "Debe seleccionar un archivo", "warning");
    }

    var formData = new FormData();
    var foto = $("#seleccionararchivo")[0].files[0];

    formData.append('f', foto);
    formData.append('n', nombres);
    formData.append('a', apellidos);    

    $.ajax({
        url:"source/controller/subirimagen.php",
        type:'POST',
        data:formData,
        contentType:false,
        processData:false,
        success:function (respuesta) {
            if(respuesta != 0) {
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'Se subio el archivo con éxito',
                    showConfirmButton: false,
                    timer: 1500
                  });
            }
        }
    });
    return false;
}