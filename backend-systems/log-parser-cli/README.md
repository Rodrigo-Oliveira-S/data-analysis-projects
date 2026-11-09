# Log Parser CLI - Analisador e Diagnosticador de Incidentes

Uma ferramenta de linha de comando (CLI) desenvolvida em **Python 3.13** para leitura, parsing e diagnóstico automatizado de arquivos de log de sistemas e aplicações. 

O projeto foi construído para simular a rotina de um **Analista de Suporte L2** e **Desenvolvedor Backend**, permitindo investigar rapidamente incidentes de produção, falhas de infraestrutura e erros HTTP (4xx e 5xx).

---

##  Funcionalidades

- **Parsing Inteligente com Regex:** Extrai data/hora, nível do log (`INFO`, `WARNING`, `ERROR`), módulo afetado, mensagem técnica e status HTTP.
- **Detecção de Falhas Críticas:** Classifica automaticamente registros com nível `ERROR` e respostas HTTP `500` (Erros de Servidor/Banco) e `4xx` (Erros de Cliente/Autenticação).
- **Interface Terminal com Rich:** Apresenta relatórios formatados em tabelas coloridas, facilitando a leitura durante a triagem de incidentes.
- **Resumo de Impacto por Módulo:** Consolida a contagem de falhas por componente (ex: `auth`, `database`, `api`).
- **Suporte a Arquivos Externos:** Aceita qualquer arquivo `.log` informado via argumento CLI (`sys.argv`).

---

## Tecnologias e Bibliotecas

- **Python 3.13:** Linguagem base do projeto.
- **Rich:** Formatação visual do terminal (tabelas, painéis e cores).
- **Re (Regex):** Expressões regulares para extração e estruturação de texto.
- **Pathlib & Sys:** Manipulação nativa de caminhos no Linux Debian e gerenciamento de execução CLI.
- **Git:** Controle de versão com fluxo de branches (`feature/log-parser`).

---

##  Estrutura do Projeto

```text
log-parser-cli/
├── data/
│   └── sample.log       # Massa de dados de teste simulando logs de aplicação
├── src/
│   └── parser.py        # Script principal da CLI de parsing
└── README.md            # Documentação do projeto
```

---

##  Como Executar

### 1. Pré-requisitos
Certifique-se de que o ambiente virtual `.venv` está ativado e as dependências instaladas:

```bash
source ~/work-environment/.venv/bin/activate
pip install rich
```

### 2. Executar com a Massa de Testes Padrão

Navegue até o diretório do projeto e execute:

```bash
python3 src/parser.py
```

### 3. Executar Analisando um Log Personalizado

Você pode passar o caminho de qualquer arquivo de log do sistema como argumento:

```bash
# Exemplo: Analisando logs extraídos do systemd (Debian)
journalctl -n 100 --no-pager > data/system.log
python3 src/parser.py data/system.log
```

---

## 📊 Exemplo de Saída no Terminal

```text
╭────────────────────────────────────────────╮
│ DIAGNÓSTICO DE INCIDENTES - LOG PARSER CLI │
╰────────────────────────────────────────────╮
Arquivo analisado: sample.log

                     Ocorrências Críticas Detectadas                     
┏━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Linha ┃ Data/Hora     ┃  Nível  ┃ Módulo   ┃ Mensagem       ┃ Status ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│   3   │ 2026-10-28    │  ERROR  │ database │ Connection     │  500   │
│       │ 10:00:05      │         │          │ timeout        │        │
├───────┼───────────────┼─────────┼──────────┼────────────────┼────────┤
│   6   │ 2026-10-28    │  ERROR  │ auth     │ Invalid        │  401   │
│       │ 10:03:10      │         │          │ credentials    │        │
└───────┴───────────────┴─────────┴──────────┴────────────────┴────────┘

Resumo de Afetados por Módulo:
 • database: 2 falhas
 • api: 2 falhas
 • auth: 1 falhas
```

---

## 🔍 Contexto de Uso em Suporte L2

Durante um chamado técnico de indisponibilidade, este script permite ao analista L2:
1. Conectar via SSH ao servidor Linux.
2. Executar a CLI sobre os arquivos de log do serviço afetado.
3. Isolar o *timestamp* e o *stacktrace* do erro em segundos.
4. Anexar o diagnóstico exato no ticket antes de escalar a falha para o time de desenvolvimento (L3/Dev).
