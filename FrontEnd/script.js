function handleFormSubmit() {
    const userInput = document.getElementById('name-input').value;
    const userInputDisplay = document.getElementById('user-input-display');

    userInputDisplay.innerHTML += `<div class="message">${'\n'.repeat(5)}${userInput}</div><br><br>`;
    document.getElementById('name-input').value = '';
    userInputDisplay.scrollTop = userInputDisplay.scrollHeight;
}

function handleImageUpload(event) {
    const fileInput = event.target;
    const files = fileInput.files;

    if (files.length > 0) {
        const image = files[0];
        const imageURL = URL.createObjectURL(image);

        const userInputDisplay = document.getElementById('user-input-display');
        userInputDisplay.innerHTML += `<div class="message"><img src="${imageURL}" alt="User Image" style="max-width: 550px; max-height: 750px;"></div><br><br>`;
        
        userInputDisplay.scrollTop = userInputDisplay.scrollHeight;
        document.getElementById('image-input').value = '';
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        event.preventDefault();

        const targetId = event.target.id;

        if (targetId === 'name-input') {
            handleFormSubmit();
        } else if (targetId === 'image-input' && event.target.value.trim() !== '') {
            handleImageUpload(event);
        }
    }
}
