import { HandleCounter } from "/static/js/counter.js";
import { showToast } from "/static/js/notifications.js";
 
document.addEventListener("DOMContentLoaded", () => {
    // controlButtonsState()

    const form = document.querySelector('#add-to-cart-form');
    form.addEventListener('submit', addToCart);
    const decrementButton = document.querySelector('.product-decrement-btn');
    const incrementButton = document.querySelector('.product-increment-btn');
    new HandleCounter(decrementButton, incrementButton);
})

// function controlButtonsState() {
//     const sizeButtons = document.querySelectorAll('.toggle-size');
//     const colorButtons = document.querySelectorAll('.toggle-color');
//     _controlButtonsState(sizeButtons);
//     _controlButtonsState(colorButtons);
// }

// function _controlButtonsState(buttons) {
//     buttons.forEach((button) => {
//         button.addEventListener('click', function () {
//           buttons.forEach((btn) => {
//             if (btn !== this) {
//                 btn.classList.remove('active');
//             }
//           });
//           this.classList.add('active');
//         });
//     });
// }

// class handleCounter{

//   constructor() {
//     this.decrementButton = document.querySelector(
//      '#decrement-btn'
//     );
//     this.incrementButton = document.querySelector(
//       '#increment-btn'
//     );
//     this.counter = document.querySelector('#counter')
//     this.decrementButton.addEventListener('click', this.decrement.bind(this));
//     this.incrementButton.addEventListener('click', this.increment.bind(this));
//   };
//   decrement(e) {
//     if (this.counter.value > 0) {
//       this.counter.value--;
//     }
//   };

//   increment(e) {
//     if (this.counter.value < 10) {
//       this.counter.value++;
//     }   
//   }
// }

function addToCart(e) {
  e.preventDefault();
  const form = e.target
  const formdata = new FormData(form)
  const sizeSelected = form.querySelector('input[name="size"]:checked');
  const colorSelected = form.querySelector('input[name="color"]:checked');
  const url = window.location.origin + '/cart/add/';
  
  if (!sizeSelected || !colorSelected) {
    return alert('Please select a size and a color before adding to cart.');
  }

  const options = {
    method: 'POST',
    body: formdata,
  };
  fetch(url, options)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      showToast("Товар успешно добавлен в корзину");
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}