function coor = knot_rotx(coor,theta)

theta = pi()/180*theta;
rotmat = [1 0 0; 0 cos(theta) -sin(theta); 0 sin(theta) cos(theta)];
coor = rotmat*coor;