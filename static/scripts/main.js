function deleteConfirm(id){
    let text = `Do you want to Delete this user? this action can not be undo.`
    if(confirm(text)==true){
        window.location.href =`/user-management/delete/${id}`;
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