document.addEventListener("DOMContentLoaded", function() {

    //Set time variable targeting html tag
    let time  = document.getElementById("js-time");

    let date = document.getElementById("js-date")

    setInterval(() =>{
        //retrieve date object
        let currentDate = new Date();
        let timeOptions = {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true // If you want to use AM/PM format
        };
        // update time varible's value to tim
        time.innerHTML = currentDate.toLocaleTimeString([],timeOptions);
        date.innerHTML = currentDate.toLocaleDateString()
    
    // Setting milliseconds 1000x per second
    },1000)

});
