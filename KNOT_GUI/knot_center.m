function coor = knot_center(coor)

coor = coor - mean(coor,2)*ones(1,length(coor));