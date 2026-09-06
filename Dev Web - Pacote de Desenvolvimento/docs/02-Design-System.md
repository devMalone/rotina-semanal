# Design System
### Versão 1.0 — Antigravity Dev Standards

---

## Objetivo

Este documento define o sistema de design visual do ecossistema Antigravity.
É a fonte única da verdade para cores, tipografia, espaçamentos, componentes visuais e tokens de design.

Todo projeto deve herdar e respeitar este Design System.

---

## Parte 1 — Tokens de Design

### 1.1 Tokens de Cor por Tema

#### Tema Claro Quente (padrão para fotografia/beleza/maternidade)

`
--bg-primary:    #FDFBF7  (creme off-white)
--bg-secondary:  #F5F1EB  (linho claro)
--bg-tertiary:   #EDE8E0  (bege suave)
--bg-dark:       #1A1817  (quase preto quente)
--bg-dark-alt:   #242120  (carvão)

--text-dark:     #2C2825  (castanho escuro)
--text-muted:    #7A6F68  (cinza rosado)
--text-light:    #FDFBF7  (creme — uso em fundo escuro)

--accent:        #9E8270  (marrom acinzentado)
--accent-hover:  #8A6F5E  (marrom escuro)
--accent-soft:   rgba(158, 130, 112, 0.12)
--accent-gold:   #C4A882  (dourado discreto)

--border:        rgba(44, 40, 37, 0.1)
--border-strong: rgba(44, 40, 37, 0.25)
`

#### Tema Escuro Premium (para projetos premium/dark mode)

`
--bg-primary:    #0F0F0F  (preto suave)
--bg-secondary:  #1A1A1A  (cinza muito escuro)
--bg-tertiary:   #252525  (cinza escuro)

--text-dark:     #F5F5F0  (branco quente)
--text-muted:    #888880  (cinza médio)
--text-light:    #F5F5F0

--accent:        #C4A882  (dourado)
--accent-hover:  #B8976F
--accent-soft:   rgba(196, 168, 130, 0.12)

--border:        rgba(255, 255, 255, 0.08)
--border-strong: rgba(255, 255, 255, 0.18)
`

#### Tema Barbearia/Masculino

`
--bg-primary:    #F8F6F3
--bg-dark:       #1C1A18
--accent:        #8B7355  (couro)
--accent-gold:   #D4A843

--text-dark:     #1C1A18
--text-muted:    #6B5F52
`

#### Tema Alimentação/Padaria

`
--bg-primary:    #FFFEF9
--bg-warm:       #FFF8F0
--accent:        #E07B39  (laranja queimado)
--accent-hover:  #C96B2A
--accent-soft:   rgba(224, 123, 57, 0.1)

--text-dark:     #2A1F14
--text-muted:    #7A6352
`

### 1.2 Tokens de Tipografia

`
--font-serif:  'Cormorant Garamond', 'Playfair Display', Georgia, serif
--font-sans:   'Inter', 'DM Sans', system-ui, -apple-system, sans-serif
--font-mono:   'JetBrains Mono', 'Fira Code', monospace  (uso raro)

--text-xs:   0.64rem
--text-sm:   0.8rem
--text-base: 1rem
--text-md:   1.25rem
--text-lg:   1.563rem
--text-xl:   1.953rem
--text-2xl:  2.441rem
--text-3xl:  3.052rem
--text-hero: clamp(2rem, 6vw, 5rem)

--line-height-tight:  1.2
--line-height-snug:   1.4
--line-height-normal: 1.6
--line-height-loose:  1.75

--tracking-tight:  -0.02em
--tracking-normal: 0em
--tracking-wide:   0.1em
--tracking-wider:  0.2em
--tracking-widest: 0.3em
`

### 1.3 Tokens de Espaçamento (escala 4pt)

`
--space-1:  4px
--space-2:  8px
--space-3:  12px
--space-4:  16px
--space-6:  24px
--space-8:  32px
--space-12: 48px
--space-16: 64px
--space-20: 80px
--space-24: 96px
--space-32: 128px

--section-padding: clamp(48px, 6.5vw, 110px) 0
`

### 1.4 Tokens de Borda e Raio

`
--radius-sm:   4px
--radius-md:   8px
--radius-lg:   14px
--radius-xl:   20px
--radius-2xl:  28px
--radius-full: 9999px  (pill shape)
`

### 1.5 Tokens de Sombra

