Bar Charts and Heatmaps

# Path of the file to read
flight_filepath = "../input/flight_delays.csv"

# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

Heatmap

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Airline")

#================================================
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
import os
if not os.path.exists("../input/ign_scores.csv"):
    os.symlink("../input/data-for-datavis/ign_scores.csv", "../input/ign_scores.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex3 import *
print("Setup Complete")

# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()

# Print the data
print(ign_data)

# Fill in the line below: What is the highest average score received by PC games,
# for any genre?
high_score = 7.759930

# Fill in the line below: On the Playstation Vita platform, which genre has the
# lowest average score? Please provide the name of the column, and put your answer
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'

# Check your answers
step_2.check()

# Bar chart showing average score for racing games by platform
# Set the width and height of the figure
plt.figure(figsize=(25,15))

# Add title
plt.title("average score for racing games, by Platform")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=ign_data.index, y=ign_data['Racing'])

# Add label for vertical axis
plt.ylabel("average score for racing games, by Platform")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=ign_data.index, y=ign_data['Racing'])

# Check your answer
step_3.a.check()

# Heatmap showing average game score by platform and genre
sns.heatmap(data=ign_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Game genre")

