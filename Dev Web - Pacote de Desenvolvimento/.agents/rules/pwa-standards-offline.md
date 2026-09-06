# ✦ Regra: Padrões PWA (Progressive Web Apps) e Resiliência Offline

> **Objetivo:** Garantir que todo sistema, utilitário ou aplicação web desenvolvida no ecossistema Antigravity seja instalável nativamente em smartphones (Android/iOS) e desktops, com suporte integral a funcionamento offline, persistência de dados local e ciclo de vida de PWA profissional.

---

## 📦 1. Manifesto da Aplicação (`manifest.json`)

O arquivo `manifest.json` é o contrato oficial entre o navegador e o sistema operacional. Ele DEVE estar localizado na raiz do projeto ou ser referenciado no `<head>`.

### 📄 Estrutura Obrigatória do Manifesto:
```json
{
  "name": "Nome Completo da Aplicação",
  "short_name": "NomeCurto",
  "description": "Descrição clara e concisa do propósito e das funcionalidades do aplicativo.",
  "start_url": "./index.html",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#0f172a",
  "theme_color": "#0f172a",
  "lang": "pt-BR",
  "categories": ["productivity", "utilities"],
  "icons": [
    {
      "src": "icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ]
}
```

> [!IMPORTANT]
> A propriedade `"purpose": "maskable"` é mandatória para evitar que o Android corte o ícone com bordas brancas feias em telas com ícones circulares ou esquilos (squircle).

---

## 🍏 2. Configurações Específicas para Apple iOS / Safari

O Safari no iOS não suporta todos os campos do manifesto de forma automática. Portanto, é **obrigatório** incluir as seguintes meta tags no `<head>` do HTML:

```html
<!-- Suporte Web App iOS -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="NomeCurto">
<link rel="apple-touch-icon" href="apple-touch-icon.png">

<!-- Cores dinâmicas para barra de status e tema -->
<meta name="theme-color" content="#0f172a">
<meta name="color-scheme" content="dark light">
```

---

## 💾 3. Arquitetura de Persistência Offline

Para sistemas que manipulam dados (rotinas, agendamentos, finanças, ponto, listas):

### 1. `localStorage` (Para Configurações e Estado Leve < 5MB):
- Ideal para preferências do usuário, flags de onboarding e payloads JSON leves serializados.
- **Sempre envolva em bloco `try/catch`** (em modo anônimo do Safari ou armazenamento cheio, `localStorage.setItem` pode lançar exceção).

```javascript
const StorageManager = {
  get(key, defaultValue = null) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : defaultValue;
    } catch (e) {
      console.warn(`[PWA Storage] Falha ao ler chave ${key}:`, e);
      return defaultValue;
    }
  },
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) {
      console.error(`[PWA Storage] Falha ao gravar chave ${key}:`, e);
      return false;
    }
  }
};
```

### 2. `IndexedDB` (Para Grandes Volumes de Dados e Mídias):
- Obrigatório para aplicações que armazenam listas com mais de centenas de registros, imagens em base64 ou logs extensos.
- Use a biblioteca leve `idb` ou a API nativa封装 com Promises.

---

## 🌐 4. Service Worker e Estratégias de Cache

Para garantir carregamento instantâneo e uso em aviões/túneis sem internet:

### Registro do Service Worker:
```javascript
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js')
      .then(reg => console.log('[PWA] Service Worker ativo:', reg.scope))
      .catch(err => console.warn('[PWA] Falha no Service Worker:', err));
  });
}
```

### Estratégia Recomendada para Single-File / Micro-Apps:
- **Cache-First para Assets Estáticos:** Ícones, fontes e bibliotecas CDN imutáveis.
- **Stale-While-Revalidate para o HTML Principal:** Carrega a versão em cache imediatamente e busca a atualização silenciosamente em background.

---

## 📲 5. Detecção de Modo Instalado (Standalone)

Permite ocultar banners de "Instalar aplicativo" quando o usuário já estiver executando o PWA em janela própria:

```javascript
function isPWAInstalled() {
  const isStandalone = window.matchMedia('(display-mode: standalone)').matches;
  const isIOSStandalone = ('standalone' in navigator) && (navigator.standalone === true);
  return isStandalone || isIOSStandalone;
}

if (isPWAInstalled()) {
  document.body.classList.add('is-pwa-standalone');
  // Ocultar chamadas de instalação
  const installBanner = document.getElementById('pwa-install-banner');
  if (installBanner) installBanner.style.display = 'none';
}
```

---

## 📋 Checklist de Aceitação para Agentes:
- [ ] `manifest.json` presente, válido e referenciado com link `rel="manifest"`.
- [ ] Ícones PNG em resoluções 192×192, 512×512 e `apple-touch-icon.png` (180×180).
- [ ] Configurações Apple iOS presentes no `<head>` (`apple-mobile-web-app-capable`).
- [ ] Leitura e escrita de armazenamento local encapsuladas com tratamento de erros.
- [ ] Aplicação funcional mesmo se desconectar a rede após o primeiro carregamento.
- [ ] Modo standalone verificado para não exibir banners redundantes.
