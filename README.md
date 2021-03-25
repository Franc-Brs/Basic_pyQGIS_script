# Basic_pyQGIS_script
Very simple script to apply an expression with QgsRasterCalculator to a Raster layer.

This script should be run in the QGIS Python Console. In this current version it will take a raster layer from the QGIS project, it will create a QgsRasterCalculator object and then it will write and load in the project a new raster file after applying a simple expression (the variable `expression` in the script).

The input raster is taken from the QGIS project, you should replace  `dtm_veneto` with the desired input raster layer name in: 

`rlayer = QgsProject.instance().mapLayersByName('dtm_veneto')[0]` 

By the way you can try with the same raster layer that I used and that you can find on this repository.
If you prefer you can load a raster file from the desired directory by uncommenting and replacing the desired file path in here (of course you also have to cancel the line where you get the raster from the QGIS project): 

`#rlayer = QgsRasterLayer("your/input/raster/path/fileName")`

The output raster is called `ideal_h.tif` by default and it is saved in the working directory, you can change this behavior by changing the `output_raster_path` passing the desired path and name. 

You will change the target crs by changing this variable:

`crs_target=QgsCoordinateReferenceSystem("EPSG:3003")`
