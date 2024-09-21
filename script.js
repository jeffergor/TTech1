document.addEventListener("DOMContentLoaded", () => {
    const loaderWrapper = document.querySelector(".loader-wrapper");

    setTimeout(() => {
        loaderWrapper.style.display = "none";
    }, 2000); // La animación de carga dura 2 segundos

    // Crear las burbujas flotantes
    const bubblesContainer = document.getElementById("floating-bubbles");

    for (let i = 0; i < 6; i++) {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");
        bubblesContainer.appendChild(bubble);
    }
});
