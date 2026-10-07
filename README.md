# ci-cd-python

API Flask de ejemplo (servida con gunicorn) desplegada automáticamente por Jenkins (ver repo `ci-cd-template`).

| Endpoint | Respuesta |
|---|---|
| `GET /` | `python-example OK` |
| `GET /books` | JSON con 3 libros |

Puertos: host **8082** → contenedor **5000**.

## Ejecutar local

```bash
docker build -t python-example:test .
docker run -d --rm --name python-example-test -p 8082:5000 python-example:test
curl http://localhost:8082/books
docker stop python-example-test
```

## Despliegue

Un push a `main` dispara el job de Jenkins (`pollSCM`, ~1–2 min): build → deploy → smoke check.
