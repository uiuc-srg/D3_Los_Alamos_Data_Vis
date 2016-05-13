# D3_Los_Alamos_Data_Vis
This repository contains the code Peter wrote for the Pass the Hash research project he was working on during FA15 and SP16.
There are a number of files in this repository that are used to create visualizations on the los alamos dataset.

In order to run the code to see the visualization all that needs to be done is to run localhost in this directory. The only html file is index.html which simply loads the visualization.

The other files are broken up as follows.

auth_data.txt
  - 1 GB sample of the original dataset. Original dataset was 70 GB.

data_files_aa
  - Sample of dataset parsed for only relevant information. We keep source users, destination users, source computers and destination computers from original dataset sample

data_breakup.py
  - python file used to make data_files_aa from auth_data.txt

index.html
  - main D3 visualization code. Template taken from D3js.org and modifying to fulfill direct needs

colorbrewer.min.js
  - Js file containing color schemes used in visualization

output.json
  - json file that is created by script.py
  - contains all of the nodes and can uncomment edges to contain all edges for graph visualization
  - necessary to stay in existing format for visualization to working

script.py
  - main file to create visualization
  - parses data_files_aa to create output.json
  - currently only parsing source and destination computers and displaying those in graph visualization
  - can be extended to also visualize source users and destination users

style
  - style sheet
