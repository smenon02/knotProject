function intersections = knot_draw(coor, number_nodes, number_intersections)
tic
xcoor = coor(1,:);
ycoor = coor(2,:);
zcoor = coor(3,:);

natoms = length(xcoor);

xcoor = [xcoor, xcoor(1)];
ycoor = [ycoor, ycoor(1)];
zcoor = [zcoor, zcoor(1)];


hold off
%figure(1)
plot(xcoor, ycoor,'k','Linewidth',1.5)
hold on
plot([xcoor(end-1), xcoor(end)], [ycoor(end-1), ycoor(end)],'--m','Linewidth',1.5)

L1 = [xcoor; ycoor];
[P,a,b] = InterX(L1); % Pairs of lines a and b cross. Crossing points P.

scatter(P(1,:),P(2,:),80,[1 1 1],'filled')

clines = [a',b];
%clines = clines(clines(:,1) < clines(:,2), :);

% plot is just a sketch. Covers and draws over intersections.
% gives a good sense of what the knot looks like for relatively 
% small proteins

intersections = [];

w = 0.5;

for i = 1:size(clines,1)
    x1a = xcoor(clines(i,1));
    y1a = ycoor(clines(i,1));
    z1a = zcoor(clines(i,1));
    x2a = xcoor(clines(i,1)+1);
    y2a = ycoor(clines(i,1)+1);
    z2a = zcoor(clines(i,1)+1);
    x1b = xcoor(clines(i,2));
    y1b = ycoor(clines(i,2));
    z1b = zcoor(clines(i,2));
    x2b = xcoor(clines(i,2)+1);
    y2b = ycoor(clines(i,2)+1);
    z2b = zcoor(clines(i,2)+1);
    
    p1 = InterX([x1a x2a; y1a y2a],[x1b x2b; y1b y2b]);
    xc = p1(1);
    yc = p1(2);
    
    zca = (xc - x1a)*(z2a - z1a)/(x2a - x1a) + z1a;
    zcb = (xc - x1b)*(z2b - z1b)/(x2b - x1b) + z1b;
    da = (y2a - y1a)/(x2a - x1a);
    db = (y2b - y1b)/(x2b - x1b);
    
    if zca > zcb
        if clines(clines(i,1) < clines(i,2), :)
            plot([xc,xc+sqrt(w/(1+da*da))],[yc,yc+da*sqrt(w/(1+da*da))],'-k','Linewidth',1.5)
            plot([xc,xc-sqrt(w/(1+da*da))],[yc,yc-da*sqrt(w/(1+da*da))],'-k','Linewidth',1.5)
        end
        intersections = [intersections; [xc, yc, zca, zcb, (xc - x1a)/(x2a - x1a), clines(i,1), clines(i,2), 1]];
    else
        if clines(clines(i,1) < clines(i,2), :)
            plot([xc,xc+sqrt(w/(1+db*db))],[yc,yc+db*sqrt(w/(1+db*db))],'-k','Linewidth',1.5)
            plot([xc,xc-sqrt(w/(1+db*db))],[yc,yc-db*sqrt(w/(1+db*db))],'-k','Linewidth',1.5)
        end
        intersections = [intersections; [xc, yc, zca, zcb, (xc - x1a)/(x2a - x1a), clines(i,1), clines(i,2), 0]];
    end
    
end
    
if ~isempty(intersections)
    intersections = sortrows(sortrows(intersections,5),6);
else
    disp('unknot')
end

% number nodes ("atoms") in black
if number_nodes==1
    for i = 1:(length(xcoor)-1)
        text(xcoor(i),ycoor(i),sprintf('%g',i),'Fontsize',12)
    end
end
    
if ~isempty(intersections)
    % number intersections in blue
    crossovers = intersections(intersections(:,8)==1,:);
    if number_intersections==1
        for i = 1:size(crossovers,1)
            text(crossovers(i,1)+.3,crossovers(i,2)-.3,sprintf('%g',i),'Fontsize',12,'color','b')
        end
    end
    
    % add the crossover number to the last column in intersections
    intersections = [intersections, zeros(size(intersections,1),1)];
    intersections(intersections(:,8)==1,9) = 1:sum(intersections(:,8));
end
