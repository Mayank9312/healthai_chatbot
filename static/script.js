function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();

    if (message === "") return;

    appendMessage("You", message);
    userInput.value = "";

    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: message }),
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => response.json())
    .then((data) => {
        appendMessage("Bot", data.response);
    })
    .catch((error) => {
        console.error("Error:", error);
        appendMessage("Bot", "Sorry, something went wrong.");
    });
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");

    const urlRegex = /(https?:\/\/[^\s]+)/g;
    const linkedMessage = message.replace(urlRegex, (url) => {
        return `<a href="${url}" target="_blank">${url}</a>`;
    });

    messageElement.innerHTML = `<strong>${sender}:</strong> ${linkedMessage}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
