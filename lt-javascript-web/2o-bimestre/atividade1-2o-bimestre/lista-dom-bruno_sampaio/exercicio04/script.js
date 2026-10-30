const formulario = document.querySelector('form');
const mensagem = document.getElementById('mensagem');

function mostrarMensagem(texto, classe) {
    mensagem.textContent = texto;
    mensagem.className = 'mensagem ' + classe;
}

const participantes = [];
const campoNome = document.getElementById('nome');
const lista = document.getElementById('lista');

function adicionarParticipante(evento) {
    evento.preventDefault();
    const nome = campoNome.value.trim();
    if (!nome) {
        mostrarMensagem('Informe o nome do participante.', 'erro');
        return;
    }
    // Compara também diferenças entre letras maiúsculas e minúsculas.
    const nomesComparaveis = participantes.map(function (participante) {
        return participante.toLocaleLowerCase('pt-BR');
    });
    if (nomesComparaveis.includes(nome.toLocaleLowerCase('pt-BR'))) {
        mostrarMensagem('Esse participante já foi cadastrado.', 'erro');
        return;
    }
    participantes.push(nome);
    const item = document.createElement('li');
    item.textContent = nome;
    lista.appendChild(item);
    document.getElementById('total').textContent = participantes.length;
    mostrarMensagem('Participante cadastrado com sucesso.', 'sucesso');
    campoNome.value = '';
    campoNome.focus();
}

formulario.addEventListener('submit', adicionarParticipante);
