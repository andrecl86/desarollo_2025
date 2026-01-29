// Alerta personalizada
function mostrarAlerta() {
    alert("¡Gracias por visitar nuestro sitio web!");
}

// Validación del formulario
document.getElementById("formulario").addEventListener("submit", function (e) {
    e.preventDefault();

    let valido = true;

    // Campos
    let nombre = document.getElementById("nombre").value.trim();
    let correo = document.getElementById("correo").value.trim();
    let mensaje = document.getElementById("mensaje").value.trim();

    // Errores
    document.getElementById("errorNombre").textContent = "";
    document.getElementById("errorCorreo").textContent = "";
    document.getElementById("errorMensaje").textContent = "";

    if (nombre === "") {
        document.getElementById("errorNombre").textContent = "El nombre es obligatorio";
        valido = false;
    }

    if (correo === "") {
        document.getElementById("errorCorreo").textContent = "El correo es obligatorio";
        valido = false;
    }

    if (mensaje === "") {
        document.getElementById("errorMensaje").textContent = "El mensaje es obligatorio";
        valido = false;
    }

    if (valido) {
        alert("Formulario enviado correctamente");
        document.getElementById("formulario").reset();
    }
});