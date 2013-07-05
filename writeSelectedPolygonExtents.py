def run_script(iface):
    """for use in QGIS script runner plugin.
    user selected polygons bounding coordinates extracted & output to file.
    
    ** very basic implementation. assumes user has selected 1 polygon, has permissions to write file &
    polygons are valid."""
    
    import os
    import sys

    # location to write text file with bounding coordinates
    # location will need to have read/write access
    #vertexCoordFile = "/temp/WX_VERTEX.txt"
    geojsonCoordFile = "/temp/WX_VERTEX.geojson"
    #bboxCoordFile = "/temp/WX_BBOX.txt"
    
    #TODO: validate polygon is selected. provide message with instructions.
    # must select polygon
    layer = iface.activeLayer()
    #TODO: allow multiple selection
    # only want the first feature
    feature = layer.selectedFeatures()[0]
    #TODO: add feature id. format as comma sep csv. add bounds description -> min east    

    # get polygon vertices
    vertex = feature.geometry().asPolygon()
    vlist=vertex[0]
    # test for coding only
    for i in vlist:
        print i
    print vlist

    #get BBOX coordinates - not needed for SIGMET generation but could be useful
    #bbox = feature.geometry().boundingBox().toString()
    
    # write contents to file
    #TODO: add coordinate system used & total number features selected. timestamped utc

    #Writes the vertex coordinates of the polygon to a txt file
    #f = open(vertexCoordFile,"w")
    #f.write("x,y"+'\n')
    #for i in vlist:
    #   vtxt = str(i[0])+","+str(i[1])
    #   f.write(vtxt+'\n')
    #   f.write((str(i[0])+","+str(i[1]))
    #f.close()
    
    #Writes the vertex coordinates of the polygon to a geojson file
    f = open(geojsonCoordFile,"w")
    f.write('{ "type": "FeatureCollection",'+'\n')
    f.write('  "features":['+'\n')
    f.write('    { "type": "Feature",'+'\n')
    f.write('         "properties":{},'+'\n')
    f.write('         "geometry": {'+'\n')
    f.write('           "type": "Polygon",'+'\n')
    f.write('             "coordinates": [['+'\n')
    f.write('         ')
    for i in vlist[:-1]:
        vtxt = '['+str(i[0])+', '+str(i[1])+'],'
        f.write(vtxt)
    f.write ('[')
    f.write (str(vlist[-1][0]))
    f.write (',')
    f.write (str(vlist[-1][1]))
    f.write(']')
    f.write('   ]]      ')
    f.write('  }}]}')
    f.close()


    #Writes the BBOX coordinates of the polygon to a txt file
    #f = open(bboxCoordFile,"w")
    #f.write(bbox)
    #f.close()