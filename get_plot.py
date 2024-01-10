import re
import os
import seaborn as sns
import matplotlib.pyplot as plt
def extract_times(input_string):
    # Regular expression to find patterns like '[OK in 8.70s]' or '[OK in 9.70s]'
    pattern = r'\[OK in (\d+\.\d+)s\]'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    # Convert matched strings to floats and return as a list
    return [float(match) for match in matches]

def read_file_to_string(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content
resulsts = []
averages = []
filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']
for filename in filenames:

    subfolder = 'logs'
    path = os.path.join(subfolder, filename)
    text = read_file_to_string(path)
    inner_result = extract_times(text)
    x = len(inner_result)
    resulsts.append(inner_result)
    averages.append(sum(inner_result) / len(inner_result))
x = range(x)
i= 0
for wykres in resulsts:
    sns.scatterplot(x = x, y=wykres)
    plt.title(f"With {i+1} instances, average time is {round(averages[i], 2)}")
    plt.ylim(0,120)
    plt.ylabel("Time of execution [s]")
    plt.xlabel("Nr of task")
    plt.show()
    i = i+1
    
sns.scatterplot( x = range(1,6), y = averages)
plt.title( "How fast task is executed depending on number of instances")
plt.xlabel("Nr of instances")
plt.ylabel("Average time of execution")
plt.show()