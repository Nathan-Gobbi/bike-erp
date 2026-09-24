[![Odoo](https://img.shields.io/badge/odoo-v18.0-a3478a)](https://github.com/odoo/odoo/tree/18.0)
[![Python](https://img.shields.io/badge/python-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Doodba deployment](https://img.shields.io/badge/deployment-doodba-2496ed?logo=docker&logoColor=white)](https://github.com/Tecnativa/doodba)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![AGPL-3.0-or-later license](https://img.shields.io/badge/license-AGPL--3.0--or--later-success)](LICENSE)

# Bike ERP

ERP para uma bicicletaria construído sobre o **Odoo 18**, cobrindo o fluxo real de
balcão: venda de peças, atendimento de oficina (Ordem de Serviço), estoque, faturamento
e pagamento — tudo em uma interface enxuta com apenas 5 apps.

O projeto segue a filosofia **reutilizar > configurar > estender > customizar > criar do
zero**: a maior parte das necessidades é resolvida com módulos nativos do Odoo e da
[OCA](https://github.com/OCA), e código próprio só é escrito quando há uma necessidade
técnica real.

## Funcionalidades

- **Ordem de Serviço sobre `sale.order`** — produtos físicos e serviços de oficina na
  mesma ordem, com estoque, fatura e pagamento nativos.
- **Leitura de código de barras** — assistente "Escanear Produto" que localiza o produto
  pelo `barcode`, incrementa a linha existente ou cria uma nova, e avisa em caso de
  código inexistente ou duplicado.
- **Relatórios PDF** — Ordem de Serviço (A4) e comprovante não fiscal para impressora
  térmica de 80 mm, com `report.paperformat` dedicado.
- **Tela inicial enxuta** — um `post_init_hook` oculta apps nativos desnecessários e
  restringe outros ao administrador, identificando os menus pelo módulo técnico
  (funciona em qualquer idioma).
- **Perfis de acesso** — grupos "Usuário" e "Administrador" do Bike ERP com ACLs
  próprias.
- **Identidade visual** — módulo de tema isolado, só CSS com variáveis de cor.

## Módulos próprios

| Módulo                                                   | Responsabilidade                                                                                              |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [`bike_base`](odoo/custom/src/private/bike_base)         | Menus, categorias de produto, grupos de segurança, dados de demonstração e o hook que organiza a tela inicial |
| [`bike_workshop`](odoo/custom/src/private/bike_workshop) | Ordem de Serviço, wizard de código de barras, relatórios, menus de Estoque e Financeiro                       |
| [`bike_theme`](odoo/custom/src/private/bike_theme)       | Paleta de cores do backend (sem lógica de negócio)                                                            |

Módulos OCA utilizados: `product_brand` (marca do produto) e `web_responsive`.

## Tecnologias

- Python e Odoo 18 (ORM, views XML, relatórios QWeb, wizards, hooks)
- PostgreSQL
- Docker + [Doodba](https://github.com/Tecnativa/doodba) (Tecnativa)
- Invoke, pre-commit, Ruff, Pylint-Odoo, Prettier
- Git Flow (branches `feature/*` → `develop` → `main`) e Conventional Commits

## Decisões de arquitetura

As decisões estão registradas como ADRs em [`docs/adr`](docs/adr) e resumidas em
[`docs/arquitetura-modulos.md`](docs/arquitetura-modulos.md). Destaques:

- A Ordem de Serviço é um `sale.order` padrão, e não um `repair.order`: o fluxo de
  balcão não tem um equipamento identificável a reparar, e `sale.order` é a base que a
  localização fiscal brasileira da OCA (`l10n_br_sale`) já pressupõe.
- Não há cadastro de bicicleta do cliente nem POS no MVP, para evitar atrito operacional
  e telas duplicadas.

O andamento do projeto está em [`docs/00-roadmap.md`](docs/00-roadmap.md).

## Como rodar localmente

Pré-requisitos: Docker com Docker Compose, Python 3, [Invoke](https://www.pyinvoke.org/)
e [pre-commit](https://pre-commit.com/) (`pipx install invoke pre-commit`).

```bash
git clone git@github.com:Nathan-Gobbi/bike-erp.git
cd bike-erp

invoke develop         # prepara o ambiente de desenvolvimento e os hooks do pre-commit
invoke img-pull        # baixa as imagens Docker
invoke git-aggregate   # baixa o código do Odoo e dos módulos OCA
invoke img-build       # constrói a imagem do Odoo
invoke resetdb --modules=bike_base,bike_workshop,bike_theme
invoke start
```

Acesse **http://localhost:18069** (usuário `admin`, senha `admin`).

Outros comandos úteis:

```bash
invoke logs                          # acompanhar os logs
invoke test --modules=bike_workshop  # rodar os testes de um módulo
invoke stop
```

## Estrutura

```text
bike-erp/
├── docs/                      # roadmap, arquitetura e ADRs
├── odoo/custom/src/
│   ├── addons.yaml            # módulos OCA habilitados
│   ├── repos.yaml             # repositórios agregados (OCB, OCA)
│   └── private/               # módulos próprios: bike_base, bike_workshop, bike_theme
├── devel.yaml / prod.yaml     # composições Docker por ambiente
└── tasks.py                   # tarefas Invoke do Doodba
```

## Próximos passos

- Testes automatizados para o wizard de código de barras e para o hook de menus
- Validação ponta a ponta (estoque → fatura → pagamento)
- Deploy em VPS com SSL, backup e CI/CD

## Autor

**Nathan Gobbi** — Desenvolvedor Python Jr.

Projeto gerado a partir do
[doodba-copier-template](https://github.com/Tecnativa/doodba-copier-template),
licenciado sob AGPL-3.0-or-later.
