# Sistema de Análisis de Viabilidad de Productos para Ecommerce

Este proyecto consiste en el desarrollo de una API que permite analizar productos en función de variables comerciales como margen de ganancia, competencia, demanda y tiempos de envío.

## Funcionalidad actual

- Análisis de productos
- Cálculo de margen
- Generación de puntaje
- Clasificación de riesgo

## Endpoint disponible

### POST /product/analyze

Ejemplo de entrada:

```json
{
  "name": "Perfume Dior",
  "cost": 50,
  "price": 120,
  "competition": "high",
  "demand": "medium",
  "shipping_days": 10
}
```

Ejemplo de salida:

```json
{
  "name": "Perfume Dior",
  "margin": 70,
  "score": 75,
  "risk": "medium"
}
```
Este endpoint corresponde a la primera fase del sistema, enfocada en el análisis de productos.
## Tecnologías

- Python
- Flask
- JSON (intercambio de datos)
- Git y GitHub (control de versiones)