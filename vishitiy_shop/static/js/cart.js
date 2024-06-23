import { HandleManyCounters } from "/static/js/counter.js";
import { CartClient } from "/static/js/cart-client.js";

document.addEventListener("DOMContentLoaded", () => {
    initCounter();
    initRemove();
    initUpdate();
})

function initCounter() {
    const decrementButtons = document.querySelectorAll('.cart-decrement-btn');
    const incrementButtons = document.querySelectorAll('.cart-increment-btn');
    new HandleManyCounters(incrementButtons, decrementButtons)
}

export function initRemove() {
    const cart = new CartClient();
    const removeForms = document.querySelectorAll('.remove-cart-form');

    removeForms.forEach((form) => {
        form.addEventListener('submit', cart.remove.bind(cart))
    })
}

export function initUpdate() {
    const cart = new CartClient();
    const updateForms = document.querySelectorAll('.update-cart-form');
    const counters = document.querySelectorAll('.cart-counter');
    updateForms.forEach((form) => {
        form.addEventListener('submit', cart.update.bind(cart))
    })
    counters.forEach((counter) => {
        counter.addEventListener('input', (e) => {
            console.log("Counter changed", e.target.value);
            const form = e.target.closest('.update-cart-form');

            const event = new Event('submit', { bubbles: true, cancelable: true });
            form.dispatchEvent(event); 
        })
    })
}
