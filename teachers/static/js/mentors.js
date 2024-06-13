function updateDropdown(dropdownId, text) {
                const button = document.getElementById(dropdownId);
                button.textContent = text;

                // Обновление значения скрытого поля
                if (dropdownId === 'experienceDropdown') {
                    document.getElementById('experienceInput').value = text;
                } else if (dropdownId === 'locationDropdown') {
                    document.getElementById('locationInput').value = text;
                }
            }