# 05 — Sistema de Tiers de Landing Pages
## Matriz Comercial & Técnica de Produtos Web

Versão 1.0 — 2026-08

---

## 1. Visão Geral & Filosofia

O Sistema de Tiers categoriza as landing pages desenvolvidas no ecossistema Antigravity não por simples "quantidade de seções", mas pelo **nível de estratégia, design, UX, motion design e execução técnica**.

Esse sistema serve a um duplo propósito:
1. **Comercial (Interno)**: Estrutura pacotes de solução com faixas de investimento e prazos indicativos para precificação e briefing.
2. **Técnico (Agente de IA)**: Funciona como um **contrato de escopo** que limita e orienta a complexidade técnica, impedindo "over-engineering" ou inclusão de características de tiers superiores sem autorização.

> [!IMPORTANT]
> **REGRA COMERCIAL FUNDAMENTAL**
> Os valores e prazos apresentados neste documento são **referências internas de planejamento**. O agente de IA ou desenvolvedor **NUNCA deve apresentar automaticamente estes valores ao cliente como orçamento definitivo**. Antes de fechar valor ou prazo, deve ser feito o enquadramento do briefing, verificando dependências e extras solicitados.

---

## 2. Matriz de Classificação de Projetos (Pontuação)

Para evitar que o cliente contrate um Tier 1 esperando um projeto de alta complexidade, utilize a seguinte pontuação de enquadramento:

| Requisito do Projeto | Pontos |
|---|---|
| Atribuição de Seções: até 6 seções | 1 pt |
| Atribuição de Seções: 7 a 10 seções | 2 pts |
| Atribuição de Seções: 11+ seções | 3 pts |
| Design: Layout baseado em tokens/componentes padrão | 1 pt |
| Design: Direção de arte personalizada e temática | 2 pts |
| Design: Visual cinematográfico / Layout editorial exclusivo | 3 pts |
| Motion: Apenas hovers e transições suaves nativas | 1 pt |
| Motion: Scroll animations (AOS/GSAP básico), microinterações | 2 pts |
| Motion: Scrolltelling, canvas/parallax complexo, transições cinematográficas | 3 pts |
| Integrações: Apenas WhatsApp e link de agendamento | 1 pt |
| Integrações: Formulários com webhook, CRM ou filtros dinâmicos | 2 pts |
| Integrações: APIs externas customizadas, banco de dados ou calculadoras | 3 pts |
| Copywriting & Conteúdo: Fornecido integralmente pelo cliente | 1 pt |
| Copywriting & Conteúdo: Revisão e adaptação estratégica | 2 pts |
| Copywriting & Conteúdo: Criação do zero com pesquisa de mercado | 3 pts |

### Enquadramento de Tier por Pontuação Total:
- **5 a 8 Pontos**: **TIER 1 — ESSENTIAL**
- **9 a 13 Pontos**: **TIER 2 — PROFESSIONAL**
- **14 a 18 Pontos**: **TIER 3 — PREMIUM**

*Se um projeto solicitar mais de 18 pontos ou customizações fora da matriz, deve ser tratado com escopo sob medida via Add-ons.*

---

## 3. Especificação dos Tiers

### 📊 Tabela Comparativa de Tiers

| Critério | Tier 1 — Essential | Tier 2 — Professional | Tier 3 — Premium |
|---|---|---|---|
| **Estratégia** | Básica / Presença Profissional | Estratégica / Foco em Conversão | Avançada / Posicionamento de Marca |
| **Design & Layout** | Clean / Tokens Base | Personalizado / Direção Editorial | Exclusivo / Cinematográfico |
| **UX & Componentes** | Essencial (Navbar, Hero, CTA) | Otimizado (Accordion, Galeria Tab) | Avançado (Lightbox, Scrolltelling) |
| **Motion & Animações** | Suave (Transitions CSS básicas) | Intermediário (Fade Reveal, Keyframes) | Cinematográfico (GSAP, Parallax) |
| **Seções Recomendadas** | 5 a 7 seções | 8 a 11 seções | 10 a 15 seções |
| **SEO & Meta Tags** | Básico (Title, Meta, Favicon) | Completo (OG Tags, Meta Social) | Técnico (Schema.org, JSON-LD) |
| **Acessibilidade** | Semântica HTML5 | WCAG 2.2 Nível A | WCAG 2.2 Nível AA |
| **Faixa Interna Indicativa** | R$ 800 — R$ 1.500 | R$ 1.800 — R$ 3.200 | R$ 3.800 — R$ 7.500+ |
| **Prazo Estimado Interno** | 2 a 4 dias úteis | 5 a 8 dias úteis | 9 a 15 dias úteis |

