# Mosaic Preview Plugin for QGIS

**Mosaic Preview** is a QGIS plugin that allows you to preview drone imagery quickly using embedded GPS metadata (EXIF), without requiring full photogrammetric processing.

It is ideal for rapid inspection, visual validation of flights, and pre-analysis in agricultural, environmental, or infrastructure monitoring contexts.

---

## 🚀 Features

- 📁 Select a folder with drone images
- 📌 Three preview modes:
  - **Footprint geometries only** (vector rectangles based on EXIF GPS)
  - **Individually georeferenced images** (quick raster layers)
  - **Quick mosaic preview** (assembled and shown as a single raster layer)
- 🧭 Automatically places images using GPS position
- 🛠️ Built with field use in mind — works offline and on lightweight machines

---

## 🧑‍🌾 Use Cases

- Agricultural inspections and sowing validation
- Rapid post-event assessment (floods, fire, wind)
- Forest and restoration monitoring
- Infrastructure construction tracking
- Drone flight quality checks on-site

---

## 📦 Installation

### Option 1 – From ZIP:
1. Download the plugin `.zip` from [Releases](https://github.com/alonzosan/mosaic-preview/releases)
2. In QGIS: go to `Plugins > Manage and Install Plugins > Install from ZIP`
3. Select the file and install.

### Option 2 – Clone manually:
```bash
git clone https://github.com/alonzosan/mosaic-preview.git
