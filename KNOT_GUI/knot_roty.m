function coor = knot_roty(coor,theta)

theta = pi()/180*theta;
rotmat = [cos(theta) 0 sin(theta); 0 1 0; -sin(theta) 0 cos(theta)];
coor = rotmat*coor;