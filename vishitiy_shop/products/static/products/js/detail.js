import { HandleCounter } from "/static/js/counter.js";
import { showToast } from "/static/js/notifications.js";
<<<<<<< HEAD
import { CartClient } from "/static/js/cart-client.js";
 
document.addEventListener("DOMContentLoaded", () => {
  initAddToCart()
  initCounter()
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
=======
 
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
>>>>>>> 4ab678e3a56e5e54be13eeb0975fd2b413ff59c8
}