const socket = new WebSocket("ws://localhost:8000/ws/products/");
const notificationList = document.querySelector(".notifications")

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const notification = document.createElement("li")

    if (data.type === "updated") { // Update notification
        for (let field in data.changes){// set changes
            notification.textContent = `Product ${data.product} - Changes in ${field}: Old value ${data.changes[field].old_value}, New value ${data.changes[field].new_value}`
        }
    } else if (data.type === "created") { // Create notification
        notification.textContent += "New product created: "+ data.message
    }

    notificationList.appendChild(notification) 
  };

  socket.onopen = function() {
    console.log("WebSocket connection established");
  };

  socket.onclose = function() {
    console.log("WebSocket connection closed");
  };