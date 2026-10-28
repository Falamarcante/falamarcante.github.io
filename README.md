# Fala Marcante — publicação

Publica no Instagram os posts de [@falamarcante](https://www.instagram.com/falamarcante/) no horário de cada um, pelo GitHub Actions.

- `queue.json`: a fila. O workflow `publish` marca cada post como publicado.
- `gh-pages`: a página do link da bio, o painel de status e a mídia que o Instagram baixa. Fica em https://falamarcante.github.io.
- `publisher/`, `shared/` e `.github/` são copiados de um repositório privado a cada lote semanal. Alterações feitas aqui são sobrescritas.

Painel de publicação: https://falamarcante.github.io/status.html
