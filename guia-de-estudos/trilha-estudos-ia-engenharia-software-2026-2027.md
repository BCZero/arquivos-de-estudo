# Trilha de Estudos — Engenharia de Software com IA

## Objetivo

Construir, até dezembro de 2027, uma base sólida para aproveitar uma pós-graduação em Engenharia de Software com IA e atuar em projetos de desenvolvimento, automação, agentes, segurança e integração de IA.

Esta trilha foi adaptada ao perfil de Bruno: estudante de ADS no SENAC/DF, servidor da PCDF/DITEC, iniciante em programação profissional, com experiências práticas em Python, FastAPI, LangChain, Ollama, agentes ReAct, automação local, análise documental e governança de TIC.

## Como usar a trilha

- Carga máxima recomendada: **10 horas por semana**.
- Organização semanal: **6 h de teoria e exercícios + 3 h de projeto + 1 h de revisão**.
- Em semanas de prova ou excesso de trabalho, reduzir o projeto e preservar a revisão dos fundamentos.
- Não avançar apenas por ter assistido às aulas. Cada fase possui critérios práticos de conclusão.
- Usar IA como tutora, revisora e parceira de depuração, mas escrever, explicar e testar o código pessoalmente.

## Visão geral do período

| Período | Foco principal | Entrega prática |
|---|---|---|
| Set–Dez/2026 | Python, lógica, Git e fundamentos de SQL | Exercícios organizados e pequenos programas |
| Jan–Mar/2027 | Orientação a objetos, SQL e bancos de dados | Sistema CRUD com banco relacional |
| Abr–Jun/2027 | FastAPI, testes e Docker | API documentada, testada e conteinerizada |
| Jul–Set/2027 | Linux, arquitetura e engenharia de software | Sistema estruturado com documentação técnica |
| Out–Dez/2027 | LLMs, agentes, RAG e avaliação | Agente com RAG, ferramentas, testes e auditoria |

---

# Fase 1 — Fundamentos de Python, lógica e Git

## Período

Setembro a dezembro de 2026.

## 1. Python e lógica de programação

Aprender:

- sintaxe básica, indentação e comentários;
- variáveis, constantes por convenção e tipos primitivos;
- strings, números, booleanos e conversões de tipo;
- operadores aritméticos, relacionais e lógicos;
- entrada e saída de dados;
- `if`, `elif` e `else`;
- `for`, `while`, `break` e `continue`;
- listas, tuplas, conjuntos e dicionários;
- índices, fatiamento e métodos de coleções;
- funções, parâmetros, argumentos e `return`;
- escopo de variáveis;
- tratamento básico de erros com `try`, `except` e `finally`;
- leitura e escrita de arquivos CSV, JSON e texto;
- módulos, imports e organização de arquivos;
- ambientes virtuais e instalação de dependências;
- compreensão de listas somente depois de dominar os laços tradicionais;
- noções de complexidade: custo constante, linear e quadrático.

### Prática mínima

Criar programas para:

1. validar dados digitados pelo usuário;
2. calcular pedidos e descontos;
3. ler e filtrar um arquivo CSV;
4. gerar um relatório em JSON;
5. consultar uma lista de processos fictícios e identificar novidades;
6. separar o código em funções e módulos.

## 2. Git e GitHub

Aprender:

- diferença entre Git e GitHub;
- repositório local e remoto;
- `clone`, `init`, `status`, `add`, `commit`, `log` e `diff`;
- `push`, `pull` e `fetch`;
- branches e merge;
- resolução de conflitos simples;
- `.gitignore`;
- README bem estruturado;
- commits pequenos e descritivos;
- não versionar senhas, tokens, arquivos `.env` ou dados sigilosos;
- noções de Pull Request e revisão de código.

### Projeto da fase

Criar o repositório **laboratorio-python**, contendo exercícios organizados por tema, README, `.gitignore`, instruções de execução e histórico de commits compreensível.

### Critério para avançar

