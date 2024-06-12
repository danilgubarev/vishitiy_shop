document.addEventListener("DOMContentLoaded", () => {
    controlButtonsState()
    new handleCounter()
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

class handleCounter{

  constructor() {
    this.decrementButton = document.querySelector(
     '#decrement-btn'
    );
    this.incrementButton = document.querySelector(
      '#increment-btn'
    );
    this.counter = document.querySelector('#counter')
    this.decrementButton.addEventListener('click', this.decrement.bind(this));
    this.incrementButton.addEventListener('click', this.increment.bind(this));
  };
  decrement(e) {
    if (this.counter.value > 0) {
      this.counter.value--;
    }
  };

  increment(e) {
    if (this.counter.value < 10) {
      this.counter.value++;
    }   
  }
}