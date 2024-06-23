import { Client } from "/static/js/client.js";

export class CartClient {

    constructor() {
        this.url = window.location.origin + '/cart/';
        this.client = new Client(); 
    }

    _remove(e, data) {
        e.target.closest('.item').remove();
    }

    remove(e) {
        e.preventDefault();
        const data = new FormData(e.target);
        this.client.sendReq(this.url + 'remove/', 'POST', data, (data) => this._remove(e, data));
    }

    add(e) {
        console.log("CartClient.add()", e);
        e.preventDefault();
        const data = new FormData(e.target);
        this.client.sendReq(this.url + 'add/', 'POST', data, (data) => this._add(e, data), 'При додаванні товару сталася помилка. Спробуйте пізніше');
    }

    _add(e, data) {
        const createdProduct = JSON.parse(data.data.product)[0]
        console.log(createdProduct [0])
        const cartItem = data.data.cart_item
        console.log(e.target);
        const itemImage = document.querySelector('.item-image').src
        const cartCounter = document.querySelector('.cart-counter')
        cartCounter.innerHTML = Number(cartCounter.innerHTML) + Number(cartItem.quantity)
        console.log(cartItem)
        let itemHtml = `
                    <div class="item ">
                    <div class="card flex flex-row card-in-cart">
                        <img src="${itemImage}" class="card-img-top" alt="..." style="width: 85px">
                        <div class="card-body">
                        <h5 class="card-title">${createdProduct.fields.type} ${createdProduct.fields.title}</h5>
                        <p class="card-text">Розмiр: ${cartItem.size}, Колiр: ${cartItem.color}</p>
                        </div>
                        <div class="card-footer flex items-center flex-col gap-2">
                            <div>
                                <div class="btn-group">
                                <button class="btn btn-outline-light text-2xl" id="decrement-btn">-</button>
                                <input type="text" id="counter" class="focus:outline-none text-center bg-transparent border text-white border-white font-semibold outline-none w-10" name="quantity" value="${cartItem.quantity}"></input>
                                <button class="btn btn-outline-light text-2xl" id="increment-btn">+</button>
                                </div>
                            </div>
                            <div>
                                <form action="/cart/remove" method="post" class="remove-from-cart-form">
                                    <input type="hidden" name="product_id" value="${createdProduct.pk}">
                                    <button class="btn text-white hover:text-red-500">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
                                            <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/>
                                        </svg>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>`

        const cartItems = document.querySelector('.cart-items')
        cartItems.insertAdjacentHTML('beforeend', itemHtml)

    }

    update(e) {
        console.log("CartClient.update()", e);
        e.preventDefault();
        const data = new FormData(e.target);
        this.client.sendReq(this.url + 'update/', 'POST', data, null, 'При зміні кількості сталася помилка. Спробуйте пізніше');
    }
}

