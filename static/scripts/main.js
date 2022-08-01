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
        }

    };
}

function deleteConfirm2(id, table, id2) {
    let text = `¿Seguro que desea eliminar este elemento? Esta accion no se puede deshacer`
    if(confirm(text)==true){
        if(table == 'Purchase'){
            window.location.href = `/harvest/${id2}/purchase/${id}/delete`            
        }
    }
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
    console.log("Ejecutandose")
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
Al ejecutarse la funcion print(table, tittle)
se buscara la tabla con el nombre especificado 
y el tittle sera el id de la tabla que se imprimira 
Para utilizarla solo es necesario ejecutar la funcion 
con la etiqueta onclick='print("table", "tittle")'
en el input table = nombre de la tabla de la Base de datos
y tittle sera id = mitabla
*/
function print(table, tittle) {
    var idTable=document.getElementById(tittle);
    var dbase = document.getElementById(table);
    var idTable = openWind.document.getElementById(tittle);
    var rank = idTable.rows;
    var i = 12
    if (idTable.rank[0].length > 12) {
        for (var j = 0; j < rank.length; j++) {
        rank[j].delete(i);   
        }
    }
    console.log(dbase)
    openwWind.print();
}


