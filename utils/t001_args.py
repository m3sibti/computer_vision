import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-n', '--name', required=True, help='Enter your name')
args = vars(ap.parse_args())

print(f'Hello Mr. {args["name"]}')
