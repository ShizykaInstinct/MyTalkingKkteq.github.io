const petImage = document.getElementById("pet-image");
const petText = document.getElementById("pet-text");

function talk() {
    const phrases = [
        "Я скучал по тебе!",
        "Как твои дела?",
        "Поиграй со мной!",
        "Ты классный!"
    ];
    petImage.src = "images/talk.png"; // ← путь к картинке "говорящий"
    petText.textContent = randomPhrase(phrases);
}

function feed() {
    petImage.src = "images/happy.png"; // ← путь к картинке "сытый"
    petText.textContent = "Ням-ням! Спасибо!";
}

function pet() {
    petImage.src = "images/pet.png"; // ← путь к картинке "гладят"
    petText.textContent = "Мурр~ Мне приятно!";
}

function randomPhrase(list) {
    return list[Math.floor(Math.random() * list.length)];
}
