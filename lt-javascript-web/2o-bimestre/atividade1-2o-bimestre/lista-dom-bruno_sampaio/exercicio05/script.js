const formulario = document.querySelector('form');
const mensagem = document.getElementById('mensagem');

function mostrarMensagem(texto, classe) {
    mensagem.textContent = texto;
    mensagem.className = 'mensagem ' + classe;
}

function formatarMoeda(valor) {
    return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

// O conteúdo fornecido pelo usuário é sempre inserido como texto.
function adicionarDetalhe(elemento, rotulo, valor) {
    const paragrafo = document.createElement('p');
    paragrafo.textContent = rotulo + ': ' + valor;
    elemento.appendChild(paragrafo);
}

function lerProduto() {
    const nome = document.getElementById('nome').value.trim();
    const textoPreco = document.getElementById('preco').value.trim();
    const textoQuantidade = document.getElementById('quantidade').value.trim();
    if (!nome || !textoPreco || !textoQuantidade) {
        mostrarMensagem('Preencha todos os campos.', 'erro');
        return null;
    }
    const preco = Number(textoPreco);
    const quantidade = Number(textoQuantidade);
    if (!Number.isFinite(preco) || preco <= 0) {
        mostrarMensagem('O preço deve ser um número maior que zero.', 'erro');
        return null;
    }
    if (!Number.isFinite(quantidade) || quantidade <= 0 || !Number.isInteger(quantidade)) {
        mostrarMensagem('A quantidade deve ser um número inteiro maior que zero.', 'erro');
        return null;
    }
    if (!Number.isFinite(preco * quantidade)) {
        mostrarMensagem('Os valores informados são muito grandes. Reduza o preço ou a quantidade.', 'erro');
        return null;
    }
    return { nome, preco, quantidade };
}

const produtos = [];

function atualizarResumo() {
    const nomes = produtos.map(function (produto) {
        return produto.nome.toLocaleLowerCase('pt-BR');
    });
    // Cadastros repetidos do mesmo nome representam o mesmo produto diferente.
    document.getElementById('total-produtos').textContent = new Set(nomes).size;
    let unidades = 0;
    let valor = 0;
    produtos.forEach(function (produto) {
        unidades += produto.quantidade;
        valor += produto.preco * produto.quantidade;
    });
    document.getElementById('total-unidades').textContent = unidades;
    document.getElementById('total-valor').textContent = formatarMoeda(valor);
}

function cadastrarProduto(evento) {
    evento.preventDefault();
    const produto = lerProduto();
    if (!produto) return;
    produtos.push(produto);
    const item = document.createElement('li');
    adicionarDetalhe(item, 'Produto', produto.nome);
    adicionarDetalhe(item, 'Preço unitário', formatarMoeda(produto.preco));
    adicionarDetalhe(item, 'Quantidade', produto.quantidade);
    adicionarDetalhe(item, 'Subtotal', formatarMoeda(produto.preco * produto.quantidade));
    document.getElementById('lista').appendChild(item);
    atualizarResumo();
    mostrarMensagem('Produto cadastrado com sucesso.', 'sucesso');
    formulario.reset();
    document.getElementById('nome').focus();
}

formulario.addEventListener('submit', cadastrarProduto);
