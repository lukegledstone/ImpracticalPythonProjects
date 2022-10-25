'''
Load a test file as a list.

Arguments: text file name
Exceptions: IO error is filename not found
Returns: A list of all works in the text file, in lower case
Requires: import sys
'''

import sys

def load(file):
    '''
    Open a text file and turn contents into a list of lowercase strings.
    '''
    try: 
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split("\n")
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)