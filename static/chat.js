document.addEventListener("DOMContentLoaded", function () {
    let chatSocket;
    let currentRoom = "group"; // Значение по умолчанию
    const userName = "Guest";

    function connectToRoom(roomName) {
        if (chatSocket) {
            chatSocket.close();
        }

        chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + roomName + "/");

        chatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            displayMessage(data.sender, data.message);
        };

        chatSocket.onclose = function () {
            console.log("WebSocket закрыт");
        };

        document.getElementById("send-button").onclick = function () {
            const inputField = document.getElementById("message-input");
            const message = inputField.value;
            if (message.trim() !== "") {
                chatSocket.send(JSON.stringify({
                    sender: userName,
                    message: message
                }));
                inputField.value = "";
            }
        };
    }

    function displayMessage(sender, message) {
        const container = document.getElementById("chat-messages");
        const el = document.createElement("div");
        el.className = "message";
        el.textContent = `${sender}: ${message}`;
        container.appendChild(el);
        container.scrollTop = container.scrollHeight;
    }

    // Обработчики кнопок переключения чатов
    const chatButtons = document.querySelectorAll(".chat-btn");
    chatButtons.forEach(function (btn) {
        btn.addEventListener("click", function () {
            chatButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            const chatType = btn.getAttribute("data-chat");
            currentRoom = chatType === "group" ? "eco_project" : "user_aliya";

            document.getElementById("chat-title").textContent = chatType === "group"
                ? "🌿 Группа: Эко-проект"
                : "👤 Личный чат: Алия";

            // Подключение к WebSocket-комнате
            connectToRoom(currentRoom);
        });
    });

    // Стартовое подключение
    connectToRoom(currentRoom);
});
