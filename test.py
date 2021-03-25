path=os.getcwd()
output_raster_path = os.path.join(path, "ideal_h.tif")

##if you want to take the raster froma different path uncomment the next line (and give the right path) and comment the one below
#rlayer = QgsRasterLayer("your/input/raster/path/fileName")
rlayer = QgsProject.instance().mapLayersByName('dtm_veneto')[0]

##choose the target crs
crs_target = QgsCoordinateReferenceSystem("EPSG:3003")

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

##QgsRasterCalculator
expression = '\"ras@1\" >150'
calculation = QgsRasterCalculator( expression, output_raster_path,'GTiff', rlayer.extent(), crs_target,rlayer.width(), \
rlayer.height(), entries, QgsCoordinateTransformContext() ) 

calculation.processCalculation()

##add the output raster to Qgis in the 
fin_res = iface.addRasterLayer(output_raster_path,"ideal_h","gdal") 
