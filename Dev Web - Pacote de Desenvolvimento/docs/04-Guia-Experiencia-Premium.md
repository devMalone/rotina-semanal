# Guia de Experiencia Premium
### Versao 1.0 -- Antigravity Dev Standards

---

## Objetivo

Este documento define os principios de experiencia premium, direcao de arte, motion design,
microinteracoes e criterios de qualidade que elevam um site de "funcional" para "extraordinario".

Um site Antigravity nao apenas funciona -- ele impressiona.

---

## Parte 1 -- O que define "Premium"

Premium nao e caro. Premium e intencional.

Um produto premium e aquele onde cada decisao foi tomada conscientemente, onde nada e aleatório,
onde a ausencia de elementos e tao poderosa quanto a presenca deles.

### 1.1 Os Quatro Pilares do Premium

CONTROLE: Nenhum elemento sem proposito. Cada pixel justificado.
QUIETUDE: Menos barulho visual. Espacos generosos. Respiracao.
QUALIDADE: Tipografia, imagens e proporcoes impecaveis.
COERENCIA: Do primeiro ao ultimo elemento, tudo comunica a mesma identidade.

### 1.2 O que destrui o Premium

- Informacao demais na mesma tela
- Cores que competem entre si
- Tipografia sem hierarquia clara
- Animacoes rapidas, bruscas ou sem proposito
- Sombras exageradas ou gradientes chamativos
- Espaco inadequado entre elementos
- CTAs urgentes e agressivos ("COMPRE AGORA!!!")
- Layout que parece template generico

---

## Parte 2 -- Direcao de Arte

### 2.1 Filosofia Visual

Toda pagina deve contar uma historia visual.
O usuario deve sentir a identidade da marca antes de ler uma unica palavra.

Perguntas obrigatorias antes de qualquer projeto:
  - Qual a emocao central que esta pagina deve despertar?
  - Qual e o perfil da pessoa que vai acessar esta pagina?
  - O que a concorrencia nao oferece que nos oferecemos?
  - Se este negocio fosse uma revista, qual seria ela?

### 2.2 Referencias por Segmento

Fotografia Maternidade / Newborn:
  - Editorial: Vogue Italia, Harper's Bazaar
  - Estudio: Leibovitz, Sebastiao Salgado (composicao)
  - Marcas: Maison de Sabre, Quiet Luxury brands
  - Paleta: cremes, bege, branco, dourado discreto

Barbearia Premium:
  - Editorial: GQ, Monocle
  - Marcas: Aesop, Le Labo
  - Paleta: preto, carvao, ouro, couro

Gastronomia / Padaria Artesanal:
  - Editorial: Kinfolk, Bon Appetit
  - Marcas: Tartine Bakery, Poilane
  - Paleta: terracota, creme, marrom quente, laranja queimado

Salao de Beleza:
  - Editorial: Vogue, InStyle
  - Marcas: Glossier, Charlotte Tilbury
  - Paleta: rosa empoeirado, nude, dourado, off-white

### 2.3 Composicao Visual

Regra dos Tercos: elementos principais nos pontos de interseccao
Peso Visual: equilibrio entre elementos pesados (fotos) e leves (texto/espaco)
Linhas de Tensao: criar tensao visual intencional que guia o olhar
Ponto de Entrada: sempre ha um elemento que recebe o olhar primeiro -- tornar esse elemento intencional
Fluxo: o olhar percorre a pagina num caminho predefinido (Z-pattern, F-pattern ou diagonal)

---

## Parte 3 -- Motion Design e Microinteracoes

### 3.1 Principios de Animacao (Disney + Web)

1. Slow In, Slow Out: objetos nao se movem em velocidade constante
   Usar ease-in-out, nunca linear
2. Antecipacao: preparar o usuario para o que vai acontecer
   Exemplo: botao "respira" levemente antes de uma acao importante
3. Follow Through: apos a acao principal, elementos menores continuam se movendo
   Exemplo: card sobe um pouco alem do alvo e suaviza de volta (spring easing)
4. Squash and Stretch (adaptado para web): elementos se "espicham" levemente ao se mover
   Implementado com scale() combinado com translate()
5. Timing: o ritmo da animacao define a personalidade
   Rapido: energico, urgente
   Lento: premium, reflexivo, confavel

### 3.2 Microinteracoes Obrigatorias

Hover em Links de Navegacao:
  - Underline crescendo da esquerda para direita
  - Duracao: 200ms ease-out
  - Implementacao: pseudo-elemento ::after com width 0 -> 100%

Hover em Botoes:
  - translateY(-2px) + sombra suave
  - Duracao: 300ms ease
  - Nunca mudanca de cor brusca

Hover em Cards:
  - translateY(-6px a -10px) + sombra aprofundada
  - Duracao: 350ms ease
  - Imagem interna: scale(1.04) com overflow hidden no container