Você deve conseguir explicar um programa próprio, corrigir um erro simples sem copiar a solução inteira e publicar alterações no GitHub com segurança.

---

# Fase 2 — Orientação a objetos e bancos de dados

## Período

Janeiro a março de 2027.

## 3. Orientação a objetos

Aprender:

- diferença entre programação procedural e orientada a objetos;
- classes e objetos;
- atributos e métodos;
- construtor `__init__`;
- `self`;
- encapsulamento por convenção;
- propriedades com `@property`;
- composição e associação;
- herança com moderação;
- polimorfismo;
- classes abstratas e protocolos em nível introdutório;
- métodos de classe e métodos estáticos;
- `dataclass`;
- exceções próprias;
- responsabilidade única e coesão;
- evitar classes gigantes e hierarquias desnecessárias.

### Prática mínima

Modelar um sistema de processos administrativos com classes como `Processo`, `Documento`, `Andamento`, `Usuario` e `Relatorio`.

## 4. SQL e bancos de dados

Aprender:

- diferença entre banco de dados, SGBD, tabela, registro e campo;
- modelo relacional;
- chaves primárias e estrangeiras;
- relacionamentos 1:1, 1:N e N:N;
- normalização até a terceira forma normal;
- `CREATE`, `ALTER`, `INSERT`, `UPDATE` e `DELETE`;
- `SELECT`, `WHERE`, `ORDER BY` e `LIMIT`;
- `JOIN`: `INNER`, `LEFT` e, depois, `RIGHT`;
- `GROUP BY`, `HAVING` e funções de agregação;
- subconsultas e CTEs em nível introdutório;
- transações, `COMMIT` e `ROLLBACK`;
- restrições `NOT NULL`, `UNIQUE`, `CHECK` e `DEFAULT`;
- índices e seus efeitos básicos;
- SQL parametrizado para evitar SQL Injection;
- diferença entre banco relacional e banco vetorial;
- PostgreSQL como banco principal da trilha;
- SQLite para protótipos locais.

### Projeto da fase

Criar o banco do **Radar SEI Local**, com tabelas de processos, documentos, andamentos, usuários e registros de execução. Produzir também um dicionário de dados e consultas SQL de relatório.

### Critério para avançar

Você deve conseguir desenhar as tabelas, justificar as chaves, escrever consultas com `JOIN` e explicar por que um dado pertence a determinada tabela.

---

# Fase 3 — FastAPI, testes e Docker

## Período

Abril a junho de 2027.

## 5. APIs com FastAPI

Aprender:

- conceito de API, cliente, servidor, rota e endpoint;
- HTTP e os métodos `GET`, `POST`, `PUT`, `PATCH` e `DELETE`;
- códigos de status HTTP;
- parâmetros de rota, query e corpo da requisição;
- JSON;
- Pydantic e validação de dados;
- schemas de entrada e saída;
- separação entre rotas, serviços, modelos e configurações;
- injeção de dependências;
- documentação automática com OpenAPI e Swagger;
- conexão com PostgreSQL ou SQLite;
- autenticação e autorização em nível introdutório;
- variáveis de ambiente e configuração segura;
- logging e tratamento de exceções;
- paginação, filtros e ordenação;
- CORS;
- operações síncronas e assíncronas;
- noções de versionamento de API.

## 6. Testes automatizados

Aprender:

- por que testar software;
- teste unitário, integração, contrato, sistema e ponta a ponta;
- pytest;
- organização de testes;
- fixtures;
- parametrização;
- mocks e stubs;
- testes de sucesso, erro e casos extremos;
- cobertura de código e suas limitações;
- testes de endpoints FastAPI;
- testes de banco de dados;
- dados de teste e isolamento;
- regressão;
- princípios básicos de TDD;
- testes de segurança e validação de entrada.

## 7. Linux e Docker

### Linux

Aprender:

