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
    if (!Number.isFinite(quantidade) || quantidade <= 0) {
        mostrarMensagem('A quantidade deve ser maior que zero.', 'erro');
        return null;
    }
    if (!Number.isFinite(preco * quantidade)) {
        mostrarMensagem('Os valores informados são muito grandes. Reduza o preço ou a quantidade.', 'erro');
        return null;
    }
    return { nome, preco, quantidade };
}

const itensPedido = [];

function atualizarPedido() {
    const lista = document.getElementById('lista');
    lista.textContent = '';
    let unidades = 0;
    let valor = 0;
    itensPedido.forEach(function (itemPedido) {
        const item = document.createElement('li');
        const subtotal = itemPedido.preco * itemPedido.quantidade;
        adicionarDetalhe(item, 'Item', itemPedido.nome);
        adicionarDetalhe(item, 'Preço unitário', formatarMoeda(itemPedido.preco));
        adicionarDetalhe(item, 'Quantidade', itemPedido.quantidade);
        adicionarDetalhe(item, 'Subtotal', formatarMoeda(subtotal));
        lista.appendChild(item);
        unidades += itemPedido.quantidade;
        valor += subtotal;
    });
    document.getElementById('total-unidades').textContent = Number(unidades.toFixed(10));
    document.getElementById('total-valor').textContent = formatarMoeda(valor);
    document.getElementById('vazio').hidden = itensPedido.length > 0;
}

function adicionarAoPedido(evento) {
    evento.preventDefault();
    const itemPedido = lerProduto();
    if (!itemPedido) return;
    itensPedido.push(itemPedido);
    atualizarPedido();
    mostrarMensagem('Item adicionado ao pedido.', 'sucesso');
    formulario.reset();
    document.getElementById('nome').focus();
}

function limparPedido() {
    if (itensPedido.length === 0) {
        mostrarMensagem('O pedido já está vazio. Não há itens para limpar.', 'erro');
        return;
    }
    itensPedido.length = 0;
    atualizarPedido();
    mostrarMensagem('Pedido limpo com sucesso.', 'sucesso');
}

formulario.addEventListener('submit', adicionarAoPedido);
document.getElementById('limpar').addEventListener('click', limparPedido);
atualizarPedido();
