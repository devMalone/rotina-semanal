# Ficha Técnica de Implementação (FTI)
### Versão 1.0 — Antigravity Dev Standards

---

## Objetivo

Este documento define todas as especificações técnicas, arquiteturais, visuais e funcionais que **devem ser seguidas rigorosamente** durante o desenvolvimento de qualquer landing page ou website no ecossistema Antigravity.

**As especificações possuem prioridade sobre qualquer decisão automática da IA.**

### Design Decision Framework (Ordem de Precedência)
Quando a IA ou o desenvolvedor precisar tomar qualquer decisão visual, funcional ou de layout não especificada de forma explícita, DEVE respeitar rigorosamente a seguinte ordem de precedência:
1. Briefing e Requisitos do Cliente
2. Ficha Técnica de Implementação (`01-FTI`)
3. Design System (`02-Design-System`)
4. Biblioteca de Componentes (`03-Biblioteca-Componentes`)
5. Guia de Experiência Premium (`04-Guia-Experiencia-Premium`)
6. Matriz de Sistema de Tiers (`05-Sistema-Tiers`)
7. Guia Comercial e Operacional (`06-Guia-Comercial-Landing-Pages`)
8. Melhores Práticas Globais de Web Performance, UX/UI e Acessibilidade
9. Inferência estética / Criatividade automatizada

Nenhuma implementação poderá ignorar este documento ou inventar padrões que violem a ordem de precedência acima.

---

## Capítulo 1 — Arquitetura Geral

### 1.1 Estrutura de Projeto (Single-File)

Todo projeto do portfólio segue arquitetura **Single-File** obrigatória:

`
Portfolio/
└── [Categoria]/
    └── [NN-nomeprojeto]/
        └── index.html   ← HTML + style + script em um único arquivo
`

**Proibido**: arquivos .css, .js externos ao index.html. Zero dependências de bundlers.

### 1.2 Organização Interna do index.html

`
head:
  1. Meta charset e viewport SEMPRE na primeira linha
  2. SEO: title, description, canonical
  3. Open Graph e Twitter Cards
  4. Preconnect a fonts e CDNs
  5. Google Fonts import
  6. style com todo o CSS organizado por seções numeradas

body:
  HTML semântico por seções
  script ao final do body com todo o JS
`

### 1.3 Organização do CSS (dentro de style)

Obrigatoriamente estruturado em seções comentadas e numeradas:

`
/* 00. CSS RESET & BASE */
/* 01. VARIÁVEIS (CSS Custom Properties / :root) */
/* 02. TIPOGRAFIA */
/* 03. COMPONENTES GLOBAIS (botões, badges, etc.) */
/* 04. NAVBAR */
/* 05. HERO */
/* 06. [SEÇÕES DA PÁGINA em ordem de aparição] */
/* N-1. RESPONSIVIDADE (breakpoints, do maior ao menor) */
/* N.   PREFERÊNCIAS DO SISTEMA (prefers-reduced-motion) */
`

### 1.4 Organização do JavaScript (dentro de script)

`
/* 1. CURSOR CUSTOMIZADO */
/* 2. NAVBAR SCROLL + MOBILE MENU */
/* 3. PARALLAX */
/* 4. INTERSECTION OBSERVER (reveal animations) */
/* 5. [FUNCIONALIDADES ESPECÍFICAS DA PÁGINA] */
/* N. INIT — lucide.createIcons() e demais inits */
`

---

## Capítulo 2 — Stack Tecnológica

HTML5 Semântico — Estrutura (header, main, section, article, footer, nav, aside)
CSS3 Moderno — Estilos (Grid, Flexbox, clamp(), custom properties)
JavaScript ES2023+ — Lógica (módulos, async/await, optional chaining)
CSS Grid — Layouts bidimensionais complexos
Flexbox — Alinhamentos e layouts lineares
Intersection Observer API — Animações on-scroll e lazy loading
Scroll API — Parallax, scroll progress
Web Animations API — Animações imperativas de alta performance
Lucide Icons — Ícones via CDN unpkg.com/lucide@latest
Google Fonts — Tipografia via preconnect + import
WebP / AVIF — Imagens otimizadas (com fallback via picture element)
SVG inline — Ícones e ilustrações críticos acima do fold

**Proibido**: jQuery, Bootstrap, Tailwind, frameworks CSS utilitários, qualquer bundler/compilador.

---

## Capítulo 3 — Princípios de UX Obrigatórios

1. Visual Hierarchy — Elementos mais importantes têm maior peso visual.
2. White Space — Espaçamento generoso. Nunca comprimir seções.
3. Progressive Disclosure — Revelar informação progressivamente.
4. Consistency — Componentes idênticos se comportam de forma idêntica.
5. Recognition over Recall — Ícones com labels. Nunca ícones sem contexto.
6. Feedback — Todo estado interativo tem resposta visual.
7. Accessibility First — Navegação por teclado, contraste WCAG 2.2 AA, ARIA.
8. User Flow — Cada seção conduz naturalmente para a próxima com CTAs.
9. Affordance — Botões parecem clicáveis, inputs parecem editáveis.
10. Fitts's Law — Áreas de toque mínimo de 44x44px em mobile.
11. Hick's Law — Máximo de 5-7 opções de navegação no menu.
12. Jakob's Law — Padrões já conhecidos (navbar no topo, logo à esquerda).
13. Miller's Law — Chunking de informação em grupos de 3-7 itens.
14. Gestalt — Proximidade, similaridade e continuidade para agrupar elementos.

