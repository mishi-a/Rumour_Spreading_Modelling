# Rumour_Spreading_Modelling

############################################################################
How to run this Project ?
   Run "test.py" present in the Project directory by using Following command.
    python3 test.py

############################################################################
Files Included within the project:
1.Network.py :- It is used to create our estimated graph using the given formula with the help of matplotlib

2.Dataset_beautifier.py :- Extracted the relevant information from the given
dataset for various phases

3.Actual_result.py :- It extracts information from the above obtained dataset
which comes after refinement

4.Test.py :- This merges all the above files and plots the relevant graph

############################################################################
Design decision :
   This project follows from the research paper "The Anatomy Of scientific Rumour".In this we have used the "Higgs Twitter Activity time" dataset to model How the Rumour spread over the network.Finally we plotted the obtained result of fraction of active user vs time.

############################################################################
Result :
  We have verified that rumour over a network can be modelled using SI (susceptible-Infected) Model.

############################################################################
Plot included :
  Plot.png : plot of obtained result through SI model vs Actual result over various phase.

############################################################################
Tools and Packages required:
1.python (version 3.4)
2.Matplotlib : A library in python for plotting obtained result.