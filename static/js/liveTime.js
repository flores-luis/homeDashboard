document.addEventListener("DOMContentLoaded", function() {

    //Set time variable targeting html tag
    let time  = document.getElementById("js-time");

    let day = document.getElementById("js-day")

    let dayname = document.getElementById("js-dayname")

    let month = document.getElementById("js-month")

    // Array of month names
    const monthNames = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ];

    // Array of day names
    const dayNames = [
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    ];

    setInterval(() =>{
        //retrieve date object
        let currentDate = new Date();
        let timeOptions = {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true // If you want to use AM/PM format
        };

        // update variable values to innetHTML text
        time.innerHTML = currentDate.toLocaleTimeString([],timeOptions);
        day.innerHTML = currentDate.getUTCDate()
        dayname.innerHTML = dayNames[currentDate.getDay()]
        month.innerHTML = monthNames[currentDate.getMonth()]
    // Setting milliseconds 1000x per second as refresh time
    },1000)

});
