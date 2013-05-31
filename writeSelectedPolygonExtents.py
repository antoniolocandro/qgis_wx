def run_script(iface):
    """for use in QGIS script runner plugin.
    user selected polygons bounding coordinates extracted & output to file.
    
    ** very basic implementation. assumes user has selected 1 polygon, has permissions to write file &
    polygons are valid."""
    
    import os
    import sys
    
    outFile = "/Users/drownedfrog/Projects/wxHondrusas_antinio/outputPolygonExtents.txt"
    
    # must select polygon
    layer = iface.activeLayer()
    # only want the first feature
    feature = layer.selectedFeatures()[0]
    # get bounding box as string
    bbox = feature.geometry().boundingBox().toString()
    
    # write contents to file
    f = open(outFile,"w")
    f.write(bbox)
    f.close()

