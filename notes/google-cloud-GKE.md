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

Billing:

<https://console.cloud.google.com/billing/>  # ver todas mis cuentas de cobro
<https://console.cloud.google.com/billing/014506-6496FA-320584>  # cuentas-de-cobro/"my-billing-account"  (es la única cuenta de cobro que tengo)
<https://console.cloud.google.com/billing/projects>  # cuentas-de-cobro/.../proyectos
<https://console.cloud.google.com/billing/credits/all>  # cuentas-de-cobro/.../vales-de-crédito  (aquí tengo el vale gratuito)
