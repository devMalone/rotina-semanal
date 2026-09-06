---
name: antigravity_dev_standards
description: >
  Ativado em qualquer tarefa de desenvolvimento web (criação, correção ou melhoria
  de landing pages, sites ou componentes HTML/CSS/JS) no workspace Antigravity/Empreender.
  Instrui o agente a ler e seguir os quatro documentos de padrões técnicos antes
  de escrever qualquer código.
---

# Antigravity Dev Standards — Instrução de Uso

Antes de planejar ou implementar qualquer projeto web neste workspace, execute as seguintes etapas **obrigatoriamente**:

## Passo 1 — Ler os Documentos

Leia os seis documentos na pasta `docs/`:

1. `docs/01-FTI-Ficha-Tecnica-Implementacao.md` — arquitetura, stack, responsividade, SEO, acessibilidade, checklist e **Capítulo 20 (Post-Mortems)**
2. `docs/02-Design-System.md` — tokens de cor, tipografia, espaçamento, sombras, grid
3. `docs/03-Biblioteca-Componentes.md` — HTML/CSS/JS prontos para Navbar, Hero, Botões, Galeria, Formulário WA, FAQ, Footer etc.
4. `docs/04-Guia-Experiencia-Premium.md` — direção de arte, motion design, microinterações, copywriting, critérios de qualidade
5. `docs/05-Sistema-Tiers.md` — especificação de tiers (Essential, Professional, Premium), matriz de pontuação, add-ons e faixas indicativas.
6. `docs/06-Guia-Comercial-Landing-Pages.md` — guia comercial e operacional consolidado de landing pages (plataformas, precificação 2026, retainers, stacks modernos, agentes IA, compliance legal LGPD, contrato, acessibilidade ABNT/WCAG, diagramas Mermaid e checklists QA).

## Passo 2 — Aplicar Rigorosamente

As especificações dos documentos têm **prioridade absoluta** sobre qualquer decisão automática.

Toda implementação deve respeitar:
- Arquitetura Single-File (HTML + `<style>` + `<script>` em `index.html`)
- Mobile-First real (estilos base para mobile, `min-width` para escalar para desktop)
- Zero overflow horizontal em qualquer breakpoint (360px a 1920px)
- Tipografia fluida com `clamp()` em todos os títulos
- Touch targets mínimos de 44x44px em todos os elementos interativos
- `height: 100dvh` no hero (nunca `100vh`)
- `font-size: 16px !important` em inputs/selects/textareas no mobile (evitar zoom iOS)
- Menu mobile com overlay backdrop (`backdrop-filter: blur`) + scroll lock (`body.menu-open`)
- `.btn-nav` e `.scroll-indicator` ocultos em mobile (`< 768px`)
- Ícones via Lucide Icons (`unpkg.com/lucide@latest`) com `lucide.createIcons()` no final do script
- Checklist do Capítulo 19 da FTI validado antes de considerar qualquer implementação concluída

## Passo 3 — Verificações Anti-Regressão (Lições Aprendidas)

Erros documentados no **Capítulo 20 da FTI**. Verificar obrigatoriamente antes de entregar:

### PM-01 — CSS de Componentes Globais Sempre Definido na Base
Todo componente presente no HTML (`.wa-float`, `.booking-form`, `.form-grid`, `.lightbox`) deve ter seu CSS declarado na seção `<style>` principal, **antes** de qualquer `@media query`. Sem isso, o elemento renderiza como bloco branco anônimo no layout (vide barra branca no rodapé do projeto Aura Studio).

### PM-02 — Grids Mobile: `display: flex; flex-direction: column` é mais Robusto que `grid-template-columns: 1fr`
Em breakpoints `<= 768px`, substituir grids multi-coluna por `display: flex; flex-direction: column; width: 100%` nos filhos. Apenas alterar `grid-template-columns: 1fr` não é suficiente — conflitos de herança de `1024px` podem manter as colunas estreitas. Quando necessário usar `grid`, adicionar `!important`.

### PM-03 — `<select>` Sempre com Seta Customizada e Placeholder
Todo `<select>` deve ter:
- `appearance: none; -webkit-appearance: none; -moz-appearance: none` + seta SVG editorial via `background-image`
- `padding-right: 2.75rem` para o texto nunca colidir com a seta
- Primeiro `<option value="" disabled selected>` como placeholder elegante

### PM-04 — Scroll Horizontal Visível ao Usuário Exige Affordance
Qualquer `overflow-x: auto` visível em mobile (filtros de galeria, carousels) deve ter:
1. Fade lateral (`.filter-fade-indicator` com `linear-gradient` para a cor de fundo)
2. Peek parcial do próximo elemento (último item visível cortado ~30%)
3. Opcionalmente: dica textual animada com `arrow-right` que desaparece após o primeiro scroll

### PM-05 — Alternância de Ícone no Toggle Mobile Sem Perda de Nó no DOM
Botões de menu mobile toggle **nunca** devem re-executar `lucide.createIcons()` alternando atributos `data-lucide` em manipuladores de clique, sob risco de substituir o nó `<i>` no DOM e desconectar referências de variáveis JS. Usar `innerText = isOpen ? '✕' : '☰'` ou alternar elementos estáticos via CSS (`display: none / block`).

