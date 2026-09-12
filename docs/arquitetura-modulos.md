# Arquitetura de Módulos — Bike ERP

> Revisado após análise arquitetural completa (ver `docs/adr/`). Prioridade:
> **reutilizar > configurar > estender > customizar > criar do zero**. A maior parte das
> áreas de negócio abaixo é resolvida por módulos nativos do Odoo 18 e da OCA,
> configurados via dados — não por módulos de código próprios por área.

```
Bike ERP
├── Odoo nativo
│   ├── res.partner            → clientes, fornecedores, contatos
│   ├── product.template/product → produtos físicos e serviços (mesmo catálogo)
│   ├── stock + sale_stock     → estoque, movimentos, picking (só produtos físicos)
│   ├── sale.order             → Ordem de Serviço (produtos + serviços na mesma linha)
│   ├── account.move/payment   → faturamento e pagamento
│   └── barcodes               → infraestrutura nativa de código de barras
│
├── OCA
│   ├── OCA/brand → product_brand        (marca do produto)
│   ├── OCA/stock-logistics-barcode → web_ir_actions_client_scan (avaliar, opcional)
│   └── (futuro) OCA/l10n-brazil          (NF-e/NFC-e/NFS-e — não instalar ainda)
│
└── Custom
    ├── bike_base       → menu raiz, categoria e grupos de segurança (Usuário/Administrador)
    ├── bike_workshop   → sale.order como Ordem de Serviço: barcode nas linhas,
    │                      relatórios (OS completa + comprovante não fiscal)
    └── bike_theme      → identidade visual, sem lógica de negócio
```

## Decisões que substituem o mapa anterior

- **Não há cadastro de bicicleta do cliente** (nem model próprio, nem `stock.lot`) —
  alta rotatividade tornaria o cadastro um atrito operacional sem benefício comprovado.
  Se necessário, texto livre na própria Ordem de Serviço.
- **Não há `repair.order`** como base da Ordem de Serviço — o model de reparo nativo
  pressupõe um equipamento identificável a reparar, o que não reflete o fluxo real do
  balcão. A Ordem de Serviço é um `sale.order` padrão.
- **Não há POS no MVP** — um único fluxo (`sale.order`) já cobre venda de produto avulso
  e atendimento de oficina sem duplicar tela/estoque/pagamento.
- **`bike_purchase`, `bike_stock`, `bike_sale`, `bike_finance`, `bike_dashboard`,
  `bike_ecommerce`, `bike_api`** do mapa original não são módulos de código — as
  necessidades correspondentes são atendidas por `purchase`/`stock`/`sale`/`account`
  nativos configurados. Um módulo próprio só é criado quando surgir uma necessidade
  técnica real não coberta por nativo/OCA.

Detalhes completos da análise (comparação `sale.order` x `repair.order`, fluxo de
estoque, segurança, fiscal futuro etc.) estão registrados no histórico de planejamento
do projeto.
