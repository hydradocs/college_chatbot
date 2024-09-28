function sendMessage() {
    const userInput = document.getElementById("userInput").value.trim();
    if (userInput === "") return;

    // Display user message
    const chatbox = document.getElementById("chatbox");
    const userMessageDiv = document.createElement("div");
    userMessageDiv.classList.add("user-message");
    userMessageDiv.innerHTML = `<p>${userInput}</p>`;
    chatbox.appendChild(userMessageDiv);

    // Clear the input field
    document.getElementById("userInput").value = "";

    // Scroll to the bottom of the chatbox
    chatbox.scrollTop = chatbox.scrollHeight;

    // Send user message to the Flask backend
    fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        const botMessageDiv = document.createElement("div");
        botMessageDiv.classList.add("bot-message");
        botMessageDiv.innerHTML = `<p>${data.response}</p>`;
        chatbox.appendChild(botMessageDiv);

        // Scroll to the bottom after response
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