### PM-06 — Evitar Colisão de Conteúdo do Hero sob Header Fixo
Contêineres `.hero` posicionados sob um `header` fixo de altura `N`px devem usar `padding-top: calc(Npx + 24px)` e `justify-content: flex-start`, além de `min-height: 100dvh; height: auto` em mobile. NUNCA usar `justify-content: flex-end` com imagens de altura fixa que empurrem os títulos do topo para trás do cabeçalho.

### PM-07 — Ocultamento Explícito de Links Desktop & Contraste do Botão Toggle em Mobile
Listas de navegadores desktop (`.nav-links`, `.nav-left`, `.nav-right`) devem ter `display: none !important` em `@media (max-width: 900px)`. O botão hambúrguer de navegação deve ter contraste elevado em relação ao fundo da navbar (`color: var(--amber)` / `color: var(--gold)` / `color: var(--text-light)`).

### PM-08 — Alinhamento de Controles do Carrossel em Contêineres Flex
Contêineres `.hero-section` com `display: flex` devem ter `flex-direction: column; justify-content: center;` em `@media (max-width: 900px)`. Isso garante que os botões de navegação do carrossel (`.carousel-controls`) fiquem empilhados abaixo do conteúdo, sem flutuar horizontalmente ao lado do texto.

### PM-09 — Dimensionamento Seguro de Logo & Botão Toggle no Header Mobile
Em `@media (max-width: 900px)`, ajustar padding do `.container` do header para `0 20px`, limitar o tamanho do logo a `clamp(1rem, 4vw, 1.25rem)` e aplicar `flex-shrink: 0`, `font-size: 1.8rem` e cor de alto contraste (`var(--amber)` / `var(--accent-gold)`) no botão `.mobile-toggle` para evitar que ele seja empurrado para fora da tela.

### PM-10 — Inclusão Obrigatória de Classes de Formulário no Colapso Mobile
Todas as classes de grid de formulários (`.form-grid`, `.form-grid-fineart`, `.form-grid-fo`, `.form-grid-dc`) DEVEM ser incluídas em `display: flex !important; flex-direction: column !important; width: 100% !important;` na media query mobile (`max-width: 900px`).

### PM-11 — Definição de Largura 100% e Reset em Elementos de Formulário e Accordion
Todos os campos de formulário (`input`, `select`, `textarea`) devem ter `width: 100%; box-sizing: border-box; display: block;` para preencher o contêiner no desktop e mobile. Todos os botões de sanfona (`.accordion-header`) devem ter `background-color: var(--bg-surface); color: var(--text-main); border: none; outline: none; appearance: none; -webkit-appearance: none;` para evitar renderização como caixas nativas.

### PM-12 — Reset Obrigatório de Listas (`<ul>`, `<ol>`) em Rodapés e Componentes
Toda lista (`ul`, `ol`) dentro de rodapés ou cards deve receber reset explícito no CSS (`list-style: none; padding: 0; margin: 0;`). Marcadores visuais devem usar pseudoelementos `::before` customizados com `display: flex; align-items: center; gap: 10px;`.

### PM-13 — Offset Obrigatório de Rolagem para Âncoras (`scroll-padding-top`)
Declarar `scroll-padding-top: var(--header-height, 80px)` em `html` e `scroll-margin-top: calc(var(--header-height, 80px) + 0.5rem)` em `section[id]` para evitar que o topo da seção fique coberto sob a navbar fixa.

### PM-14 — Prevenção de Quebra de Linha em Ícones e Caracteres de Ação em Botões
Botões e links com setas indicadoras (`.card-cta-btn`) nunca devem utilizar caracteres de texto soltos (`›`, `>`, `→`). Devem usar SVG nativo com `flex-shrink: 0`, e o contêiner configurado com `display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; white-space: nowrap;`.

### PM-15 — Arquitetura Single-File Autocontida para Tier 1 (Imagens Base64 Embutidas)
Em entregas Tier 1 (Essential) com requisito de portabilidade máxima, as imagens devem ser otimizadas (PIL ~80% qualidade) e embutidas diretamente como Data URIs Base64 (`data:image/jpeg;base64,...`) em `index.html`, mantendo o bundle abaixo de 600KB e 100% funcional fora de pastas locais.

### PM-16 — Badges, Pills e Tags sem Quebra Órfã (`white-space: nowrap`)
Toda tag ou pill de status (`.section-tag`, `.badge-pill`) DEVE possuir `white-space: nowrap; max-width: 100%; font-size: clamp(...)` para evitar quebras órfãs de palavras únicas em visores intermediários.

### PM-17 — Alinhamento Rente em Micro-Badges e Prova Social
Listas de badges verticais ou empilhadas no mobile com ícones e textos (`.hero-badges`, `.badge-item`) DEVEM manter alinhamento à esquerda rígido (`align-items: flex-start; text-align: left;`) com ícones de dimensões fixas (`flex-shrink: 0`) e contêiner centralizado (`margin: 0 auto; max-width: 280px;`), garantindo que todos os ícones fiquem rigorosamente na mesma linha guia vertical.

## Passo 4 — Na Ausência de Definição

Se alguma especificação não estiver coberta pelos documentos, aplicar as melhores práticas modernas de:
- UX/UI Design
- Web Performance (LCP, CLS, INP)
- HTML5 Semântico
- CSS3 / JavaScript ES2023+
- Acessibilidade WCAG 2.2 AA


