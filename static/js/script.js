document.addEventListener("DOMContentLoaded", function () {
    console.log("JS Loaded");

    const form = document.querySelector('form[action="/submit-feedback"]');

    if (form) {
        form.addEventListener("submit", function (e) {
            const rating = document.querySelector('input[name="rating"]:checked');

            if (!rating) {
                e.preventDefault();
                showRatingPopup();
            }
        });
    }

    const urlParams = new URLSearchParams(window.location.search);
    const successModal = document.getElementById('successModal');

    if (urlParams.get('success') && successModal) {
        const modal = new bootstrap.Modal(successModal);
        modal.show();
    }
});

function showRatingPopup() {
    const popup = document.getElementById("ratingPopup");
    if (popup) {
        popup.style.display = "flex";
    }
}

function closeRatingPopup() {
    const popup = document.getElementById("ratingPopup");
    if (popup) {
        popup.style.display = "none";
    }
}


function openDeletePopup() {
    const popup = document.getElementById("deletePopup");
    if (popup) {
        popup.style.display = "flex";
    }
}

function closePopup() {
    const popup = document.getElementById("deletePopup");
    if (popup) {
        popup.style.display = "none";
    }
}

function confirmDelete() {
    window.location.href = "/delete-all";
}