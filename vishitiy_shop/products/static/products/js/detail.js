import { HandleCounter } from "/static/js/counter.js";
import { showToast } from "/static/js/notifications.js";
 
document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector('#add-to-cart-form');
    form.addEventListener('submit', addToCart);
    const decrementButton = document.querySelector('.product-decrement-btn');
    const incrementButton = document.querySelector('.product-increment-btn');
    new HandleCounter(decrementButton, incrementButton);
})


function addToCart(e) {
  e.preventDefault();
  const form = e.target
  const formdata = new FormData(form)
  const sizeSelected = form.querySelector('input[name="size"]:checked');
  const colorSelected = form.querySelector('input[name="color"]:checked');
  const url = window.location.origin + '/cart/add/';
  
  if (!sizeSelected || !colorSelected) {
    return showToast('Будь ласка, оберіть розмір та кольор перед додаванням до кошика', 'warning');
  }

  const options = {
    method: 'POST',
    body: formdata,
  };
  fetch(url, options)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
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
      showToast('Произошла ошибка при добавлении в корзину', 'danger');
    });
}