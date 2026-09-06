# Regra de CRO & UX para Alimentação, Gastronomia e Negócios Locais

## Diretriz Geral

Landing pages e sites para **padarias, confeitarias, restaurantes, lanchonetes, cafeterias e delivery local** possuem uma dinâmica de conversão única: **o visitante frequentemente acessa a página movido por apetite, urgência de compra ou necessidade imediata de contato**.

Qualquer obstáculo ou bloco denso de texto que fique entre a fome do cliente e a ação de pedir reduz drasticamente as taxas de conversão.

---

## 1. A Regra da Fome vs. História (Hierarquia Visual)

### ❌ O que NÃO fazer
- Colocar blocos longos de "Quem Somos", "Nossa História" ou "Missão/Visão" logo abaixo do Hero.
- Forçar o usuário faminto a rolar várias telas para conseguir ver o que a casa vende ou qual é o preço/cardápio.
- Utilizar apenas ilustrações abstratas ou ícones genéricos quando fotos reais dos alimentos poderiam despertar o apetite.

### ✅ O que FAZER (Obrigatório)
1. **Hero Sensorial e Direto:**
   - Headline com apelo sensorial (*"Pão quentinho saindo do forno"*, *"Bolos artesanais para o seu café"*).
   - Imagem de produto apetitosa e nítida.
   - Dois CTAs claros: **CTA Primário** (Pedir no WhatsApp / Fazer Pedido) e **CTA Secundário** (Ver Cardápio / Especialidades).
2. **Cardápio / Destaques do Forno Imediatamente após o Hero:**
   - Em páginas **Tier 1 (Essential)**, o bloco seguinte ao Hero deve ser obrigatoriamente as Especialidades/Cardápio com fotos reais, descrição apetitosa e botão de pedido.
   - Em páginas **Tier 2 (Professional)**, pode haver uma introdução de 1 frase institucional, seguida imediatamente por um menu interativo com abas de categorias e fotos.
3. **História / Tradição como Apoio de Confiança:**
   - A narrativa da família/fundadores e a tradição da casa devem ser condensadas (1 a 2 parágrafos curtos) e posicionadas **após** o cliente já ter conhecido os produtos.

---

## 2. CTAs de WhatsApp Segmentados por Produto

Para comércios locais que atendem pelo WhatsApp, **nunca use um link genérico sem mensagem pré-formatada**.

Cada card de produto ou categoria do cardápio deve enviar um texto contextualizado:

```html
<!-- Exemplo para Pães / Fornada -->
<a href="https://wa.me/551732491092?text=Ol%C3%A1%2C%20gostaria%20de%20saber%20os%20hor%C3%A1rios%20das%20fornadas%20de%20p%C3%A3o%20fresco%21" class="btn btn-primary">
  <span>Consultar Fornadas</span>
</a>

<!-- Exemplo para Bolos & Encomendas de Festa -->
<a href="https://wa.me/551732491092?text=Ol%C3%A1%2C%20gostaria%20de%20solicitar%20o%20cat%C3%A1logo%20de%20bolos%20para%20encomenda%21" class="btn btn-primary">
  <span>Pedir Catálogo de Bolos</span>
</a>

<!-- Exemplo para Tábuas de Frios e Salgados -->
<a href="https://wa.me/551732491092?text=Ol%C3%A1%2C%20gostaria%20de%20fazer%20um%20or%C3%A7amento%20de%20t%C3%A1bua%20de%20frios%20e%20salgados." class="btn btn-primary">
  <span>Orçar para Evento</span>
</a>
```

---

## 3. Microcopy Sensorial e Gatilhos de Apetite

A linguagem de gastronomia deve estimular os sentidos e responder às dúvidas imediatas do cliente:

| Tipo de Informação | Copy Corporativa Fria (Evitar) | Microcopy Sensorial & Persuasiva (Usar) |
|---|---|---|
| Pães | *"Comercializamos pães artesanais diversos"* | *"Pão francês de casca dourada e miolo macio, quentinho a toda hora"* |
| Confeitaria | *"Fabricamos bolos sob encomenda"* | *"Bolos fofinhos para o café e bolos confeitados com recheio generoso"* |
| Salgados | *"Salgados fritos e assados"* | *"Coxinhas crocantes e empadas que derretem na boca"* |
| Atendimento | *"Horário comercial"* | *"Aberto todos os dias a partir das 6h da manhã. Retire quentinho no balcão"* |
| Rapidez | *"Entre em contato"* | *"Peça no WhatsApp e retire pronto em poucos minutos"* |

