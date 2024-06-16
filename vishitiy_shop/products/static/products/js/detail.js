import { HandleCounter } from "/static/js/counter.js";
import { CartClient } from "/static/js/cart-client.js";
 
document.addEventListener("DOMContentLoaded", () => {
  initCounter()
  initAddToCart()
})

function initCounter() {
  const decrementButton = document.querySelector('.product-decrement-btn');
  const incrementButton = document.querySelector('.product-increment-btn');
  new HandleCounter(decrementButton, incrementButton);
}

function initAddToCart() {
  const cart = new CartClient();
  const form = document.querySelector('#add-to-cart-form');
  form.addEventListener('submit', (e) => {
    e.preventDefault()
    const sizeSelected = form.querySelector('input[name="size"]:checked');
    const colorSelected = form.querySelector('input[name="color"]:checked');
    if (!sizeSelected || !colorSelected) {
      return showToast('Будь ласка, оберіть розмір та кольор перед додаванням до кошика', 'warning');
    }
    cart.add.bind(cart)(e);
  });
}