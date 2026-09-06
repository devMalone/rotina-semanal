# Biblioteca de Componentes
### Versao 1.0 -- Antigravity Dev Standards

---

## Objetivo

Este documento cataloga todos os componentes reutilizaveis do ecossistema Antigravity.
Cada componente possui estrutura HTML, comportamento, variantes e estados documentados.
Todo novo projeto deve construir seus componentes a partir desta biblioteca.

---

## Componente 01 -- Navbar

### Estrutura HTML

```html
<header id="navbar" class="navbar" role="banner">
  <div class="container">
    <nav class="nav-container" aria-label="Navegacao principal">
      <a href="#" class="brand-logo" aria-label="Ir para o inicio">
        NOME MARCA
        <span>subtitulo</span>
      </a>
      <ul class="nav-menu" id="navMenu" role="list">
        <li><a href="#secao">Link</a></li>
        <li><a href="#contato" class="btn btn-nav">CTA Principal</a></li>
      </ul>
      <button class="mobile-toggle" id="mobileToggle"
              aria-label="Abrir menu de navegacao"
              aria-expanded="false"
              aria-controls="navMenu">
        <i data-lucide="menu"></i>
      </button>
    </nav>
  </div>
</header>
```

### Estados

- default: transparente (hero por baixo)
- scrolled: background com backdrop-filter blur(16px), border-bottom solid --border
- menu-open: mobile drawer ativo, body bloqueado

### Comportamento JS (padrao para todos os projetos)

```js
const navOverlay = document.getElementById("navOverlay");
const navMenu = document.getElementById("navMenu");
const mobileToggle = document.getElementById("mobileToggle");

function toggleMobileMenu(open) {
  const shouldOpen = open !== undefined ? open : !navMenu.classList.contains("active");
  navMenu.classList.toggle("active", shouldOpen);
  navOverlay.classList.toggle("active", shouldOpen);
  document.body.classList.toggle("menu-open", shouldOpen);
  mobileToggle.setAttribute("aria-expanded", shouldOpen ? "true" : "false");
}

mobileToggle.addEventListener("click", () => toggleMobileMenu());
navOverlay.addEventListener("click", () => toggleMobileMenu(false));
navMenu.querySelectorAll("a").forEach(link => link.addEventListener("click", () => toggleMobileMenu(false)));
document.addEventListener("keydown", e => { if (e.key === "Escape") toggleMobileMenu(false); });
```

### HTML do Overlay (logo apos body)

```html
<div class="mobile-nav-overlay" id="navOverlay"></div>
```

### CSS Critico

```css
.navbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  transition: all 0.4s ease;
}
.navbar.scrolled {
  background: rgba(253,251,247,0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  box-shadow: var(--shadow-sm);
}
.mobile-nav-overlay {
  position: fixed; inset: 0;
  background: rgba(26,24,23,0.65);
  backdrop-filter: blur(5px);
  z-index: 999; opacity: 0; pointer-events: none;
  transition: opacity 0.4s ease;
}
.mobile-nav-overlay.active { opacity: 1; pointer-events: auto; }
body.menu-open { overflow: hidden; touch-action: none; }
```

---

## Componente 02 -- Hero Section

### Variante A -- Full Viewport com Imagem de Fundo

```html
<section class="hero" id="inicio">
  <div class="hero-bg" id="heroBg" style="background-image: url(imagem.webp);"
       role="img" aria-label="Descricao da imagem de fundo"></div>
  <div class="hero-overlay" aria-hidden="true"></div>
  <div class="hero-content">
    <span class="hero-badge">Label da categoria</span>
    <h1 class="hero-title">Titulo Principal da Pagina</h1>
    <p class="hero-subtitle">Subtitulo com proposta de valor clara e direta.</p>
    <div class="hero-buttons">
      <a href="#contato" class="btn btn-primary">CTA Principal</a>
      <a href="#portfolio" class="btn btn-outline">CTA Secundario</a>
    </div>
  </div>
  <div class="scroll-indicator" aria-hidden="true">
    <span>Role para descobrir</span>
    <div class="line"></div>
  </div>
</section>
```