---

## 4. Uso de Imagens Reais e Sem Emojis na UI

1. **Fotos Reais dos Produtos:**
   - Sempre priorizar fotos reais de pães, bolos, salgados e ambiente do próprio cliente.
   - Aplicar `object-fit: cover` e `aspect-ratio` adequado nos cards de produto para garantir uniformidade visual.
2. **Cumprimento Estrito da Regra `no-emoji-ui.md`:**
   - Nunca usar emojis como 🥖, 🎂, 🥐 ou ☕ nos títulos de seção, badges ou botões.
   - Usar ícones SVG (Lucide Icons ou inline) e caracteres tipográficos neutros (`✦`, `—`, `›`).

---

## 5. Matriz de Tiers para Gastronomia & Delivery Local

| Recurso | Tier 1 — Essential | Tier 2 — Professional | Tier 3 — Premium |
|---|---|---|---|
| **Hero** | Headline sensorial + Foto real/alta resolução + WhatsApp | Split Hero + Carrossel de Destaques + CTA duplo | Hero cinematográfico com vídeo/parallax |
| **Cardápio** | Grade direta de 4 a 6 especialidades com fotos | Menu interativo com abas de categorias e filtros | Cardápio interativo com modal de detalhes e cálculo |
| **Encomendas** | Botão direto para WhatsApp com mensagem prévia | Formulário com seleção de data, tamanho e recheio | Montador visual de encomendas (customizador) |
| **História** | Box de 1 a 2 parágrafos com foto da fachada/equipe | Seção completa com linha do tempo e manifesto | Storytelling editorial imersivo |
| **Prova Social** | Depoimentos resumidos em card | Avaliações do Google com fotos e estrelas SVG | Galeria de eventos e depoimentos em vídeo |
| **Localização** | Card com endereço, telefone e botão Google Maps | Mapa interativo integrado + rotas rápidas | Mapa interativo com cálculo de taxa de entrega/raio |

---

## 6. Padrões Técnicos e Anti-Regressão (PM-14 e PM-15)

1. **Prevenção de Quebra de Ícones em Botões (PM-14):**
   - Nunca utilizar caracteres de texto soltos (`›`, `>`, `→`) no final de botões de cardápio.
   - Sempre usar `<svg>` com `flex-shrink: 0` e configurar a classe `.card-cta-btn` com `display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; white-space: nowrap;`.
2. **Entrega 100% Autocontida em Tier 1 (PM-15):**
   - Em projetos Tier 1 Essential, embutir imagens otimizadas como `data:image/jpeg;base64` ou `data:image/webp;base64` direto no `index.html`. Isso garante portabilidade total, eliminando dependências de pastas e links quebrados ao abrir o arquivo isoladamente.

---

## 7. Roadmap de Recursos para Próximas Atualizações & Criações

Ao criar novas variações ou evoluir projetos de gastronomia existentes para Tiers superiores, priorizar a inclusão dos seguintes módulos:

1. **Filtro Dinâmico de Categorias por Abas (Tier 2):**
   - Abas com botões de alternância suave (*Pães*, *Bolos & Doces*, *Salgados*, *Frios & Queijos*) com contadores de itens e busca rápida.
2. **Calculadora de Encomendas para Festas (Tier 2/3):**
   - Widget interativo onde o cliente insere o número de convidados (ex: 20 pessoas) e o site calcula a estimativa de salgadinhos (cento), peso do bolo (kg) e bebidas, montando a mensagem completa pronta para envio no WhatsApp.
3. **Badge Dinâmico de Status em Tempo Real:**
   - Script JS leve que verifica a hora atual do visitante:
     - `6h às 19h`: Badge verde pulsante *"Aberto Agora — Saindo Fornada Quente"*.
     - `Fora do horário`: Badge informativo *"Fechado no momento — Faça sua encomenda para retirada amanhã"*.
4. **Modal Lightbox de Detalhes:**
   - Modal com zoom e lista detalhada de ingredientes/tamanhos ao clicar nas fotos de bolos confeitados e tábuas de frios especiais.

