# rozwiązanie typu built-in python 2
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--text")
args = parser.parse_args()
print(args.text)