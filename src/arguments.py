import argparse
from constants import *

def retrieve_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument(LIBRARY_FILE_TAG)
    parser.add_argument(CALIBRE_LOCATION_TAG)

    
    args = parser.parse_args()
    
    return args