---

## Capítulo 4 — Direção de Arte

### 4.1 Estética Obrigatória

- Minimalismo Editorial: menos elementos, mais impacto.
- Luxo Discreto: qualidade que se sente, não que grita.
- Referências: Apple, Leica, Porsche, Aesop, The Row, Bottega Veneta.

### 4.2 Características Visuais

- Espaço negativo generoso e intencional
- Fotografia como protagonista
- Tipografia com caráter (serifada elegante + sans-serif clean)
- Paletas cromáticas neutras e quentes
- Transições suaves e deliberadas
- Grid rigoroso; nunca layout ao acaso

### 4.3 Proibido

- Cores saturadas e vibrantes sem propósito
- Sombras exageradas (box-shadow com opacidade maior que 0.25 e blur maior que 30px)
- Gradientes multicoloridos chamativos
- Bordas espessas decorativas
- Efeitos neon, brilhos, glassmorphism excessivo
- Animações lentas (mais de 800ms) ou que causem distração
- Stock photos genéricas ou ilustrações clip-art

---

## Capítulo 5 — Tipografia

### 5.1 Escala Tipográfica (Minor Third 1.250)

| Token        | Tamanho   | Uso                        |
|--------------|-----------|----------------------------|
| --text-xs    | 0.64rem   | Labels, badges, captions   |
| --text-sm    | 0.8rem    | Body small, meta           |
| --text-base  | 1rem      | Body padrão                |
| --text-md    | 1.25rem   | Lead text                  |
| --text-lg    | 1.563rem  | Section subtitles          |
| --text-xl    | 1.953rem  | Section titles small       |
| --text-2xl   | 2.441rem  | Section titles             |
| --text-3xl   | 3.052rem  | Hero subtitle              |
| --text-4xl   | 3.815rem  | Hero title                 |
| --text-hero  | clamp(2.5rem, 7vw, 5.5rem) | Hero fluido |

### 5.2 Regras Tipográficas

- Comprimento máximo de linha: 65-75 caracteres (max-width: 65ch)
- Altura de linha body: 1.6–1.75
- Altura de linha headings: 1.1–1.25
- Peso heading: 300 (Light) ou 400 (Regular) — nunca bold em displays serifados
- Letter-spacing headings: -0.01em a -0.03em (tracking apertado = luxo)
- Letter-spacing labels/badges: 0.1em a 0.3em (all-caps tracking = elegância)

### 5.3 Fontes Padrão

Serif (títulos/displays): Cormorant Garamond, Playfair Display
Sans-serif (corpo/UI): Inter, DM Sans

---

## Capítulo 6 — Sistema de Grid

Container: width 90%, max-width 1200px, margin auto

| Nome      | Largura       | Colunas | Gutter |
|-----------|---------------|---------|--------|
| ultrawide | maior 1600px  | 12      | 32px   |
| desktop   | 1200–1599px   | 12      | 24px   |
| notebook  | 1024–1199px   | 12      | 20px   |
| tablet-l  | 768–1023px    | 8       | 20px   |
| tablet-p  | 600–767px     | 4       | 16px   |
| mobile-l  | 480–599px     | 4       | 16px   |
| mobile    | 360–479px     | 2       | 12px   |
| mobile-s  | menor 360px   | 2       | 8px    |

---

## Capítulo 7 — Responsividade

### 7.1 Princípio

Código escrito Mobile-First: estilos base para mobile, media queries min-width para expansão.

### 7.2 Regras Universais

- Nunca usar overflow: hidden no body de forma permanente (apenas com .menu-open)
- Sempre usar box-sizing: border-box global
- Sempre usar unidades fluidas (clamp, vw, %, rem) — nunca px fixo para fontes
- Viewport Height: Hero deve usar `min-height: 100dvh` (nunca `height: 100dvh` fixo), respeitando conteúdo, safe areas e viewport móvel sem provocar corte ou overflow
- Imagens: max-width: 100%; height: auto; display: block
- Inputs/Selects/Textareas: font-size: 16px no mobile (evita zoom automático iOS)
- Touch targets: min-width: 44px; min-height: 44px em todos elementos interativos mobile

### 7.3 Especificações por Breakpoint

Mobile Small (menor que 360px):
  - Container: width 94%
  - Fonte hero: clamp(1.4rem, 6.5vw, 1.75rem)
  - Botões: width 100%, min-height 44px
  - Grid: 1 coluna em todas as seções

Mobile (360–479px):
  - Container: width 92%
  - Fonte hero: clamp(1.55rem, 6.8vw, 2.1rem)
  - Hero buttons: stacked, largura 100%
  - Navegação Header Mobile (Estratégia CRO):
    * Landing Pages de Conversão Rápida / WhatsApp (Tiers 1 e 2 enxutas): Header mobile exibe `Logo à esquerda + Botão CTA Principal à direita` (ex: "WhatsApp", "Quero Pão!", "Agendar"). Omite-se o hambúrguer para evitar esconder o botão de conversão e manter a tomada de decisão a 1 toque.
    * Landing Pages Extensas / Institucionais (Tier 3 ou 8+ seções): Header mobile utiliza botão hambúrguer com drawer lateral (82% largura, max-width 380px) acompanhado do botão CTA.
  - Scroll indicator: oculto
  - Btn-nav: visível ou otimizado para a ação de conversão principal

Mobile Large (480–599px):
  - Fonte hero: clamp(1.75rem, 7vw, 2.4rem)
  - Filtros de galeria: swipe horizontal