---

### TIER 1 — ESSENTIAL

**Posicionamento Comercial**: Solução rápida e profissional para pequenos negócios ou profissionais liberais que precisam iniciar sua presença digital com alta performance e credibilidade.

- **Faixa de Investimento Interna**: R$ 800 a R$ 1.500
- **Prazo Estimado Interno**: 2 a 4 dias úteis
- **Complexidade**: Baixa

#### Escopo & Seções Típicas (5 a 7 seções)
1. **Hero Section**: Headline forte, sub-headline, imagem/video de fundo básico, botão CTA principal.
2. **Sobre / Apresentação**: Resumo da empresa ou profissional.
3. **Serviços / Produtos**: Cards explicativos com ícones (Lucide Icons).
4. **Benefícios / Diferenciais**: Lista com checkmarks ou cards com hover leve.
5. **Galeria Simples**: Grid de fotos com layout responsivo limpo.
6. **CTA Final / Contato**: Chamada direta para WhatsApp.
7. **Footer**: Direitos autorais, redes sociais e links básicos.

#### O que INCLUI:
- Arquitetura Single-File (HTML + CSS + JS em `index.html`)
- Responsividade total Mobile-First (360px a 1920px)
- Otimização de imagens (WebP) e carregamento rápido
- Integração direta de WhatsApp (Link formatado)
- SEO Básico (Meta title, description, favicon, OpenGraph simples)
- Componentes padronizados do Design System

#### O que NÃO INCLUI:
- Motion avançado ou bibliotecas pesadas de animação
- Galerias interativas com filtros dinâmicos ou Lightbox
- Animações de scroll complexas
- Formulação de texto (copywriting) do zero
- Produção ou manipulação avançada de mídia/vídeos

---

### TIER 2 — PROFESSIONAL

**Posicionamento Comercial**: Para empresas consolidadas ou prestadores de serviço que buscam diferenciar-se da concorrência, aumentar a taxa de conversão e transmitir autoridade visual.

- **Faixa de Investimento Interna**: R$ 1.800 a R$ 3.200
- **Prazo Estimado Interno**: 5 a 8 dias úteis
- **Complexidade**: Média

#### Escopo & Seções Típicas (8 a 11 seções)
- **Tudo do Tier 1 +**:
1. **Hero Section Elaborado**: Badge com animação pulse, títulos fluidos, background com overlay gradiente.
2. **Como Funciona / Passo a Passo**: Processo explicativo em linha do tempo ou cards numéricos.
3. **Galeria Avançada**: Sistema de abas (Filtros por categoria) ou carousel simples.
4. **Depoimentos / Prova Social**: Cards de avaliação com estrelas e fotos de clientes.
5. **FAQ Accordion**: Dúvidas frequentes com expandir/recolher interativo.
6. **Formulário de Contato / Reserva**: Validação JS e máscara de telefone, pronto para integração via Webhook/WhatsApp.
7. **Banner Flutuante / Floating WA**: Botão flutuante com indicador de status online.

#### O que INCLUI:
- Tudo do Tier 1
- Direção de arte personalizada alinhada à identidade da marca
- Motion Design Intermediário: Animações de entrada no scroll (`IntersectionObserver`), efeitos hover refinados, microinterações
- Galerias com filtragem dinâmica por categoria
- SEO Completo (OpenGraph rico para WhatsApp/Instagram, Twitter Cards, Meta Robots)
- Script de Validação de Formulário avançado
- Smooth Scroll nativo e navegação responsiva com drawer flutuante

#### O que NÃO INCLUI:
- Transições de página 3D ou Canvas WebGL
- Animações complexas acionadas por posição exata de scroll (scrolltelling)
- Integrações complexas com múltiplos sistemas/CRMs de terceiros

---

### TIER 3 — PREMIUM

**Posicionamento Comercial**: Produto de alto padrão para marcas premium, estúdios de fotografia fine art, clínicas de estética de luxo e marcas que exigem uma experiência digital cinematográfica e inesquecível.

