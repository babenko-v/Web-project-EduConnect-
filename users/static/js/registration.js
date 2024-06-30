document.getElementById('togglePassword').addEventListener('click', function (e) {
    const passwordField = document.getElementById('id_password1');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    // Переключаем иконку
    const icon = this.querySelector('.material-icons');
    icon.textContent = type === 'password' ? 'visibility' : 'visibility_off';
});


