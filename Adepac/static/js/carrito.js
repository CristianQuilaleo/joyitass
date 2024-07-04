

document.addEventListener('DOMContentLoaded', () => {
    const listaProduct = document.querySelector('#row-item');
    let allProducts = [];
    let totalCarrito = 0;

    listaProduct.addEventListener('click', (e) => {
        if (e.target.classList.contains('btn-add-cart')) {
            const product = e.target.parentElement;

            const infoProduct = {
                quantity: 1,
                title: product.querySelector('h5').textContent,
                price: parseFloat(product.querySelector('.price').textContent.replace('$', '')),
            };

            allProducts = [...allProducts, infoProduct];
            totalCarrito += infoProduct.price;
            actualizarTotalCarrito();
        }
    });

    function actualizarTotalCarrito() {
        document.getElementById('totalCarrito').innerText = `Total: $${totalCarrito.toFixed(2)}`;
    }
});