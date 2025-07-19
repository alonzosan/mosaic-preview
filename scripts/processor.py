
import os
from qgis.core import (
    QgsVectorLayer,
    QgsRasterLayer,
    QgsProject,
    QgsProcessingFeatureSourceDefinition,
)
from qgis import processing

def process_footprint(folder_path, logger):
    logger.append("Generating footprint polygons from drone images (JPG) in: " + folder_path)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg"):
            raster_path = os.path.join(folder_path, filename)
            layer_name = os.path.splitext(filename)[0]
            output_path = os.path.join(folder_path, f"{layer_name}_footprint.gpkg")
            try:
                processing.run("gdal:polygonize", {
                    'INPUT': raster_path,
                    'BAND': 1,
                    'FIELD': 'DN',
                    'EIGHT_CONNECTEDNESS': False,
                    'EXTRA': '',
                    'OUTPUT': output_path
                })
                logger.append(f"✓ Footprint created: {output_path}")
            except Exception as e:
                logger.append(f"✗ Error creating footprint for {filename}: {e}")
    logger.append("Footprint generation complete.")

def process_geoimage(folder_path, logger):
    logger.append("Loading georeferenced drone images (JPG) from: " + folder_path)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            raster_layer = QgsRasterLayer(image_path, filename)
            if raster_layer.isValid():
                QgsProject.instance().addMapLayer(raster_layer)
                logger.append(f"✓ Loaded: {filename}")
            else:
                logger.append(f"✗ Failed to load: {filename}")
    logger.append("GeoImage loading complete.")

def process_mosaic(folder_path, logger):
    logger.append("Creating mosaic from drone images (JPG) in: " + folder_path)
    inputs = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg"):
            inputs.append(os.path.join(folder_path, filename))
    if not inputs:
        logger.append("✗ No JPG images found to mosaic.")
        return
    output_path = os.path.join(folder_path, "mosaic.tif")
    try:
        processing.run("gdal:merge", {
            'INPUT': inputs,
            'PCT': False,
            'SEPARATE': False,
            'NODATA_INPUT': None,
            'NODATA_OUTPUT': None,
            'OPTIONS': '',
            'DATA_TYPE': 0,
            'OUTPUT': output_path
        })
        raster_layer = QgsRasterLayer(output_path, "Mosaic")
        if raster_layer.isValid():
            QgsProject.instance().addMapLayer(raster_layer)
            logger.append("✓ Mosaic created and added to QGIS.")
        else:
            logger.append("✗ Mosaic creation succeeded but layer is not valid.")
    except Exception as e:
        logger.append(f"✗ Error creating mosaic: {e}")
    logger.append("Mosaic creation complete.")
