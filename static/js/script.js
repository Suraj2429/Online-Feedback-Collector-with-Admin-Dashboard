document.addEventListener("DOMContentLoaded", function () {
    console.log("JS Loaded");

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (e) {
            const rating = document.querySelector('input[name="rating"]:checked');

            if (!rating) {
                e.preventDefault();
                showRatingPopup();
            }
        });
    }

    // Success popup 
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('success')) {
        const modal = new bootstrap.Modal(document.getElementById('successModal'));
        modal.show();
    }
});


/* CUSTOM RATING POPUP */

function showRatingPopup() {
    document.getElementById("ratingPopup").style.display = "flex";
}

function closeRatingPopup() {
    document.getElementById("ratingPopup").style.display = "none";
}


/* DELETE POPUP */

function openDeletePopup() {
    document.getElementById("deletePopup").style.display = "flex";
}

function closePopup() {
    document.getElementById("deletePopup").style.display = "none";
}

function confirmDelete() {
    window.location.href = "/delete-all";
}