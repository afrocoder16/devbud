document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('dark-mode-toggle');
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
        });
    }
});

// for login page

document.addEventListener('DOMContentLoaded', function() {
    // Add focus animation for inputs
    const inputs = document.querySelectorAll('.login-input');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.querySelector('.input-icon').style.color = '#2a5298';
        });
        input.addEventListener('blur', function() {
            this.parentElement.querySelector('.input-icon').style.color = '#6c757d';
        });
    });
});

// register page
document.addEventListener('DOMContentLoaded', function() {
    // Existing login page JS
    const loginInputs = document.querySelectorAll('.login-input');
    loginInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.querySelector('.input-icon').style.color = '#2a5298';
        });
        input.addEventListener('blur', function() {
            this.parentElement.querySelector('.input-icon').style.color = '#6c757d';
        });
    });

    // Register page: Password match validation
    const password = document.getElementById('password');
    const passwordConfirm = document.getElementById('password_confirm');
    const passwordMatchError = document.getElementById('password-match-error');
    const registerForm = document.getElementById('register-form');

    if (password && passwordConfirm) {
        passwordConfirm.addEventListener('input', function() {
            if (password.value !== passwordConfirm.value) {
                passwordMatchError.classList.remove('d-none');
                passwordConfirm.style.borderColor = '#dc3545';
            } else {
                passwordMatchError.classList.add('d-none');
                passwordConfirm.style.borderColor = '#ced4da';
            }
        });

        // Add focus animation for register inputs
        const registerInputs = document.querySelectorAll('.register-input');
        registerInputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.querySelector('.input-icon').style.color = '#2a5298';
            });
            input.addEventListener('blur', function() {
                this.parentElement.querySelector('.input-icon').style.color = '#6c757d';
            });
        });
    }
});