// Очікування завантаження DOM
document.addEventListener('DOMContentLoaded', function () {
    // Вибір всіх елементів з класом '.collect'
    const collectionCards = document.querySelectorAll('.collect');
    // Перебір кожної знайденої карточки колекції
    collectionCards.forEach(function(card) {
        // Додавання обробника подій 'click' до кожної карточки
        card.addEventListener('click', function() {
            // Отримання ідентифікатора колекції з атрибута 'data-collection-id'
            const collectionId = card.getAttribute('data-collection-id');
            // Якщо ідентифікатор колекції є
            if (collectionId) {
                // Формування нового URL для переходу на сторінку з продуктами,
                // фільтруючи за типом і ідентифікатором колекції
                const newUrl = `/products/?type=&collection=${collectionId}`;
                // Перенаправлення користувача на новий URL
                window.location.href = newUrl;
            } else {
                // Виведення помилки в консоль, якщо ідентифікатор колекції не знайдено
                console.error('Collection ID not found');
            }
        });
    });
});