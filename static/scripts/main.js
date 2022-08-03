function deleteConfirm(id, table){
    let text = `¿Seguro que desea eliminar este elemento? Esta accion no se puede deshacer`
    if(confirm(text)==true) {
        if(table == 'User'){
            window.location.href =`/user-management/delete/${id}`;
        }
        else if(table == 'User_rol'){
            window.location.href =`/user-rol-management/delete/${id}`;
        }
        else if(table == 'Productor'){
            window.location.href = `/productor-data/delete/${id}`;
        }
        else if(table == 'Productor_type'){
            window.location.href = `/productor-type/delete/${id}`;            
        }
        else if(table == 'Harvest'){
            window.location.href = `/harvest/delete/${id}`;            
        }
        else if(table == 'Logger'){
            window.location.href = `/logger/delete/${id}`;            
        }
        else if(table == 'Financing'){
            window.location.href = `/logger/delete/${id}`;            
        }        
    };
}

function deleteConfirm2(id, table, id2) {
    let text = `¿Seguro que desea eliminar este elemento? Esta accion no se puede deshacer`
    if(confirm(text)==true){
        if(table == 'Purchase'){
            window.location.href = `/harvest/${id2}/purchase/${id}/delete`;            
        }
        else if(table == 'Financing'){
            window.location.href = `/harvest/${id2}/financing/${id}/delete`;            
        }
    };
}

function unmaskPassword(id){
    element = document.getElementById(id);
    if(element.type == 'password'){
        element.type = 'text';
    }
    else{
        element.type = 'password';
    }
}

function showForm(){
    element = document.getElementById("create-form");
    element.hidden = false;
}

function hiddeForm(){
    element = document.getElementById("create-form");
    element.hidden = true
}



/*
Al ejecutarse la funcion searchEngine()
se buscara el tbody con id = table-body-data
para filtrar sus datos segun el valor del 
input con id = search-bar
Si se desea usar en otras vistas solamente es necesario 
ejecutar esta funcion con la etiqueta onkeyup="searchEngine()" en
el input con id = search-bar y la funcion filtrara los datos
de la tabla con id = table-body-data
*/
function searchEngine()
{
    console.log("Ejecutando Busqueda")
    var input, filter, tbody, tr, td, textValue;
    input = document.getElementById("search-bar");
    filter = input.value.toUpperCase();
    tbody = document.getElementById("table-body-data");
    tr = tbody.getElementsByTagName("tr")
    for( var i = 0; i < tr.length; i++ )
    {
        td = tr[i].getElementsByTagName("td");
        tr[i].style.display = "none";
        for( var j = 0; j < td.length; j++ ) {
            txtValue = td[j].textContent || td[j].innerText
            if ( txtValue.toUpperCase().indexOf(filter) > -1 ) {
                tr[i].style.display = "";
            }
        }        
    }

}


/*
Se Implementan las funciones a ejecutar al
cargar la vista de /harvest/{id}/financing
Estas funciones corresponden a los calculos 
en el tfoot
*/

function obtenerCantidadDeRecolectores( id_destino, table_id){
    var campo = document.getElementById(id_destino);
    var tabla = document.getElementById(table_id);
    tr = tabla.getElementsByTagName("tr");
    var ans = tr.length;
    campo.innerHTML = ans;
};


 function obtenerCantidadYTotalFinanciamiento( id_financ, id_total, tabla_id,
                                                col_status, status, col_monto ){
    tbody = document.getElementById(tabla_id);
    filas = tbody.getElementsByTagName("tr");
    total = 0;
    cantidad = 0;
    for( var i = 0; i < filas.length; i++ )
    {
        let celdas = filas[i].getElementsByTagName("td");
        if ( celdas[col_status-1].textContent ==status ) {
            cantidad ++;
            total += parseInt(celdas[col_monto-1].textContent);            
        }      
    }
    document.getElementById(id_financ).innerHTML = cantidad;
    document.getElementById(id_total).innerHTML = total;
};

function obtenerPlazosVencidos( id_destino, tabla_id, col_plazos ){
    tbody = document.getElementById(tabla_id);
    filas = tbody.getElementsByTagName("tr");
    cantidad = 0;
    date = new Date();
    let dia = date.getDate()
    let mes = date.getMonth() + 1
    let anio = date.getFullYear()
    var actual = `${anio}-${mes}-${dia}`;
    for( var i = 0; i < filas.length; i++ )
    {
        let celdas = filas[i].getElementsByTagName("td");
        let fecha_a_verificar = celdas[col_plazos-1].textContent;
        if ( fecha_a_verificar < actual ) {
            cantidad ++;
        }      
    }
    document.getElementById(id_destino).innerHTML = cantidad;
};

function obtenerTotalFinaciamientos(id_destino, tabla_id, col_total ){
    tbody = document.getElementById(tabla_id);
    filas = tbody.getElementsByTagName("tr");
    total = 0;
    for( var i = 0; i < filas.length; i++ )
    {
        let celdas = filas[i].getElementsByTagName("td");
        let monto = parseInt(celdas[col_total-1].textContent);
        total += monto;
    }
    document.getElementById(id_destino).innerHTML = total;
};



/*
Al ejecutarse la funcion print(table, title)
se buscara la tabla con el nombre especificado 
y el title sera el id de la tabla que se imprimira 
Para utilizarla solo es necesario ejecutar la funcion 
con la etiqueta onclick='print("table", "tittle")'
en el input table = nombre de la tabla de la Base de datos
y tittle sera id = mitabla*/

function generatePDF(miTabla) {
    window.print()
}


/*
Filtro Por fecha
*/

function filterByDate( table_id, from_id, to_id, col_date){

    console.log("Ejecutando Fitro por Fecha")
    from_date = new Date(document.getElementById(from_id).value)
    to_date = new Date(document.getElementById(to_id).value)
    from = ( from_date.getFullYear() + '-' + 
    (from_date.getMonth() + 1).toString().padStart(2, '0') + '-' +
    (from_date.getDate()+1).toString().padStart(2, '0')
    );
    to = ( to_date.getFullYear() + '-' + 
    (to_date.getMonth() + 1).toString().padStart(2, '0') + '-' +
    (to_date.getDate()+1).toString().padStart(2, '0')
    );

    var tbody, tr, td, txtValue;
    tbody = document.getElementById(table_id);
    filas = tbody.getElementsByTagName("tr");
    for( var i = 0; i < filas.length; i++ )
    {
        var cols = filas[i].getElementsByTagName("td");
        filas[i].style.display = "none";
        if( cols.length > col_date ) {
            txtValue = cols[col_date-1].textContent;
            if ( filas.length > col_date && (from <= txtValue) && (txtValue <= to) ) {
                filas[i].style.display = "";
            }
        }
    }
    
    // Reiniciar tabla
    if( from == "NaN-NaN-NaN" || to == "NaN-NaN-NaN" ){
        for( var i = 0; i < filas.length; i++ ){
            filas[i].style.display = "";
        }
    }

}