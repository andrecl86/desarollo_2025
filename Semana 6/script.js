const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const edad = document.getElementById("edad");
const btnEnviar = document.getElementById("btnEnviar");

const errorNombre = document.getElementById("errorNombre");
const errorCorreo = document.getElementById("errorCorreo");
const errorPassword = document.getElementById("errorPassword");
const errorConfirm = document.getElementById("errorConfirm");
const errorEdad = document.getElementById("errorEdad");

function validarNombre() {
    if (nombre.value.length >= 3) {
        nombre.classList.add("valido");
        nombre.classList.remove("invalido");
        errorNombre.textContent = "";
        return true;
    } else {
        nombre.classList.add("invalido");
        nombre.classList.remove("valido");
        errorNombre.textContent = "El nombre debe tener al menos 3 caracteres";
        return false;
    }
}

function validarCorreo() {
    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (regexCorreo.test(correo.value)) {
        correo.classList.add("valido");
        correo.classList.remove("invalido");
        errorCorreo.textContent = "";
        return true;
    } else {
        correo.classList.add("invalido");
        correo.classList.remove("valido");
        errorCorreo.textContent = "Correo electrónico inválido";
        return false;
    }
}

function validarPassword() {
    const regexPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])/;
    if (password.value.length >= 8 && regexPassword.test(password.value)) {
        password.classList.add("valido");
        password.classList.remove("invalido");
        errorPassword.textContent = "";
        return true;
    } else {
        password.classList.add("invalido");
        password.classList.remove("valido");
        errorPassword.textContent = "Debe tener 8 caracteres, un número y un carácter especial";
        return false;
    }
}

function validarConfirmPassword() {
    if (confirmPassword.value === password.value && confirmPassword.value !== "") {
        confirmPassword.classList.add("valido");
        confirmPassword.classList.remove("invalido");
        errorConfirm.textContent = "";
        return true;
    } else {
        confirmPassword.classList.add("invalido");
        confirmPassword.classList.remove("valido");
        errorConfirm.textContent = "Las contraseñas no coinciden";
        return false;
    }
}

function validarEdad() {
    if (edad.value >= 18) {
        edad.classList.add("valido");
        edad.classList.remove("invalido");
        errorEdad.textContent = "";
        return true;
    } else {
        edad.classList.add("invalido");
        edad.classList.remove("valido");
        errorEdad.textContent = "Debe ser mayor o igual a 18 años";
        return false;
    }
}

function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmPassword() &&
        validarEdad()
    ) {
        btnEnviar.disabled = false;
    } else {
        btnEnviar.disabled = true;
    }
}

nombre.addEventListener("input", validarFormulario);
correo.addEventListener("input", validarFormulario);
password.addEventListener("input", validarFormulario);
confirmPassword.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);

document.getElementById("formulario").addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Formulario enviado correctamente. Validación exitosa.");
});
