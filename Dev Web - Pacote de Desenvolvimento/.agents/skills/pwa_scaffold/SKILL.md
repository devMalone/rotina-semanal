---
name: pwa_scaffold
description: >
  Automação e padronização para transformar qualquer aplicação web ou página HTML/JS
  em um Progressive Web App (PWA) instalável nativamente no iOS, Android e Desktop.
  Gera automaticamente o manifesto web, pacote de ícones de alta resolução (180, 192, 512, favicon),
  meta tags do Safari e Service Worker com persistência offline.
---

# PWA Scaffold & Mobile App Packager

> **Gatilho:** Esta skill é ativada sempre que o usuário solicita criar um "aplicativo", "app web",
> "sistema de ponto/rotina/contabilidade", transformar uma landing page em aplicativo instalável no celular,
> ou preparar uma página para ser salva na tela de início do smartphone.

---

## 🎯 Objetivo

Eliminar a fricção de empacotar aplicações web para smartphones e desktops. Em um único comando, o agente gera todos os ativos visuais (ícones nos tamanhos exigidos pelo Google Play/Chrome e Apple Store/iOS), o arquivo `manifest.json` com especificações maskable e o boilerplate de meta tags do Safari.

---

## 🛠️ Passo a Passo de Execução

### Passo 1 — Execução do Gerador de Assets

Execute o script Python fornecido passando os parâmetros da aplicação:

```bash
python .agents/skills/pwa_scaffold/scripts/generate_pwa_assets.py \
  --name "Nome da Aplicação" \
  --short-name "AppCurto" \
  --theme-color "#0f172a" \
  --bg-color "#0f172a" \
  --accent-color "#6366f1" \
  --symbol "A" \
  --output-dir "./"
```

*Se houver uma imagem de logo existente fornecida pelo usuário, passe o parâmetro `--logo "caminho/logo.png"` para centralizar o logotipo no ícone.*

Arquivos gerados automaticamente no diretório de destino:
- `manifest.json` (com diretivas `standalone`, `maskable` e `portrait-primary`)
- `apple-touch-icon.png` (180×180px)
- `icon-192.png` (192×192px)
- `icon-512.png` (512×512px)
- `favicon.png` (64×64px)

---

### Passo 2 — Injeção de Meta Tags no HTML (`<head>`)

Adicione o bloco obrigatório de cabeçalho no arquivo principal da aplicação (ex: `index.html`):

```html
<!-- Manifesto e Favicon -->
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" href="favicon.png">

<!-- Suporte iOS / Safari -->
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="AppCurto">

<!-- Cores de Tema do Sistema -->
<meta name="theme-color" content="#0f172a">
<meta name="color-scheme" content="dark light">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, maximum-scale=1.0, user-scalable=no">
```

---

### Passo 3 — Detecção e Captura de Instalação (PWA UX)

Insira a lógica de captura do evento `beforeinstallprompt` no script principal para oferecer uma instalação elegante ao usuário:

```javascript
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  // Impede o banner padrão do navegador
  e.preventDefault();
  deferredPrompt = e;
  
  // Exibe botão personalizado de instalação se não estiver em standalone
  const installBtn = document.getElementById('pwa-install-trigger');
  if (installBtn) {
    installBtn.style.display = 'inline-flex';
    installBtn.addEventListener('click', async () => {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`Resultado da instalação: ${outcome}`);
        deferredPrompt = null;
        installBtn.style.display = 'none';
      }
    });
  }
});
```

---

## 📋 Checklist de Qualidade do PWA:
- [ ] O `manifest.json` valida sem erros no Chrome DevTools (Application > Manifest).
- [ ] O ícone `apple-touch-icon.png` aparece perfeitamente na tela de início do iOS sem fundo transparente quebrado (Apple adiciona fundo preto se o PNG for transparente; o script resolve isso usando cor sólida).
- [ ] Ao abrir no celular pelo ícone da tela inicial, a barra de navegação do browser desaparece (`display: standalone`).
- [ ] A aplicação persiste dados no `localStorage` ou `IndexedDB` mesmo fechando o app ou reiniciando o aparelho.
