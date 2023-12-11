# chess-CLI

This project's aim is to create a program that allows for two users to play each other over a game of a variation of chess. After the game has been initialized and started, the players are continually able to make moves simply by calling one method (make_move()). Additionally, either play can always check the state of the game at any point by calling the get_game_state() method.

For this version of chess, the objective is to capture all of one type of piece from your opponent (all of your opponent's rooks for example). The first player to capture all of one type of chess piece from their opponent wins the game.

The legal moves for each of the chess piece types remain the same as the classic version of chess.

## Program Analysis

### Initializing the ChessVar class
Upon initializing the ChessVar class, the game_state is initialized to 'UNFINISHED', white_pieces and black_pieces
are initialized to empty lists, current_player is initialized to 'white', and the start_game method is called to
create all the chess pieces and initialize their positions on the board, and add them to the white_pieces and
black_pieces lists.

### Keeping track of turn order
After each legal move, the ChessVar class current_player data member will switch to the opponent so that it's set to the
next player's turn.

### Keeping track of the current board position
The program will be keeping track of the current board position of each piece by storing the data as strings as a data
member for each ChessPiece object. There's a setter method for this data member so that the ChessVar class can set the
position to a new position upon a legal move being made.

### Determining if a regular move is valid
The program will determine if a move is valid in a method called is_legal within the ChessVar class. This method will be
called upon a player calling the make_move method to move one of their chess piece's.

### Determining if a capture is valid
The program will determine if a capture is valid within the make_move method to see if one of the opponent's chess
pieces is currently located at the square that the current player is moving to. If there is an opponent piece there, then
the opponent's piece will be removed from its respective data member list part of the ChessVar class.

### Determining the current state of the game
The program will determine the current state of the game at two points within the ChessVar class. It will check the state
every time make_move is called to verify that the game is unfinished.
