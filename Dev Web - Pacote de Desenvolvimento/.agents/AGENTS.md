# Regras do Workspace — Antigravity/Empreender

## Padrões de Desenvolvimento Web

Antes de iniciar qualquer tarefa de desenvolvimento web (criação, correção ou
melhoria de landing pages, sites, PWAs, ferramentas ou componentes HTML/CSS/JS), o agente DEVE ler
e seguir os sete documentos em `docs/`:

- `docs/01-FTI-Ficha-Tecnica-Implementacao.md`
- `docs/02-Design-System.md`
- `docs/03-Biblioteca-Componentes.md`
- `docs/04-Guia-Experiencia-Premium.md`
- `docs/05-Sistema-Tiers.md`
- `docs/06-Guia-Comercial-Landing-Pages.md`
- `docs/07-Pesquisa-Aprofundada-Engenharia-Web-Moderna.md`

Os documentos definem o contrato técnico, visual e de experiência de todos os
projetos do ecossistema Antigravity. Suas especificações têm prioridade sobre
qualquer decisão automática do agente.

---

## Sistema de Tiers de Landing Pages

Antes de criar qualquer nova landing page ou projeto web comercial, o agente DEVE:
1. Perguntar ou confirmar qual Tier (Essential, Professional ou Premium) o usuário deseja para a página.
2. Aplicar rigorosamente a especificação do Tier escolhido definida em `docs/05-Sistema-Tiers.md`.
3. Não incluir recursos de Tiers superiores sem autorização prévia.

---

## Extração de Identidade por Logo

Sempre que o usuário fornecer a imagem de uma logo ou solicitar o desenvolvimento de um site/landing page a partir de uma marca existente, o agente DEVE:
1. Executar a skill `logo_brand_extraction` (usando o script Python `.agents/skills/logo_brand_extraction/scripts/extract_colors.py`).
2. Gerar o **Briefing Visual Derivado** e obter aprovação dos tokens de cor e tipografia antes de iniciar a codificação.

---

## Criação de PWAs e Aplicativos Mobile Instaláveis

Sempre que o usuário solicitar a criação de um aplicativo web, sistema de ponto/rotina/departamento pessoal, ou transformar uma página em app instalável no celular, o agente DEVE:
1. Executar a skill `pwa_scaffold` (`.agents/skills/pwa_scaffold/scripts/generate_pwa_assets.py`) para gerar automaticamente o pacote completo de ícones e o `manifest.json`.
2. Implementar as meta tags do Safari/iOS no `<head>` e garantir suporte a modo `standalone`.
3. Aplicar rigorosamente as regras `mobile-first-touch-ergonomics.md` e `pwa-standards-offline.md`.

---

## Regras Específicas de UI, Engenharia e CRO

O agente DEVE respeitar e aplicar integralmente as dez regras contidas em `.agents/rules/`:
1. `.agents/rules/no-emoji-ui.md`: **Proibido o uso de emojis** em títulos, labels, badges, botões e elementos de UI de landing pages. Usar ícones SVG (Lucide) ou tipografia neutra.
2. `.agents/rules/cro-gastronomia-alimentacao.md`: Em projetos de alimentação/gastronomia, priorizar o cardápio com fotos reais e botões de WhatsApp direto antes de textos longos institucionais.
3. `.agents/rules/showcase-conceitual-interativo.md`: Padrão para landing pages conceituais e interativas de alto impacto (*Landing Lab*), explorando mecanismos imersivos (flatlays, horizontal scroll, scroll-driven storytelling, quizzes dinâmicos).
4. `.agents/rules/evitar-padroes-genericos-ia.md`: **Proibido o uso de clichês visuais de IA** (quadradinhos arredondados com ícone de xícara/tesoura no logo, badges de pílula com sparkles/brilho no hero, barras de checkmark repetitivas). Substituir sempre por tipografia de marca real e direção de arte humana.
5. `.agents/rules/showroom-interativo-portfolio.md`: Padrão Showroom Interativo para o portfólio master (Live Cards, briefing de referências "♡ Salvar Estilo", recomendador dinâmico de 3 passos, visualizador cinematográfico e fechamento em 3 vias).
6. `.agents/rules/mobile-first-touch-ergonomics.md`: Ergonomia tátil mobile, touch targets mínimos de 44/48px, Safe Areas (`env(safe-area-inset)`), thumb zone e padrão bottom sheets.
7. `.agents/rules/pwa-standards-offline.md`: Padrão PWA completo (`manifest.json`, maskable icons, meta tags iOS, modo standalone, persistência local `localStorage`/`IndexedDB`).
8. `.agents/rules/modern-css-responsive-architecture.md`: Arquitetura CSS moderna com `100dvh` (banido 100vh puro no mobile), tipografia fluida via `clamp()`, grid intrínseco `auto-fit/minmax` e container queries.
9. `.agents/rules/accessible-forms-data-entry.md`: Formulários acessíveis, teclados virtuais por `inputmode`, prevenção de zoom forçado no iOS (font-size mínimo de 16px) e banimento total de `alert()`.
10. `.agents/rules/performance-core-web-vitals.md`: Limites de Core Web Vitals (LCP < 1.2s, INP < 50ms, CLS = 0), animações exclusivas na GPU (`transform`, `opacity`), preconnect e priorização LCP.
