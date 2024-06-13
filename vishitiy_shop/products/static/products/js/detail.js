document.addEventListener("DOMContentLoaded", () => {
    controlButtonsState()
})

function controlButtonsState() {
    const sizeButtons = document.querySelectorAll('.toggle-size');
    const colorButtons = document.querySelectorAll('.toggle-color');
    _controlButtonsState(sizeButtons);
    _controlButtonsState(colorButtons);
}

function _controlButtonsState(buttons) {
    buttons.forEach((button) => {
        button.addEventListener('click', function () {
          buttons.forEach((btn) => {
            if (btn !== this) {
                btn.classList.remove('active');
            }
          });
          this.classList.add('active');
        });
    });
}

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

function addToCart() {
  const quantity = document.querySelector('#counter').value;
  const price = document.querySelector('span#price').innerHTML;
  console.log(document.querySelector('.toggle-size.active'));
  const size = document.querySelector('.toggle-size.active').dataset.size;
  const color = document.querySelector('.toggle-color.active').dataset.color;
  const product_id = document.querySelector('input[name="product_id"]').value;
  const url = window.location.origin + '/cart/add/';
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  console.log(JSON.stringify({ quantity, size, color, price, product_id }));
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({ quantity, size, color, price, product_id }),
  };
  fetch(url, options)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}