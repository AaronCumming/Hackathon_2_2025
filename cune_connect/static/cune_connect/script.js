// Rotating Images Feature
const rotatingImages = [
    "{% static 'cune_connect/images/intramurals.jpg' %}",
    "{% static 'cune_connect/images/business2.jpg' %}",
    "{% static 'cune_connect/images/art_club.jpg' %}",
    "{% static 'cune_connect/images/programming_team.jpg' %}",
    "{% static 'cune_connect/images/social_science.jpg' %}"
];

let currentIndex = 0;
const rotatingImg = document.getElementById("rotating-image");

function changeRotatingImage() {
    currentIndex = (currentIndex + 1) % rotatingImages.length;
    rotatingImg.src = rotatingImages[currentIndex];
    setTimeout(changeRotatingImage, Math.floor(Math.random() * (15000 - 5000 + 1) + 5000)); // Random interval 5-15 seconds
}

setTimeout(changeRotatingImage, 5000);

document.addEventListener("DOMContentLoaded", function () {
    const orgCards = document.querySelectorAll(".org-card");

    orgCards.forEach(card => {
        const images = card.querySelectorAll(".org-image");

        if (images.length > 1) {
            let currentIndex = 0;

            setInterval(() => {
                const nextIndex = (currentIndex + 1) % images.length;
                images[currentIndex].classList.remove("active");
                images[nextIndex].classList.add("active");
                currentIndex = nextIndex;
            }, Math.floor(Math.random() * (10000 - 5000 + 1)) + 5000); // Random interval between 5-10 seconds
        }
    });
});