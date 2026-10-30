const formulario = document.querySelector('form');
const mensagem = document.getElementById('mensagem');

function mostrarMensagem(texto, classe) {
    mensagem.textContent = texto;
    mensagem.className = 'mensagem ' + classe;
}

function calcularMedia(nota1, nota2) {
    return (nota1 + nota2) / 2;
}

function definirSituacao(media) {
    if (media >= 7) return { texto: 'Aprovado', classe: 'aprovado' };
    if (media >= 5) return { texto: 'Recuperação', classe: 'recuperacao' };
    return { texto: 'Reprovado', classe: 'reprovado' };
}

function verificarSituacao(evento) {
    evento.preventDefault();
    const nome = document.getElementById('nome').value.trim();
    const textoNota1 = document.getElementById('nota1').value.trim();
    const textoNota2 = document.getElementById('nota2').value.trim();
    if (!nome || !textoNota1 || !textoNota2) {
        mostrarMensagem('Preencha o nome e as duas notas.', 'erro');
        return;
    }
    const nota1 = Number(textoNota1);
    const nota2 = Number(textoNota2);
    if (!Number.isFinite(nota1) || !Number.isFinite(nota2) || nota1 < 0 || nota1 > 10 || nota2 < 0 || nota2 > 10) {
        mostrarMensagem('As notas devem ser números entre 0 e 10.', 'erro');
        return;
    }
    const media = calcularMedia(nota1, nota2);
    const situacao = definirSituacao(media);
    mostrarMensagem('Estudante: ' + nome + ' | Média: ' + media.toFixed(2) + ' | Situação: ' + situacao.texto, situacao.classe);
}

formulario.addEventListener('submit', verificarSituacao);
