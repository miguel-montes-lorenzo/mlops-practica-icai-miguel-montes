# Notas Google Cloud - GKE

## ¿Qué es Google Cloud?

Google Cloud Platform es la plataforma de computación en la nube de Google. Proporciona infraestructura y servicios para crear, ejecutar y escalar aplicaciones sin gestionar servidores físicos.

**¿Qué ofrece?**

- Infraestructura (IaaS): máquinas virtuales, redes, almacenamiento.
- Plataforma (PaaS): entornos gestionados para desplegar aplicaciones.
- Servicios gestionados: bases de datos, colas, analítica, ML.

## ¿Cómo funciona el sistema de cobro de Google Cloud?

Un billing account es un perfil creado dentro de Google Cloud para pagar el uso de los recursos de Google Cloud.

- Contiene un método de pago (tarjeta, domiciliación, etc.).
- Puede tener créditos promocionales asociados.

**Relación entre proyecto y billing account**

Toda la facturación real ocurre a nivel de billing account, no de proyecto.

- Cada proyecto debe estar asociado a una única billing account.
- Una billing account puede estar vinculada a varios proyectos.

**Modelo de cobro: pago por uso**

Google Cloud utiliza un modelo pay-as-you-go:

- No se paga por adelantado.
- Se factura exactamente lo que se consume.

El coste depende de:

- Tiempo de uso (CPU, memoria, nodos, horas de VM).
- Cantidad de datos almacenados.
- Tráfico de red.
- Número de peticiones o ejecuciones (en servicios serverless).

## ¿Qué es un proyecto?

Un projecto en Google Cloud es una agrupación de recursos necesarios para poner en marcha una aplicación. Todo proyecto está vinculado a un billing account.

Los recursos pueden ser cualquier tipo de herramienta u objeto cuya utilización o almacenamiento requiere una infraestructura técnica. Esta infraestructura técnica  cuesta dinero y que Google Cloud se encarga de proveer.

## ¿Qué es GKE?

GKE (Google Kubernetes Engine) es el servicio de Google Cloud para ejecutar Kubernetes sin tener que gestionarlo "a mano".

Google Cloud se encarga de:

- **Control plane (master)**: conjunto de componentes centrales de Kubernetes que representan y mantienen el estado lógico del clúster (API server, scheduler, etcd).
- **Actualizaciones**: procesos de cambio de versión y parcheo del propio software de Kubernetes que compone el clúster.
- **Alta disponibilidad**: propiedad arquitectónica por la cual el clúster sigue operativo aunque fallen algunos de sus componentes.
- **Seguridad básica**: configuración inicial de mecanismos de protección del clúster (identidad, certificados, aislamiento, políticas base).
- **Integración con IAM, Monitoring, Logs**: conexión nativa del clúster Kubernetes con los servicios de identidad y observabilidad de Google Cloud.

Tú te encargas de:

- **Contenedores**: imágenes autocontenidas que empaquetan una aplicación junto con su entorno de ejecución y dependencias.
- **Pods**: unidades mínimas de ejecución en Kubernetes, que agrupa uno o varios contenedores que comparten red y almacenamiento.
- **Deployments**: recursos declarativos de Kubernetes que describen el estado deseado de un conjunto de pods gestionados.
- **Servicios**: recursos de red de Kubernetes que definen una abstracción estable para acceder a un conjunto de pods.

## ENDPOINTS RELEVANTES

> La web de Google Cloud está organizada en secciones y subsecciones.
> Las secciones son:
>
> - Facturación
> - IAM y administración
> - Marketplace
> - Vertex AI
> - Compute Engine
> - Kubernetes Engine
> - Cloud Storage
> - Seguridad
> - BigQuery
> - Monitoring
> - Cloud Run
> - Red de VPC
> - Cloud SQL
>
> Para cambiar de sección hay que:
>
> 1. Entrar en Google Cloud Console
> ![](figures/GKE/google-cloud-main-menu.png)
> 2. Desplegar el menú de arriba a la izquierda:
> ![](figures/GKE/google-cloud-console.png)

Facturación:

<https://console.cloud.google.com/billing/>  # facturación/
<https://console.cloud.google.com/billing/014506-6496FA-320584>  # facturación/descripción general/
<https://console.cloud.google.com/billing/projects>  # facturación/descripción general/
<https://console.cloud.google.com/billing/014506-6496FA-320584/credits/all>  # facturación/<cuenta>/creditos/todos los creditos/

APIs y Servicios:

