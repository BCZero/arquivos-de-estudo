# 🧠 Dominando o Git — Guia Pessoal de Fluxo de Trabalho

> **Objetivo:** Manter na memória os comandos e fluxos do Git para trabalhar com repositórios em duas ou mais máquinas diferentes, sem perder código nem criar conflitos.

---

## 📌 Índice

1. [Configuração inicial do projeto](#1-configuração-inicial-do-projeto)
2. [Fluxo de salvamento local (commit)](#2-fluxo-de-salvamento-local-commit)
3. [Conectar ao GitHub e fazer o primeiro push](#3-conectar-ao-github-e-fazer-o-primeiro-push)
4. [Clonar o repositório em uma nova máquina](#4-clonar-o-repositório-em-uma-nova-máquina)
5. [Fluxo diário de trabalho — começando a sessão](#5-fluxo-diário-de-trabalho--começando-a-sessão)
6. [Fluxo diário de trabalho — encerrando a sessão](#6-fluxo-diário-de-trabalho--encerrando-a-sessão)
7. [Verificar sem alterar: git fetch vs git pull](#7-verificar-sem-alterar-git-fetch-vs-git-pull)
8. [Resumo visual do ciclo completo](#8-resumo-visual-do-ciclo-completo)
9. [Regra de ouro](#9-regra-de-ouro)

---

## 1. Configuração inicial do projeto

Antes de qualquer comando Git, proteja os arquivos sensíveis e desnecessários criando o `.gitignore` na raiz do projeto:

```
.venv/
__pycache__/
.env
*.pyc
```

> ⚠️ O `.venv/` é a pasta do ambiente virtual Python (pesada e não deve ser enviada).
> O `.env` contém chaves e senhas privadas — **nunca suba esse arquivo.**

---

## 2. Fluxo de salvamento local (commit)

Execute esses comandos **dentro da pasta do projeto** para inicializar o Git e fazer o primeiro registro:

```bash
# 1. Inicializa o repositório Git na pasta atual
git init

# 2. Prepara todos os arquivos para serem salvos ("staged")
git add .

# 3. Cria o primeiro ponto de salvamento (commit)
git commit -m "primeiro commit: descrição do que foi feito"
```

> 💡 O commit é como um "ponto de restore". Cada commit registra o estado dos arquivos naquele momento.

---

## 3. Conectar ao GitHub e fazer o primeiro push

Crie um repositório vazio no GitHub (sem README, sem `.gitignore`) e use a URL gerada:

```bash
# 1. Conecta a pasta local ao repositório remoto do GitHub
git remote add origin https://github.com/seu-usuario/nome-do-repo.git

# 2. Garante que a branch principal se chame "main"
git branch -M main

# 3. Envia o código ao GitHub pela primeira vez
git push -u origin main
```

> 💡 O `-u origin main` só é necessário **no primeiro push**. Nos próximos, basta `git push`.

---

## 4. Clonar o repositório em uma nova máquina

Quando for usar o projeto em outro computador pela **primeira vez**, não use `git init`. Use `git clone`:

```bash
# Baixa o repositório completo e já configura a conexão com o GitHub
git clone https://github.com/BCZero/arquivos-de-estudo.git

# Entre na pasta do projeto
cd .\arquivos-de-estudo\
```

> ⚠️ Nunca rode `git init` depois de um `git clone`. O clone já faz isso automaticamente.

---

## 5. Fluxo diário de trabalho — começando a sessão

**Sempre** faça isso ao abrir o projeto, especialmente se trabalhou em outra máquina:

```bash
# Verifica o estado atual dos arquivos
git status

# Baixa e aplica as atualizações do GitHub na máquina atual
git pull
```

> ✅ Isso garante que você sempre está trabalhando com a versão mais recente do código.

---

## 6. Fluxo diário de trabalho — encerrando a sessão

**Sempre** faça isso antes de fechar o computador ou trocar de máquina:

```bash
# Verifica o que mudou
git status

# Adiciona todos os arquivos modificados
git add .

# Registra o que foi feito com uma mensagem descritiva
git commit -m "descrição clara do que foi estudado ou modificado"

# Envia para o GitHub
git push
```

> ✅ Isso garante que a outra máquina poderá baixar a versão mais recente com `git pull`.

---

## 7. Verificar sem alterar: git fetch vs git pull

| Comando | O que faz | Altera seus arquivos locais? |
|---|---|---|
| `git fetch` | Consulta o GitHub e atualiza as informações remotas | **Não** |
| `git pull` | Traz as alterações do GitHub para a pasta de trabalho | **Sim** |
| `git push` | Envia seus commits locais ao GitHub | No GitHub |

### Quando usar `git fetch`?

Use quando quiser **ver** o que mudou no GitHub antes de aplicar:

```bash
# Busca informações remotas sem alterar nada localmente
git fetch

# Mostra se há commits no GitHub que ainda não estão na sua máquina
git log HEAD..origin/main --oneline

# Depois de revisar, aplique com:
git pull
```

> 💡 Útil em projetos colaborativos, quando você quer examinar as mudanças antes de incorporá-las.

---

## 8. Resumo visual do ciclo completo

```
                    PRIMEIRA VEZ NA MÁQUINA
                            │
                       git clone
                            │
                    ┌───────▼────────┐
                    │  Projeto local │
                    └───────┬────────┘
                            │
        ┌───────────────────▼──────────────────────┐
        │           CICLO DIÁRIO DE TRABALHO        │
        │                                           │
        │   1. git pull   ← começa aqui sempre      │
        │          │                                │
        │   2. edita / cria arquivos                │
        │          │                                │
        │   3. git add .                            │
        │          │                                │
        │   4. git commit -m "descrição"            │
        │          │                                │
        │   5. git push   ← termina aqui sempre     │
        │          │                                │
        └──────────┼────────────────────────────────┘
                   │
            GitHub atualizado ✅
```

---

## 9. Regra de ouro

> **Antes de começar:** `git pull`
> **Antes de trocar de computador:** `git commit` + `git push`

Seguindo essa regra, seu código estará sempre sincronizado entre as máquinas, sem conflitos.

---

*Arquivo de referência pessoal — Bruno Sampaio | ADS SENAC/DF | 2026*
