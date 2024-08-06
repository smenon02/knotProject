function coor = knot_rotz(coor,theta)

theta = pi()/180*theta;
rotmat = [cos(theta) -sin(theta) 0; sin(theta) cos(theta) 0; 0 0 1];
coor = rotmat*coor;