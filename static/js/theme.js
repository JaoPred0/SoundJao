document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const htmlElement = document.documentElement;

    // Verifica se há um tema salvo no localStorage
    const savedTheme = localStorage.getItem("theme") || "light";
    htmlElement.setAttribute("data-bs-theme", savedTheme);

    // Atualiza o texto do botão
    updateButtonText(savedTheme);

    themeToggle.addEventListener("click", function (event) {
        event.preventDefault(); // Impede recarregamento

        // Alterna entre os temas "light" e "dark"
        const newTheme = htmlElement.getAttribute("data-bs-theme") === "light" ? "dark" : "light";
        htmlElement.setAttribute("data-bs-theme", newTheme);
        
        // Salva no localStorage
        localStorage.setItem("theme", newTheme);

        // Atualiza o texto do botão
        updateButtonText(newTheme);
    });

    function updateButtonText(theme) {
        themeToggle.textContent = theme === "light" ? "Tema Escuro" : "Tema Claro";
    }
});