### CSS Critico (Hero Full Viewport)

```css
.hero {
  position: relative; width: 100%;
  height: 100dvh; min-height: 540px;
  display: flex; align-items: center; justify-content: center; text-align: center;
  overflow: hidden;
}
.hero-bg {
  position: absolute; top: 0; left: 0; width: 100%; height: 115%;
  background-size: cover; background-position: center; z-index: 1;
}
.hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(253,251,247,0.35) 0%, rgba(253,251,247,0.75) 100%);
  z-index: 2;
}
.hero-content {
  position: relative; z-index: 3;
  max-width: 880px; width: 100%; padding: 0 1.5rem; box-sizing: border-box;
}
```

### Responsividade do Hero (padrao)

```css
@media (max-width: 768px) {
  .btn-nav, .scroll-indicator, .scroll-indicator * {
    display: none !important;
  }
}
@media (max-width: 480px) {
  .hero-content { margin-top: 0.5rem; padding: 0 0.25rem; }
  .hero-badge { font-size: 0.65rem; letter-spacing: 0.08em; white-space: normal; word-break: break-word; }
  .hero-title { font-size: clamp(1.55rem, 6.8vw, 2.1rem); line-height: 1.22; overflow-wrap: break-word; }
  .hero-subtitle { font-size: 0.88rem; line-height: 1.55; }
  .hero-buttons { flex-direction: column; width: 100%; gap: 0.75rem; }
  .hero-buttons .btn { width: 100%; min-height: 48px; }
}
```

---

## Componente 03 -- Botoes

### HTML

```html
<!-- Primario (filled) -->
<a href="#" class="btn btn-primary">TEXTO DO BOTAO</a>

<!-- Secundario (outline) -->
<a href="#" class="btn btn-outline">TEXTO DO BOTAO</a>

<!-- Com icone -->
<a href="#" class="btn btn-primary">
  <i data-lucide="message-circle" style="width:18px;height:18px;margin-right:8px;"></i>
  TEXTO DO BOTAO
</a>

<!-- WhatsApp -->
<a href="https://wa.me/5511999999999?text=Mensagem" class="btn btn-primary" target="_blank" rel="noopener noreferrer">
  Falar no WhatsApp
</a>
```

### CSS Completo

```css
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 0.85rem 2.2rem;
  border-radius: var(--radius-full, 9999px);
  font-family: var(--font-sans);
  font-size: 0.78rem; font-weight: 500;
  letter-spacing: 0.12em; text-transform: uppercase;
  text-decoration: none; cursor: pointer;
  transition: all 0.35s ease;
  min-height: 44px; border: 1px solid transparent;
  white-space: nowrap;
}
.btn-primary {
  background: var(--accent); color: var(--bg-primary);
  border-color: var(--accent);
}
.btn-primary:hover {
  background: var(--accent-hover); border-color: var(--accent-hover);
  transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}
.btn-outline {
  background: transparent; color: var(--text-dark);
  border-color: var(--border-strong, rgba(0,0,0,0.25));
}
.btn-outline:hover {
  background: var(--text-dark); color: var(--bg-primary);
  border-color: var(--text-dark);
}
.btn:disabled, .btn[aria-disabled="true"] {
  opacity: 0.4; cursor: not-allowed; pointer-events: none;
}
```

---

## Componente 04 -- Cards de Servico / Sessao

### HTML

```html
<div class="session-card" role="article">
  <div class="session-img">
    <img src="foto.webp" alt="Descricao do servico" loading="lazy" width="400" height="280">
  </div>
  <div class="session-info">
    <span class="session-tag">CATEGORIA</span>
    <h3 class="session-title">Nome do Servico</h3>
    <p class="session-desc">Descricao breve do que esta incluido neste servico.</p>
    <div class="session-details">
      <span><i data-lucide="clock"></i> 2-3 horas</span>
      <span><i data-lucide="image"></i> 40 fotos</span>
    </div>
    <a href="#contato" class="btn btn-primary">Agendar</a>
  </div>
</div>
```

