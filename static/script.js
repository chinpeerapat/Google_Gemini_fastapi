function handleFormSubmit() {
    const userInput = document.getElementById('name-input').value;
    const userInputDisplay = document.getElementById('user-input-display');

    fetch(`http://localhost:8000/gemini?query=${encodeURIComponent(userInput)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message');
            
            // const converter = new showdown.Converter();
            // const htmlContent = converter.makeHtml(data);

            messageElement.innerHTML = data;

            userInputDisplay.appendChild(messageElement);
        })
        .catch(error => {
            console.error(error);
        });

    document.getElementById('name-input').value = '';
    userInputDisplay.scrollTop = userInputDisplay.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        
        const userInput = document.getElementById('name-input').value;

        if (userInput.trim().length > 0) {
            handleFormSubmit();
        } else {
            console.log("Input is empty. Not doing the work.");
        }
    }
}