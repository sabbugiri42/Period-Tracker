// Initialize Flatpickr for the date range input
document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#calendar-input", {
        mode: "range", // Allows selecting a range of dates
        dateFormat: "F j, Y", // Display format
        inline: true
        
    });
});

