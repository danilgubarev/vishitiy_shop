import { HandleManyCounters } from "/static/js/counter.js";


document.addEventListener("DOMContentLoaded", () => {
    const decrementButtons = document.querySelectorAll('.cart-decrement-btn');
    const incrementButtons = document.querySelectorAll('.cart-increment-btn');
    new HandleManyCounters(incrementButtons, decrementButtons)
})