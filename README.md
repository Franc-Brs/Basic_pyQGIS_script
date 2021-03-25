# Basic_pyQGIS_script
Very simple script to apply an expression with QgsRasterCalculator to a Raster layer.

This script should be run in the QGIS Python Console. In this current version it will take a raster layer from the QGIS project, it will create a QgsRasterCalculator object and then it will write and load in the project a new raster file after applying a simple expression (the variable "expression" in the script).

#choose the target crs
crs_target=QgsCoordinateReferenceSystem("EPSG:3003")

#check id the input raster is valid
if rlayer.isValid():
    print("The raster is valid")
else:
    print("The raster is not valid")
    
##QgsRasterCalculatorEntry
entries = []
ras = QgsRasterCalculatorEntry()
ras.ref = 'ras@1'
ras.raster = rlayer
ras.bandNumber = 1
entries.append(ras)
