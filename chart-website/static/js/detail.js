const detailBox = document.getElementById("product-detail");

let currentProduct = null;

window.onload = fetchProduct;

function fetchProduct() {
    fetch(`https://fakestoreapi.com/products/${PRODUCT_ID}`)
        .then(res => res.json())
        .then(product => {
            currentProduct = product;
            renderDetail(product);
        });
}

function renderDetail(product) {
    detailBox.innerHTML = `
        <div class="detail-card">
            <img src="${product.image}" />
            <div class="detail-info">
                <h2>${product.title}</h2>
                <p class="price">${product.price} $</p>
                <p>${product.description}</p>
                <button id="add-cart-btn">장바구니 담기</button>
            </div>
        </div>
    `;

    // 버튼 이벤트는 JS에서 연결
    document
        .getElementById("add-cart-btn")
        .addEventListener("click", addToCart);
}

function addToCart() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push(PRODUCT);
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("장바구니에 담겼습니다!");
}

