document.addEventListener("DOMContentLoaded", function() {
    console.log("🚀 Algomatics Frontend Loaded!");

    document.getElementById("plotButton").onclick = function() {
        let equation = document.getElementById("InputEquation").value;
        document.getElementById("DisplayEquation").innerText = "Equation " + equation;
    };
});