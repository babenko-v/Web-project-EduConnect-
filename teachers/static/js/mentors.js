function updateDropdown(dropdownId, value) {
    const button = document.getElementById(dropdownId);
    button.textContent = value + ' studying';

                // Обновление значения скрытого поля
            if (dropdownId === 'experienceDropdown') {
                document.getElementById('experienceInput').value = value + ' studying';
            } else if (dropdownId === 'locationDropdown') {
                document.getElementById('locationInput').value = value + ' studying';
            }


}


