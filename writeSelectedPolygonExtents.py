def run_script(iface):
    """for use in QGIS script runner plugin.
    user selected polygons bounding coordinates extracted & output to file.
    
    ** very basic implementation. assumes user has selected 1 polygon, has permissions to write file &
    polygons are valid."""
    
    import os
    import sys
    import math

    # location to write text file with bounding coordinates
    # location will need to have read/write access
    vertexCoordFile = "/temp/WX_VERTEX.txt"
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
    # test for debug coding only
    #for i in vlist:
    #    print i
    # print vlist

    #get BBOX coordinates - not needed for SIGMET generation but could be useful
    #bbox = feature.geometry().boundingBox().toString()
    
    # write contents to file
    #TODO: add coordinate system used & total number features selected. timestamped utc

    #Writes the vertex coordinates of the polygon to a txt file
    f = open(vertexCoordFile,"w")
    s=''
    for i in vlist[:-1]:
        y_d=int(float(str(i[1]).split('.')[0]))
        y_m=int(round(float(('.'+str(i[1]).split('.')[1]))*60,0))
        x_d=int(float(str(i[0]).split('.')[0]))
        x_m=int(round(float(('.'+str(i[0]).split('.')[1]))*60,0))

        def y_deg (y_d):
            if abs(y_d) < 10:
                return '0'+str(y_d)
            else:
                return str(y_d)

        def y_min (y_m):
             if abs(y_m) < 10:
                return '0'+str(y_m)+'N'
             else:
                return str(y_m)+'N'

        def x_deg (x_d):
            if abs(x_d) < 10:
                return '00'+str(x_d)[1:]
            elif abs(x_d) >9 and abs(x_d)<100:
                return '0'+str(x_d)[1:]
            else:
                return str(x_d)[1:]

        def x_min (x_m):
            if abs(x_m) < 10:
                return '0'+str(x_m)+'W'
            else:
                return str(x_m)+'W'
        sigmetlist=(y_deg(y_d)+y_min(y_m)+x_deg(x_d)+x_min(x_m)+' - ')
        s+=sigmetlist
        f.write(sigmetlist)


    j= vlist[:-1][0]
    #print j
    y_df=int(float(str(j[1]).split('.')[0]))
    y_mf=int(round(float(('.'+str(j[1]).split('.')[1]))*60,0))
    x_df=int(float(str(j[0]).split('.')[0]))
    x_mf=int(round(float(('.'+str(j[0]).split('.')[1]))*60,0))

    def y_deg (y_df):
        if abs(y_df) < 10:
            return '0'+str(y_df)
        else:
            return str(y_df)

    def y_min (y_mf):
        if abs(y_mf) < 10:
            return '0'+str(y_mf)+'N'
        else:
            return str(y_mf)+'N'

    def x_deg (x_df):
         if abs(x_df) < 10:
            return '00'+str(x_df)[1:]
         elif abs(x_df) >9 and abs(x_df)<100:
            return '0'+str(x_df)[1:]
         else:
            return str(x_df)[1:]

    def x_minf (x_mf):
         if abs(x_mf) < 10:
             return '0'+str(x_mf)+'W'
         else:
             return str(x_mf)+'W'
    sigmetlistf=(y_deg(y_df)+y_min(y_mf)+x_deg(x_df)+x_min(x_mf))
    s+=sigmetlistf
    f.write(sigmetlistf)
    f.close()
    #print s
    #Writes the vertex coordinates of the polygon to a geojson file
    f = open(geojsonCoordFile,"w")
    f.write('{ "type": "FeatureCollection",'+'\n')
    f.write('  "features":['+'\n')
    f.write('    { "type": "Feature",'+'\n')
    f.write('         "properties":{"AUTHOR":"Antonio Locandro","SIGMET-COORD":"'+ s +'"},\n')
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