document.addEventListener("DOMContentLoaded", function() {
    console.log("🚀 Algomatics Frontend Loaded!");
        document.getElementById("plotButton").onclick = function() {
            document.getElementById("Input Equation").innerText = document.getElementById("Display Equation").value
        };
    });