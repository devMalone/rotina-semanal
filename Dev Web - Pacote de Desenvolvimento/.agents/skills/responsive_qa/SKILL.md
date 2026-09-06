---
name: responsive_qa
description: >
  Ativado quando o agente conclui a geração ou correção de qualquer landing page,
  site ou componente HTML/CSS no workspace Antigravity/Empreender. Instrui o agente
  a executar o protocolo completo de QA responsivo antes de declarar a página como
  entregue. Cobre 9 resoluções canônicas (de 320px a 1920px), checklist estruturado
  por categoria e um relatório de saída padronizado.
---

# Responsive QA — Protocolo de Validação de Entrega

> **Gatilho:** Esta skill deve ser executada **obrigatoriamente** ao final de qualquer
> criação, correção ou modificação significativa de landing page ou componente web.
> Não declare uma página como "pronta" ou "entregue" sem passar por este protocolo.

---

## Objetivo

Garantir que toda página do ecossistema Antigravity funcione corretamente nas
resoluções mais utilizadas no Brasil, eliminando o cenário de "a página fica boa
na maioria das telas mas quebra em algumas".

---

## Parte 1 — As 9 Resoluções Canônicas

Valide (mentalmente via análise de código, ou fisicamente via DevTools) a página
nas seguintes resoluções, em ordem crescente:

| # | Viewport    | Dispositivo Referência            | Breakpoint CSS |
|---|-------------|-----------------------------------|----------------|
| 1 | 320 × 568   | iPhone SE 1ª geração, Android min | `< 360px`      |
| 2 | 360 × 800   | Android popular (Samsung A-series)| `≥ 360px`      |
| 3 | 375 × 667   | iPhone SE 2ª e 3ª geração         | `≥ 360px`      |
| 4 | 390 × 844   | iPhone 14 / 15                    | `≥ 390px`      |
| 5 | 414 × 896   | iPhone XR / 11                    | `≥ 390px`      |
| 6 | 768 × 1024  | iPad portrait                     | `≥ 768px`      |
| 7 | 1280 × 800  | Laptops mais comuns               | `≥ 1024px`     |
| 8 | 1440 × 900  | MacBook Air, laptops mid-range    | `≥ 1440px`     |
| 9 | 1920 × 1080 | Monitor Full HD padrão            | `≥ 1920px`     |

---

## Parte 2 — Checklist por Categoria

Para cada uma das 9 resoluções acima, valide os itens abaixo.

### 🔲 OVERFLOW & LAYOUT
- [ ] Nenhum elemento ultrapassa a largura do viewport (sem scroll horizontal)
- [ ] `.container` mantém padding lateral ≥ 16px em telas ≤ 480px
- [ ] Grids colapsam para coluna única abaixo de 768px
- [ ] Elementos com `position: absolute` não escapam do pai

### 🔲 TIPOGRAFIA
- [ ] `h1` legível em 320px — verificar se `clamp()` está correto
- [ ] Body text `font-size` ≥ 14px em todos os viewports
- [ ] Nenhum texto cortado por `overflow: hidden`
- [ ] Line-height suficiente para o tamanho de fonte usado

### 🔲 BOTÕES & TOUCH TARGETS
- [ ] Todo elemento interativo: `min-height: 44px; min-width: 44px`
- [ ] Botões com texto longo: `white-space: normal` + `word-break: break-word`
- [ ] Botões de CTA em mobile: `width: 100%` ou contidos no container pai
- [ ] Botão flutuante WhatsApp (`.wa-float`) não cobre conteúdo crítico
- [ ] `font-size: 16px` em todos os `<input>`, `<select>`, `<textarea>` no mobile (evita zoom iOS)

### 🔲 IMAGENS & MÍDIA
- [ ] Imagens: `max-width: 100%; height: auto; display: block`
- [ ] Hero usa `min-height: 100dvh` (nunca `height: 100dvh` fixo)
- [ ] Aspect-ratios preservados em resize progressivo
- [ ] Imagens com `object-fit: cover` não distorcem o sujeito principal

