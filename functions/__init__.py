import sys
import os

# Add the parent directory of 'functions' to the system path
workshop_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Workshop path: {workshop_path}")
if workshop_path not in sys.path:
    sys.path.append(workshop_path)
        
# export PYTHONPATH=~/Documents/workshop
