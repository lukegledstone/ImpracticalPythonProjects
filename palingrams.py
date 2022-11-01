import sys

try:
    with open(2of4brif.txt, 'r') as in_file:
        pass
except IOError as error:
    print(f"{error}\n Error opening {error}. Terminating program. ", file=sys.stderr)
    sys.exit(1)