Hover em Imagens de Galeria:
  - scale(1.04) + overlay semitransparente com label
  - Duracao: 400ms ease
  - Label slide-in de baixo para cima

Click em Botao de Formulario:
  - Scale 0.97 no momento do click (feeling de pressionar)
  - Spinner de loading enquanto processa
  - Feedback de sucesso/erro visual

Abertura do Menu Mobile:
  - Drawer slide da direita: 400ms cubic-bezier(0.4, 0, 0.2, 1)
  - Overlay fade-in: 400ms ease
  - Icone hamburguer -> X com rotacao: 300ms ease

Scroll Progress Bar:
  - Transicao suave: 100ms ease-out
  - Gradiente da cor de acento

### 3.3 Animacoes de Entrada de Secao

Padrao basico (todas as secoes):
  opacity: 0 + translateY(32px) -> opacity: 1 + translateY(0)
  Duracao: 700ms ease
  Threshold: 15% visivel na tela

Variantes por tipo de conteudo:

Cards em grid: entrada em cascata (staggered)
  - Cada card com delay crescente de 80-100ms
  - Total maximo de delay: 400ms

Titulos de secao: 
  - Apenas opacity (sem translate) para nao perturbar o layout
  - Duracao: 800ms ease

Imagens grandes:
  - translateY(24px) + scale(1.02) -> translateY(0) + scale(1)
  - Duracao: 900ms ease

### 3.4 Parallax

Uso permitido apenas em:
  - Imagem de background do hero
  - Imagens de secao de depoimentos ou about (se forem backgrounds)
  - Elementos decorativos (nao texto)

Regras:
  - Speed maxima: 0.1 (muito sutil)
  - Nunca em mobile (desativar com pointer: coarse)
  - Sempre via requestAnimationFrame (nunca no handler de scroll direto)
  - Testar para garantir que nao causa CLS

```js
// Implementacao padrao de parallax
let ticking = false;
window.addEventListener("scroll", () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      const speed = 0.08;
      const y = window.scrollY * speed;
      heroBg.style.transform = "translateY(" + y + "px) scale(1.05)";
      ticking = false;
    });
    ticking = true;
  }
}, { passive: true });
```

---

## Parte 4 -- Experiencia de Navegacao

### 4.1 Scroll Suave

```css
html { scroll-behavior: smooth; scroll-padding-top: 80px; }
```

Scroll padding compensa a navbar fixa (altura da navbar + 8px de folga).

### 4.2 Smooth Scroll via JS (para maior controle)

```js
document.querySelectorAll("a[href^='#']").forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      const offsetTop = target.getBoundingClientRect().top + window.scrollY - 88;
      window.scrollTo({ top: offsetTop, behavior: "smooth" });
    }
  });
});
```

### 4.3 Feedback de Estado Ativo na Navegacao

```css
.nav-menu a[aria-current="page"],
.nav-menu a.active {
  color: var(--accent);
}
.nav-menu a[aria-current="page"]::after {
  width: 100%;
}
```

```js
// Destacar secao ativa conforme scroll
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-menu a[href^='#']");
const activeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => link.removeAttribute("aria-current"));
      const activeLink = document.querySelector(".nav-menu a[href='#" + entry.target.id + "']");
      if (activeLink) activeLink.setAttribute("aria-current", "page");
    }
  });
}, { threshold: 0.5 });
sections.forEach(s => activeObserver.observe(s));
```

---

## Parte 5 -- Touch e Mobile Premium

### 5.1 Gestos e Touch Feedback

- Todo elemento clicavel deve ter resposta visual instantanea ao toque
- Usar :active com escala 0.97 em botoes para feedback tatil visual
- Evitar delays de 300ms (garantido com viewport meta correto)

```css
.btn:active { transform: scale(0.97); }
.filter-btn:active { opacity: 0.7; }
```

### 5.2 Swipe em Galerias (mobile)

Para filtros e tabs em mobile, usar swipe horizontal nativo:

```css
.filter-tabs {
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}
.filter-btn {
  scroll-snap-align: start;
  flex-shrink: 0;
}
```

### 5.3 Safe Area (iPhone com notch)

```css
.navbar {
  padding-top: max(1.2rem, env(safe-area-inset-top));
  padding-left: max(0px, env(safe-area-inset-left));
  padding-right: max(0px, env(safe-area-inset-right));
}
.wa-float {
  bottom: max(28px, calc(28px + env(safe-area-inset-bottom)));
  right: max(28px, env(safe-area-inset-right));
}
```

---

## Parte 6 -- Copywriting de Alta Conversao

### 6.1 Hierarquia de Copy

1. Headline (H1): promessa principal, transformacao, resultado
   Nao: "Fotografia de Newborn"
   Sim: "Eternize os primeiros capitulos da sua historia."