`
--shadow-sm:  0 2px 8px rgba(0,0,0,0.06)
--shadow-md:  0 8px 24px rgba(0,0,0,0.10)
--shadow-lg:  0 20px 40px rgba(0,0,0,0.14)
--shadow-xl:  0 32px 64px rgba(0,0,0,0.18)
`

### 1.6 Tokens de Transição

`
--transition-fast:   all 0.2s ease
--transition-base:   all 0.35s ease
--transition-smooth: all 0.5s cubic-bezier(0.4, 0.0, 0.2, 1)
--transition-spring: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)
`

---

## Parte 2 — Tipografia em Prática

### 2.1 Hierarquia Visual

Nível 1 — Hero Title:
  - Fonte: serif
  - Peso: 300 (Light) ou 400 (Regular)
  - Tamanho: clamp(2rem, 6vw, 5rem)
  - Tracking: -0.02em a -0.01em
  - Line-height: 1.15–1.2
  - Cor: --text-dark

Nível 2 — Section Title (h2):
  - Fonte: serif
  - Peso: 300–400
  - Tamanho: clamp(1.8rem, 4vw, 3.2rem)
  - Tracking: -0.01em
  - Line-height: 1.2
  - Cor: --text-dark

Nível 3 — Subsection Title (h3):
  - Fonte: sans-serif
  - Peso: 400–500
  - Tamanho: 1.25rem–1.563rem
  - Tracking: 0em
  - Line-height: 1.3

Nível 4 — Label / Badge:
  - Fonte: sans-serif
  - Peso: 500
  - Tamanho: 0.64rem–0.8rem
  - Tracking: 0.15em–0.3em
  - Text-transform: uppercase
  - Cor: --accent

Nível 5 — Body:
  - Fonte: sans-serif
  - Peso: 300–400
  - Tamanho: 1rem (desktop), 0.9rem–1rem (mobile)
  - Line-height: 1.65–1.75
  - max-width: 65ch

### 2.2 Regras de Ouro

- Nunca misturar mais de 2 famílias tipográficas por projeto
- Serif para emoção e elegância; sans-serif para clareza e função
- Hierarquia legível a 1 metro de distância (teste de squint)
- Nunca usar bold em displays serifados decorativos
- Nunca usar letter-spacing negativo em textos de corpo

---

## Parte 3 — Componentes Visuais

### 3.1 Cards

Anatomia padrão:
  - border-radius: var(--radius-xl) (20px)
  - background: var(--bg-secondary)
  - border: 1px solid var(--border)
  - overflow: hidden
  - transition: transform 0.35s ease, box-shadow 0.35s ease

Estados:
  - default: sem sombra ou sombra mínima (--shadow-sm)
  - hover: transform translateY(-6px), box-shadow var(--shadow-lg)

### 3.2 Imagens em Cards

- object-fit: cover
- width: 100%
- height fixo por tipo:
    - card pequeno: 220px–260px
    - card médio: 280px–320px
    - card grande: 380px–420px
- hover: transform scale(1.04) (aplicado na img, não no card)
- overflow: hidden no container da img para conter o scale

### 3.3 Seção Hero

Padrão visual:
  - height: 100dvh; min-height: 540px
  - background image cobrindo 100% + parallax layer
  - overlay: linear-gradient 180deg do transparente ao --bg-primary (40–75%)
  - conteúdo centralizado com z-index 3
  - badge → título → subtítulo → botões (espaçamentos progressivos)
  - scroll indicator com animação de bounce (oculto em mobile)

### 3.4 Badges e Pills

  - display: inline-block ou inline-flex
  - padding: 0.35rem 1rem
  - border-radius: var(--radius-full)
  - font-size: 0.65rem–0.8rem
  - letter-spacing: 0.15em–0.25em
  - text-transform: uppercase
  - Variantes:
      pill-accent: background --accent-soft, color --accent
      pill-dark: background --bg-dark, color --text-light
      pill-outline: border 1px solid --border, color --text-muted

### 3.5 Dividers

  - Nunca usar hr simples
  - Preferir espaçamento generoso como separador
  - Quando necessário: width 1px, height 60–80px, background --border, margin auto

### 3.6 Overlays e Glassmorphism

  - Máximo: backdrop-filter blur(12px)
  - Background: rgba(fundo, 0.75–0.9)
  - Usar com moderação — apenas em modais, nav scrolled, e overlays de destaque
  - Nunca em múltiplos elementos na mesma view

