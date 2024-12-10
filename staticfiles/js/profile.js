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
            let apptId = e.target.getAttribute("data-appt_id");
            console.log(apptId)
            deleteConfirm.href = `/appointments/${apptId}/delete`;
            deleteModal.show();
        });
    }
    
    });