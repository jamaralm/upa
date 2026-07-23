// Configuração para o HTMX enviar o Token CSRF do Django nas requisições POST
document.body.addEventListener('htmx:configRequest', (event) => {
    let cookie = document.cookie.match(/csrftoken=([^;]+)/);
    if (cookie) {
        event.detail.headers['X-CSRFToken'] = cookie[1];
    }
});