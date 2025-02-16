document.addEventListener("DOMContentLoaded", function() {
    console.log("🚀 Algomatics Frontend Loaded!");
        document.getElementById("plotButton").onclick = function() {
            let equation = document.getElementById("Input Equation").value;
            document.getElementById("Display Equation").innerText = "equationDisplay" + equation;
        };
});