---

## Parte 4 — Layout e Grid em Prática

### 4.1 Layouts de Seção

Seção de Destaque (feature):
  - 2 colunas: imagem 55% + conteúdo 45%
  - Alternar lado da imagem a cada seção

Seção de Cards:
  - 3 colunas (desktop), 2 (tablet), 1 (mobile)
  - Gap: var(--space-8)

Seção de Testemunhos:
  - Masonry ou grid 2-3 colunas
  - Cards com alturas variadas

Seção FAQ:
  - 1 coluna centralizada (max-width 760px)
  - Accordion com animação suave de max-height

Seção Hero Assimétrico:
  - 60% conteúdo + 40% imagem (desktop)
  - 100% empilhado (mobile)

### 4.2 Regras de Espaçamento entre Seções

  - Seção normal → seção normal: --section-padding (clamp 48–110px)
  - Seção hero → próxima seção: 0 (hero já tem 100dvh)
  - Seções irmãs com destaque alternado: nenhuma margem adicional entre elas

---

## Parte 5 — Estados e Interatividade

### 5.1 Estados de Hover

Regra geral de hover:
  - Elementos navegáveis: underline ou opacity change
  - Botões: translateY(-2px) + sombra suave
  - Cards: translateY(-6px) + sombra
  - Imagens em grid: scale(1.04)
  - Ícones: scale(1.1) ou color change

### 5.2 Estados de Focus (obrigatório)

`
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 4px;
}
`

### 5.3 Cursor Customizado

Apenas em desktop (pointer: fine):
  - Cursor ponto: 10–14px, background --accent, border-radius 50%
  - Cursor anel: 40px, border 1px solid --accent, border-radius 50%, mix-blend-mode: difference
  - Estado active (hover em interativos): anel expande, ponto desaparece

---

## Parte 6 — Responsividade Visual

### 6.1 Imagens Responsivas

Mobile:
  - Sempre width 100%, height auto
  - Mínimo height via clamp quando necessário (ex: clamp(220px, 45vw, 380px))
  - object-fit: cover em containers com height fixo

Desktop:
  - Respeitar aspect-ratio consistente
  - Usar srcset + sizes para performance

### 6.2 Tipografia Fluida

Títulos principais sempre com clamp():
  - clamp(valor-mobile, valor-vw, valor-desktop)
  - O valor vw deve produzir escala suave entre os extremos
  - Testar manualmente em 375px, 768px e 1200px

### 6.3 Navegação Mobile

Sempre drawer lateral (right drawer):
  - Entrada: right: -100% → right: 0
  - Overlay: opacity 0 → 1 com backdrop-filter blur
  - Body lock: overflow hidden + touch-action none
  - Links do menu: font-size maior (1.1–1.3rem), espaçamento generoso (1.5rem entre itens)
  - Botão de CTA principal repetido no menu mobile (o que está oculto no header)

---

## Parte 7 — Fluxo de Extração por Logo (Logo → Design System)

### 7.1 Filosofia
Quando o cliente fornece uma logo ou identidade visual pré-existente, o Design System não substitui a marca — ele **herda e expande a marca** em tokens CSS padronizados.

### 7.2 Mapeamento Automático de Cores
O script Python (`extract_colors.py`) quantiza os pixels visíveis da logo (ignorando transparências) e gera:
1. **`--accent`**: Cor saturada de maior contraste/presença.
2. **`--accent-hover`**: Variação com -10% de luminosidade HSL para feedback visual em botões.
3. **`--accent-soft`**: RGBA da cor primária com `0.12` de opacidade para pílulas, badges e fundos sutis.
4. **`--accent-secondary`**: Segunda cor de maior destaque para tags ou elementos complementares.
5. **`--border`**: RGBA derivado com `0.15` de opacidade.

### 7.3 Mapeamento Tipográfico Equivalente (Google Fonts)
- **Logos Serifadas / Manuscritas**: Sugerir `Cormorant Garamond` ou `Playfair Display` para títulos.
- **Logos Sans / Geométricas**: Sugerir `Inter`, `DM Sans` ou `Outfit` para títulos e corpo.
- **Logos Robustas / Bold**: Sugerir `Cinzel` ou `Montserrat` (peso 700+).

---

*Versão 1.1 | Antigravity Dev Standards | 2026-08*

