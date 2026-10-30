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

const pacientes = [];

function atualizarFila() {
    const lista = document.getElementById('lista');
    lista.textContent = '';
    let prioritarios = 0;
    pacientes.forEach(function (paciente, indice) {
        const item = document.createElement('li');
        adicionarDetalhe(item, 'Paciente', paciente.nome);
        adicionarDetalhe(item, 'Idade', paciente.idade);
        adicionarDetalhe(item, 'Atendimento', paciente.tipo);
        const botao = document.createElement('button');
        botao.type = 'button';
        botao.textContent = 'Remover';
        botao.setAttribute('aria-label', 'Remover ' + paciente.nome);
        botao.addEventListener('click', function () {
            removerPaciente(indice);
        });
        item.appendChild(botao);
        lista.appendChild(item);
        if (paciente.tipo === 'Prioritário') prioritarios++;
    });
    document.getElementById('total').textContent = pacientes.length;
    document.getElementById('total-prioritarios').textContent = prioritarios;
    document.getElementById('vazio').hidden = pacientes.length > 0;
}

function removerPaciente(indice) {
    const pacienteRemovido = pacientes.splice(indice, 1)[0];
    atualizarFila();
    mostrarMensagem('Paciente ' + pacienteRemovido.nome + ' removido da fila.', 'sucesso');
}

function cadastrarPaciente(evento) {
    evento.preventDefault();
    const nome = document.getElementById('nome').value.trim();
    const textoIdade = document.getElementById('idade').value.trim();
    const tipoSelecionado = document.getElementById('tipo').value;
    if (!nome || !textoIdade || !tipoSelecionado) {
        mostrarMensagem('Preencha o nome, a idade e o tipo de atendimento.', 'erro');
        return;
    }
    const idade = Number(textoIdade);
    if (!Number.isInteger(idade) || idade <= 0) {
        mostrarMensagem('A idade deve ser um número inteiro maior que zero.', 'erro');
        return;
    }
    if (!['Normal', 'Prioritário'].includes(tipoSelecionado)) {
        mostrarMensagem('Selecione um tipo de atendimento válido.', 'erro');
        return;
    }
    const tipo = idade >= 60 ? 'Prioritário' : tipoSelecionado;
    pacientes.push({ nome, idade, tipo });
    atualizarFila();
    mostrarMensagem(idade >= 60 ? 'Paciente cadastrado como prioritário por ter 60 anos ou mais.' : 'Paciente cadastrado com sucesso.', 'sucesso');
    formulario.reset();
    document.getElementById('nome').focus();
}

formulario.addEventListener('submit', cadastrarPaciente);
atualizarFila();
