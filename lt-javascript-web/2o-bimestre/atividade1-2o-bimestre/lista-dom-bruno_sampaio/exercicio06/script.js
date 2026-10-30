const formulario = document.querySelector('form');
const mensagem = document.getElementById('mensagem');

function mostrarMensagem(texto, classe) {
    mensagem.textContent = texto;
    mensagem.className = 'mensagem ' + classe;
}

// O conteúdo fornecido pelo usuário é sempre inserido como texto.
function adicionarDetalhe(elemento, rotulo, valor) {
    const paragrafo = document.createElement('p');
    paragrafo.textContent = rotulo + ': ' + valor;
    elemento.appendChild(paragrafo);
}

const tarefas = [];
const classesPrioridade = { Baixa: 'prioridade-baixa', 'Média': 'prioridade-media', Alta: 'prioridade-alta' };

function atualizarLista() {
    const lista = document.getElementById('lista');
    lista.textContent = '';
    let altas = 0;
    tarefas.forEach(function (tarefa) {
        const item = document.createElement('li');
        item.className = classesPrioridade[tarefa.prioridade];
        adicionarDetalhe(item, 'Tarefa', tarefa.descricao);
        adicionarDetalhe(item, 'Responsável', tarefa.responsavel);
        adicionarDetalhe(item, 'Prioridade', tarefa.prioridade);
        lista.appendChild(item);
        if (tarefa.prioridade === 'Alta') altas++;
    });
    document.getElementById('total').textContent = tarefas.length;
    document.getElementById('total-altas').textContent = altas;
}

function cadastrarTarefa(evento) {
    evento.preventDefault();
    const descricao = document.getElementById('descricao').value.trim();
    const responsavel = document.getElementById('responsavel').value.trim();
    const prioridade = document.getElementById('prioridade').value;
    if (!descricao || !responsavel || !prioridade) {
        mostrarMensagem('Preencha a descrição, o responsável e selecione a prioridade.', 'erro');
        return;
    }
    if (!['Baixa', 'Média', 'Alta'].includes(prioridade)) {
        mostrarMensagem('Selecione uma prioridade válida.', 'erro');
        return;
    }
    tarefas.push({ descricao, responsavel, prioridade });
    atualizarLista();
    mostrarMensagem('Tarefa cadastrada com sucesso.', 'sucesso');
    formulario.reset();
    document.getElementById('descricao').focus();
}

formulario.addEventListener('submit', cadastrarTarefa);
