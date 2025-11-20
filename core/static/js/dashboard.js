const msgbox = document.getElementById("message-box");
const socket = new WebSocket('ws://' + window.location.host + '/ws/products/');

socket.onopen = (event) => {
    console.log('WebSocket connection established');
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    
    let messageElement = document.createElement("div");
    messageElement.classList.add("message-element");
    
    let typeElement = document.createElement("div");
    typeElement.classList.add("type-element");
    typeElement.textContent = "Action: " + data.action;
    
    let contentElement = document.createElement("div");
    contentElement.style.color = "#666";
    contentElement.textContent = data.message;
    
    messageElement.appendChild(typeElement);
    messageElement.appendChild(contentElement);
    msgbox.appendChild(messageElement);
};

socket.onerror = (event) => {
    console.error('WebSocket error:', event);
};

socket.onclose = (event) => {
    console.log('WebSocket connection closed');
};