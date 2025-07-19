
Mosaic Preview Plugin for QGIS - Guía para desarrolladores
==========================================================

Directorio del plugin:
    C:/BUSINESS_INTELLIGENCE/TA/Proyectos/QGISPlugins/mosaic_preview

Directorio de plugins de QGIS (usuario):
    C:/Users/<usuario>/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins

Pasos para desarrollo y pruebas:

  1. Copia el directorio completo del plugin a la carpeta de plugins de QGIS.
  2. Compila los recursos con:
         pyrcc5 resources.qrc -o resources.py
  3. Compila la interfaz si modificas el archivo .ui:
         pyuic5 mosaic_preview_dialog_base.ui -o mosaic_preview_dialog_base.py
  4. Ejecuta los tests:
         make test
  5. Activa el plugin en QGIS desde el administrador de complementos.
  6. Personaliza el código en `mosaic_preview.py` y la interfaz en Qt Designer.
  7. Cambia el ícono por uno propio en icon.png si lo deseas.
  8. Usa el Makefile o pb_tool para automatizar tareas de build y despliegue.

Documentación de usuario y casos de uso:
  Consulta el archivo README.md para instrucciones detalladas, ejemplos y capturas de pantalla.

Enlaces útiles:
  - PyQGIS Developer Cookbook: https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/
  - Repositorio del plugin: https://github.com/alonzosan/mosaic-preview
  - Reporte de issues: https://github.com/alonzosan/mosaic-preview/issues

Contacto:
  Techno Analytics - info@bitechnoanalytics.com

(C) 2025 Techno Analytics
