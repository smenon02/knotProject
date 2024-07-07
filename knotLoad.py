#Requires: pdb file
#Modifies:
#Effects: Helper function that takes in a pdb file and returns a corresponding .txt file. Used for parsing
def convert_pdb_to_txt(pdb_filename):
    #Creates variable name to initialize name of text file
    txt_filename = pdb_filename.replace('.pdb','.txt')
    #Write each line of pdb file to .txt file
    with open(pdb_filename, 'r') as pdb_file, open(txt_filename, 'w') as txt_file:
        for line in pdb_file:
            txt_file.write(line)
    return txt_filename

#Requires: pdb file
#Modifies:
#Effects:Takes in a pdb file and returns a set of coordinates representing a connected chain of every 4th
#alpha carbon
def connect_4th_alphas(pdb_filename):
    #Convert pdb file to txt file
    txt_filename = convert_pdb_to_txt(pdb_filename)
    #Initialize empty list to hold coordinates for connected alpha carbon chain
    alpha_carbons = []

    # Open and read the text file
    with open(txt_filename, 'r') as file:
        #iterate through each line in text file
        for line in file:
            #Looks for lines corresponding with alpha carbons
            if line.startswith("ATOM") and " CA " in line:
                # Extract the coordinates (x, y, z) from the line
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                alpha_carbons.append((x, y, z))
    #Returns subset of alpha carbon coordinates corresponding with every 4th alpha carbon
    connected_alphas = list(list(alpha_carbons[i]) for i in range(0, len(alpha_carbons) - 4, 4))
    return connected_alphas
