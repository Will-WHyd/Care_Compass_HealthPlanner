

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        console.log('Button clicked');
        let apptId = e.target.getAttribute("data-appt_id");
        deleteConfirm.href = `${apptId}/delete`;
        deleteModal.show();
    });
}

