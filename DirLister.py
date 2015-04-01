import os

with open('dirs.txt') as f:
    dirs = list(f)

out = open('Program list.txt', 'w')

for directory in dirs:
    directory = directory.replace('\n', '')   # Remove newlines which aren't actually in the paths.
    indentation = directory.count('\t')       # Count the indentation on the line in dirs.txt.
    directory = directory.replace('\t', '')   # Clean up tabs, as they're not actually part of the paths.

    out.write('{0}{1}:'.format(indentation*'\t', directory) + '\n')
    
    contents = os.listdir(directory)

    for item in contents:
        out.write((indentation+1)*'\t' + item + '\n')

    out.write('\n') #Make a newline, for clarity's sake.