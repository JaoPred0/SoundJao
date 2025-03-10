async function baixarMusica() {
    const url = document.getElementById("url").value;
    const loading = document.getElementById("loading");

    if (!url) {
        alert("Por favor, insira uma URL válida.");
        return;
    }

    loading.classList.remove("d-none");

    try {
        const response = await fetch('/baixar', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: url })
        });

        if (response.ok) {
            const blob = await response.blob();
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "musica.mp3";
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        } else {
            alert("Erro ao baixar a música!");
        }
    } catch (error) {
        alert("Erro de conexão! Tente novamente.");
    } finally {
        loading.classList.add("d-none");
    }
}
