# Roadmap Bike ERP

## Fase 1 - Fundação do Projeto

Status: Em andamento

- [x] Criar repositório GitHub
- [x] Definir objetivo do projeto
- [x] Criar estrutura inicial
- [ ] Configurar ambiente Doodba
- [ ] Subir primeiro ambiente Odoo

---

## Fase 2 - Ambiente Desenvolvimento

- [ ] Docker
- [ ] PostgreSQL
- [ ] Odoo local
- [ ] VS Code configurado
- [ ] Claude Code configurado

---

## Fase 3 - Desenvolvimento dos módulos

- [x] bike_base (fundação: menu, categoria, grupos de segurança)
- [x] Catálogo (produtos físicos + serviços, configuração via UI, sem código)
- [ ] bike_workshop (Ordem de Serviço sobre sale.order, barcode, relatórios)
  - [x] Menu/ação "Ordem de Serviço" sobre `sale.order`
  - [ ] Diários de pagamento (Caixa/PIX/Débito/Crédito) — configurar via UI depois de
        instalar a contabilidade (depende da localização/plano de contas escolhido; não
        hardcoded em dados para não quebrar o install)
  - [ ] Validação fim a fim (estoque + fatura + pagamento) com o ambiente Doodba rodando
  - [x] Leitura de código de barras nas linhas (assistente "Escanear Produto": localiza
        produto por `barcode`, incrementa linha existente ou cria nova; avisa se não
        encontrado ou se houver ambiguidade) — falta testar no navegador com o ambiente
        rodando
  - [x] Relatórios: "Ordem de Serviço" (PDF/A4, reaproveita o corpo do relatório nativo
        de `sale.order`) + "Comprovante (sem valor fiscal)" (térmico 80mm,
        `report.paperformat` dedicado) — falta validar a renderização PDF/impressão com
        o ambiente rodando
- [x] bike_theme (identidade visual: CSS com paleta placeholder em variáveis
      `--bike-primary`/`--bike-primary-dark`, sem lógica de negócio; trocar pelas cores
      reais da bicicletaria quando definidas; logo continua sendo configurado em
      Settings > Companies, não em código) — falta validar visualmente no navegador
- [x] Tela inicial enxuta (5 apps de topo, sem o antigo "Bike ERP" guarda-chuva):
      Estoque e Financeiro (bike_workshop, novos e enxutos: Produtos/Ajuste de Estoque e
      Faturas/Pagamentos, reaproveitando `product.template`, `stock.quant`,
      `account.move`, `account.payment` diretamente), Ordem de Serviço (agora top-level,
      não mais dentro de "Bike ERP"), Contatos e Usuários+Grupos (bike_base).
      Discuss/Painéis/Rastreio de links/Contatos-nativo/Vendas-nativo ficam ocultos para
      todo mundo, e Inventário/Faturamento nativos ficam restritos ao Administrador —
      tudo via um `post_init_hook` em `bike_base` (identifica os menus pelo módulo
      técnico dono, não pelo nome, então funciona em qualquer idioma). Administrador
      também ganha `base.group_system` (mantém Aplicativos e Definições). **Pendente de
      verificar ao testar:** se `stock.group_stock_user` (que `group_bike_user` implica)
      realmente permite editar quantidade em "Ajuste de Estoque" — o Odoo às vezes
      reserva isso para o grupo de gerente de estoque; se o Usuário só conseguir
      visualizar sem editar, precisamos ajustar o ACL/direito específico depois de
      confirmar o comportamento real.

---

## Fase 4 - Produção

- [ ] VPS
- [ ] Docker produção
- [ ] SSL
- [ ] Backup
- [ ] CI/CD
