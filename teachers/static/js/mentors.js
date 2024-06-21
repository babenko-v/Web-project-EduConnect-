function updateDropdown(displayElementId, value, hiddenInputId) {
    // Получаем элемент для отображения текста
    const displayElement = document.getElementById(displayElementId);

    const sort_name = {
        '-last_name': 'Z-A',
        'last_name': 'A-Z',
        'experience': 'By experience',
        'age': 'By age'
    };

    // Обновляем текст элемента отображения в зависимости от типа
    if (displayElementId === 'expId') {
        displayElement.innerText = value + ' studying';
    } else if (displayElementId === 'sortId') {
        displayElement.innerText = sort_name[value];
    } else {
        displayElement.innerText = value;
    }

    // Обновляем значение скрытого поля
    const hiddenInput = document.getElementById(hiddenInputId);
    hiddenInput.value = value; // Устанавливаем значение скрытого поля
}
