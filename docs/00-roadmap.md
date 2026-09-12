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
  - [ ] Relatórios (OS completa + comprovante não fiscal)
- [ ] bike_theme (identidade visual)

---

## Fase 4 - Produção

- [ ] VPS
- [ ] Docker produção
- [ ] SSL
- [ ] Backup
- [ ] CI/CD
