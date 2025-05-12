Knot Project

This project is intended to apply Monte Carlo simulation and knot theoretic moves to unfold protein knots and unveil knot theoretic properties

The simulation can be run by running "python main.py". The pdb file to be read in can be altered in main.py.

The current code identifies existing foreground loops for pdb files in 2D space. Future steps include:
    Applying knot unfolding moves to remove foreground loops
    Tracking the number of moves needed to unfold the protein
    Incorporation of Monte Carlo simulation to identify the fewest number of moves required