- **Faixa de Investimento Interna**: R$ 3.800 a R$ 7.500+
- **Prazo Estimado Interno**: 9 a 15 dias úteis
- **Complexidade**: Alta

#### Escopo & Seções Típicas (10 a 15 seções)
- **Tudo do Tier 2 +**:
1. **Hero Cinematográfico**: Vídeo de alta definição com fallback, tipografia editorial gigante, parallax controlado.
2. **Storytelling / Manifesto**: Seção editorial imersiva com tipografia de destaque.
3. **Galeria Sofisticada + Lightbox Premium**: Zoom de imagem em alta definição, controle via teclado/swipe e contador.
4. **Interactive Showcase / Comparador**: Sliders interativos (antes/depois ou especificações técnicas).
5. **Diferenciais Exclusivos**: Cards com efeito glassmorphism e sombras projetadas personalizadas.
6. **Seção de Credenciais / Mídia**: Logos de imprensa ou certificações com animação contínua.
7. **Formulário Multi-Step ou Agendamento**: Experiência fluida por etapas.
8. **Footer Editorial**: Design expandido com assinatura visual da marca e mapa/localização styled.

#### O que INCLUI:
- Tudo do Tier 2
- Direção de arte exclusiva e única (nível Awwwards / Editorial)
- Animações Cinematográficas & Scrolltelling (GSAP / ScrollTrigger / Parallax sutil)
- Lightbox customizado em Modal com suporte a gestos e transições fluidas
- Performance Extrema (Preload de fontes críticas, lazy loading inteligente, otimização de imagens LCP < 1.2s)
- SEO Técnico com Dados Estruturados (`Schema.org` / JSON-LD para `LocalBusiness` ou `Product`)
- Acessibilidade WCAG 2.2 AA (Navegação via teclado completa, contraste verificado, atributos ARIA)

---

## 4. Sistema de Add-ons & Extras

Para manter o escopo dos Tiers padronizado sem limitar a receita, utilize os add-ons para expansão:

| Add-on / Serviço Adicional | Faixa Indicativa Interna | Descrição |
|---|---|---|
| **Copywriting Estratégico** | + R$ 400 — R$ 900 | Criação completa de textos focados em conversão e VSL script |
| **Tratamento / Otimização Visual** | + R$ 300 — R$ 600 | Edição de imagens, remoção de fundo e padronização cromática |
| **Página Adicional (Ex: Obrigado, Termos)** | + R$ 250 — R$ 500 | Página secundária com o mesmo padrão visual do site |
| **Integração Externa (Webhook / CRM / RD)** | + R$ 300 — R$ 700 | Envio de formulário direto para CRM ou disparador de e-mail |
| **Blog / CMS Leve (Local ou Strapi/Decap)** | + R$ 800 — R$ 1.500 | Sistema para publicação de artigos de conteúdo/SEO |
| **SEO Local Avançado (Google Meu Negócio)** | + R$ 400 — R$ 800 | Otimização do perfil do Google + geolocalização no site |
| **Manutenção & Hospedagem Mensal** | R$ 100 — R$ 300 / mês | Atualizações, backups, monitoramento de uptime e SSL |

---

## 5. Instrução de Execução para Agentes de IA

Ao criar ou modificar landing pages neste workspace, o agente DEVE:

1. **Perguntar/Confirmar o Tier antes da criação**: Nunca assumir o escopo sem definir se o projeto é Tier 1 (Essential), Tier 2 (Professional) ou Tier 3 (Premium).
2. **Inserir Metadado no HTML**: Todo arquivo `index.html` deve conter o metadado no cabeçalho:
   ```html
   <!-- 
     Antigravity Dev Standards
     Project Tier: TIER 2 - PROFESSIONAL
     Specification: 05-Sistema-Tiers.md
   -->
   ```
3. **Respeitar o Teto do Tier**:
   - Se o projeto for Tier 1, **NÃO** incluir plugins de scrolltelling ou galerias complexas com lightbox.
   - Se o projeto for Tier 2, manter as animações focadas em CSS/IntersectionObserver sem sobrecarregar com scripts externos pesados.
   - Se o projeto for Tier 3, aplicar todos os refinamentos de acessibilidade, SEO técnico (Schema.org) e microinterações avançadas.

---

*Antigravity Dev Standards — 05-Sistema-Tiers v1.0 | 2026-08*
