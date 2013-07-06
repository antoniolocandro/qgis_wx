__author__ = 'ANTONIO'

coord = (12.037887489399837,-87.11819891815)
y_d=int(float(str(coord[0]).split('.')[0]))
y_m=int(round(float(('.'+str(coord[0]).split('.')[1]))*60,0))
x_d=int(float(str(coord[1]).split('.')[0]))
x_m=int(round(float(('.'+str(coord[1]).split('.')[1]))*60,0))

def y_deg (y_d):
    if y_d < 10:
        return '0'+str(y_d)
    else:
        return str(y_d)

def y_min (y_m):
    if y_m < 10:
        return '0'+str(y_m)+'N'
    else:
        return str(y_m)+'N'
def x_deg (x_d):
    if x_d < 10:
        return '00'+str(x_d)[1:]
    elif x_d >9 and x_d<100:
        return '0'+str(x_d)[1:]
    else:
        return str(x_d)[1:]

def x_min (x_m):
    if x_m < 10:
        return '0'+str(x_m)+'W'
    else:
        return str(x_m)+'W'

print y_deg(y_d)+y_min(y_m)+x_deg(x_d)+x_min(x_m)
