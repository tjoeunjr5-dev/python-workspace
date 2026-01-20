const cartList = document.getElementById("cart-list");

window.onload = loadCart;

function loadCart() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];

    if (cart.length === 0) {
        cartList.innerHTML = "<p>장바구니가 비어있습니다.</p>";
        return;
    }

    cart.forEach(product => {
        const item = document.createElement("div");
        item.className = "cart-item";

        item.innerHTML = `
            <img src="${product.image}">
            <div>
                <h3>${product.title}</h3>
                <p>${product.price} $</p>
            </div>
        `;

        cartList.appendChild(item);
    });
}