Tablet Portrait (600–767px):
  - Grid: 2 colunas

Tablet Landscape (768–1023px):
  - Grid: 2–3 colunas
  - Btn-nav: visível

Notebook (1024–1199px):
  - Grid: 3 colunas

Desktop (1200–1439px):
  - Grid: 3–4 colunas
  - Cursor customizado ativo

Desktop Large (1440–1919px):
  - Container: max-width 1200px centralizado com margens generosas
  - Grid: 4 colunas; espaçamento de seções aumentado (padding: clamp(80px, 7vw, 120px) 0)
  - Verificar se grids de cards não ficam com células excessivamente largas (max 400px/coluna)

Ultrawide (1920px+):
  - Container: max-width 1200px (nunca deixar conteúdo full-width em ultrawide)
  - Verificar ausência de "ilhas de conteúdo" com espaço vazio excessivo nas laterais
  - Backgrounds de seções podem se estender full-width, mas o conteúdo fica contido

### 7.4 Matriz de Resoluções-Alvo Oficiais (Obrigatórias no QA)

Esta é a lista canônica de resoluções que **todo projeto deve ser validado** antes da entrega.

| Nível | Breakpoint CSS | Resolução(ões)-Alvo | Dispositivo Referência |
|-------|----------------|---------------------|------------------------|
| `xs`  | `< 360px`      | 320×568             | iPhone SE 1ª geração, Android antigo |
| `sm`  | `≥ 360px`      | 360×800, 375×667    | Android popular, iPhone SE 2/3 |
| `md`  | `≥ 390px`      | 390×844, 414×896    | iPhone 14, iPhone XR/11 |
| `lg`  | `≥ 480px`      | 480×854             | Android médio landscape |
| `xl`  | `≥ 768px`      | 768×1024            | iPad portrait |
| `2xl` | `≥ 1024px`     | 1024×768            | iPad landscape, laptop entry |
| `3xl` | `≥ 1280px`     | 1280×800, 1366×768  | Laptops mais comuns |
| `4xl` | `≥ 1440px`     | 1440×900, 1536×864  | MacBook Air, laptops mid-range |
| `5xl` | `≥ 1920px`     | 1920×1080           | Monitor Full HD padrão |

### 7.5 Checklist de QA Responsivo (executar em cada resolução)

Antes de declarar qualquer página como entregue, validar **mentalmente** (e fisicamente sempre que possível) cada item abaixo para as 9 resoluções da tabela 7.4:

```
OVERFLOW & LAYOUT
□ Nenhum elemento ultrapassa a largura do viewport (sem scroll horizontal)
□ Container permanece com padding lateral ≥ 16px em qualquer resolução
□ Grids colapsam corretamente para colunas únicas abaixo de 768px

TIPOGRAFIA
□ Títulos h1 legíveis em 320px sem quebra de linha excessiva
□ Body text ≥ 14px em todos os viewports
□ Nenhum texto cortado por overflow hidden

BOTÕES & TOUCH
□ Todo elemento interativo: min-height 44px, min-width 44px
□ Botões com texto longo: white-space: normal ou quebra de linha controlada
□ Botões de CTA em mobile: width: 100% ou contidos no container

IMAGENS & MÍDIA
□ Imagens: max-width: 100%; height: auto (nunca overflow do container)
□ Hero: usa min-height: 100dvh (nunca height: 100dvh fixo)
□ Aspect-ratios preservados em resize

NAVEGAÇÃO
□ Header fixo compensa padding-top no hero
□ Menu mobile abre e fecha corretamente
□ Ícone hambúrguer não some após toggle (PM-05)

DESKTOP LARGO (1440px–1920px)
□ Conteúdo centralizado (container com max-width)
□ Cards não ficam excessivamente largos (max ~400px por coluna)
□ Nenhuma seção parece vazia ou "perdida" em ultrawide
```

---

## Capítulo 8 — Componentes

### 8.1 Botões

Estados obrigatórios: default, hover, focus (ring visível), active, disabled (opacity 0.4), loading (spinner).

Padrão:
  - padding: 0.85rem 2rem
  - border-radius: 40px
  - font-size: 0.8rem, letter-spacing: 0.1em, text-transform: uppercase
  - min-height: 44px
  - transition: all 0.35s ease
  - hover: translateY(-2px)

### 8.2 Navbar

- Fixo no topo (`position: fixed; top: 0; z-index: 1000`)
- Transparente inicialmente → classe `scrolled` após 50px de scroll
- Mobile: drawer lateral ou overlay completo com backdrop (`backdrop-filter: blur(5px)`)
- `aria-expanded` no toggle hambúrguer
- `body.menu-open` bloqueia scroll
- **Offset de Rolagem de Âncoras Obrigatório**: Todo projeto com navbar fixo DEVE implementar offset nativo via CSS vinculando a variável `--header-height`:
  ```css
  html {
    scroll-behavior: smooth;
    scroll-padding-top: var(--header-height, 80px);
  }
  section[id], [id] {
    scroll-margin-top: calc(var(--header-height, 80px) + 0.5rem);
  }
  ```
  Isso previne que o título da seção de destino fique escondido atrás do header fixo ao clicar em links `#id` ou acessar URLs diretas com fragmento `#secao`.

### 8.3 Formulários

