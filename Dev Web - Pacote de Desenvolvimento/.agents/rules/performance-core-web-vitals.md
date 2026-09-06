# ✦ Regra: Performance Extrema e Métricas Core Web Vitals (LCP, INP, CLS)

> **Objetivo:** Estabelecer parâmetros rígidos de performance de renderização no navegador, garantindo pontuações superiores a 95+ no Google Lighthouse, carregamento em menos de 1.2s em conexões móveis 4G e fluidez contínua a 60/120 FPS.

---

## 🎯 1. Metas Oficiais de Core Web Vitals

Toda página ou aplicação desenvolvida DEVE perseguir os seguintes limites técnicos:

| Métrica | Nome Completo | Meta Antigravity | Limite Máximo Aceitável |
| :--- | :--- | :--- | :--- |
| **LCP** | Largest Contentful Paint (Renderização do maior elemento) | **< 1.0s** | < 2.0s |
| **INP** | Interaction to Next Paint (Tempo de resposta a cliques/toques) | **< 50ms** | < 150ms |
| **CLS** | Cumulative Layout Shift (Estabilidade visual e saltos de tela) | **0.00** | < 0.05 |
| **FCP** | First Contentful Paint (Primeiro elemento desenhado) | **< 0.6s** | < 1.2s |
| **TBT** | Total Blocking Time (Tempo de bloqueio da thread principal) | **0ms** | < 100ms |

---

## 🚀 2. Animações Exclusivas na GPU (Compositor Thread)

O navegador processa páginas em três etapas: **Layout (Reflow) ➔ Paint (Repaint) ➔ Composite**. 
Animar propriedades geométricas força o navegador a recalcular o layout de toda a árvore do DOM a cada frame (60 a 120 vezes por segundo), derrubando a taxa de quadros em celulares.

### 🚫 Propriedades Proibidas para Animação/Transição Contínua:
- ❌ `width`, `height`, `min-width`, `max-height`
- ❌ `top`, `bottom`, `left`, `right`
- ❌ `margin`, `padding`
- ❌ `border-width`

### ✅ As Únicas Duas Propriedades Seguras (GPU Composited):
1. **`transform`:** (`translate3d()`, `scale()`, `rotate()`)
2. **`opacity`:** (`0` a `1`)

```css
/* ERRADO — Provoca Reflow massivo */
.bad-drawer {
  left: -300px;
  transition: left 0.3s ease;
}
.bad-drawer.open {
  left: 0;
}

/* CORRETO — Executado diretamente na placa gráfica (GPU) */
.good-drawer {
  transform: translate3d(-100%, 0, 0);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
}
.good-drawer.open {
  transform: translate3d(0, 0, 0);
}
```

---

## 🛑 3. Eliminação Total de Saltos de Layout (Zero CLS)

Saltos de conteúdo ocorrem quando imagens, anúncios ou fontes carregam depois e empurram o texto para baixo enquanto o usuário está lendo ou clicando.

### 🖼️ Regra para Imagens e Vídeos:
Sempre declare dimensões intrínsecas (`width` e `height`) ou use `aspect-ratio` no CSS:

```html
<!-- O navegador reserva o espaço exato antes mesmo do download começar -->
<img 
  src="foto-produto.webp" 
  alt="Descrição da foto" 
  width="800" 
  height="600" 
  loading="lazy" 
  decoding="async"
  style="width: 100%; height: auto; aspect-ratio: 4/3;"
>
```

### 🔤 Fontes Sem Salto Visual (FOIT / FOUT):
Ao importar fontes externas (Google Fonts), use sempre `display=swap`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
```

---

## ⚡ 4. Otimização de Imagens e Priorização (LCP)

1. **Imagem de Destaque do Hero (LCP Hero):**
   - Nunca aplique `loading="lazy"` na imagem principal do topo!
   - Aplique `fetchpriority="high"` para indicar ao navegador que aquele arquivo tem prioridade máxima:
   ```html
   <img src="hero-banner.webp" fetchpriority="high" alt="Hero Principal">
   ```

2. **Todas as Demais Imagens:**
   - Devem ter `loading="lazy"` e `decoding="async"`.
   - Preferir formatos de última geração: **WebP** ou **AVIF** (60% menores que JPEG/PNG).

---

## ⏱️ 5. JavaScript e Ouvintes de Eventos Passivos

Ouvintes de rolagem (`scroll`) e toque (`touchstart`, `touchmove`) podem travar o scroll se o navegador precisar esperar a execução do script.

```javascript
// CORRETO: Declarar ouvinte como passivo para não bloquear a thread de rolagem
window.addEventListener('scroll', handleScroll, { passive: true });
window.addEventListener('touchmove', handleTouch, { passive: true });

// Otimização de busca/redimensionamento com Debounce
function debounce(func, wait = 150) {
  let timeout;
  return function executedFunction(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

window.addEventListener('resize', debounce(() => {
  // Ajuste de layout leve
}, 200));
```

---

## 📋 Checklist de Aceitação para Agentes:
- [ ] Animações usam apenas `transform` e `opacity`.
- [ ] Todas as imagens possuem atributos `width`, `height` e `aspect-ratio`.
- [ ] A imagem principal do topo tem `fetchpriority="high"`, sem `loading="lazy"`.
- [ ] Imagens fora da primeira dobra possuem `loading="lazy"` e `decoding="async"`.
- [ ] Listeners de `scroll` e `touch` usam `{ passive: true }`.
- [ ] CDNs externas utilizam `<link rel="preconnect">`.
