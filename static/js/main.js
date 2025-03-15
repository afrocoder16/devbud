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

document.addEventListener('DOMContentLoaded', function() {
    // Existing login/register JS
    const loginInputs = document.querySelectorAll('.login-input');
    loginInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.querySelector('.input-icon').style.color = '#2a5298';
        });
        input.addEventListener('blur', function() {
            this.parentElement.querySelector('.input-icon').style.color = '#6c757d';
        });
    });

    const registerInputs = document.querySelectorAll('.register-input');
    const password = document.getElementById('password');
    const passwordConfirm = document.getElementById('password_confirm');
    const passwordMatchError = document.getElementById('password-match-error');

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

        registerInputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.querySelector('.input-icon').style.color = '#2a5298';
            });
            input.addEventListener('blur', function() {
                this.parentElement.querySelector('.input-icon').style.color = '#6c757d';
            });
        });
    }

    // Settings page: Profile picture preview
    const profilePicInput = document.getElementById('profile_picture');
    const profilePicPreview = document.getElementById('profile-pic-preview');

    if (profilePicInput) {
        profilePicInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    profilePicPreview.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Settings page: Smooth scrolling for sidebar links
    const sidebarLinks = document.querySelectorAll('.sidebar .nav-link');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            targetSection.scrollIntoView({ behavior: 'smooth' });

            // Update active link
            sidebarLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Settings page: Add focus animation for inputs
    const settingsInputs = document.querySelectorAll('.settings-input');
    settingsInputs.forEach(input => {
        input.addEventListener('focus', function() {
            const wrapper = this.parentElement;
            if (wrapper.classList.contains('input-wrapper')) {
                wrapper.querySelector('.input-icon').style.color = '#2a5298';
            }
        });
        input.addEventListener('blur', function() {
            const wrapper = this.parentElement;
            if (wrapper.classList.contains('input-wrapper')) {
                wrapper.querySelector('.input-icon').style.color = '#6c757d';
            }
        });
    });
});