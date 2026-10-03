# Plano de Projetos Integrados: CoreELEC + Trilha ADS/DevOps/IA (2026-2027)

Este documento detalha quatro projetos evolutivos para o servidor CoreELEC, utilizando o bot do Telegram integrado ao qBittorrent[cite: 6] como laboratório prático para cumprir os marcos da trilha acadêmica de ADS, DevOps e Engenharia de Software com IA[cite: 7].

## 1. Migração para Docker Compose e Rede Isolada
**Meta da trilha:** Janeiro de 2027[cite: 7]
**Foco:** Dockerfile, imagens, volumes e Compose[cite: 7].

*   **Implementação:** Criar um arquivo `docker-compose.yml` para orquestrar o qBittorrent, o bot do Telegram e um banco de dados (como PostgreSQL) simultaneamente[cite: 7].
*   **Benefício DevOps:** Substituir o parâmetro `--net=host`[cite: 6] por uma rede interna do Docker. O bot passará a se comunicar com o qBittorrent através do nome do serviço local, isolando a aplicação da rede externa e permitindo a execução de todo o ambiente com o comando `docker compose up -d`[cite: 7].

## 2. Catálogo de Mídia com FastAPI e Banco de Dados
**Meta da trilha:** Março a Abril de 2027[cite: 7]
**Foco:** API (HTTP, rotas, persistência de dados), validação e CRUD[cite: 7].

*   **Implementação:** Integrar um banco de dados PostgreSQL ao projeto[cite: 7]. Modificar o script do bot para que, ao adicionar um magnet link[cite: 6], ele registre no banco os metadados do download.
*   **Expansão Frontend:** Desenvolver uma API em FastAPI para expor a lista de itens armazenados no SSD (`/var/media/SSD_DATA`)[cite: 6] e criar uma interface simples em JavaScript que consuma essa API e exiba a biblioteca em uma página web hospedada no próprio CoreELEC[cite: 7].

## 3. Pipeline de CI/CD para Atualização do Bot
**Meta da trilha:** Maio de 2027[cite: 7]
**Foco:** Azure Pipelines, artefatos, testes automáticos e implantação[cite: 7].

*   **Implementação:** Configurar um pipeline no Azure DevOps (ou GitHub Actions) acionado a cada alteração no código do bot[cite: 7]. O fluxo executará testes automáticos (`pytest`) nas funções de conexão à API do qBittorrent, criará a imagem Docker atualizada e a enviará para um *registry*[cite: 7].
*   **Benefício DevOps:** Eliminar a necessidade de reconstruir a imagem Docker manualmente no terminal da TV Box[cite: 6]. O processo garantirá que a versão em execução seja auditável e rastreável desde o commit até a implantação[cite: 7].

## 4. Agente de IA para Consulta da Biblioteca via Telegram
**Meta da trilha:** Setembro a Novembro de 2027[cite: 7]
**Foco:** LLMs, embeddings, sistema RAG e rastreamento de agentes com ferramentas limitadas[cite: 7].

*   **Implementação:** Adicionar RAG (Geração Aumentada por Recuperação) ao bot do Telegram para ingerir resumos ou arquivos de legendas salvos no disco[cite: 7].
*   **Operação:** O bot atuará como um agente conversacional. Ao receber consultas (ex.: "Quais filmes de ficção científica eu tenho no disco?"), ele buscará informações contextuais no banco vetorial[cite: 7] e formulará respostas precisas fundamentadas nos documentos recuperados[cite: 7]. O agente incluirá limites de chamadas de ferramentas e tratamento de erros para controle de execução[cite: 7].