const formulario = document.querySelector('form');
const mensagem = document.getElementById('mensagem');

function mostrarMensagem(texto, classe) {
    mensagem.textContent = texto;
    mensagem.className = 'mensagem ' + classe;
}

function apresentarMensagem(evento) {
    evento.preventDefault();
    const nome = document.getElementById('nome').value.trim();
    if (!nome) {
        mostrarMensagem('Informe seu nome.', 'erro');
        return;
    }
    mostrarMensagem('Olá, ' + nome + '! Boas-vindas ao sistema.', 'sucesso');
}

document.getElementById('acao').addEventListener('click', apresentarMensagem);
formulario.addEventListener('submit', apresentarMensagem);
