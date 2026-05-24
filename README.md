# Sistema de Análisis y Optimización de Productos para Ecommerce

Aplicación web desarrollada para analizar la viabilidad comercial de productos para ecommerce mediante variables estratégicas como margen, competencia, demanda y tiempos de envío.

## Demo en producción

Aplicación desplegada en Railway:

https://ecommerce-analyzer-production.up.railway.app

---

## Objetivo

Evaluar productos potenciales para ecommerce y generar recomendaciones automáticas basadas en indicadores comerciales.

---

## Funcionalidades

- Análisis de margen de ganancia
- Evaluación de nivel de competencia
- Evaluación de demanda
- Consideración de tiempos de envío
- Generación automática de score
- Cálculo de nivel de riesgo
- Recomendación final del producto

---

## Tecnologías utilizadas

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Despliegue
- Railway

### Control de versiones
- Git
- GitHub

---

## Estructura del proyecto

```plaintext
ecommerce-analyzer/
│
├── app.py
├── models.py
├── services.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Instalación local

Clonar repositorio:

```bash
git clone https://github.com/Santiago-Marchena/Ecommerce-analyzer.git
```

Entrar al proyecto:

```bash
cd Ecommerce-analyzer
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python app.py
```

Abrir navegador:

```plaintext
http://127.0.0.1:5000
```

---

## Variables de análisis

| Variable | Descripción |
|----------|-------------|
| Costo | Valor de adquisición |
| Precio | Precio de venta |
| Competencia | Nivel competitivo |
| Demanda | Nivel esperado |
| Días envío | Tiempo logístico |

---

## Resultado generado

El sistema calcula:

- Margen
- Score
- Riesgo
- Recomendación comercial

---

## Autor

Santiago Marchena

Proyecto académico orientado al análisis de productos para ecommerce.