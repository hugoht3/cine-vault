// Get all edit buttons and delete buttons
const editButtons = document.querySelectorAll(".btn-edit");
const deleteButtons = document.querySelectorAll(".btn-delete");

// Get other required elements
const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");


/* Edit comment function */
editButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
        // Get the comment ID from the data attribute
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;

        // Update the comment text area with the content of the comment
        commentText.value = commentContent;

        // Change the button text to "Update" and modify the form action URL
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
        console.log(commentId);
    });
});

/* Delete comment function */
deleteButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
        // Get the comment ID from the data attribute
        let commentId = e.target.getAttribute("data-comment_id");

        // Update the delete confirmation URL and show the modal
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
});


