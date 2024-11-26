# stockfish-live-feed
Script to feed live WCC data into the stockfish engine

This script will sync data every 60 seconds by default

# Requirements
Python and python-chess and requests libraries

pip install chess

pip install requests

# Config:
Seup your config at the top

MOVES_URL = "http://example.com/moves.txt" # Data feed location

STOCKFISH_PATH = "/path/to/stockfish"  # Local Stockfish path

CHECK_INTERVAL = 60  # Check every 60 seconds

#Usage

To run in the forground:

python stockfish-live-feed.py


To run as a background process:

nohup python stockfish-live-feed.py &