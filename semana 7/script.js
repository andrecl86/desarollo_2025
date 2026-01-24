// Productos poco utilizados (humanizados)
let productos = [
    {
        nombre: "Escáner portátil",
        valor: 95,
        descripcion: "Ideal para estudiantes o docentes que necesitan digitalizar documentos rápidamente sin usar una impresora grande"
    },
    {
        nombre: "Lector de tarjetas SD",
        valor: 12,
        descripcion: "Pequeño accesorio muy útil para pasar fotos o archivos desde cámaras y celulares antiguos"
    },
    {
        nombre: "Base refrigerante para laptop",
        valor: 30,
        descripcion: "Ayuda a evitar que la laptop se caliente demasiado durante largas horas de uso"
    }
];

// Elementos del DOM
const lista = document.getElementById("lista-productos");
const btnAgregar = document.getElementById("btnAgregar");

// Mostrar productos en pantalla
function mostrarProductos() {
    lista.innerHTML = "";

    productos.forEach((producto) => {
        const li = document.createElement("li");

        li.innerHTML = `
            <strong>${producto.nombre}</strong><br>
            Precio aproximado: $${producto.valor}<br>
            ¿Para qué sirve?: ${producto.descripcion}
            <hr>
        `;

        lista.appendChild(li);
    });
}

// Agregar nuevo producto
btnAgregar.addEventListener("click", () => {
    const nombre = document.getElementById("nombre").value.trim();
    const valor = document.getElementById("valor").value.trim();
    const descripcion = document.getElementById("descripcion").value.trim();

    if (nombre === "" || valor === "" || descripcion === "") {
        alert("Por favor, completa todos los campos antes de agregar el producto");
        return;
    }

    const nuevoProducto = {
        nombre: nombre,
        valor: valor,
        descripcion: descripcion
    };

    productos.push(nuevoProducto);
    mostrarProductos();

    // Limpiar campos del formulario
    document.getElementById("nombre").value = "";
    document.getElementById("valor").value = "";
    document.getElementById("descripcion").value = "";
});

// Mostrar productos al cargar la página
mostrarProductos();
