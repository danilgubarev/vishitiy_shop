document.addEventListener("DOMContentLoaded", () => {
    new handleCounter()
})
class handleCounter {

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