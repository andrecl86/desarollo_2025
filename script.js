const gallery = document.getElementById("gallery");
const imageUrlInput = document.getElementById("imageUrl");
const addImageBtn = document.getElementById("addImage");
const deleteImageBtn = document.getElementById("deleteImage");

let selectedImage = null;

// Agregar imagen
addImageBtn.addEventListener("click", () => {
  const url = imageUrlInput.value.trim();
  if (url === "") {
    alert("Ingrese una URL válida");
    return;
  }

  const img = document.createElement("img");
  img.src = url;

  img.addEventListener("click", () => {
    selectImage(img);
  });

  gallery.appendChild(img);
  imageUrlInput.value = "";
});

// Seleccionar imagen
function selectImage(img) {
  if (selectedImage) {
    selectedImage.classList.remove("selected");
  }
  selectedImage = img;
  img.classList.add("selected");
}

// Eliminar imagen seleccionada
deleteImageBtn.addEventListener("click", () => {
  if (!selectedImage) {
    alert("Seleccione una imagen primero");
    return;
  }
  gallery.removeChild(selectedImage);
  selectedImage = null;
});

// Atajo de teclado
document.addEventListener("keydown", (e) => {
  if (e.key === "Delete" && selectedImage) {
    gallery.removeChild(selectedImage);
    selectedImage = null;
  }
});

