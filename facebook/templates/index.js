function validateLoginForm() 

{ // JavaScript function for form validation.
    var username = document.getElementById('username').value; // Get the value of the username input field.
    var password = document.getElementById('password').value; // Get the value of the password input field.

    // validation logic
    if (username === '' || password === '') { // Check if either username or password is empty.
        alert('Please fill in all fields.'); // Show an alert message if fields are empty.
        return false; // Prevent form submission if validation fails.
    }
    

    return true; // Form submission will proceed if validation passes.
}