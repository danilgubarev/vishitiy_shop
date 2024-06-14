class BaseCounter {
  decrement(counter) {
    if (counter.value > 0) {
      counter.value--;
    }
  }

  increment(counter) {
    if (counter.value < 10) {
      counter.value++;
    }
  }

  handleEvent(e) {
    const counter = e.target.parentElement.querySelector('[data-id="counter"]');
    if (counter) { // добавлено условие для проверки существования элемента counter
      if (e.target.dataset.id === 'increment') {
        this.increment(counter);
      } else if (e.target.dataset.id === 'decrement') {
        this.decrement(counter);
      }
    } else {
      console.error('Counter element not found');
    }
  }
}

class HandleCounter extends BaseCounter {
  constructor(decrementButton, incrementButton) {
    super();
    this.decrementButton = decrementButton;
    this.incrementButton = incrementButton;
    if (this.decrementButton && this.incrementButton) { // проверка на null
      this.decrementButton.addEventListener('click', this.handleEvent.bind(this));
      this.incrementButton.addEventListener('click', this.handleEvent.bind(this));
    } else {
      console.error('Decrement or Increment button not found');
    }
  }
}

class HandleManyCounters extends BaseCounter {
  constructor(incrementButtons, decrementButtons) {
    super();
    this.decrementButtons = decrementButtons;
    this.incrementButtons = incrementButtons;
    if (this.decrementButtons && this.incrementButtons) { // проверка на null
      this.decrementButtons.forEach(btn => btn.addEventListener('click', this.handleEvent.bind(this)));
      this.incrementButtons.forEach(btn => btn.addEventListener('click', this.handleEvent.bind(this)));
    } else {
      console.error('Decrement or Increment buttons not found');
    }
  }
}

export { HandleCounter, HandleManyCounters };