const arrowUp = `
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="#f8050e" class="bi bi-arrow-up-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 0 0 8a8 8 0 0 0 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z"/>
</svg>
<p class="mt-2 text-white">Гортай вгору</p>
`
const arrowDown = `
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="#f8050e" class="bi bi-arrow-down-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z"/>
</svg>
<p class="mt-2 text-white">Гортай вниз</p>
`
function scrollPage(e) {
    var currentPosition = window.scrollY || window.pageYOffset;
    var windowHeight = window.innerHeight;
    var bodyHeight = document.body.scrollHeight;

    if (currentPosition + windowHeight >= bodyHeight) {
    // Вверх
    window.scrollTo({ top: 0, behavior: 'smooth' });
    switchArrow("up")

    } else {
    // Вниз
    window.scrollTo({ top: bodyHeight, behavior: 'smooth' });
    switchArrow("down")
    }
}
function switchArrow() {
    var el = document.querySelector("#scrollButton");
    var currentPosition = window.scrollY || window.pageYOffset;
    var windowHeight = window.innerHeight;
    var bodyHeight = document.body.scrollHeight;

    if (currentPosition + windowHeight >= bodyHeight) {
        el.innerHTML = arrowUp;
    } else {
        el.innerHTML = arrowDown;
    }
}

switchArrow();

window.addEventListener('scroll', switchArrow);