2. Subheadline: especificacao e diferenciais
   Nao: "Fazemos fotos de bebes"
   Sim: "Ensaios de gestante, newborn e acompanhamento infantil com delicadeza, seguranca e sensibilidade."

3. Prova Social: numeros, depoimentos, resultados
   "Mais de 500 familias eternizadas | 12 anos de experiencia | Porto Alegre e regiao"

4. CTA: unico, claro, beneficio implicito
   Nao: "Enviar" ou "Clique aqui"
   Sim: "Agendar meu ensaio" ou "Ver disponibilidade"

### 6.2 Linguagem por Segmento

Fotografia / Maternidade:
  - Tom: acolhedor, sensivel, poetico
  - Palavras-chave: eternizar, momento, historia, delicadeza, amor, registro
  - Evitar: barato, oferta, desconto, urgencia

Barbearia Premium:
  - Tom: masculino, direto, confiante
  - Palavras-chave: precisao, artesanato, ritual, identidade, estilo
  - Evitar: feminino, florido, delicado

Gastronomia:
  - Tom: artesanal, autentico, convidativo
  - Palavras-chave: feito a mao, ingredientes selecionados, tradicao, sabor, experiencia
  - Evitar: industrial, rapido, pratico (para premium artesanal)

---

## Parte 7 -- Criterios de Qualidade Final

### 7.1 O Teste do Squint

Feche os olhos pela metade olhando para a pagina.
  - Voce consegue identificar o elemento mais importante?
  - Ha uma hierarquia visual clara?
  - O design "respira" (ha espaco suficiente)?
  - Os blocos de informacao estao bem delimitados?

Se nao: ajustar tamanho de fonte, espaco, peso e contraste.

### 7.2 O Teste de 5 Segundos

Mostre a pagina para alguem por 5 segundos e feche.
Pergunte:
  - O que voce viu?
  - Qual e o negocio?
  - O que voce acha que eles vendem?
  - O que voce faria a seguir?

Se as respostas nao estao alinhadas com a intencao: revisar headline, hero e CTA.

### 7.3 O Teste de Polegar (Mobile)

Segure o celular com uma mao so, com o polegar.
  - Todos os CTAs principais estao na zona de alcance do polegar?
  - Nenhum link importante esta escondido em cantos superiores?
  - O formulario e preenchivel com uma mao?

Zona segura de alcance do polegar: parte inferior e central da tela.

### 7.4 O Teste da Lentidao

Simule conexao 3G no Chrome DevTools.
  - O site carrega em menos de 3 segundos?
  - O layout nao pula durante o carregamento (CLS)?
  - As imagens tem placeholder ou dimensoes declaradas?

### 7.5 Criterios Numericos de Aprovacao

| Criterio                    | Meta          |
|-----------------------------|---------------|
| Lighthouse Performance      | >= 85         |
| Lighthouse Accessibility    | >= 95         |
| Lighthouse Best Practices   | >= 90         |
| Lighthouse SEO              | 100           |
| LCP (Largest Contentful Paint) | < 2.5s    |
| CLS (Cumulative Layout Shift) | < 0.1      |
| INP (Interaction to Next Paint) | < 200ms  |
| Contraste minimo texto      | 4.5:1         |
| Tamanho minimo touch target | 44x44px       |
| Overflow horizontal         | 0px em todos  |

---

## Parte 8 -- Prompt de Uso com IA

Ao solicitar a criacao ou correcao de uma pagina, usar este prompt estruturado:

---

PROMPT PADRAO ANTIGRAVITY:

"Implemente [DESCRICAO DO PROJETO] seguindo rigorosamente os quatro documentos de padroes Antigravity:

01-FTI-Ficha-Tecnica-Implementacao.md -- arquitetura e padroes tecnicos
02-Design-System.md -- tokens, cores, tipografia, espacamento
03-Biblioteca-Componentes.md -- HTML/CSS/JS reutilizavel de cada componente
04-Guia-Experiencia-Premium.md -- UX, direcao de arte, motion design e criterios de qualidade

Prioridades absolutas:
1. Arquitetura Single-File (HTML + style + script em index.html)
2. Mobile-First real (base para mobile, min-width para desktop)
3. Zero overflow horizontal em qualquer breakpoint (360px a 1920px)
4. Tipografia fluida com clamp() em todos os titulos
5. Touch targets >= 44px em todos elementos interativos
6. Menu mobile com overlay backdrop e scroll lock
7. 100dvh no hero (nao 100vh)
8. font-size 16px em inputs (sem zoom iOS)
9. Scroll indicator oculto em mobile
10. Btn-nav oculto no header em mobile

Toda decisao nao descrita nos documentos deve seguir as melhores praticas modernas
de UX, UI, HTML, CSS e JavaScript.

Nenhuma implementacao podera ignorar os padroes definidos."

---

*Versao 1.0 | Antigravity Dev Standards | 2026-08*
