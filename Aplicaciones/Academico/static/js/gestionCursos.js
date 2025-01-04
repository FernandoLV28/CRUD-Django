document.addEventListener("DOMContentLoaded", () => {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener("click", (e) => {
            const confirmacion = confirm("¿Desea eliminar el elemento?");
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
});

