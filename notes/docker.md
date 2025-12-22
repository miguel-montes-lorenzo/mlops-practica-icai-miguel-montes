# Notas docker

## intro

DVC es una herramienta de **control de versiones para datos y modelos**, similar a Git pero diseñada para control de datos de proyectos de data science y machine learning, en lugar de control de código.

Permite **rastrear datasets pesados, reproducir experimentos y gestionar pipelines** de forma eficiente y reproducible.

---

## instalación

...

---

## comandos básicos

login

```
docker login
```

construir una imagen

```
docker build -t <docker-username>/<image-name> .
```

ejecución de contenedor

```
docker run -p 5000:5000 <docker-username>/<image-name>
```