- estrutura de diretórios;
- terminal e navegação;
- permissões e proprietário;
- processos e serviços;
- variáveis de ambiente;
- redirecionamento e pipes;
- `grep`, `find`, `curl`, `less`, `tail` e `man`;
- SSH;
- gerenciamento de pacotes;
- logs;
- scripts Bash básicos;
- portas, processos e conectividade;
- noções de segurança e menor privilégio.

### Docker

Aprender:

- imagem, container, volume e rede;
- Dockerfile;
- construção e execução de imagens;
- variáveis de ambiente;
- persistência com volumes;
- Docker Compose;
- comunicação entre API e banco;
- logs e health checks;
- redução do tamanho das imagens;
- usuário não root;
- separação entre desenvolvimento e produção;
- noções de registro de imagens e CI.

### Projeto da fase

Construir uma API FastAPI do Radar SEI Local com PostgreSQL, testes automatizados e execução completa por Docker Compose.

### Critério para avançar

Você deve conseguir iniciar o projeto em outra máquina seguindo o README, executar os testes, consultar a documentação Swagger e identificar os principais logs de erro.

---

# Fase 4 — Arquitetura e engenharia de software

## Período

Julho a setembro de 2027.

## 8. Fundamentos de arquitetura de software

Aprender:

- requisitos funcionais e não funcionais;
- domínio, casos de uso e limites do sistema;
- coesão e acoplamento;
- separação de responsabilidades;
- princípios SOLID;
- Clean Code;
- arquitetura em camadas;
- MVC e arquitetura hexagonal em nível introdutório;
- monólito modular e microsserviços;
- APIs e contratos;
- filas e processamento assíncrono;
- cache;
- idempotência;
- resiliência, timeout, retry e circuit breaker;
- escalabilidade, latência e disponibilidade;
- observabilidade: logs, métricas e traces;
- segurança desde o desenho;
- custo operacional e manutenção;
- decisões arquiteturais e trade-offs.

## 9. Engenharia de software

Aprender:

- ciclo de vida do software;
- levantamento e gestão de requisitos;
- histórias de usuário e critérios de aceitação;
- planejamento de tarefas;
- versionamento e revisão de código;
- documentação técnica;
- diagramas UML e C4;
- ADR — Architecture Decision Record;
- integração contínua;
- entrega contínua em nível introdutório;
- qualidade, revisão e refatoração;
- gestão de configuração;
- segurança de dependências;
- análise de riscos;
- manutenção evolutiva e correção de defeitos;
- diferença entre protótipo, MVP e sistema pronto para produção.

### Projeto da fase

Produzir a documentação técnica completa do Radar SEI Local:

- visão do produto;
- requisitos;
- casos de uso ou user stories;
- diagrama C4;
- modelo de dados;
- ADRs;
- arquitetura da API;
- plano de testes;
- riscos de segurança e privacidade;
- manual de execução e operação.

### Critério para avançar

Você deve conseguir justificar as principais decisões do sistema, explicar seus trade-offs e alterar a arquitetura sem depender exclusivamente da IA.

---

# Fase 5 — LLMs, agentes, RAG e avaliação

## Período

Outubro a dezembro de 2027.

Essa fase deve vir por último porque agentes e RAG dependem de programação, APIs, bancos, testes, arquitetura e segurança.

## 10. Fundamentos de LLMs

Aprender:

- tokens e janela de contexto;
- embeddings;
- inferência;
- temperatura e outros parâmetros;
- modelos locais e modelos via API;
- custo, latência e limites;
- alucinação;
- determinismo e não determinismo;
- prompt do sistema, usuário e ferramentas;
- contexto estruturado;
- diferenças entre fine-tuning, RAG e prompting;
- proteção de dados e classificação da informação.

## 11. RAG

Aprender:

- ingestão de documentos;
- limpeza e normalização;
- divisão em chunks;
- metadados;
- geração e armazenamento de embeddings;
- busca semântica;
- busca híbrida;
- reranking em nível introdutório;
- montagem do contexto;
- resposta com fontes;
- filtros por metadados e permissões;
- atualização e remoção de documentos;
- avaliação de recuperação;
- limites do RAG;
- segurança contra documentos maliciosos e prompt injection.

