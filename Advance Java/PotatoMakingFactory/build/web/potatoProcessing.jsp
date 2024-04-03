<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Potato Processing System</title>
<script>
    // Function to update status with "Done" after a delay
    function updateStatusWithDelay(statusElement, status, delay) {
        setTimeout(function() {
            statusElement.innerHTML = status + " Done";
        }, delay); // Delay specified in milliseconds
    }

    // Function to start updating status for all elements
    function startStatusUpdates() {
        var delay = 2000; // Initial delay
        var startTime = Date.now(); // Record start time
        updateStatusWithDelay(document.getElementById("peelingStatus"), "Peeling Status:", delay);
        delay += 2000; // Increment delay for next status
        updateStatusWithDelay(document.getElementById("chipCuttingStatus"), "Chip Cutting Status:", delay);
        delay += 6000; // Increment delay for next status
        updateStatusWithDelay(document.getElementById("fryingStatus"), "Frying Status:", delay);
        delay += 4000; // Increment delay for next status
        updateStatusWithDelay(document.getElementById("packingStatus"), "Packing Status:", delay);
        
        // Calculate and display total time taken for 1 potato
        setTimeout(function() {
            var totalTime1Potato = (Date.now() - startTime) / 1000; // Convert to seconds
            document.getElementById("totalTime1Potato").innerHTML = "Total time taken for 1 potato: " + totalTime1Potato + " seconds";

            // Calculate and display total time taken for 5000 potatoes
            var totalTime5000Potatoes = totalTime1Potato * 5000;
            document.getElementById("totalTime5000Potatoes").innerHTML = "Total time taken for 5000 potatoes: " + totalTime5000Potatoes + " seconds";
        }, delay);
    }

    // Start updating status when the page loads
    window.onload = startStatusUpdates;
</script>
</head>
<body>
    <h1>Potato Processing System</h1>
    <p>Status:</p>
    <p id="peelingStatus">Peeling Status:</p>
    <p id="chipCuttingStatus">Chip Cutting Status:</p>
    <p id="fryingStatus">Frying Status:</p>
    <p id="packingStatus">Packing Status:</p>
    <p id="totalTime1Potato">Total Time for 1 Potato :</p>
    <p id="totalTime5000Potatoes">Total Time for 5000 Potatoes :</p>
</body>
</html>
