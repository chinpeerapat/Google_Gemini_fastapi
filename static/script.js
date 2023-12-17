function handleFormSubmit() {
    const userInput = document.getElementById('name-input').value;
    const userInputDisplay = document.getElementById('user-input-display');

    fetch(`http://localhost:8000/gemini?query=${encodeURIComponent(userInput)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            userInputDisplay.innerHTML += `<div class="message"><br><br>${userInput}<br>${data}<br><br></div>`;
        })
        .catch(error => {
            console.error(error);
        });

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

        fetch(`http://localhost:8000/gemini/img?queryimg=${encodeURIComponent(userInput)}&image_url=${encodeURIComponent(imageURL)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                userInputDisplay.innerHTML += `<div class="message"><br><br><img src="${imageURL}" alt="User Image" style="max-width: 550px; max-height: 750px;"></div><br>${data}`;
            })
            .catch(error => {
                console.error(error);
            });

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