- Label sempre visível (não apenas placeholder)
- Focus ring com box-shadow 0 0 0 3px rgba(accent, 0.2)
- Validação visual inline
- Submit via WhatsApp (wa.me) ou endpoint real
- **Todo `<select>` deve ter seta customizada** via SVG no `background-image` com `appearance: none` + `-webkit-appearance: none`. Nunca usar a seta padrão do navegador (colidem com texto em containers estreitos)
- **Todo `<select>` deve ter `<option value="" disabled selected>`** como primeiro item para funcionar como placeholder elegante
- **O CSS de `.booking-form`, `.form-grid` e `.form-group` deve sempre estar declarado na seção de estilos base** (antes das media queries), nunca apenas dentro de media queries

### 8.4 Galeria

- Grid CSS com grid-template-areas para layouts assimétricos
- Hover: transform scale(1.03) + overlay semitransparente
- Filtros com classe active e transition suave

---

## Capítulo 9 — Sistema de Espaçamento

Escala de 4pt (múltiplos de 4px):

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

**Regra**: Nunca usar valores arbitrários como 13px, 17px, 22px.
Padding de seções: clamp(48px, 6.5vw, 110px) 0

---

## Capítulo 10 — Paleta de Cores

Tokens semânticos obrigatórios:
  --bg-primary, --bg-secondary, --bg-tertiary
  --text-dark, --text-muted, --text-light
  --accent, --accent-hover, --accent-soft
  --border, --border-strong
  --success: #22c55e
  --warning: #f59e0b
  --error:   #ef4444
  --info:    #3b82f6

Contraste mínimo (WCAG 2.2 AA):
  - Texto normal: 4.5:1
  - Texto grande (maior que 18px bold ou maior que 24px): 3:1
  - Componentes UI e estados foco: 3:1

### Regra de Distribuição de Cores
- A cor de acento/CTA (`--accent` / Terracota / Destaque) deve ser utilizada predominantemente para ações e elementos de destaque pontuais — nunca como cor dominante em grandes superfícies ou backgrounds de seções inteiras.
- A maior parte da interface deve permanecer em tons neutros e limpos (`--bg-primary`, `--bg-secondary`), permitindo que a fotografia do produto seja o principal protagonista visual.

---

## Capítulo 11 — Ícones

- Biblioteca: Lucide Icons exclusivamente (unpkg.com/lucide@latest)
- Espessura: stroke-width 1.5 para decorativos, 2 para ações
- Tamanho: 20–24px para UI, 32–48px para features
- Alinhamento: sempre via flexbox (display flex, align-items center)
- Inicialização: lucide.createIcons() obrigatório ao final do script

---

## Capítulo 12 — Animações e Motion Design

Durações padrão:
  --duration-fast:   200ms (hover, focus states)
  --duration-base:   400ms (reveals, transitions)
  --duration-slow:   700ms (hero, page elements)
  --duration-slower: 1200ms (parallax, grandes movimentos)

Easing padrão:
  --ease-out:   cubic-bezier(0.0, 0.0, 0.2, 1)
  --ease-in:    cubic-bezier(0.4, 0.0, 1, 1)
  --ease-inout: cubic-bezier(0.4, 0.0, 0.2, 1)
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1)

Reveal padrão (Intersection Observer):
  Inicial: opacity 0, translateY 32px
  Visível: opacity 1, translateY 0
  Threshold: 0.15 | rootMargin: 0px 0px -50px 0px

Parallax:
  - Apenas em imagens hero e backgrounds
  - Speed: 0.08 (sutil)
  - Somente em desktop (desabilitado em pointer coarse)

Obrigatório: respeitar prefers-reduced-motion: reduce em todas as animações.

---

## Capítulo 13 — Performance

### Imagens
- Formato preferencial: WebP com fallback JPEG via picture element
- `srcset` + `sizes` declarados para imagens críticas e responsivas (`srcset="foto-400.webp 400w, foto-800.webp 800w"` + `sizes="(max-width: 480px) 100vw, 50vw"`)
- `loading="lazy"` em todas as imagens below the fold
- `loading="eager"` + `fetchpriority="high"` na imagem principal do hero
- `width` e `height` sempre declarados explicitamente (previne CLS)
- `alt` descritivo preenchido obrigatoriamente (acessibilidade e SEO)

### Fontes
- preconnect em fonts.googleapis.com e fonts.gstatic.com
- font-display: swap sempre

### CSS
- Sem CSS não utilizado ou duplicado
- Propriedades animadas via GPU: transform, opacity
- Nunca animar top, left, width, height

### JavaScript
- defer em scripts externos
- requestAnimationFrame para animações imperativas
- Debounce em scroll/resize handlers (16ms = 60fps)
- Event delegation quando possível

### Métricas Alvo (Lighthouse)
| Métrica        | Meta     |
|----------------|----------|
| Performance    | >= 90    |
| Accessibility  | >= 95    |
| Best Practices | >= 95    |
| SEO            | 100      |
| LCP            | < 2.5s   |
| CLS            | < 0.1    |
| INP            | < 200ms  |

---

## Capítulo 14 — SEO

Obrigatório em toda página:

`
meta charset UTF-8
meta viewport content=width=device-width, initial-scale=1.0
title com palavra-chave principal + nome do negócio + cidade/nicho
meta name description (150-160 chars com palavra-chave + CTA)
link rel canonical
og:type, og:title, og:description, og:image (1200x630), og:url, og:locale pt_BR
twitter:card summary_large_image, twitter:title, twitter:description, twitter:image
`

HTML Semântico:
- Um único h1 por página (palavra-chave principal)
- Hierarquia: h1 > h2 > h3 sem pulos
- nav com aria-label
- main envolvendo o conteúdo principal
- section com id para âncoras

