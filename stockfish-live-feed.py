import requests
import chess
import chess.engine
import time

# Configuration
MOVES_URL = "http://example.com/moves.txt" # Data feed location
STOCKFISH_PATH = "/path/to/stockfish"  # Local Stockfish path
CHECK_INTERVAL = 60  # Check every 60 seconds

# Download the list of moves from the given URL
def download_moves(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip().split("\n")
    except requests.RequestException as e:
        print(f"Error downloading moves: {e}")
        return None

# Analyze a list of chess moves using Stockfish
def analyze_moves(moves, engine_path):
    try:
        # Initialize the chess board
        board = chess.Board()
        
        # Start Stockfish engine
        with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
            for move in moves:
                try:
                    # Make the move on the board
                    board.push_san(move)
                    
                    # Analyze the current board position
                    result = engine.analyse(board, chess.engine.Limit(time=0.5))
                    score = result["score"].relative
                    
                    # Display the board and the evaluation
                    print(board)
                    print(f"Move: {move}, Evaluation: {score}")
                    print("-" * 40)
                except ValueError as e:
                    print(f"Invalid move {move}: {e}")
                    break
    except FileNotFoundError:
        print(f"Stockfish not found at {engine_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Loop
def main():
    last_checked_moves = None
    while True:
        print("Checking for new moves...")
        
        # Download the moves
        moves = download_moves(MOVES_URL)
        if moves is None:
            print("No moves found or error occurred.")
        elif moves != last_checked_moves:
            print(f"New moves detected: {len(moves)} moves.")
            analyze_moves(moves, STOCKFISH_PATH)
            last_checked_moves = moves
        else:
            print("No new moves.")

        # Wait for the next check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

