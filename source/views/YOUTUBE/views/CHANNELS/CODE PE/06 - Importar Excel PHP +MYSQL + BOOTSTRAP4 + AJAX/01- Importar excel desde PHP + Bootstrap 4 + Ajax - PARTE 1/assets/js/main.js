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
        }
    });
    return false;
}