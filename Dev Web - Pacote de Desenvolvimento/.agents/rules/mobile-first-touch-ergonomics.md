# ✦ Regra: Ergonomia Tátil e Engenharia Mobile-First

> **Objetivo:** Estabelecer padrões rigorosos de usabilidade tátil, alcance polegar (Thumb Zone), cálculo de áreas seguras (Safe Areas) e interatividade fluida em dispositivos móveis, garantindo que qualquer aplicação ou página web proporcione experiência equivalente ou superior a apps nativos.

---

## 📱 1. Diretrizes Fundamentais de Toque (Touch Targets)

Em dispositivos touchscreen, a precisão do usuário é determinada pela ponta dos dedos (área de contato entre 8mm e 10mm). Alvos pequenos geram frustração, toques acidentais e aumento nas taxas de abandono.

### 📐 Dimensões Mínimas Mandatórias:
- **Alvos primários e botões de ação:** Mínimo absoluto de **48 × 48 px** (área de toque recomendada pelo W3C/WCAG 2.2 e Apple HIG).
- **Alvos secundários (ícones em cabeçalhos, links de lista):** Mínimo absoluto de **44 × 44 px**.
- **Espaçamento entre alvos adjacentes:** Mínimo de **8px** de separação livre para evitar toques concorrentes.

```css
/* Padrão para elementos interativos móveis */
.touch-target, 
button, 
.nav-link, 
.action-btn {
  min-height: 48px;
  min-width: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

/* Quando o elemento visual precisa parecer menor (ex: ícone 24px),
   expanda a área de toque invisível via pseudo-elemento */
.icon-only-btn {
  position: relative;
  width: 28px;
  height: 28px;
}

.icon-only-btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 48px;
  height: 48px;
  min-width: 48px;
  min-height: 48px;
}
```

---

## 🖐️ 2. Thumb Zone (A Zona do Polegar)

Mais de 75% da navegação em smartphones ocorre usando apenas uma das mãos, onde o polegar domina a tela.

### 🗺️ Mapeamento de Zonas em Tela Vertical:
1. **Zona Natural (Confortável):**
   - Terço inferior e centro da tela.
   - **Obrigatório:** Ações primárias (Salvar, Comprar, Avançar, Adicionar, Toggle Menu, Bottom Navigation).
2. **Zona de Extensão (Alcançável com esforço):**
   - Centro superior da tela.
   - **Recomendado:** Conteúdo de leitura, resumos, cartões informativos.
3. **Zona Proibida para Ações Críticas (Hard to reach):**
   - Cantos superiores esquerdo e direito (ex: botão salvar no canto superior direito a 850px de altura).
   - **Regra:** Nunca coloque a ação primária de um formulário ou fluxo no topo do viewport móvel.

### 🔽 Padrão Bottom Sheet em vez de Modal Central:
- Em telas `< 768px`, evite caixas de diálogo e modais centralizados no topo da tela.
- Use gavetas que deslizam da base (**Bottom Sheet**), com bordas arredondadas no topo (`border-radius: 20px 20px 0 0`) e ações ao alcance do polegar.

```css
/* Padrão Bottom Sheet Móvel */
@media (max-width: 768px) {
  .modal-dialog {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    margin: 0;
    max-height: 85dvh;
    border-radius: 20px 20px 0 0;
    padding-bottom: calc(1rem + env(safe-area-inset-bottom, 16px));
    transform: translateY(0);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
}
```

---

## 🛡️ 3. Safe Areas (Notches, Ilhas Dinâmicas e Barras de Navegação)

Smartphones modernos (iOS e Android com gestos) possuem cantos arredondados, câmeras frontais em notch/ilha e barras de gesto na base do sistema.

### ⚙️ Configuração Obrigatória no HTML:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, maximum-scale=1.0, user-scalable=no">
```

### 📐 Aplicação de Variáveis CSS de Ambiente:
Sempre utilize as funções `env(safe-area-inset-*)` com valor de fallback em elementos fixos ou colados nas extremidades:

```css
/* Cabeçalho fixo no topo */
.header-fixed {
  padding-top: max(12px, env(safe-area-inset-top));
}

/* Barra de ação ou navegação colada na base */
.bottom-nav, 
.floating-cta-bar {
  padding-bottom: calc(12px + env(safe-area-inset-bottom, 12px));
  padding-left: max(16px, env(safe-area-inset-left));
  padding-right: max(16px, env(safe-area-inset-right));
}
```

---

## ⚡ 4. Otimizações de Toque e Latência

### 🚫 Remoção do Atraso de 300ms (Tap Delay):
Navegadores móveis antigos aguardavam 300ms após um toque para verificar duplo toque de zoom. Elimine essa latência expressamente:

```css
html, body, button, a, input, select {
  touch-action: manipulation;
}
```

### 👆 Feedback Háptico Visual (Active States):
Dispositivos móveis não possuem `:hover` persistente. Um botão sem feedback ao toque parece travado.
- Use estados `:active` rápidos com redução sutil de escala:

```css
.btn-touchable {
  transition: transform 0.1s ease, opacity 0.1s ease;
  -webkit-tap-highlight-color: transparent; /* Remove o retângulo azul padrão do Android/iOS */
}

.btn-touchable:active {
  transform: scale(0.96);
  opacity: 0.9;
}
```

### 🛡️ Proteção de Hover em Dispositivos Sem Cursor:
Nunca condicione funcionalidades ou visibilidade de botões a interações de `:hover` em telas móveis:

```css
/* Aplique regras de hover exclusivamente quando houver cursor preciso */
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
  }
}

/* Em dispositivos móveis (touch), mantenha o elemento sempre acessível */
@media (hover: none) and (pointer: coarse) {
  .card-action-always-visible {
    opacity: 1 !important;
  }
}
```

---

## 📋 Checklist de Aceitação para Agentes:
- [ ] Todas as áreas clicáveis têm no mínimo 44×44px (ideal 48×48px).
- [ ] O viewport possui `viewport-fit=cover`.
- [ ] Barras fixas inferiores compensam `env(safe-area-inset-bottom)`.
- [ ] Ações críticas de formulários ficam na metade inferior da tela.
- [ ] Não há seletores `:hover` obrigatórios para revelar botões essenciais.
- [ ] `-webkit-tap-highlight-color: transparent` e `:active` implementados.
