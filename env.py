import os

current_directory = os.path.dirname(os.path.realpath(__file__))

browser = os.path.join(current_directory, "browser")

os.environ["PATH"] += os.pathsep + current_directory

print(current_directory)