Structured Data (Schema.org / JSON-LD):
- Toda landing page de negócio local deve incluir o script `<script type="application/ld+json">` contendo o Schema `LocalBusiness` (ou extensão específica como `BarberShop`, `Bakery`, `NailSalon`, `AutoRepair`) com `name`, `image`, `telephone`, `address`, `openingHoursSpecification` e `geo`.

---

## Capítulo 15 — Acessibilidade (WCAG 2.2 AA)

- Contraste: mínimo 4.5:1 texto normal, 3:1 texto grande
- Focus ring: sempre visível com contraste >= 3:1
- aria-label em links/botões sem texto descritivo
- aria-expanded em menus
- aria-current="page" em nav ativa
- alt text em toda imagem; decorativas com alt vazio
- Sem tabindex positivo
- Skip link no topo: a href="#main" Pular para o conteúdo
- lang="pt-BR" no html

---

## Capítulo 16 — JavaScript

Padrões:
- Usar const e let (nunca var)
- Sem variáveis globais expostas no window
- Sem innerHTML com dados do usuário
- requestAnimationFrame para animações
- IntersectionObserver para reveals (não scroll loop)
- Debounce/throttle em handlers pesados
- Promises e async/await para operações assíncronas

---

## Capítulo 17 — Convenções de Código

CSS: BEM — .block, .block__element, .block--modifier
JavaScript: camelCase para variáveis e funções, UPPER_SNAKE_CASE para constantes
HTML: kebab-case para classes e IDs
Comentários em CSS: por seção e para regras não óbvias
Comentários em JS: JSDoc para funções públicas

---

## Capítulo 18 — Compatibilidade

| Browser        | Versão mínima |
|----------------|---------------|
| Chrome         | 90+           |
| Firefox        | 88+           |
| Safari         | 14+           |
| Edge           | 90+           |
| Chrome Android | 90+           |
| Safari iOS     | 14.5+         |

Testar obrigatoriamente em:
- iPhone SE (375px), iPhone 14 (390px), Pixel 7 (412px), iPad (768px)
- Firefox Responsive Design Mode
- Safari (se disponível)

---

## Capítulo 19 — Checklist de Qualidade (Obrigatório)

### Layout e Visual
- [ ] Nenhum overflow horizontal em nenhum breakpoint (360px a 1920px)
- [ ] Nenhum elemento sobreposto de forma indevida
- [ ] Nenhum texto cortado ou truncado sem intenção
- [ ] Espaçamento consistente com a escala de 4pt
- [ ] Hierarquia visual clara em todos os tamanhos de tela

### Funcionalidade
- [ ] Todos os links funcionam (sem âncoras mortas)
- [ ] Formulários validam e enviam corretamente
- [ ] Menu mobile abre, fecha pelo overlay, fecha por link, fecha por ESC
- [ ] Scroll progress bar funcional
- [ ] WhatsApp float button abre no número correto

### Acessibilidade
- [ ] Contraste >= 4.5:1 em todo texto normal
- [ ] Focus ring visível em todos os elementos interativos
- [ ] alt em todas as imagens
- [ ] aria-expanded no menu toggle
- [ ] Navegação por Tab funcional e em ordem lógica

### Performance
- [ ] Imagens com loading="lazy" (exceto hero)
- [ ] Fontes com preconnect e font-display: swap
- [ ] Zero console.error no DevTools
- [ ] Sem reflows causados por JS

### SEO
- [ ] title único e com palavra-chave
- [ ] meta description preenchido (150-160 chars)
- [ ] Open Graph completo
- [ ] Um único h1 por página
- [ ] lang="pt-BR" no html

### Mobile Específico
- [ ] Touch targets >= 44x44px
- [ ] Inputs com font-size 16px (sem zoom iOS)
- [ ] Hero com min-height 100dvh (respeitando conteúdo sem corte ou overflow)
- [ ] Scroll indicator oculto em mobile (menor que 768px)
- [ ] Nav CTA button oculto em mobile (menor que 768px)
- [ ] Nenhum elemento ultrapassa a largura da viewport
- [ ] Todos os grids multi-coluna colapsam para `display: flex; flex-direction: column` em mobile (360–768px) — nunca confiar apenas em `grid-template-columns: 1fr` sem verificar conflitos de herança
- [ ] Componentes globais (`.wa-float`, `.booking-form`, `.form-grid`) têm CSS base declarado **fora** de media queries
- [ ] Elementos com scroll horizontal (filtros, carousels) têm affordance visual: fade lateral + dica textual animada `Deslize →`
- [ ] Todo `<select>` tem seta customizada via SVG e `appearance: none`
- [ ] Todo `<select>` tem `<option value="" disabled selected>` como placeholder
- [ ] **Conteúdo Fictício**: Nenhum depoimento, avaliação, número de clientes, prêmio ou certificação foi gerado artificialmente pela IA sem constar no briefing do cliente. Onde o dado não for fornecido, a seção foi omitida ou marcada com `[INSERIR DADO REAL]`.

---

## Capítulo 20 — Lições Aprendidas (Post-Mortems)

> Este capítulo documenta erros reais encontrados em projetos do ecossistema Antigravity.
> Cada lição é uma regra obrigatória a partir da próxima implementação.

---

### PM-01 — CSS de Componentes Globais Fora do Fluxo

**Projeto**: Aura Studio (`Portfolio/Fotografia/02-aurastudio`)

