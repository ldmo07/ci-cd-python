# CLAUDE.md

Repo independiente (`github.com/ldmo07/ci-cd-python`), clonado dentro de `CI-CD/` pero ignorado por el repo raíz. Se commitea y pushea desde esta carpeta.

- App: Flask en `app.py` (rutas `/` y `/books`), dependencias fijadas en `requirements.txt`, corre con `gunicorn -b 0.0.0.0:5000 app:app`. No hay tests; la verificación es `docker build` + `curl`. `python` no está instalado en el host: probar siempre vía Docker.
- `Jenkinsfile`: copia de `templates/Jenkinsfile.template` del repo raíz. Solo editar `APP_NAME` (`python-example`), `HOST_PORT` (`8082`), `CONTAINER_PORT` (`5000`).
- Push a `main` => Jenkins despliega en ~1–2 min. Un build roto conserva el contenedor anterior.
- `.gitattributes` fuerza LF; CRLF en el `Jenkinsfile` rompe el pipeline.
- No agregar GitHub Actions: solo Jenkins hace CI/CD.
