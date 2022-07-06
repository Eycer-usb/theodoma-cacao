function deleteConfirm(id, table){
    let text = `¿Seguro que desea eliminar este elemento? Esta accion no se puede deshacer`
    if(confirm(text)==true){
        if(table == 'User'){
            window.location.href =`/user-management/delete/${id}`;
        }
        else if(table == 'User_rol'){
            window.location.href =`/user-rol-management/delete/${id}`;
        }
        else if(table == 'Productor'){
            window.location.href = `/productor-data/delete/${id}`
        }
        else if(table == 'Productor_type'){
            window.location.href = `/productor-type/delete/${id}`            
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