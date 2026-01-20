const productList = document.getElementById("product-list");

window.onload = fetchProducts;

function fetchProducts() {
    fetch("https://fakestoreapi.com/products")
        .then(res => res.json())
        .then(products => renderProducts(products));
}

function renderProducts(products) {
    products.forEach(product => {
        const card = document.createElement("div");
        card.className = "product-card";

        card.innerHTML = `
            <img src="${product.image}" />
            <h3>${product.title}</h3>
            <p>${product.price} $</p>
            <button onclick="goDetail(${product.id})">상세보기</button>
        `;

        productList.appendChild(card);
    });
}

function goDetail(id) {
    location.href = `/product/${id}`;
}
