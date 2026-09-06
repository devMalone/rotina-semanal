# Antigravity Dev Standards
## Manual de Desenvolvimento de Sites e Aplicações Web

Versão 1.1 — 2026-09

---

Este diretório contém os sete documentos permanentes que definem todos os padrões
técnicos, visuais, de componentes, de experiência, de PWA/engenharia moderna e comerciais do ecossistema Antigravity.

Todo projeto novo deve seguir estes documentos rigorosamente.

---

## Documentos

### 01-FTI-Ficha-Tecnica-Implementacao.md
O contrato técnico. Define arquitetura, stack, responsividade, performance, SEO,
acessibilidade, JavaScript, convenções de código e o checklist obrigatório de qualidade.
Leia antes de escrever qualquer linha de código.

### 02-Design-System.md
A fonte de verdade visual. Define todos os tokens de design: cores por tema,
tipografia, espaçamento, bordas, sombras, transições e sua aplicação prática
em layouts, imagens e navegação responsiva.

### 03-Biblioteca-Componentes.md
O catálogo de componentes reutilizáveis com HTML, CSS e JS prontos para uso.
Contém: Navbar, Hero (2 variantes), Botões, Cards, Galeria com filtros, Formulário
WhatsApp, FAQ Accordion, Depoimentos, Float WhatsApp, Scroll Progress, Footer,
Reveal Animation e Cursor Customizado.

### 04-Guia-Experiencia-Premium.md
Os princípios que elevam um site de funcional para extraordinário.
Contém: o que define premium, direção de arte por segmento, motion design,
microinterações, experiência mobile, copywriting de conversão, testes de qualidade
e o prompt padrão para uso com IA.

### 05-Sistema-Tiers.md
A matriz comercial e técnica de produtos web.
Contém: classificação por pontuação, especificação de escopo/limites dos Tiers (Essential,
Professional, Premium), faixas indicativas internas de preço/prazo, tabela de Add-ons e
regras de seleção obrigatória para agentes.

### 06-Guia-Comercial-Landing-Pages.md
O guia comercial e operacional consolidado de landing pages.
Contém: tabela comparativa de plataformas, tabela de precificação 2026, retainers de manutenção mensal,
stack moderno (Next.js/Tailwind/Vercel/CI-CD), ecossistema de ferramentas (Stripe, Hotjar, Zapier, Figma),
pipelines de Agentes IA (Antigravity IDE), compliance legal LGPD, contrato, acessibilidade (LBI/ABNT/WCAG),
diagramas Mermaid (Integrações e Gantt) e checklists de QA por tier.

### 07-Pesquisa-Aprofundada-Engenharia-Web-Moderna.md
O relatório mestre de pesquisa aprofundada em engenharia web (desktop & smartphone).
Contém: arquitetura PWA profissional, CSS Moderno (`clamp`, `dvh`, Container Queries), ergonomia tátil mobile
(Thumb Zone, Safe Areas, alvos de toque 48px), formulários de alta precisão (`inputmode`, zero zoom no iOS),
métricas Core Web Vitals (LCP < 1.2s, INP < 50ms, CLS = 0), combate aos 8 clichês de IA e o Playbook Pré-Voo
para Agentes Autônomos.

---

## Como Usar com IA

Ao pedir a criação de um novo site, PWA ou correção de um existente, inclua no prompt:

"Siga rigorosamente os documentos Antigravity Dev Standards:
01-FTI, 02-Design-System, 03-Biblioteca-Componentes, 04-Guia-Experiencia-Premium, 05-Sistema-Tiers, 06-Guia-Comercial e 07-Pesquisa-Aprofundada-Engenharia-Web-Moderna.
As especificações têm prioridade sobre qualquer decisão automática."

---

## Estrutura do Ecossistema

```
Dev Web - Pacote de Desenvolvimento/
├── .agents/                 <- Regras e skills dos agentes
│   ├── AGENTS.md            <- Orquestrador mestre dos agentes
│   ├── rules/               <- 10 regras específicas (PWA, Ergonomia, Anti-IA, etc.)
│   └── skills/              <- Skills operacionais (pwa_scaffold, etc.)
│
└── docs/                    <- Este diretório (padrões permanentes)
    ├── README.md
    ├── 01-FTI-Ficha-Tecnica-Implementacao.md
    ├── 02-Design-System.md
    ├── 03-Biblioteca-Componentes.md
    ├── 04-Guia-Experiencia-Premium.md
    ├── 05-Sistema-Tiers.md
    ├── 06-Guia-Comercial-Landing-Pages.md
    └── 07-Pesquisa-Aprofundada-Engenharia-Web-Moderna.md
```

---

## Histórico de Versões

- **v1.1 (2026-09):** Adição do documento 07 de Engenharia Web Moderna e PWA, novas regras de ergonomia tátil, padrões PWA, formulários sem bloqueios e criação da skill `pwa_scaffold`.
- **v1.0 (2026-08):** Versão inicial com documentos 01 a 06 e base de regras e skills.

---

*Antigravity Dev Standards v1.1 | 2026-09*
