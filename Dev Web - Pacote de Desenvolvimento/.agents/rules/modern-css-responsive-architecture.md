# ✦ Regra: Arquitetura CSS Moderna e Responsividade Matemática

> **Objetivo:** Banir práticas obsoletas de estilização (como 100vh instável em smartphones, cascata caótica de dezenas de media queries rígidas e tipografia fixa em pixels), substituindo-as por matemática fluida nativa (`clamp`, `dvh`), CSS Grid intrínseco e Container Queries modernas.

---

## 🚫 1. Proibição Expressa do `100vh` em Dispositivos Móveis

### ⚠️ O Problema do `100vh`:
Em navegadores móveis (Safari iOS, Chrome Android), a barra de endereços e a barra de ferramentas aparecem e desaparecem conforme o usuário rola a página. O cálculo de `100vh` ignora essas barras dinâmicas, fazendo com que botões colados no fundo fiquem cortados ou sofram saltos bruscos visuais (layout shift).

### ✅ A Solução Mandatória: Viewport Units Dinâmicas (`dvh`, `svh`, `lvh`)
- **`dvh` (Dynamic Viewport Height):** Adapta-se ativamente ao tamanho real visível quando as barras do navegador expandem ou recolhem.
- **`svh` (Small Viewport Height):** Considera as barras expandidas (pior cenário de espaço vertical).
- **`lvh` (Large Viewport Height):** Considera as barras recolhidas (tela cheia).

```css
/* Padrão para telas cheias, heros e modais */
.fullscreen-hero,
.app-screen,
.modal-overlay {
  min-height: 100vh; /* Fallback para navegadores muito antigos */
  min-height: 100dvh; /* Padrão moderno estável */
  height: auto;
}
```

---

## 📐 2. Tipografia e Espaçamento Fluido com `clamp()`

Em vez de alterar tamanhos de fonte repetitivamente em cada breakpoint com media queries (`@media (min-width: 640px)`, `@media (min-width: 768px)`, etc.), utilize funções matemáticas nativas do CSS que calculam o valor proporcionalmente à largura da tela.

### 🧮 Fórmula `clamp(MÍNIMO, PREFERIDO_DINÂMICO, MÁXIMO)`:
```css
:root {
  /* Escala tipográfica fluida entre telas de 360px e 1440px */
  --font-xs:   clamp(0.75rem,  0.70rem + 0.25vw, 0.875rem);
  --font-sm:   clamp(0.875rem, 0.80rem + 0.35vw, 1rem);
  --font-base: clamp(1rem,     0.92rem + 0.40vw, 1.125rem);
  --font-lg:   clamp(1.125rem, 1.00rem + 0.60vw, 1.375rem);
  --font-xl:   clamp(1.25rem,  1.10rem + 0.85vw, 1.75rem);
  --font-2xl:  clamp(1.5rem,   1.25rem + 1.25vw, 2.25rem);
  --font-hero: clamp(2rem,     1.50rem + 2.50vw, 3.5rem);

  /* Espaçamentos e Gaps Fluidos */
  --space-sm: clamp(8px, 1.5vw, 14px);
  --space-md: clamp(16px, 2.5vw, 28px);
  --space-lg: clamp(24px, 4vw, 48px);
  --space-xl: clamp(36px, 6vw, 72px);

  /* Largura máxima de containers com padding lateral automático */
  --container-pad: clamp(16px, 4vw, 32px);
}
```

---

## 🧩 3. Layouts Intrínsecos com CSS Grid (Grid Sem Media Queries)

Evite criar regras separadas para 1 coluna no mobile, 2 no tablet e 3 no desktop. O CSS Grid moderno é capaz de calcular automaticamente o número de colunas baseado na largura real disponível.

### 💎 O Idioma Canônico do Grid Intrínseco:
```css
.card-grid {
  display: grid;
  /* Cria tantas colunas de no mínimo 280px quantas couberem; 
     o min(100%, 280px) protege contra telas menores que 280px */
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: var(--space-md);
  width: 100%;
}
```

---

## 📦 4. Container Queries (`@container`)

Media queries olham para a janela inteira do navegador (`viewport`). Já as **Container Queries** permitem que um componente altere seu layout com base no tamanho do seu elemento pai imediato.

Isso é fundamental para widgets que podem ser colocados tanto em uma barra lateral estreita (300px) quanto na área principal larga (800px):

```css
/* 1. Declare o elemento pai como container */
.widget-card-wrapper {
  container-type: inline-size;
  container-name: card-container;
}

/* 2. Estilize o filho baseado no container */
.widget-card {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Quando o container pai tiver 450px ou mais, passe para layout horizontal */
@container card-container (min-width: 450px) {
  .widget-card {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }
}
```

---

## 🌐 5. Propriedades Lógicas CSS (Logical Properties)

Substitua propriedades físicas direcionais (`left`, `right`, `top`, `bottom`) por propriedades lógicas independentes do sentido de escrita:

- `margin-left` / `margin-right` ➔ **`margin-inline`**
- `margin-top` / `margin-bottom` ➔ **`margin-block`**
- `padding-left` / `padding-right` ➔ **`padding-inline`**
- `padding-top` / `padding-bottom` ➔ **`padding-block`**
- `width` ➔ **`inline-size`**
- `height` ➔ **`block-size`**

---

## 🎨 6. Arquitetura de Temas e Tokens Visuais

Não faça hardcode de cores hexadecimais no meio do CSS. Centralize tudo em variáveis CSS organizadas com suporte automático a `light` e `dark`:

```css
:root {
  /* Cores Base Escuras (Default Moderno) */
  --bg-primary: #0b0f17;
  --bg-surface: #131b2e;
  --bg-surface-hover: #1c2742;
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-active: rgba(99, 102, 241, 0.4);
  
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-faint: #64748b;
  
  --accent-primary: #6366f1;
  --accent-hover: #4f46e5;
  --accent-glow: rgba(99, 102, 241, 0.25);
  
  --color-success: #10b981;
  --color-danger: #ef4444;
  --color-warning: #f59e0b;
}

/* Suporte dinâmico a tema claro quando explicitado */
[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-surface-hover: #f1f5f9;
  --border-subtle: #e2e8f0;
  --border-active: rgba(99, 102, 241, 0.3);
  
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-faint: #94a3b8;
}
```

---

## 📋 Checklist de Aceitação para Agentes:
- [ ] Nenhum elemento de tela cheia usa apenas `100vh` sem `100dvh`.
- [ ] A tipografia principal usa `clamp()` para transição suave sem saltos de quebra.
- [ ] Grids utilizam `repeat(auto-fit, minmax(...))` com proteção `min(100%, ...)`.
- [ ] Todas as cores e tamanhos recorrentes usam variáveis CSS `:root`.
- [ ] Propriedades lógicas (`margin-inline`, `padding-block`) utilizadas onde aplicável.
