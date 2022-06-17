
var id_prenda = 1;

function add() {


    var table_cell_tipo = document.createElement("td");

    var tipo = document.createElement("input");
    tipo.setAttribute("type", "text");
    tipo.setAttribute("name", "tipo_"+id_prenda);
    tipo.setAttribute("placeholder", "Tipo de Prenda");

    table_cell_tipo.appendChild(tipo);





    var table_cell_cantidad = document.createElement("td");

    var cantidad = document.createElement("input");
    cantidad.setAttribute("type", "number");
    cantidad.setAttribute("name", "cantidad_"+id_prenda);
    cantidad.setAttribute("placeholder", "Cantidad");

    table_cell_cantidad.appendChild(cantidad);






    var table_row = document.createElement("tr");

    table_row.appendChild(table_cell_tipo);
    table_row.appendChild(table_cell_cantidad);


    var tabla = document.getElementById("tabla_prendas");

    tabla.appendChild(table_row);

    id_prenda += 1;

}