**Problema**: O botão flutuante do WhatsApp (`.wa-float`) e o formulário de agendamento (`.booking-form`) não tinham CSS base declarado na seção de estilos. Resultado: o link `<a class="wa-float">` renderizou como um bloco inline anônimo branco no rodapé da página, criando uma barra horizontal estranha.

**Causa Raiz**: O CSS foi adicionado de forma incremental por sessões diferentes, sem uma seção base coerente para os componentes globais.

**Regra**: Todo componente global que aparece no HTML base da página (floating button, form, lightbox) deve ter seu CSS declarado na seção de estilos principal do `<style>`, **antes** de qualquer `@media`. A ausência de CSS nunca é silenciosa — produz comportamento de layout inesperado.

---

### PM-02 — Grids Multi-Coluna Não Colapsando em Mobile

**Projeto**: Aura Studio

**Problema**: Seções com `display: grid; grid-template-columns: repeat(3, 1fr)` (Tipos de Ensaio, Timeline, Diferenciais) mantinham 3 colunas em telas de 375px, espremendo cards a ~100px de largura com texto e imagens ilegíveis.

**Causa Raiz**: As media queries `max-width: 768px` definiam `grid-template-columns: 1fr` mas em alguns casos o grid herdava configurações de 1024px. A abordagem desktop-first com `max-width` é frágil para cascata.

**Regra**: Em breakpoints mobile, prefira **substituir `display: grid` por `display: flex; flex-direction: column`** com `width: 100%` explícito nos filhos. Isso é mais robusto na cascata do que `grid-template-columns: 1fr`. Quando usar `grid`, sempre adicionar `!important` ao colapso mobile para evitar herança indesejada.

---

### PM-03 — Select Nativo Sem Personalização

**Projeto**: Aura Studio

**Problema**: O campo `<select>` do formulário exibia a seta padrão cinza do navegador colidindo com o texto da opção `"Gestante & Maternidade"`, que ficava cortado. Em dispositivos iOS o select tinha fundo e estilo totalmente divergente do resto do formulário.

**Causa Raiz**: Nenhuma regra `appearance: none` aplicada; seta de sistema competia com o padding interno do campo.

**Regra**: Todo `<select>` deve receber:
```css
appearance: none;
-webkit-appearance: none;
-moz-appearance: none;
background-image: url("data:image/svg+xml,..."); /* seta SVG editorial */
background-repeat: no-repeat;
background-position: right 1.1rem center;
padding-right: 2.75rem;
```
E sempre ter um placeholder com `value="" disabled selected` para não iniciar com uma opção funcional.

---

### PM-04 — Ausência de Affordance em Scroll Horizontal (Filtros)

**Projeto**: Aura Studio

**Problema**: Em mobile (375px), os botões de filtro da galeria (`Todos`, `Gestante`, `Newborn`...) estavam configurados como `overflow-x: auto` mas o último botão visível terminava exatamente na borda da tela, sem nenhuma indicação de que havia mais itens além.

**Causa Raiz**: Não havia nenhum elemento visual (gradiente de borda, peek parcial do próximo botão, dica textual) sinalizando scroll horizontal.

**Regra**: Qualquer contêiner com `overflow-x: auto` visível ao usuário em mobile **deve** ter:
1. Um elemento de **fade lateral** (`linear-gradient` transparente → cor de fundo) na borda direita para indicar continuidade
2. Um **peek parcial** do próximo elemento (ajuste de `padding-right` + `width` do contêiner para cortar ~30% do último item visível)
3. Opcionalmente: dica textual animada `"Deslize para ver mais →"` que desaparece após o primeiro scroll (`{ passive: true }` listener)

---

### PM-05 — Troca Dinâmica do Ícone do Menu Mobile (Lucide Icons vs DOM)

**Projeto**: Padaria Panetteria / Forno & Origem

**Problema**: Ao clicar no botão hambúrguer mobile, o ícone "X" de fechar aparecia na primeira vez mas desaparecia ou travava nas interações subsequentes.

**Causa Raiz**: O JS modificava o atributo `data-lucide="x"` em um elemento `<i id="menuIcon">` e em seguida invocava `lucide.createIcons()`. A biblioteca Lucide substitui o nó `<i>` no DOM por um novo nó `<svg>` desanexando o `<i>` original do DOM sem preservar o `id`. Nas chamadas seguintes, a variável JS `menuIcon` apontava para um elemento desanexado do documento.

**Regra**:
1. Para botões toggle mobile, priorizar alternância de texto simples (`innerText = isOpen ? '✕' : '☰'`).
2. Se utilizar Lucide no toggle, manter dois elementos estáticos no HTML (`<i data-lucide="menu" class="icon-open"></i>` e `<i data-lucide="x" class="icon-close"></i>`) alternando visibilidade via CSS (`display: none / block`). NUNCA re-invocar `lucide.createIcons()` trocando atributos `data-lucide` dinamicamente no evento de clique.

---

### PM-06 — Colisão do Conteúdo do Hero sob Header Fixo

**Projeto**: Padaria Dona Clara

**Problema**: Em resoluções com menor altura de tela, o título da Hero (`A MAIS QUERIDA DA CIDADE`) ficava escondido parcialmente atrás do cabeçalho fixo (`header { position: fixed; top: 0; }`).

**Causa Raiz**: `.hero` configurado com `justify-content: flex-end; height: 100vh; overflow: hidden;` combinado com imagens fixas de 420px. Quando a altura da tela é menor que a soma do texto + imagem, o contêiner alinha o conteúdo à base e empurra o topo do título para cima contra o header.

