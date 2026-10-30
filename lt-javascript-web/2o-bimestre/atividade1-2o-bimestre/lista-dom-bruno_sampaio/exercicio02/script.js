const formulario = document.querySelector('form');
const mensagem = document.getElementById('mensagem');

function mostrarMensagem(texto, classe) {
    mensagem.textContent = texto;
    mensagem.className = 'mensagem ' + classe;
}

function formatarMoeda(valor) {
    return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 });
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

function calcularTotal(preco, quantidade) {
    return preco * quantidade;
}

function calcularCompra(evento) {
    evento.preventDefault();
    const resultado = document.getElementById('resultado');
    resultado.hidden = true;
    const produto = lerProduto();
    if (!produto) return;
    const detalhes = document.getElementById('detalhes');
    detalhes.textContent = '';
    const linhas = [
        'Produto: ' + produto.nome,
        'Preço unitário: ' + formatarMoeda(produto.preco),
        'Quantidade: ' + produto.quantidade,
        'Total da compra: ' + formatarMoeda(calcularTotal(produto.preco, produto.quantidade))
    ];
    linhas.forEach(function (texto) {
        const item = document.createElement('li');
        item.textContent = texto;
        detalhes.appendChild(item);
    });
    resultado.hidden = false;
    mostrarMensagem('Compra calculada com sucesso.', 'sucesso');
}

formulario.addEventListener('submit', calcularCompra);
