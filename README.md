

**Mosaic Preview** es un complemento para QGIS que permite previsualizar imágenes de dron en formato JPG usando metadatos GPS (EXIF), sin requerir procesamiento fotogramétrico completo.

El usuario debe seleccionar una carpeta que contenga imágenes de dron en formato JPG (.JPG). El plugin procesará únicamente archivos JPG.

Ideal para inspección rápida, validación visual de vuelos y pre-análisis en agricultura, medio ambiente, monitoreo de infraestructura y más.


## 🚀 Features

  - **Footprint geometries only** (vector rectangles based on EXIF GPS)
  - **Individually georeferenced images** (quick raster layers)
  - **Quick mosaic preview** (assembled and shown as a single raster layer)


## 🧑‍🌾 Casos de uso

- Inspección agrícola: Validación de siembra, conteo de plantas, monitoreo de cultivos.
- Evaluación rápida post-evento: Inundaciones, incendios, tormentas, desastres naturales.
- Monitoreo ambiental: Seguimiento de restauración ecológica, reforestación, erosión de suelos.
- Infraestructura: Supervisión de obras civiles, carreteras, líneas eléctricas, construcción.
- Control de calidad de vuelos: Verificación en campo de la cobertura y calidad de las imágenes antes de procesar ortomosaicos.
- Inspección de parcelas, lotes o zonas rurales con vuelos de dron.

## 📦 Installation


### Opción 1 – Desde ZIP:
1. Descarga el `.zip` desde [Releases](https://github.com/alonzosan/mosaic-preview/releases)
2. En QGIS: `Complementos > Administrar e instalar complementos > Instalar desde ZIP`
3. Selecciona el archivo y haz clic en instalar

### Opción 2 – Clonar manualmente:
```bash
git clone https://github.com/alonzosan/mosaic-preview.git

## 📝 Uso rápido

1. Abre QGIS y activa el complemento desde el menú de complementos
2. Haz clic en el botón "Mosaic Preview" o accede desde el menú
3. Selecciona la carpeta que contiene las imágenes de dron en formato JPG (.JPG)
4. Elige el modo de previsualización y haz clic en "Run"
5. Visualiza los resultados en el panel de capas y en la consola del plugin
