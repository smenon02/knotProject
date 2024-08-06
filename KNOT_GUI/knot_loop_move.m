function coor = knot_loop_move(coor, intersections, intersection_number)

if isempty(intersections)
    disp('No moves possible for this projection. This is the unknot!')
end

n = find(intersections(:,9)==intersection_number);
a = intersections(n,6);
b = intersections(n,7);
m = find((intersections(:,6)==b).*(intersections(:,7)==a));

if (n < m) && ( sum(intersections(n:(m-1),8)==0) == 0 )
    disp('loop move type I')
    
    newpoint1 = intersections(n,1:3)';
    newpoint2 = [intersections(n,1) + rand()*0.001; 
                intersections(n,2) + rand()*0.001;
                intersections(n,4) + rand()*0.001];
            
    coor = [coor(:,1:a), newpoint1, newpoint2, coor(:,(b+1):end)];
    
elseif (m < n) && ( sum(intersections((m+1):n,8)==0) == 0 )
    disp('loop move type II')
    
    newpoint1 = [intersections(n,1); intersections(n,2); intersections(n,4)];
    newpoint2 = [intersections(n,1) + rand()*0.001; 
                intersections(n,2) + rand()*0.001;
                intersections(n,3) + rand()*0.001];
    
    coor = [coor(:,1:b), newpoint1, newpoint2, coor(:,(a+1):end)];
    
elseif (n < m) && ( sum(intersections(1:n,8)==0) == 0 ) && ( sum(intersections((m+1):end,8)==0) == 0 )
    disp('loop move type III')
    
    newpoint1 = intersections(n,1:3)';
    newpoint2 = [intersections(n,1) + rand()*0.001; 
                intersections(n,2) + rand()*0.001;
                intersections(n,4) + rand()*0.001];
            
    coor = [newpoint2, newpoint1, coor(:,(a+1):b)];
    
elseif (m < n) && ( sum(intersections(1:(m-1),8)==0) == 0 ) && ( sum(intersections(n:end,8)==0) == 0 )
    
    disp('loop move type IV')
    
    newpoint1 = intersections(n,1:3)';
    newpoint2 = [intersections(n,1) + rand()*0.001; 
                intersections(n,2) + rand()*0.001;
                intersections(n,4) + rand()*0.001];
            
    coor = [newpoint1, newpoint2, coor(:,(b+1):a)];
    
else
    disp('no loop move possible')
    
end