---

## Componente 05 -- Galeria Editorial (Grid de Portfolio)

### HTML (com Affordance de Scroll Horizontal em Mobile)

```html
<!-- Wrapper obrigatório para o fade lateral -->
<div class="filter-wrapper">
  <div class="filter-tabs" role="tablist" aria-label="Filtros de portfólio">
    <button class="filter-btn active" data-filter="all" role="tab" aria-selected="true">Todos</button>
    <button class="filter-btn" data-filter="newborn" role="tab" aria-selected="false">Newborn</button>
    <button class="filter-btn" data-filter="gestante" role="tab" aria-selected="false">Gestante</button>
  </div>
  <!-- Fade lateral: indica visualmente que há mais itens além da borda -->
  <div class="filter-fade-indicator" aria-hidden="true"></div>
</div>
<!-- Dica textual animada (apenas mobile, some após scroll) -->
<div class="filter-swipe-hint" id="filterSwipeHint">
  <span>Deslize para ver mais categorias</span>
  <i data-lucide="arrow-right"></i>
</div>

<div class="editorial-grid" id="galeriaGrid">
  <div class="grid-item item-large" data-category="newborn">
    <img src="foto1.webp" alt="Ensaio newborn" loading="lazy">
    <div class="grid-overlay"><span class="grid-label">Newborn</span></div>
  </div>
</div>
```

### CSS do Wrapper de Filtros (com affordance mobile)

```css
.filter-wrapper {
  position: relative;
  width: 100%;
}

/* Dica textual: oculta por padrão em desktop */
.filter-swipe-hint {
  display: none;
}

@media (max-width: 600px) {
  .filter-fade-indicator {
    position: absolute; top: 0; right: 0; bottom: 0; width: 48px;
    background: linear-gradient(90deg, transparent 0%, var(--bg-primary) 100%);
    pointer-events: none; z-index: 2;
    transition: opacity 0.3s ease;
  }

  .filter-tabs {
    justify-content: flex-start; overflow-x: auto;
    padding-bottom: 0.6rem; padding-right: 2.5rem;
    flex-wrap: nowrap; -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory; scrollbar-width: none;
    margin-bottom: 0.75rem;
  }
  .filter-tabs::-webkit-scrollbar { display: none; }

  .filter-btn {
    white-space: nowrap; flex-shrink: 0;
    scroll-snap-align: start;
  }

  .filter-swipe-hint {
    display: flex; align-items: center; gap: 0.35rem;
    font-size: 0.72rem; color: var(--accent-brown);
    letter-spacing: 0.05em; margin-bottom: 2rem;
    transition: opacity 0.3s ease;
  }
  .filter-swipe-hint i { animation: hintArrowMove 1.5s infinite ease-in-out; }
}
@keyframes hintArrowMove {
  0%, 100% { transform: translateX(0); }
  50% { transform: translateX(5px); }
}
```

### JS de Filtro (com scroll listener para esconder dica)

```js
const filterBtns = document.querySelectorAll(".filter-btn");
const gridItems = document.querySelectorAll(".grid-item");
const filterTabsEl = document.querySelector(".filter-tabs");
const filterFade = document.querySelector(".filter-fade-indicator");
const filterHint = document.querySelector(".filter-swipe-hint");

filterBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    filterBtns.forEach(b => { b.classList.remove("active"); b.setAttribute("aria-selected","false"); });
    btn.classList.add("active"); btn.setAttribute("aria-selected","true");
    const filter = btn.dataset.filter;
    gridItems.forEach(item => {
      const show = filter === "all" || item.dataset.category === filter;
      item.style.opacity = show ? "1" : "0";
      item.style.transform = show ? "scale(1)" : "scale(0.95)";
      item.style.pointerEvents = show ? "auto" : "none";
    });
  });
});

if (filterTabsEl) {
  filterTabsEl.addEventListener("scroll", () => {
    const maxScroll = filterTabsEl.scrollWidth - filterTabsEl.clientWidth;
    const atEnd = filterTabsEl.scrollLeft >= maxScroll - 15;
    if (filterFade) filterFade.style.opacity = atEnd ? "0" : "1";
    if (filterHint) filterHint.style.opacity = atEnd ? "0" : (filterTabsEl.scrollLeft > 15 ? "0.4" : "1");
  }, { passive: true });
}
```