**Regra**:
1. Todo `.hero` sob `header` fixo de altura `N`px DEVE ter `padding-top: calc(Npx + 24px)` e utilizar `justify-content: flex-start` ou `space-between` (nunca `flex-end`).
2. Em telas menores, usar `min-height: 100dvh; height: auto; padding-bottom: 40px;` para permitir rolagem sem cortar conteúdos.
3. Imagens da Hero em dispositivos mobile devem possuir limite responsivo de altura (`max-height: 260px; height: auto`).

---

### PM-07 — Ocultamento Obrigatório de Nav Links Desktop em Mobile & Contraste

**Projeto**: Padaria Forno & Origem

**Problema**: Em telas mobile (`<= 900px`), a lista de links horizontais da navegação desktop (`.nav-links`) continuava visível horizontalmente no topo da tela, e o botão hambúrguer ficava com cor escura invisível sobre o fundo escuro da navbar.

**Causa Raiz**: Ausência de `.nav-links, .nav-left, .nav-right { display: none; }` na media query mobile e uso de `color: var(--text-dark)` em header escuro.

**Regra**:
1. Sempre garantir que `.nav-links`, `.nav-left` e `.nav-right` fiquem explicitamente ocultos (`display: none`) em `@media (max-width: 900px)`.
2. O botão hambúrguer (`.menu-toggle`) DEVE possuir cor de alto contraste (`color: var(--amber)` / `color: var(--gold)` / `color: var(--text-light)`) adequada à cor de fundo da navbar.

---

### PM-08 — Alinhamento Vertical dos Controles do Carrossel em Contêineres Flex

**Projeto**: Padaria Forno & Origem

**Problema**: Em visores mobile, as setas e pontos do carrossel (`.carousel-controls`) renderizavam na lateral direita do texto da Hero, flutuando sobre a descrição e cortando os botões.

**Causa Raiz**: O contêiner pai `.hero-section` possuía `display: flex; align-items: center;` sem especificar `flex-direction: column`. Em telas móveis com `position: static` nos controles, o navegador alinhava a pista do carrossel e os botões em linha horizontal (`flex-direction: row`).

**Regra**:
1. Contêineres flexíveis com carrossel DEVEM receber `flex-direction: column; justify-content: center;` na media query mobile (`<= 900px`).
2. Garantir que os botões de controle (`.carousel-controls`) fiquem sempre empilhados verticalmente abaixo da área de conteúdo principal.

---

### PM-09 — Prevenção de Estouro do Logotipo & Botão Hambúrguer Off-Screen em Mobile

**Projeto**: Malone Souza Fine Art

**Problema**: Em dispositivos móveis de 360px–375px, o botão hambúrguer no topo direito da navbar ficava empurrado para fora da tela ou sumia visualmente.

**Causa Raiz**: O logotipo da marca (`MALONE SOUZA FINE ART PHOTOGRAPHY`) possuía largura de ~280px e o contêiner utilizava `padding: 0 32px`. A soma do padding + logo ultrapassava a largura de 375px da viewport, empurrando o botão hambúrguer para fora do contêiner.

**Regra**:
1. Em `@media (max-width: 900px)`, ajustar o padding do `.container` do header para `padding: 0 20px` e aplicar `font-size: clamp(1rem, 4vw, 1.25rem)` na marca/logo.
2. O botão hambúrguer (`.mobile-toggle`) DEVE sempre ter `flex-shrink: 0`, `font-size: 1.8rem` e `color: var(--amber)` / `var(--accent-gold)`.

---

### PM-10 — Inclusão Obrigatória de Formulários Específicos nos Breakpoints Mobile

**Projeto**: Malone Souza Fine Art

**Problema**: Em telas mobile, o formulário de reserva/contato permanecia em 2 colunas, fazendo os campos da direita (Telefone, Data) vazarem para fora da borda da tela.

**Causa Raiz**: Criação de classe específica de grid de formulário (`.form-grid-fineart`) sem incluí-la no bloco de colapso `@media (max-width: 900px)`.

**Regra**: Sempre incluir **TODAS** as variações de classe de formulário (`.form-grid`, `.form-grid-fineart`, `.form-grid-fo`, `.form-grid-dc`) dentro de `display: flex !important; flex-direction: column !important; width: 100% !important;` na media query mobile.

---

### PM-11 — Definição de Largura 100% e Reset em Elementos de Formulário e Accordion

**Projeto**: Malone Souza Fine Art

**Problema**: Em visores desktop e mobile, os campos de formulário (`input`, `select`, `textarea`) renderizavam estreitos com largura nativa do navegador (150px) desalinhados à esquerda, e os botões da sanfona FAQ exibia aparências padrão de caixas desformatadas.

**Causa Raiz**: Ausência de `width: 100%; box-sizing: border-box; display: block;` nos seletores de formulário, e ausência de `background-color: var(--bg-surface) !important; color: var(--text-main) !important; border: none;` no botão da sanfona `.accordion-header`.

**Regra**:
1. Todos os seletores de formulário (`input`, `select`, `textarea`) DEVEM possuir `width: 100%; box-sizing: border-box; display: block;`.
2. Todos os botões de sanfona (`.accordion-header`) DEVEM possuir `width: 100%; display: flex; justify-content: space-between; background-color: var(--bg-surface); color: var(--text-main); border: none; outline: none;`.

---

### PM-12 — Reset Obrigatório de Listas (`<ul>`, `<ol>`) em Rodapés e Componentes