## Pasos seguidos en la práctica

Ejectuar lo siguiente en la consola de Google Cloud para poner en marcha el clúster:

```
export PROJECT_ID="digital-gearbox-476106-a0"  # proyect ID del proyecto ICAI2025
gcloud config set project $PROJECT_ID  # configura el proyecto activo por defecto del CLI gcloud

gcloud container clusters create mlops-gke-cluster \
  --zone us-central1-a  # indica en qué zona física de Google Cloud se despliega el clúster \
  --num-nodes 2  # crea un node pool inicial con 2 nodos \
  --service-account="icai2025@$PROJECT_ID.iam.gserviceaccount.com"  # indicar el uso de la cuenta de servicio son los permisos adecuados

gcloud container clusters create mlops-gke-cluster \
  --zone us-central1-a \
  --num-nodes 2 \
  --service-account="icai2025@${PROJECT_ID}.iam.gserviceaccount.com"
```

> Ejecutar lo siguiente para pararlo
>
> ```
> gcloud container clusters delete mlops-gke-cluster \
>   --zone us-central1-a \
>   --project digital-gearbox-476106-a0
> ```

Añadir los siguientes secretos a GitHub (**Settings** $\to$ **Secrets and variables** $\to$ **Actions**):

- **GCP_SA_KEY**: Contenido completo del JSON de la service account.

- **GCP_PROJECT_ID**: ID del proyecto (**digital-gearbox-476106-a0**)

- **GKE_CLUSTER**: Nombre dado al clúster (**mlops-gke-cluster**)

- **GKE_ZONE**: Zona horaria seleccionada para el alojamiento del clúster (**us-central1-a**)

---

Añadir este job al cml.yaml:

```
  deploy-to-gke:
    needs: train-and-report
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Authenticate to Google Cloud
        uses: google-github-actions/auth@v2
        with:
          credentials_json: '${{ secrets.GCP_SA_KEY }}'

      - name: Set up gcloud CLI and kubectl
        uses: google-github-actions/setup-gcloud@v2
        with:
          install_components: gke-gcloud-auth-plugin

      - name: Debug vars
        run: |
          echo "GKE_CLUSTER='${{ secrets.GKE_CLUSTER }}'"
          echo "GKE_ZONE='${{ secrets.GKE_ZONE }}'"
          echo "GCP_PROJECT_ID='${{ secrets.GCP_PROJECT_ID }}'"
          test -n "${{ secrets.GKE_ZONE }}" || (echo "GKE_ZONE está VACÍA" && exit 1)

      - name: Get GKE credentials
        run: |
          gcloud container clusters get-credentials \
            ${{ secrets.GKE_CLUSTER }} \
            --zone ${{ secrets.GKE_ZONE }} \
            --project ${{ secrets.GCP_PROJECT_ID }}

      - name: Configure Docker for GCR
        run: |
          gcloud auth configure-docker gcr.io --quiet

      - name: Build and Push API Docker Image
        run: |
          IMAGE="gcr.io/${{ secrets.GCP_PROJECT_ID }}/mlops-api:latest"
          docker build -t "$IMAGE" .
          docker push "$IMAGE"

      - name: Deploy API to GKE
        run: |
          kubectl apply -f k8s/api-deployment.yaml
          kubectl apply -f k8s/api-service.yaml
```

GitHub Actions solo ejecuta comandos en una máquina temporal; no decide permisos ni almacena la imagen. No estás haciendo un push a GitHub, sino a **Google Cloud** (`gcr.io`).

En este paso del workflow te autenticas **como una service account de Google Cloud**:

```yaml
- uses: google-github-actions/auth@v2
  with:
    credentials_json: '${{ secrets.GCP_SA_KEY }}'
```

Después, Docker se configura para usar esa identidad al hacer push a `gcr.io`:

```yaml
- name: Configure Docker for GCR
  run: gcloud auth configure-docker gcr.io --quiet
```

Cuando ejecutas:

```yaml
- name: Build and Push API Docker Image
  run: |
    docker build -t gcr.io/${{ secrets.GCP_PROJECT_ID }}/mlops-api:latest .
    docker push gcr.io/${{ secrets.GCP_PROJECT_ID }}/mlops-api:latest
```

Google Cloud comprueba los permisos de **esa service account**. Como `gcr.io` ahora está gestionado por **Artifact Registry**, si el repositorio no existe exige el permiso `artifactregistry.repositories.createOnPush`. Si la service account no lo tiene, el push falla.