---

## Componente 06 -- Formulario de Agendamento WhatsApp

> **IMPORTANTE**: Todo o CSS de `.booking-form`, `.form-grid`, `.form-group` deve estar
> declarado na seção de estilos base (<style>), **antes** de qualquer `@media`.
> Sem isso, a tag renderiza como elemento bruto no layout.

### HTML

```html
<section class="contato-section" id="contato">
  <div class="container">
    <h2 class="section-title">Agende seu Ensaio</h2>
    <p class="section-subtitle">Preencha e receba orçamento personalizado via WhatsApp.</p>
    <form class="booking-form" id="bookingForm" novalidate>
      <div class="form-grid">
        <div class="form-group">
          <label for="nome">Nome Completo</label>
          <input type="text" id="nome" name="nome" placeholder="Seu nome" required autocomplete="name">
        </div>
        <div class="form-group">
          <label for="mes">Mês Desejado</label>
          <input type="text" id="mes" name="mes" placeholder="Ex: Setembro / Outubro" required>
        </div>
        <!-- Tipo de Ensaio em largura total para evitar corte de texto -->
        <div class="form-group full-width">
          <label for="ensaio">Tipo de Ensaio Desejado</label>
          <select id="ensaio" name="ensaio" required>
            <!-- OBRIGATÓRIO: primeiro item é sempre placeholder disabled -->
            <option value="" disabled selected>Selecione o tipo de ensaio...</option>
            <option>Newborn</option>
            <option>Gestante</option>
            <option>Família</option>
          </select>
        </div>
        <div class="form-group full-width">
          <label for="mensagem">Mensagem (opcional)</label>
          <textarea id="mensagem" name="mensagem" rows="3" placeholder="Conte um pouco sobre o que imagina..."></textarea>
        </div>
      </div>
      <button type="submit" class="btn btn-primary btn-submit-wa">
        <i data-lucide="message-circle"></i>
        Enviar pelo WhatsApp
      </button>
    </form>
  </div>
</section>
```

### CSS Base Obrigatório (fora de @media)

```css
.booking-form {
  background: rgba(253, 251, 247, 0.96);
  backdrop-filter: blur(15px);
  padding: 2.5rem;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  width: 100%;
  box-sizing: border-box;
  text-align: left;
}

/* Grid de 2 colunas em desktop, 1 coluna em mobile */
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.5rem;
  width: 100%;
}

.form-group label {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent-brown);
  font-weight: 600;
}

.form-group input,
.form-group select,
.form-group textarea {
  display: block;
  width: 100%;
  padding: 0.85rem 1.1rem;
  border-radius: 10px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-primary);
  color: var(--text-dark);
  font-family: var(--font-sans);
  font-size: 16px; /* Previne zoom automático iOS */
  box-sizing: border-box;
}

/* OBRIGATÓRIO: seta customizada em todo <select> */
.form-group select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%239E8270' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1.1rem center;
  background-size: 18px 18px;
  padding-right: 2.75rem;
  cursor: pointer;
}

.form-group.full-width { grid-column: span 2; }

/* Mobile: colapso para 1 coluna */
@media (max-width: 768px) {
  .form-grid {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  .form-group.full-width { width: 100%; }
  .booking-form { padding: 1.5rem 1.15rem; }
}
```

### JS -- Numero do WhatsApp: 5511957835028