**Projeto**: Fermento & Arte Padaria Artesanal

**Problema**: Em visores desktop e mobile, os itens da lista do rodapé (`Horários de Fornada`) exibiam marcadores padrão do navegador (`disc`) colados ou parcialmente cortados no limite esquerdo da coluna.

**Causa Raiz**: O navegador aplica por padrão `padding-left: 40px` e `list-style-type: disc`. Sem reset no CSS base, os marcadores ficam desalinhados em contêineres com padding flexível.

**Regra**:
1. Toda lista (`ul`, `ol`) dentro de rodapés, cards ou componentes DEVE receber reset explícito no CSS base:
```css
.footer-col ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
```
2. Quando forem necessários marcadores visuais, utilizar pseudoelementos `::before` customizados e alinhados via `display: flex; align-items: center; gap: 10px;` na cor de acento do projeto, garantindo 100% de alinhamento com a margem do título da coluna.

---

### PM-13 — Offset Obrigatório de Rolagem para Âncoras (`scroll-padding-top` e `scroll-margin-top`)

**Projeto**: Dra. Nathalia Leite & Projetos de Navegação One-Page

**Problema**: Ao clicar em links de navegação interna (`href="#sobre"`, `href="#servicos"`), o topo da seção de destino ficava sobreposto e cortado pelo menu fixo no topo (`position: fixed`), omitindo o título `h2` da seção sob a navbar.

**Causa Raiz**: Ausência das propriedades CSS de ajuste de scroll (`scroll-padding-top` no elemento `html` e `scroll-margin-top` nos elementos com `id`), fazendo com que o navegador alinhasse a borda superior exata da seção no topo do viewport, exatamente onde o header transparente/opaco se encontra.

### PM-14 — Prevenção de Quebra de Linha em Ícones e Caracteres de Ação em Botões

**Projeto**: Padaria e Confeitaria Bom Jesus & Componentes de Cardápio

**Problema**: Caracteres de seta/chevron de texto (ex: `›`, `>`, `→`) no final de botões e links de ação (`.card-cta-btn`) quebravam sozinhos para a linha seguinte em visores mobile ou cards de grid estreito (~260px a 320px), gerando um visual desalinhado e antiestético.

**Causa Raiz**: Inclusão do caractere tipográfico solto na mesma string de texto sem `white-space: nowrap` ou sem isolamento em elemento SVG dedicado com `flex-shrink: 0`.

**Regra**:
1. Todo botão ou link com seta indicadora de ação DEVE usar ícone SVG nativo com `flex-shrink: 0` e a classe do botão configurada com:
```css
.card-cta-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  min-height: 44px;
  padding: 0.75rem 1rem;
  white-space: nowrap;
  line-height: 1.25;
}
.card-cta-btn svg {
  width: 14px;
  height: 14px;
  stroke-width: 2.5;
  flex-shrink: 0;
  transition: transform 0.2s ease;
}
.card-cta-btn:hover svg {
  transform: translateX(3px);
}
```
2. Proibido o uso de `›` ou `>` como texto plano em botões de ação quando o contêiner tiver largura fluida.

---

### PM-15 — Arquitetura Single-File Autocontida para Tier 1 (Imagens Base64 Embutidas)

### PM-16 — Badges, Pills e Tags sem Quebra Órfã (`white-space: nowrap`)

**Projeto**: Padaria e Confeitaria Bom Jesus & Tags de Seção

**Problema**: Badges do tipo pílula (`.section-tag`, `.badge-pill`) com textos médios quebravam a última palavra isolada para a segunda linha em visores intermediários (ex: "✦ FORNADAS QUENTES TODOS OS" na linha 1 e "DIAS" na linha 2), arruinando o equilíbrio visual da pílula.

**Causa Raiz**: Ausência de `white-space: nowrap;` e falta de dimensionamento fluido com `clamp()` no seletor base da tag.

**Regra**:
1. Toda tag de seção, pill ou badge de status DEVE possuir:
```css
.section-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.35rem 0.95rem;
  font-size: clamp(0.72rem, 2vw, 0.82rem);
  white-space: nowrap;
  max-width: 100%;
}
```
2. Manter a microcopy da tag concisa (preferencialmente de 2 a 4 palavras) para evitar que a pílula ultrapasse a largura útil em telas de 320px.

---

### PM-17 — Alinhamento Rente em Micro-Badges e Prova Social

**Projeto**: Padaria e Confeitaria Bom Jesus & Seção Hero

**Problema**: Micro-badges de apoio (`.hero-badges`, `.badge-item`) com ícones circulares e textos de apoio empilhados pareciam desalinhados e soltos quando o bloco pai recebia `text-align: center` no mobile, quebrando a linha guia vertical dos ícones.

**Causa Raiz**: Itens flexíveis alinhados ao centro da página sem um contêiner delimitador de largura máxima definida, fazendo com que textos com diferentes extensões deslocassem visualmente os círculos dos ícones.

**Regra**:
1. Em listas de badges com ícone + título + subtítulo empilhados no mobile, o contêiner DEVE manter alinhamento à esquerda rígido (`align-items: flex-start; text-align: left;`) com largura máxima definida e centralizada no bloco (`margin: 0 auto; max-width: 280px;`).
2. Todos os ícones circulares DEVEM possuir dimensões fixas com `flex-shrink: 0` (ex: `width: 40px; height: 40px;`) para garantir que compartilhem rigorosamente a mesma linha vertical (x=0).

---

*Versão 1.9 | Antigravity Dev Standards | 2026-08*


