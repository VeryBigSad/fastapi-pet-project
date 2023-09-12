import os
import sys


if len(sys.argv) < 2:
    raise Exception("Please provide an access key as an argument")
ACCESS_KEY = sys.argv[1]
IS_DEBUG = os.getenv("DEBUG", "False").lower() == "true"
