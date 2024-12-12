document.addEventListener("DOMContentLoaded", () => {

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = deleteModal._element.querySelector("#deleteConfirm");
    
    document.getElementById("deleteModal").addEventListener("hidden.bs.modal", () => {
        deleteConfirm.href = "#"; // Reset the href
        
    });
    
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            console.log('Button clicked');
            let ObjID = e.target.getAttribute("data-id");
            let modelType = e.target.getAttribute("data-model");

            console.log(ObjID, modelType);
            if (modelType === "appointment"){
                deleteConfirm.href = `/appointments/${ObjID}/delete`;
            } else if (modelType === "consultant"){
                deleteConfirm.href = `/consultant/${ObjID}/delete`;
                
            }
            console.log(deleteConfirm.href)

            deleteModal.show();
        });
    }
    
    });

    setTimeout(function() {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