```js
const bookingForm = document.getElementById("bookingForm");
const WA_NUMBER = "5511957835028";
if (bookingForm) {
  bookingForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const nome = document.getElementById("nome").value.trim();
    const ensaio = document.getElementById("ensaio").value;
    const mes = document.getElementById("mes").value;
    const mensagem = document.getElementById("mensagem").value.trim();
    if (!nome || !ensaio || !mes) {
      alert("Por favor, preencha nome, tipo de ensaio e mes.");
      return;
    }
    let texto = "Ola! Me chamo " + nome + " e gostaria de agendar um ensaio de " + ensaio + " para o mes de " + mes + ".";
    if (mensagem) texto += " Mensagem: " + mensagem;
    window.open("https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(texto), "_blank", "noopener,noreferrer");
  });
}
```

---

## Componente 07 -- FAQ Accordion

### HTML

```html
<section class="faq-section" id="faq">
  <div class="container">
    <h2 class="section-title">Perguntas Frequentes</h2>
    <div class="faq-list">
      <div class="faq-item">
        <button class="accordion-header" aria-expanded="false" aria-controls="faq-1">
          <span>Qual a duracao de uma sessao?</span>
          <i data-lucide="plus" aria-hidden="true"></i>
        </button>
        <div class="accordion-body" id="faq-1" hidden>
          <p>Uma sessao tipica dura entre 1 e 3 horas, dependendo do tipo de ensaio.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

### JS de Accordion

```js
document.querySelectorAll(".accordion-header").forEach(btn => {
  btn.addEventListener("click", () => {
    const isOpen = btn.getAttribute("aria-expanded") === "true";
    document.querySelectorAll(".accordion-header").forEach(b => {
      b.setAttribute("aria-expanded", "false");
      const body = document.getElementById(b.getAttribute("aria-controls"));
      if (body) body.hidden = true;
    });
    if (!isOpen) {
      btn.setAttribute("aria-expanded", "true");
      const body = document.getElementById(btn.getAttribute("aria-controls"));
      if (body) body.hidden = false;
    }
  });
});
```

---

## Componente 08 -- Depoimentos (Testimonials)

### HTML

```html
<section class="testimonials-section" id="depoimentos">
  <div class="container">
    <h2 class="section-title">O Que Dizem Nossas Clientes</h2>
    <div class="testimonials-grid">
      <article class="testimonial-card">
        <div class="stars" aria-label="5 estrelas">*****</div>
        <blockquote class="testimonial-text">
          "Texto do depoimento aqui. Descricao autentica e especifica da experiencia."
        </blockquote>
        <footer class="testimonial-author">
          <cite>Nome da Cliente</cite>
          <span>Tipo de ensaio realizado</span>
        </footer>
      </article>
    </div>
  </div>
</section>
```

---

## Componente 09 -- Floating WhatsApp Button

### HTML

```html
<a href="https://wa.me/5511957835028?text=Ola!%20Gostaria%20de%20saber%20mais%20sobre%20os%20ensaios."
   class="wa-float"
   target="_blank"
   rel="noopener noreferrer"
   aria-label="Falar com a gente pelo WhatsApp">
  <i data-lucide="message-circle"></i>
</a>
```

### CSS

```css
.wa-float {
  position: fixed; bottom: 28px; right: 28px;
  width: 56px; height: 56px;
  background: #25D366; color: #fff;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 24px rgba(37,211,102,0.4);
  z-index: 999; text-decoration: none;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  animation: pulseWa 2.5s infinite;
}
.wa-float:hover { transform: scale(1.1); box-shadow: 0 12px 30px rgba(37,211,102,0.5); }
@keyframes pulseWa {
  0%   { box-shadow: 0 0 0 0 rgba(37,211,102,0.6); }
  70%  { box-shadow: 0 0 0 14px rgba(37,211,102,0); }
  100% { box-shadow: 0 0 0 0 rgba(37,211,102,0); }
}
```

---

## Componente 10 -- Scroll Progress Bar

### HTML

```html
<div class="scroll-progress" id="scrollProgress" role="progressbar"
     aria-label="Progresso de leitura" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
