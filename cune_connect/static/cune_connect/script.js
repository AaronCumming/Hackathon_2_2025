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