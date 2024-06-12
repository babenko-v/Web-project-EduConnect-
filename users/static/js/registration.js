document.getElementById('togglePassword').addEventListener('click', function (e) {
    const passwordField = document.getElementById('password');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    // Переключаем иконку
    const icon = this.querySelector('.material-icons');
    icon.textContent = type === 'password' ? 'visibility' : 'visibility_off';
});