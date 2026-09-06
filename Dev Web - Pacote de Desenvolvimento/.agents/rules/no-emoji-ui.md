# Regra: Uso de Emojis em Landing Pages e Sites

## Diretriz Geral

**Emojis são proibidos em textos, títulos, labels, badges, CTAs e qualquer elemento de UI** de landing pages e sites do ecossistema Antigravity, salvo em situações explicitamente aprovadas pelo cliente.

O uso de emojis em interfaces web é um marcador reconhecido de conteúdo gerado por IA sem curadoria humana. Passa a mensagem de que o operador não revisou os detalhes da entrega, o que compromete a credibilidade do trabalho e da agência.

---

## O Problema Específico

Emojis em textos de interface (títulos de seção, badges, labels, bullets, CTAs, top bars):

- Transmitem **informalidade excessiva**, incompatível com qualquer posicionamento profissional ou premium.
- São um **auto-indicador de geração por IA** sem revisão — mesmo que o cliente não saiba disso conscientemente, percebe que algo está "genérico".
- **Desviam atenção** de um design bem construído, poluindo a hierarquia visual.
- Não escalam bem: em diferentes dispositivos, sistemas operacionais e tamanhos de tela, emojis renderizam de maneiras distintas e incontroláveis.

---

## Substitutos Obrigatórios

Toda vez que a tentação de usar um emoji surgir, utilize uma das alternativas abaixo, dependendo do contexto:

### 1. Ícones SVG Inline ou via CDN (Preferido)
Use a biblioteca **Lucide Icons** (CDN pública, leve, SVG SVG nativo) para ícones de interface:

```html
<!-- Via CDN (para Tier 1 - single-file) -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>

<!-- Uso inline: -->
<i data-lucide="bread-slice" class="icon"></i>
<i data-lucide="phone" class="icon"></i>
<i data-lucide="map-pin" class="icon"></i>
<i data-lucide="star" class="icon"></i>
```

Alternativa: SVG inline direto no HTML (sem dependência externa). Preferível para Tier 1.

### 2. Caracteres Tipográficos Especiais
Para badges, separadores e elementos decorativos leves:

```
✦  →  símbolo decorativo neutro (estrela de 4 pontas) — uso aprovado com moderação
—  →  em dash para separadores elegantes
›  →  seta tipográfica em CTAs e links
```

> [!NOTE]
> O símbolo `✦` (U+2726) é um caracter tipográfico, não um emoji. Ele renderiza de forma consistente e neutra em todos os sistemas, sem as variações de cor e estilo dos emojis. É aprovado para uso como acento decorativo pontual.

### 3. Elementos Gráficos via CSS Puro
Para bullets, marcadores e destaques visuais:

```css
/* Bullet decorativo via CSS — sem emoji */
.list-item::before {
  content: '';
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--accent);
  margin-right: 0.6rem;
  vertical-align: middle;
}

/* Linha decorativa de destaque */
.section-tag::before {
  content: '';
  display: inline-block;
  width: 16px;
  height: 2px;
  background-color: currentColor;
  vertical-align: middle;
  margin-right: 0.5rem;
}
```

### 4. Texto Puro com Tipografia de Qualidade
Muitas vezes, a melhor substituição para um emoji é simplesmente **texto bem escrito e tipograficamente forte**. Um badge `"Fornadas Diárias"` não precisa do 🥖 — o texto já comunica.

---

## Regras Práticas de Aplicação

| Contexto | Proibido | Permitido |
|---|---|---|
| Títulos de seção (`h1`–`h4`) | `🥖 Panificação Artesanal` | `Panificação Artesanal` |
| Labels e badges | `🌾 Fornadas Diárias` | `Fornadas Diárias` (texto puro) ou ícone SVG |
| Bullets de lista | `• 🎂 Bolos personalizados` | `• Bolos personalizados` + `.menu-card-items li::before` CSS |
| Ícones de contato | `📍 Endereço` | Ícone Lucide `map-pin` SVG |
| CTAs e botões | `📲 Falar no WhatsApp` | `Falar no WhatsApp` (texto puro) |
| Seção About/Quote | `"... 🙏"` | Sem caractere final — o texto carrega |
| Top bar informativa | `📍 Av...` | `Av...` com ícone SVG ou texto puro |
| Ícones decorativos de card | `🎂` como visual âncora | Ícone SVG temático + fundo com `background-color` accent |

---

## Exceções Permitidas

Os emojis **só podem aparecer** em:

1. **Posts e stories para redes sociais** (Instagram, WhatsApp, Facebook) — contexto em que emojis são culturalmente esperados e funcionam como linguagem da plataforma.
2. **Chat de atendimento / mensagens de WhatsApp pré-formatadas** — contexto conversacional.
3. **Conteúdo explicitamente solicitado pelo cliente** com justificativa clara de posicionamento (ex: marca de produtos infantis com aprovação prévia do designer responsável).

---

## Resumo da Regra

> **Nenhum emoji em UI de sites e landing pages. Sempre.**
> Substitua com SVG icons, caracteres tipográficos neutros, elementos CSS ou texto puro bem escrito.
