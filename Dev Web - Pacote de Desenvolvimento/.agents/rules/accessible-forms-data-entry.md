# ✦ Regra: Formulários Acessíveis e Entrada de Dados Eficiente

> **Objetivo:** Garantir que todo formulário, tela de cadastro ou entrada de dados ofereça experiência impecável em celulares e desktops, acionando o teclado virtual correto, evitando zooms indesejados no iOS Safari, banindo popups bloqueantes (`alert()`) e assegurando total acessibilidade semântica (WCAG / ABNT).

---

## ⌨️ 1. Teclados Virtuais Inteligentes via `inputmode`

Dispositivos móveis oferecem teclados virtuais especializados. Quando um campo pede um número e o navegador abre o teclado alfanumérico com letras minúsculas, o atrito de preenchimento aumenta exponencialmente.

### 🎯 Tabela de Mapeamento Obrigatório:
| Dado a Inserir | Atributo Obrigatório | Efeito no Smartphone |
| :--- | :--- | :--- |
| **Ponto / Horário** | `type="time"` | Roda de rolagem nativa de horas/minutos |
| **Data de Nascimento / Vencimento** | `type="date"` | Calendário nativo do sistema operacional |
| **CPF, CEP, Código 2FA, PIN** | `type="text" inputmode="numeric" pattern="[0-9]*"` | Teclado numérico gigante estilo discador |
| **Valores em Reais (R$), Salário, Preço** | `type="text" inputmode="decimal"` | Teclado numérico com vírgula/ponto decimal |
| **E-mail** | `type="email" autocomplete="email"` | Teclado com tecla `@` e `.com` no visor |
| **Telefone / WhatsApp** | `type="tel" autocomplete="tel"` | Teclado telefônico com `+`, `*`, `#` |
| **Links / URLs** | `type="url" autocomplete="url"` | Teclado com `/` e `.com` |

---

## 🔍 2. Prevenção do Zoom Automático Indesejado no iOS Safari

### ⚠️ O Bug do Zoom no iPhone:
Se um `<input>`, `<select>` ou `<textarea>` tiver uma propriedade `font-size` menor do que **16px**, o iOS Safari forçará um zoom abrupto em toda a página quando o campo receber foco, desalinhando o layout e quebrando a experiência visual.

### ✅ A Regra Mandatória:
```css
/* NUNCA defina font-size inferior a 16px em inputs para mobile */
input, 
select, 
textarea {
  font-size: 16px !important; /* Mínimo para neutralizar zoom forçado no iOS */
  min-height: 48px;            /* Ergonomia de toque recomendada */
  padding: 12px 14px;
  border-radius: 8px;
  box-sizing: border-box;
}
```

---

## 🏷️ 3. Associação Semântica e Rótulos (Labels Acessíveis)

### 🚫 Proibição: Placeholder como Rótulo Único
- **O erro:** Omitir `<label>` e colocar apenas `placeholder="Digite seu nome"`.
- **Por que é proibido:** Ao começar a digitar, o placeholder desaparece. Usuários com TDAH, idosos ou que se distraem esquecem o que aquele campo pedia. Além disso, leitores de tela têm dificuldade para anunciar o campo.

### ✅ Estrutura Semântica Correta:
```html
<div class="form-group">
  <label for="user-email" class="form-label">
    E-mail Corporativo <span class="required" aria-hidden="true">*</span>
  </label>
  <input 
    type="email" 
    id="user-email" 
    name="email" 
    class="form-input" 
    placeholder="seu.nome@empresa.com.br"
    autocomplete="email"
    required
    aria-required="true"
    aria-describedby="email-hint"
  >
  <span id="email-hint" class="form-hint">Enviaremos o comprovante para este endereço.</span>
</div>
```

---

## 🚫 4. Banimento Total do `alert()`, `prompt()` e `confirm()`

O uso de janelas modais nativas do navegador (`alert()`, `confirm()`, `prompt()`):
1. Trava a thread de execução do JavaScript.
2. Não pode ser estilizado (exibe a URL da página no topo de forma amadora).
3. Degrada a confiança do usuário final.

### ✅ Padrão Antigravity: Toasts e Mensagens de Validação Inline
Utilize mensagens integradas ao DOM ou banners flutuantes leves (toasts):

```javascript
// Função padrão de Notificação Não-Bloqueante (Toast)
function showToast(message, type = 'success') {
  const existingToast = document.querySelector('.app-toast');
  if (existingToast) existingToast.remove();

  const toast = document.createElement('div');
  toast.className = `app-toast toast-${type}`;
  toast.setAttribute('role', 'alert');
  toast.innerHTML = `
    <span class="toast-msg">${message}</span>
  `;
  document.body.appendChild(toast);

  // Animação de entrada e auto-remoção após 3.5s
  requestAnimationFrame(() => toast.classList.add('visible'));
  setTimeout(() => {
    toast.classList.remove('visible');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}
```

---

## 🎯 5. Anéis de Foco de Alto Contraste (`:focus-visible`)

Campos de formulário devem indicar com clareza cristalina qual elemento está ativo, tanto para navegação por teclado (Tab) quanto para toque.

```css
input:focus-visible, 
select:focus-visible, 
textarea:focus-visible,
button:focus-visible {
  outline: 2px solid var(--accent-primary, #6366f1);
  outline-offset: 2px;
  box-shadow: 0 0 0 4px var(--accent-glow, rgba(99, 102, 241, 0.25));
}
```

---

## 📋 Checklist de Aceitação para Agentes:
- [ ] Todo input possui `font-size: 16px` no mobile para impedir zoom no iPhone.
- [ ] Todos os campos numéricos, telefones e e-mails usam o `inputmode` e `autocomplete` adequados.
- [ ] Todo campo possui um `<label for="...">` devidamente associado.
- [ ] Não há nenhuma ocorrência de `window.alert()`, `window.confirm()` ou `window.prompt()`.
- [ ] Estados de validação exibem feedback visual e mensagem textual acessível.
- [ ] Altura mínima dos inputs é de pelo menos 44px (ideal 48px).
