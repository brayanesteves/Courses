$('input[type="file"]').on('change', function () {
    var ext = $(this).val().split('.').pop();
    if($(this).val() != '') {
        if (ext == "xls" || ext == "xlsx" || ext == "csv") {
            if($(this)[0].files[0].size > 1048576) {
                Swal.fire("El documento excede el tamaño máximo", "", "warning");
            }          
        } else {
            $(this).val('');
            Swal.fire("Mensaje De Error", "Extensión no permitida: " + ext, "", "Error");
        }
    }
});

function CargarExcel() {
    var excel = $("#txt_archivo").val();
    if(excel === "") {
        return Swal.fire("Mensaje De Advertencia", "Seleccionar un archivo excel", "warning");
    }

    var formData = new FormData();
    var files = $("#txt_archivo")[0].files[0]; 
    formData.append('archivoexcel', files);

    $.ajax({
        url: 'source/controller/importar_excel_ajax.php',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (resp) {
            $("#div_table").html(resp);
            // Habilitar botón de Guardar Datos
            document.getElementById('btn_registrar').disabled = false;
        }
    });
    return false;
}

function Registrar_Excel() {
    // Contamos las filas de los datos que hemos extraido en el Excel
    var contador         = 0;
    var arreglo_id       = new Array();
    var arreglo_producto = new Array();
    $("#tabla_detalle tbody#tbody_tabla_detalle tr").each(function () {
        /**
         * find('td') = Es para obtener el dato que esta internamente en la etiqueta <td></td>
         */
        arreglo_id.push($(this).find('td').eq(0).text());
        arreglo_producto.push($(this).find('td').eq(1).text());
        contador++;
    });

    if(contador == 0) {
        return Swal.fire("Mensaje De Advertencia", "La tabla tiene que tener como minimo 1 dato", "warning");
    }
    //alert(arreglo_id + " - " + arreglo_producto);

    var idproducto = arreglo_id.toString();
    var producto   = arreglo_producto.toString();

    $.ajax({
        url: 'source/controller/controlador_registro.php',
        type: 'POST',
        data: {
            id: idproducto,
            p:  producto
        }
    }).done(function(resp) {
        if(resp == 1) {
            Swal.fire("Mensaje de confirmación", "Datos registrados", "success");
        } else {
            Swal.fire("Mensaje de error", "Datos no registrados", "error");
        }
    });
}