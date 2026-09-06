---
name: logo_brand_extraction
description: >
  Ativado sempre que o usuário fornece a imagem de uma logo (PNG, JPG, WEBP, SVG)
  ou solicita a criação/adaptação de uma landing page ou site baseado em uma identidade
  visual pré-existente. Instrui o agente a extrair automaticamente a paleta de cores via
  script Python, analisar a tipografia e o tom da marca, e emitir o Briefing Visual Derivado.
---

# Logo & Brand Identity Extractor — Protocolo de Identidade Visual

> **Gatilho:** Esta skill é ativada quando o usuário envia uma imagem de logo ou solicita
> desenvolver uma landing page/site a partir de uma identidade visual já existente.

---

## 🎯 Objetivo

Garantir que a landing page gerada reflita 100% da identidade visual da marca do cliente,
mapeando automaticamente as cores da logo nos tokens de CSS do Design System Antigravity
e sugerindo a tipografia e o tom de voz mais alinhados antes de iniciar a escrita de código.

---

## 🛠️ Passo a Passo da Execução

### Passo 1 — Extração Automática de Cores (Script Python)

Sempre que um arquivo de logo for disponibilizado localmente ou nos artefatos da conversa,
execute o script utilitário de extração:

```bash
python .agents/skills/logo_brand_extraction/scripts/extract_colors.py <caminho_da_imagem_da_logo>
```

O script filtrará a transparência do fundo, agrupará as cores mais representativas e retornará um JSON contendo:
- **Cores HEX / RGB / HSL exatas**
- **Sugestão do Tema Base** (`Tema Claro Quente`, `Tema Escuro Premium`, `Tema Barbearia/Masculino`, `Tema Alimentação/Padaria`)
- **Mapeamento de Tokens CSS**: `--accent`, `--accent-hover`, `--accent-soft`, `--accent-secondary`, `--bg-primary`, `--text-dark`, `--border`

---

### Passo 2 — Análise Visual de Tipografia & Personalidade

Além das cores extraídas pelo script, realize a **análise visual da logo** cobrindo os seguintes eixos:

1. **Estilo Tipográfico da Logo**:
   - *Serifada (Elegante/Clássica)* → Sugerir `Cormorant Garamond` ou `Playfair Display`
   - *Sans-serif Geométrica (Moderna/Tech)* → Sugerir `Inter`, `DM Sans` ou `Outfit`
   - *Script/Handwritten (Artesanal/Humana)* → Sugerir `Great Vibes` ou `Alex Brush` (apenas para detalhes/badges)
   - *Bold/Slab (Robusta/Masculina)* → Sugerir `Cinzel` ou `Montserrat` (peso 700+)

2. **Personalidade & Tom de Voz da Marca**:
   - Definir se a estética é *Minimalista Clean*, *Dark Luxury*, *Orgânica/Sustentável*, *Corporativa Sória*, ou *Vibrante/Jovem*.

3. **Nicho Deduzido**:
   - Identificar o segmento provável (saúde, beleza, gastronomia, advocacia, tecnologia, etc.).

---

### Passo 3 — Emissão do Briefing Visual Derivado (Obrigatório)

Antes de gerar qualquer linha de código HTML/CSS, apresente ao usuário o **Briefing Visual Derivado** utilizando o template padronizado abaixo:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📸 BRIEFING VISUAL DERIVADO DA LOGO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Identidade: [Nome do Cliente / Negócio]
Nicho Deduzido: [Segmento]

🎨 PALETA DE CORES EXTRAÍDA (Script + Análise)
 • Cor Primária (--accent):        #[HEX] — [Nome descritivo]
 • Hover Botões (--accent-hover):  #[HEX] — [Tom ajustado]
 • Soft Accent (--accent-soft):   rgba(...)
 • Cor Secundária (--accent-sec): #[HEX] — [Nome descritivo]
 • Fundo Base (--bg-primary):     #[HEX] — [Nome descritivo]
 • Texto Principal (--text-dark): #[HEX] — [Nome descritivo]

✍️ TIPOGRAFIA SUGERIDA (Google Fonts)
 • Títulos (Serif / Display): [Nome da Fonte] (Estilo equivalente)
 • Corpo e UI (Sans-serif):   [Nome da Fonte] (Estilo equivalente)

🎭 PERSONALIDADE DA MARCA
 • Tom Visual: [Minimalista / Dark Luxury / Orgânico / Corporativo]
 • Tema Base do Design System: [Tema escolhido]

⚙️ TOKENS DE CSS PRONTOS PARA A LANDING PAGE
:root {
  --accent:           #[HEX];
  --accent-hover:     #[HEX];
  --accent-soft:      rgba(...);
  --accent-secondary: #[HEX];
  --bg-primary:       #[HEX];
  --bg-secondary:     #[HEX];
  --text-dark:        #[HEX];
  --text-muted:       #[HEX];
  --border:           rgba(...);
}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Passo 4 — Aprovação & Aplicação no Código

1. Aguarde a confirmação do usuário ou eventuais ajustes manuais nos HEX/Fontes.
2. Com a aprovação, integre os tokens CSS no bloco `<style>` da landing page.
3. Garanta o encadeamento com as demais skills:
   - **`landing_page_tier_selector`**: Enquadrar o Tier (1, 2 ou 3).
   - **`antigravity_dev_standards`**: Aplicar os padrões técnicos e bibliotecas do ecossistema.
   - **`responsive_qa`**: Executar a validação em 9 resoluções.

---

*Versão 1.0 | Antigravity Dev Standards | 2026-08*
