# Notas MLflow

## intro

MLflow es una plataforma open-source que busca estandarizar el proceso de análisis y refinamiento de modelos machine learning proporcionando una interfaz unificada para registrar, versionar y desplegar modelos creados con diferentes lenguajes y frameworks. Incluye herramientas para el seguimiento de experimentos, el empaquetado reproducible de código y la gestión de modelos.

MLflow crea del directorio **`mlruns/`** en la raiz del *workspace*. Este es el directorio donde MLflow guarda localmente por defecto todo el tracking: experimentos, runs, métricas, parámetros, artefactos y modelos.

`mlruns/` contiene estructuras de archivos de esta forma:

```bash
mlruns/
 ├─ 0/
 │   ├─ meta.yaml
 │   └─ ...
 ├─ 1/
 │   ├─ meta.yaml
 │   ├─ <run_id_1>/
 │   │     ├─ metrics/
 │   │     ├─ params/
 │   │     ├─ artifacts/
 │   │     └─ meta.yaml
 │   ├─ <run_id_2>/
 │   │     ├─ ...
 └── ...
```

donde:

* **Los números (0, 1, 2, …)** identifican experimentos.
* **Cada experimento** contiene:

  * un `meta.yaml`
  * una carpeta por cada *run* ejecutado.
* **Cada run** contiene:

  * `metrics/` → valores registrados (`train_loss`, `accuracy`, etc.)
  * `params/` → hiperparámetros (`lr`, `batch_size`, …)
  * `artifacts/` → cualquier archivo que loguees (modelos, figuras, checkpoints)
  * `meta.yaml` → información del run (ID, fechas, tags, etc.)

> [!Note]
> `mlruns/` suele añadirse a `.gitignore` porque es un directorio grande, generado automáticamente y dependiente del entorno.

---

## instalación

MLflow tiene APIs oficiales para los siguientes lenguajes:

* Python
* R
* Java
* Scala

Dentro del ecosistema Python puede instalarse directamente en un entorno virtual a través de pip:

```bash
pip install mlflow
```

Una vez instalado, mlflow permite activar una UI web (que se aloja localmente, por lo general en: ) para analizar los datos asociados a cada entrenamiento registrado. La interfaz se activa con el comando:

```bash
mlflow ui
```

---

## API Python

---
