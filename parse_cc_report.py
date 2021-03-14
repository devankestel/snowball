from matplotlib import pyplot as plt 
import numpy as np

# Using readlines()
file1 = open('django_current_cc.md', 'r')
lines = file1.readlines()
 
count = 0
# Strips the newline character

report_dict = {}
# {'filename': {'block_name': [block_type, num_lines, letter_grade, score]}}
score_list = []

for line in lines:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))
    line = line.strip()
    if line.startswith('django/'):
        filename = line
        report_dict[filename] = {}
    elif line.startswith('M') or line.startswith('C') or line.startswith('F'):
        # block_type, num_lines, letter_grade, score = line
        print(line)
        [block_type, line_info, block_name, dash, letter_grade, score_info] = line.split()
        num_lines = int(line_info[-1])
        score = int(score_info[1:-1])
        report_dict[filename][block_name] = [block_type, num_lines, letter_grade, score]
        score_list.append(score)
    else: 
        continue

scores = np.array(score_list)
print(scores.max())
print(scores.min())
print(np.median(scores))
print(scores.mean())
print(scores.std())
# divide each score by total number of blocks to get percentage based histogram

hist, bins = np.histogram(scores,bins = [0,5,10,15,20,25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) 
print(hist) 
print(bins) 

plt.hist(scores, bins = bins) 
plt.title("histogram") 
plt.show()






        