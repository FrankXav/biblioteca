var columns = ['Nombre','Autor','Pasillo','Charola'];

const dataTableOptions = {
    //scrollX: "2000px",
    lengthMenu: [5, 10, 15, 20, 100, 200, 500],
    pageLength: 10,
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3] },
        //{ orderable: false, targets: [] },
        //{ searchable: false, targets: [1] }
        //{ width: "50%", targets: [0] }
    ],
    destroy: true,
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords: "Ningún Libro encontrado",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Ningún Libro encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar:",
        loadingRecords: "Cargando...",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
};


$( document ).ready(function(){
    $.ajax({
        url : '/list',
        type : 'GET',
        dataType : 'json',
        success : function(datos) {
            tabla = document.getElementById('Libros');
            headt = document.createElement('thead');
            fila = document.createElement('tr');
            columns.forEach(titcol =>{
                celda = document.createElement('th');
                celda.innerHTML = titcol;
                fila.appendChild(celda);
            })
            headt.appendChild(fila);
            tabla.appendChild(headt);
            tabbody = document.createElement('tbody');
            datos.forEach(element => {
                fila = document.createElement('tr');
                celdanom = document.createElement('td');
                celdanom.innerHTML = element.nombre;
                fila.appendChild(celdanom);
                celdaautor = document.createElement('td');
                celdaautor.innerHTML = element.autor;
                fila.appendChild(celdaautor);
                /* celdades = document.createElement('td');
                celdades.innerHTML = element.descripcion;
                fila.appendChild(celdades); */
                celdaest = document.createElement('td');
                celdaest.innerHTML = element.estante;
                fila.appendChild(celdaest);
                celdarep = document.createElement('td');
                celdarep.innerHTML = element.Repisa;
                fila.appendChild(celdarep);
                tabbody.appendChild(fila);
            });
            tabla.appendChild(tabbody);
            foott = document.createElement('tfoot');
            fila = document.createElement('tr');
            columns.forEach(titcol =>{
                celda = document.createElement('th');
                celda.innerHTML = titcol;
                fila.appendChild(celda);
            })
            foott.appendChild(fila);
            tabla.appendChild(foott);
            $('#Libros').DataTable(dataTableOptions);
        }

    });
    /* $('#Libros').DataTable( {
        ajax: '/list',
        columns: [ 'Nombre','autor','descripcion','Repisa','estante']
    } ); */
    /* $('#Libros').DataTable({
        ajax: '/list',
        columns: [
            { data: 'nombre' },
            { data: 'autor' },
            { data: 'descripcion' },
            { data: 'estante' },
            { data: 'Repisa' },
        ],
    }); */
});