### 🔲 NAVEGAÇÃO & ROLAGEM DE ÂNCORAS
- [ ] Header fixo compensa `padding-top` do hero (`calc(var(--header-height) + X)`)
- [ ] `scroll-padding-top: var(--header-height)` no `html` e `scroll-margin-top` nas seções `[id]` declarados (PM-13)
- [ ] Links do menu (`href="#id"`) posicionam o título `h2` da seção visível **abaixo** do header fixo (sem ser escondido)
- [ ] Acesso direto via URL com hash (`#secao`) posiciona o topo da seção corretamente
- [ ] Menu hambúrguer abre e fecha corretamente
- [ ] Ícone hambúrguer **não some** após toggle (PM-05 — nunca recriar o nó com `innerHTML` dentro do evento `click`)
- [ ] `body.menu-open` trava o scroll quando o menu está aberto
- [ ] Links do menu fecham o drawer ao clique

### 🔲 DESKTOP LARGO (1440px e 1920px)
- [ ] Conteúdo centralizado via `max-width` no container
- [ ] Cards individuais não excedem ~400px de largura em grids
- [ ] Nenhuma seção parece "perdida" com espaço em branco excessivo nas laterais
- [ ] Backgrounds de seção se estendem full-width, mas texto fica contido

### 🔲 ACESSIBILIDADE BÁSICA
- [ ] Contraste de texto ≥ 4.5:1 (WCAG AA) nos elementos principais
- [ ] `alt` descritivo em todas as imagens (`alt=""` apenas em imagens decorativas)
- [ ] Elementos interativos acessíveis via teclado (`Tab`, `Enter`, `Space`)
- [ ] `aria-label` nos botões sem texto visível (ex: ícones)

---

## Parte 3 — Protocolo de Execução

### Como executar a validação

**Opção A — Via código (análise estática)**
Percorra o CSS do arquivo `index.html` e verifique:
1. Existência de media queries para `480px`, `768px`, `992px`
2. Botões: `white-space: normal`, `max-width: 100%`, `word-break: break-word`
3. Container: `padding: 0 1rem` em mobile
4. `.hero`: `min-height: 100dvh`
5. Grids: `display: flex; flex-direction: column` em mobile

**Opção B — Via ferramenta de navegador (DevTools)**
Instrua o usuário a abrir o arquivo no Chrome e testar nas dimensões:
`320px`, `375px`, `390px`, `768px`, `1280px`, `1440px`, `1920px`

---

## Parte 4 — Relatório de Saída (Obrigatório)

Ao final do QA, o agente **deve** emitir um relatório resumido no seguinte formato:

```
📋 RELATÓRIO DE QA RESPONSIVO — [Nome da Página]
Tier: [Tier N — Nome] | Data: [data]

RESOLUÇÕES VALIDADAS:
  ✅ 320px — OK: layout em coluna, sem overflow
  ✅ 375px — OK: CTA contida, botões width:100%
  ✅ 390px — OK: tipografia fluida
  ✅ 414px — OK
  ✅ 768px — OK: grid 2 colunas
  ✅ 1280px — OK: grid 3 colunas
  ✅ 1440px — OK: container centralizado
  ✅ 1920px — OK: sem "ilhas de conteúdo"

CATEGORIAS:
  ✅ Overflow & Layout
  ✅ Tipografia
  ✅ Botões & Touch Targets
  ✅ Imagens & Mídia
  ✅ Navegação
  ✅ Desktop Largo
  ✅ Acessibilidade Básica

PROBLEMAS ENCONTRADOS: nenhum / [listar se houver]
STATUS: ✅ APROVADA PARA ENTREGA
```

Se houver falhas, corrigi-las **antes** de emitir o STATUS como aprovado.

---

## Parte 5 — Regras de Não-Regressão

Ao fazer qualquer correção de responsividade, verificar se a mudança não quebra:
1. O layout em desktop (1440px) — os breakpoints com `max-width` só afetam mobile
2. A seção anterior ou posterior à que foi corrigida
3. O componente `.wa-float` (costuma ser afetado por mudanças em `z-index` e `position`)
4. O menu hambúrguer (sensível a mudanças em `overflow` do body)

---

## Referências Obrigatórias

- **FTI Capítulo 7** — `docs/01-FTI-Ficha-Tecnica-Implementacao.md` (Seções 7.1 a 7.5)
- **Post-Mortems PM-01 a PM-11** — FTI Capítulo 20
- **Checklist QA por Tier** — `docs/06-Guia-Comercial-Landing-Pages.md`