</div>
```

### CSS

```css
.scroll-progress {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent) 0%, var(--accent-gold, #C4A882) 100%);
  width: 0%; z-index: 10001; transition: width 0.1s ease-out;
}
```

### JS

```js
const scrollProgress = document.getElementById("scrollProgress");
window.addEventListener("scroll", () => {
  const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
  scrollProgress.style.width = scrolled + "%";
  scrollProgress.setAttribute("aria-valuenow", Math.round(scrolled));
}, { passive: true });
```

---

## Componente 11 -- Footer

### HTML

```html
<footer class="footer" id="rodape">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="#" class="brand-logo">NOME MARCA</a>
        <p class="footer-tagline">Tagline ou proposta de valor breve.</p>
        <div class="footer-social">
          <a href="https://instagram.com/" aria-label="Instagram" target="_blank" rel="noopener">
            <i data-lucide="instagram"></i>
          </a>
        </div>
      </div>
      <div class="footer-links">
        <h4>Links Rapidos</h4>
        <ul>
          <li><a href="#inicio">Inicio</a></li>
          <li><a href="#portfolio">Portfolio</a></li>
          <li><a href="#contato">Agendar</a></li>
        </ul>
      </div>
      <div class="footer-contact">
        <h4>Contato</h4>
        <p><i data-lucide="map-pin"></i> Cidade, Estado</p>
        <p><i data-lucide="phone"></i> (11) 99999-9999</p>
        <p><i data-lucide="mail"></i> email@email.com</p>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Nome da Marca. Todos os direitos reservados.</p>
    </div>
  </div>
</footer>
```

---

## Componente 12 -- Reveal Animation (Intersection Observer)

### CSS

```css
.reveal-section {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.reveal-section.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### JS

```js
const sectionObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.15, rootMargin: "0px 0px -50px 0px" });
document.querySelectorAll(".reveal-section").forEach(s => sectionObserver.observe(s));
```

---

## Componente 13 -- Cursor Customizado (Desktop Only)

### HTML (logo apos body)

```html
<div class="cursor-dot" id="cursorDot" aria-hidden="true"></div>
<div class="cursor-ring" id="cursorRing" aria-hidden="true"></div>
```

### CSS

```css
.cursor-dot, .cursor-ring {
  position: fixed; border-radius: 50%; pointer-events: none;
  z-index: 99999; transition: opacity 0.3s ease;
}
.cursor-dot { width: 8px; height: 8px; background: var(--accent); transform: translate(-50%, -50%); }
.cursor-ring {
  width: 36px; height: 36px; border: 1px solid var(--accent);
  transform: translate(-50%, -50%);
  transition: transform 0.15s ease, width 0.3s ease, height 0.3s ease;
}
.cursor-ring.active { width: 56px; height: 56px; opacity: 0.5; }
```

### JS (Desktop Only)

```js
if (window.matchMedia("(pointer: fine)").matches) {
  const dot = document.getElementById("cursorDot");
  const ring = document.getElementById("cursorRing");
  let mouseX = 0, mouseY = 0, ringX = 0, ringY = 0;
  document.addEventListener("mousemove", e => { mouseX = e.clientX; mouseY = e.clientY; });
  const animate = () => {
    dot.style.left = mouseX + "px"; dot.style.top = mouseY + "px";
    ringX += (mouseX - ringX) * 0.12; ringY += (mouseY - ringY) * 0.12;
    ring.style.left = ringX + "px"; ring.style.top = ringY + "px";
    requestAnimationFrame(animate);
  };
  animate();
  document.querySelectorAll("a, button").forEach(el => {
    el.addEventListener("mouseenter", () => ring.classList.add("active"));
    el.addEventListener("mouseleave", () => ring.classList.remove("active"));
  });
}
```

---

*Versao 1.0 | Antigravity Dev Standards | 2026-08*
