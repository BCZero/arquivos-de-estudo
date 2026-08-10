### 1. Preparação: O Arquivo `.gitignore`

Antes de dar o primeiro comando, precisamos dizer ao Git para **não** salvar a pasta `.venv` (que é pesada) nem o arquivo `.env` (que tem sua chave privada).

Crie um arquivo chamado `.gitignore` na raiz do projeto e cole isso:

Plaintext

`.venv/
__pycache__/
.env
*.pyc`

### 2. Comandos para Salvar Localmente

Abra o terminal no diretório do projeto e execute esta sequência:

1. **Inicializar o repositório:**
    
    Bash
    
    `git init`
    
2. **Adicionar os arquivos para "staged" (preparar para salvar):**Bash
    
    `git add .`
    
3. **Criar o primeiro "ponto de salvamento" (Commit):**
    
    Bash
    
    `git commit -m "mensagem do commit"`

### 3. Upload para o GitHub

Agora, vá ao seu GitHub e crie um novo repositório (pode chamar de `intellidoc-visao`). Não marque a opção de criar README ou .gitignore por lá, pois já criamos aqui.

Após criar, o GitHub vai te dar uma URL (ex: `https://github.com/seu-usuario/intellidoc-visao.git`). Use os comandos abaixo:

1. **Conectar seu PC ao GitHub:**Bash
    
    `git remote add origin https://github.com/seu-usuario/intellidoc-visao.git`
    
2. **Renomear a branch principal para 'main' (padrão atual):**
    
    Bash
    
    `git branch -M main`
    
3. **Enviar o código:**
    
    Bash
    
    `git push -u origin main`
    
    Obs:  “-u origin main” só precisa ser inserido no primeiro push após sincronizar a main local com a origin remota. Após esse primeiro push, os próximos podem ser apenas git push
    
4. Fazendo atualizações no código:

`git add .` -> `git commit -m "descrição da mudança"` -> `git push`

### 4. Fluxo de baixar arquivos do servidor github

### Fluxo recomendado para seus dois computadores

Em cada computador, o repositório deve ser clonado apenas uma vez:

```
git clone https://github.com/BCZero/arquivos-de-estudo.gitcd .\arquivos-de-estudo\
```

Não use `git init` depois de clonar, porque o `clone` já cria e configura o repositório.

Sempre que começar a estudar ou programar em um dos computadores:

```
cd caminho\para\arquivos-de-estudogitstatusgitpull
```

Depois, trabalhe normalmente. Ao terminar:

```
git status git add .gitcommit-m"Descreve o que foi estudado"gitpush
```

Seu ciclo será:

git clone

    git clone https://github.com/BCZero/arquivos-de-estudo.gitcd .\arquivos-de-estudo\

Começou a trabalhar
        ↓
git pull
        ↓
cria ou altera arquivos
        ↓
git add .
        ↓
git commit
        ↓
git push
        ↓
GitHub fica atualizado

| Comando | O que faz | Altera seus arquivos locais? |
| --- | --- | --- |
| `git fetch` | Consulta o GitHub e atualiza as informações sobre o repositório remoto | Não |
| `git pull` | Consulta o GitHub e traz as alterações para sua pasta de trabalho | Sim |
| `git push` | Envia seus commits locais ao GitHub | No GitHub |

### 5. git fetch

### Quando usar `git fetch`

Use quando quiser apenas verificar se há novidades no GitHub, sem alterar imediatamente seus arquivos:

```
git fetch 
git status
```

Você também pode visualizar quais commits estão no GitHub e ainda não chegaram à máquina:

```
gitlogHEAD..origin/main--oneline
```

Isso é útil em projetos profissionais, quando você quer examinar as mudanças antes de incorporá-las.

### 6. Resumo Fluxo 2 máquinas

A regra mais importante é: antes de começar, faça 'git pull'; antes de trocar de computador, faça 'commit' e 'push'.