document.addEventListener("DOMContentLoaded", function () {
    const preloader = document.getElementById("preloader");

    // Minimum 7 seconds delay (you can change to 5000 for 5 seconds)
    const MIN_LOAD_TIME = 1000; 

    // Record the time when loading starts
    const startTime = Date.now();

    // When page finishes loading
    window.addEventListener("load", function () {
        const loadDuration = Date.now() - startTime;
        const remainingTime = MIN_LOAD_TIME - loadDuration;

        // Hide preloader after the remaining delay
        setTimeout(() => {
            preloader.classList.add("hidden");
        }, remainingTime > 0 ? remainingTime : 0);
    });
});
