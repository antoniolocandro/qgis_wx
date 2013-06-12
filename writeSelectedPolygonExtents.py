def run_script(iface):
    """for use in QGIS script runner plugin.
    user selected polygons bounding coordinates extracted & output to file.
    
    ** very basic implementation. assumes user has selected 1 polygon, has permissions to write file &
    polygons are valid."""
    
    import os
    import sys

    # location to write text file with bounding coordinates
    # location will need to have read/write access
    vertexCoordFile = "/temp/WX_VERTEX.txt"
    bboxCoordFile = "/temp/WX_BBOX.txt"
    
    #TODO: validate polygon is selected. provide message with instructions.
    # must select polygon
    layer = iface.activeLayer()
    #TODO: allow multiple selection
    # only want the first feature
    feature = layer.selectedFeatures()[0]
    #TODO: add feature id. format as comma sep csv. add bounds description -> min east    
    # get bounding box as string
    vertex = feature.geometry().asPolygon()
    bbox = feature.geometry().boundingBox().toString()
    # write contents to file
    #TODO: add coordinate system used & total number features selected. timestamped utc

    # Writes the vertex coordinates of the polygon to a txt file
    f = open(vertexCoordFile,"w")
    for i in vertex:
      f.write(' '.join(str(s) for s in i) + '\n')
    f.close()

    #Writes the BBOX coordinates of the polygon to a txt file
    f = open(bboxCoordFile,"w")
    f.write(bbox)
    f.close()