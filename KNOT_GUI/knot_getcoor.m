function [coor4, ca_coor] = knot_getcoor(pdb_file, join_outside_mol)
% coor4 is every fourth alpha carbon. 
% ca_coor is every alpha carbon.
%
% if join_outside_mol, add coordinates at intersection points of endpoint
% connections with the rest of the protein, with just greater than the 
% maximal z coordinate
%
% eventually, we implement more complex closure strategies

prot = pdbread(pdb_file);

allx = [prot.Model.Atom.X];
ally = [prot.Model.Atom.Y];
allz = [prot.Model.Atom.Z];
residue_number = [prot.Model.Atom.resSeq];

is_ca = strcmp({prot.Model.Atom.AtomName},'CA');
ca_coor = [allx(is_ca); ally(is_ca); allz(is_ca)];
ca_resnum = residue_number(is_ca);
duplicate = zeros(1,length(ca_resnum));
for i = 2:length(duplicate)
    if ca_resnum(i)==ca_resnum(i-1)
        duplicate(i) = 1;
    end
end

ca_coor(:,duplicate==1) = [];

coor4 = ca_coor(:,1:4:length(ca_coor));

randx = 360*rand();
randy = 360*rand();
randz = 360*rand();
ca_coor = knot_rotx(ca_coor, randx);
ca_coor = knot_roty(ca_coor, randy);
ca_coor = knot_rotz(ca_coor, randz);
coor4 = knot_rotx(coor4, randx);
coor4 = knot_roty(coor4, randy);
coor4 = knot_rotz(coor4, randz);

if join_outside_mol
    zmax = max(coor4(3,:));
    P = InterX([coor4(1,end), coor4(1,1); coor4(2,end), coor4(2,1)], coor4(1:2,2:end-1));
    P = sortrows(P')';
    P = [P; ones(1,size(P,2))*(zmax+1)];
    if coor4(1,end) < coor4(1,1)
        coor4 = [coor4, P];
    else
        coor4 = [coor4, fliplr(P)];
    end
end

