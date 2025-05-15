// Пример подключения к WebSocket, roomName можно передавать из шаблона Django
const roomName = "eco_project"; // Если есть динамический параметр, замените на: "{{ room_name }}"
const userName = "Guest";       // Если пользователь авторизован, можно передать имя пользователя из Django

const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    displayMessage(data.sender, data.message); // Важно!
};


chatSocket.onclose = function(e) {
    console.error('Socket закрыт');
};

document.getElementById("send-button").addEventListener("click", function () {
    const inputField = document.getElementById("message-input");
    const message = inputField.value;
    if (message.trim() !== "") {
        chatSocket.send(JSON.stringify({
            'sender': userName,
            'message': message
        }));
        inputField.value = "";
    }
});

// Функция для отображения сообщения
function displayMessage(sender, message) {
    const messagesContainer = document.getElementById("chat-messages");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.textContent = sender + ": " + message;
    messagesContainer.appendChild(messageElement);
    // Прокрутка вниз
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Пример переключения чатов по кнопкам в сайдбаре
const chatButtons = document.querySelectorAll('.chat-btn');
chatButtons.forEach(function(button) {
    button.addEventListener('click', function () {
        // Удаляем класс active у всех кнопок
        chatButtons.forEach(btn => btn.classList.remove('active'));
        // Добавляем класс active к выбранной
        this.classList.add('active');
        // Получаем data-chat значение для дальнейшей логики переключения комнаты
        const chatType = this.getAttribute('data-chat');
        document.getElementById("chat-title").textContent = chatType === "group"
            ? "🌿 Группа: Эко-проект"
            : "👤 Личный чат: Алия";
        // Здесь можно добавить логику для переключения подключения к другому WebSocket эндпоинту
    });
});

chatSocket.send(JSON.stringify({
    'sender': userName,
    'message': message
}));
console.log("Сообщение отправлено:", message);
