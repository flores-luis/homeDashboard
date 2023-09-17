// Function to update the time on the page every second
function updateTime() {
    const now = new Date();
    const currentTime = now.toLocaleTimeString('en-US', { hour12: true });
    document.getElementById('current-time').innerText = currentTime;
}

// Update the time immediately when the page loads
updateTime();

// Schedule to update the time every second (1000 milliseconds)
setInterval(updateTime, 60000);