## 12. Agentes

Aprender:

- diferença entre chatbot, aplicação com LLM e agente;
- objetivo, estado, memória, plano e execução;
- tools e function calling;
- aprovação humana;
- agentes com fluxo determinístico;
- agentes ReAct;
- agentes com memória;
- orquestração e subagentes;
- LangChain e LangGraph;
- comparação conceitual com CrewAI e Google ADK;
- MCP e integração com ferramentas externas;
- sessões e persistência;
- limites de autonomia;
- guardrails;
- logs e rastreamento;
- fallback e tratamento de falhas;
- princípio do menor privilégio para ferramentas.

## 13. Avaliação de LLMs e agentes

Aprender:

- conjunto de avaliação;
- casos normais, casos difíceis e casos adversariais;
- precisão, recall e F1 quando aplicáveis;
- avaliação de recuperação;
- avaliação da resposta final;
- groundedness e fidelidade às fontes;
- avaliação por critérios;
- LLM-as-judge e suas limitações;
- testes de prompts;
- testes de regressão;
- datasets reais e sintéticos;
- rastreabilidade de versão de prompt, modelo e documentos;
- observabilidade;
- custo por execução;
- segurança, privacidade e revisão humana.

### Projeto final

Construir uma versão acadêmica e fictícia do **Radar SEI Local** que:

1. recebe documentos de teste;
2. extrai e indexa o conteúdo;
3. responde perguntas com RAG;
4. consulta ferramentas autorizadas;
5. registra fontes e decisões;
6. exige aprovação antes de qualquer ação sensível;
7. roda localmente com Ollama ou com uma API configurável;
8. possui testes de recuperação, resposta, segurança e regressão;
9. apresenta logs, métricas e custo estimado;
10. deixa explícito que não utiliza dados reais sigilosos durante o desenvolvimento acadêmico.

### Critério final

Você estará pronto para uma pós desse perfil quando conseguir explicar, implementar e testar o fluxo abaixo:

```text
usuário → API → autenticação → agente → ferramenta/RAG → modelo → resposta fundamentada → logs e avaliação
```

---

# Rotina semanal recomendada

| Bloco | Tempo | Atividade |
|---|---:|---|
| Bloco 1 | 2 h | Teoria e anotações próprias |
| Bloco 2 | 2 h | Exercícios sem copiar a solução |
| Bloco 3 | 2 h | Implementação do projeto |
| Bloco 4 | 2 h | Continuação do projeto e depuração |
| Bloco 5 | 1 h | Testes, documentação ou Git |
| Bloco 6 | 1 h | Revisão, questões e registro de erros |

## Regra de estudo com IA

Para cada código gerado ou sugerido pela IA:

1. pedir uma explicação do objetivo e das dependências;
2. executar e observar o resultado;
3. alterar uma parte por conta própria;
4. provocar um erro controlado;
5. corrigir o erro;
6. escrever um teste;
7. registrar o que foi aprendido.

# Resultado esperado em dezembro de 2027

Ao concluir a trilha, você deverá ser capaz de:

- programar em Python com autonomia básica/intermediária;
- modelar classes e responsabilidades;
- criar APIs FastAPI conectadas a banco de dados;
- escrever consultas SQL úteis;
- trabalhar com Git, GitHub, Linux e Docker;
- criar testes automatizados;
- compreender arquitetura e decisões de engenharia;
- construir aplicações com LLMs, RAG e agentes;
- avaliar respostas e detectar falhas;
- tratar segurança, privacidade, custo e observabilidade;
- ler o material de uma pós avançada com muito menos dependência de explicações básicas.

## Condição de sucesso

O objetivo não é dominar todas as tecnologias do mercado até dezembro de 2027. O objetivo é chegar à pós com fundamentos sólidos, um portfólio de projetos explicáveis e capacidade de aprender novos frameworks sem começar do zero.
