// Get references to HTML elements with specific IDs
const inputBar = document.getElementById('input-bar'); // Input field for adding tasks
const inputList = document.getElementById('input-list'); // List where tasks will be displayed

// Load tasks from localStorage when the page loads
window.onload = function() {
    showData();
};

function addTask() {
    if (inputBar.value === '') {
        alert("Error!!! Need An Input!!!");
    } else {
        // Create a task object
        var task = {
            text: inputBar.value, // The text of the task
            completed: false // Indicates whether the task is completed or not
        };

        // Add the task to the tasks array
        tasks.push(task);

        // Update the display of tasks
        displayTasks();

        // Save tasks to localStorage
        saveData();

        // Reset the input field
        inputBar.value = '';
    }
}

function saveData() {
    // Save the tasks array as a JSON string in localStorage
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function showData() {
    // Retrieve saved tasks from localStorage
    var savedTasks = localStorage.getItem("tasks");

    if (savedTasks) {
        // Parse the JSON string to populate the tasks array
        tasks = JSON.parse(savedTasks);

        // Update the display of tasks
        displayTasks();
    }
}

// Initialize the tasks array to store task objects
var tasks = [];

function displayTasks() {
    // Clear the list of tasks
    inputList.innerHTML = '';

    // Iterate through the tasks and create HTML elements for each task
    tasks.forEach(function (task, index) {
        var container = document.createElement('div'); // Container for a task
        var cir = document.createElement('i'); // Checkmark or circle icon
        var del = document.createElement('i'); // Trash icon
        var text = document.createElement('div'); // Text of the task

        // Set initial classes and content based on the completion state of the task
        cir.classList.add('bi', task.completed ? 'bi-check-circle' : 'bi-circle');
        del.classList.add('bi', 'bi-trash3-fill');
        text.innerHTML = task.text;

        cir.onclick = function () {
            // Toggle the completion state of the task
            task.completed = !task.completed;

            // Save the updated tasks to localStorage
            saveData();

            // Update the display of tasks
            displayTasks();
        };

        del.onclick = function () {
            // Remove the task from the tasks array
            tasks.splice(index, 1);

            // Save the updated tasks to localStorage
            saveData();

            // Update the display of tasks
            displayTasks();
        };

        // Assemble the elements within the task container
        container.appendChild(cir);
        container.appendChild(text);
        container.appendChild(del);

        // Apply CSS classes for styling
        container.classList.add('d-flex', 'align-items-center');

        // Add the task container to the list of tasks
        inputList.appendChild(container);
    });
}
