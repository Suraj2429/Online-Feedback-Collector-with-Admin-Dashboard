document.addEventListener("DOMContentLoaded", function () {
    console.log("JS Loaded ✅");

    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const rating = document.querySelector('input[name="rating"]:checked');

        if (!rating) {
            alert("Please select a rating ⭐");
            e.preventDefault();
        }
    });

    window.onload = function () {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('success')) {
            const modal = new bootstrap.Modal(document.getElementById('successModal'));
            modal.show();
        }
    };
});