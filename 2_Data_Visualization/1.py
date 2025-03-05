import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Set up code checking
import os
if not os.path.exists("../input/fifa.csv"):
    os.symlink("../input/data-for-datavis/fifa.csv", "../input/fifa.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex1 import *
print("Setup Complete")

#=====================================================================
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Set up code checking
import os
if not os.path.exists("../input/fifa.csv"):
    os.symlink("../input/data-for-datavis/fifa.csv", "../input/fifa.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex1 import *
print("Setup Complete")

# Path of the file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Check your answer
step_2.check()

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)

# Check your answer
step_3.a.check()

sns.lineplot(data=financial_data)

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song
sns.lineplot(data=spotify_data)

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

# Add label for horizontal axis
plt.xlabel("Date")

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

#=====================================================================


#=====================================================================


#=====================================================================


#=====================================================================