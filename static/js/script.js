document.addEventListener("DOMContentLoaded", () => {


    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    
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
                deleteConfirm.href = `/consultants/${ObjID}/delete`;
            }
            
            deleteModal.show();
        });
    }
    
    });