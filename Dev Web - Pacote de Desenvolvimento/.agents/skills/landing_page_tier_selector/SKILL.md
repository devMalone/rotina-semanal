---
name: landing_page_tier_selector
description: >
  Ativado em qualquer solicitação de criação, planejamento ou desenvolvimento de landing page, site ou página web no workspace Antigravity/Empreender.
  Obriga o agente a perguntar e definir qual categoria (Tier 1 — Essential, Tier 2 — Professional ou Tier 3 — Premium) a página deve seguir antes de escrever qualquer código.
---

# Landing Page Tier Selector — Instrução de Seleção de Categoria

Sempre que o usuário solicitar a criação de uma nova landing page, site ou projeto web (ou refinamento estrutural de um site existente), você **DEVE** seguir este fluxo rigoroso **ANTES** de gerar HTML, CSS ou estrutura de arquivos:

---

## Passo 0 — Interrupção Obrigatória: Definir o Tier

**NÃO comece a escrever código imediatamente.** 

Você deve primeiro **perguntar ao usuário** qual é a categoria/tier desejado para a landing page, ou ajudar no enquadramento caso o escopo ainda seja incerto.

Apresente a pergunta de forma clara com as 3 opções disponíveis:

1. **Tier 1 — Essential (Presença Profissional)**
   - *Escopo*: 5 a 7 seções, layout clean, responsivo, botões CTA/WA, SEO básico.
   - *Ideal para*: Projetos rápidos, pequenos negócios, baixo orçamento.

2. **Tier 2 — Professional (Experiência que Converte)**
   - *Escopo*: 8 a 11 seções, direção de arte personalizada, FAQ accordion, galeria com abas/filtros, animações de scroll (`IntersectionObserver`), formulários validados.
   - *Ideal para*: Empresas consolidadas, prestadores de serviço buscando destaque comercial.

3. **Tier 3 — Premium (Experiência Digital Exclusiva)**
   - *Escopo*: 10 a 15 seções, visual editorial/cinematográfico, scrolltelling, Lightbox modal avançado, SEO técnico (`Schema.org`), WCAG 2.2 AA.
   - *Ideal para*: Marcas de alto padrão, clínicas premium, estúdios fine art.

*Nota*: Se o usuário já tiver especificado o tier na mensagem inicial (ex: "Crie uma LP Tier 2 para barbearia"), confirme a escolha e prossiga para o Passo 1.

---

## Passo 1 — Ler a Especificação do Tier Selecionado

Após a confirmação do Tier, leia os seguintes documentos em `docs/`:

1. `docs/05-Sistema-Tiers.md` — verifique o escopo, seções incluídas e proibições do tier escolhido.
2. `docs/01-FTI-Ficha-Tecnica-Implementacao.md` — arquitetura e checklist.
3. `docs/02-Design-System.md` — tokens visuais.
4. `docs/03-Biblioteca-Componentes.md` — código base dos componentes.
5. `docs/04-Guia-Experiencia-Premium.md` — diretrizes de UX e acabamento.

---

## Passo 2 — Aplicar o Tier como Contrato Rígido

A especificação do Tier funciona como **teto máximo e piso mínimo**:

- **Não ultrapassar o escopo**: Se o projeto for Tier 1 ou 2, **NÃO** adicione bibliotecas pesadas de animação, scrolltelling ou recursos exclusivos de Tier 3 sem solicitação explícita do usuário.
- **Respeitar as inclusões obrigatórias**: Certifique-se de que todas as seções e recursos previstos para aquele Tier estão presentes no projeto.
- **Setor de Gastronomia & Alimentação Local**: Aplicar obrigatoriamente a regra `.agents/rules/cro-gastronomia-alimentacao.md`:
  - **Tier 1 (Essential)**: Hero sensorial + Especialidades com fotos reais e botões de WhatsApp direto + Fornadas/Horários + Localização e Mapa.
  - **Tier 2 (Professional)**: Abas de categorias no cardápio + Formulário de encomendas/orçamentos + Depoimentos + Tradição da casa.
  - **Tier 3 (Premium)**: Catálogo interativo de alta gastronomia + Montagem customizada de pedidos + Experiência imersiva.

---

## Passo 3 — Registrar o Metadado no HTML

Em todo arquivo `index.html` criado ou atualizado, inclua o comentário no topo do `<head>`:

```html
<!-- 
  Antigravity Dev Standards
  Project Tier: TIER [1|2|3] - [ESSENTIAL|PROFESSIONAL|PREMIUM]
  Specification: docs/05-Sistema-Tiers.md
-->
```
