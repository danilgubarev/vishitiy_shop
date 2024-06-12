let slideIndex = 0;

// Инициализация слайдера
const initSlider = () => {
    plusSlides(1); // Перейти к первому слайду
    showSlides(slideIndex);

    // Получаем элементы DOM
    const prevButton = document.querySelector(".prev");
    const nextButton = document.querySelector(".next");

    // Обработчики событий для кнопок
    prevButton.addEventListener("click", () => plusSlides(-1));
    nextButton.addEventListener("click", () => plusSlides(1));

    // Автоматическая смена слайдов каждые 5 секунд
    setInterval(() => {
        plusSlides(1);
    }, 5000);
}

// Функция для изменения слайда на n
const plusSlides = (n) => {
    showSlides(slideIndex += n);
}

// Функция для показа текущего слайда
const showSlides = (n) => {
    const slides = document.querySelectorAll(".slider-item");
    if (n >= slides.length) {
        slideIndex = 0;
    }
    if (n < 0) {
        slideIndex = slides.length - 1;
    }
    slides.forEach(slide => {
        slide.style.display = "none";
    });
    slides[slideIndex].style.display = "flex";
}

// Вызов функции при загрузке страницы
window.addEventListener("load", initSlider);