import { HandleCounter } from "/static/js/counter.js";
import { showToast } from "/static/js/notifications.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('#add-to-cart-form');
    if (form) {
        form.addEventListener('submit', addToCart);
    }

    const decrementButton = document.querySelector('.product-decrement-btn');
    const incrementButton = document.querySelector('.product-increment-btn');

    if (decrementButton && incrementButton) {
        new HandleCounter(decrementButton, incrementButton);
    } else {
        console.error('Decrement or Increment button not found');
    }
});

function addToCart(e) {
  e.preventDefault();
  const form = e.target;
  const formdata = new FormData(form);
  const sizeSelected = form.querySelector('input[name="size"]:checked');
  const colorSelected = form.querySelector('input[name="color"]:checked');
  const url = window.location.origin + '/cart/add/';

  if (!sizeSelected || !colorSelected) {
    return showToast('Будь ласка, оберіть розмір та колір перед додаванням до кошика', 'warning');
  }

  const options = {
    method: 'POST',
    body: formdata,
  };

  fetch(url, options)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      if (data.errors) {
        for (const [key, value] of Object.entries(data.errors)) {
          showToast(value, 'danger');
        }
        return;
      }
      showToast("Товар успешно добавлен в корзину");
    })
    .catch((error) => {
      console.error('Error:', error);
      showToast('Виникла помилка при додаванні товару до кошика', 'danger');
    });
}
