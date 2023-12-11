# Author: Sirus Salari
# GitHub Username: sirus-the-beaver
# Date: 11/30/2023
# Description: This project's aim is to create a program that allows for two users to play each other over a game
# chess. After the game has been initialized and started, the players are continually able to make moves simply by
# calling one method (make_move()). Additionally, either play can always check the state of the game at any point
# by calling the get_game_state() method.

# ********************************
"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

1. Initializing the ChessVar class
Upon initializing the ChessVar class, the game_state is initialized to 'UNFINISHED', white_pieces and black_pieces
are initialized to empty lists, current_player is initialized to 'white', and the start_game method is called to
create all the chess pieces and initialize their positions on the board, and add them to the white_pieces and
black_pieces lists.

2. Keeping track of turn order
After each legal move, the ChessVar class current_player data member will switch to the opponent so that it's set to the
next player's turn.

3. Keeping track of the current board position
The program will be keeping track of the current board position of each piece by storing the data as strings as a data
member for each ChessPiece object. There's a setter method for this data member so that the ChessVar class can set the
position to a new position upon a legal move being made.

4. Determining if a regular move is valid
The program will determine if a move is valid in a method called is_legal within the ChessVar class. This method will be
called upon a player calling the make_move method to move one of their chess piece's.

5. Determining if a capture is valid
The program will determine if a capture is valid within the make_move method to see if one of the opponent's chess
pieces is currently located at the square that the current player is moving to. If there is an opponent piece there, then
the opponent's piece will be removed from its respective data member list part of the ChessVar class.

6. Determining the current state of the game
The program will determine the current state of the game at two points within the ChessVar class. It will check the state
every time make_move is called to verify that the game is unfinished.

It'll also check to see if the game is over after a capture, and appropriately change the game_state data member if so.

"""
# ********************************

class ChessPiece:
    """
    This has 3 data members: current_square (a string), piece_type (a string), and color (a string).

    The current_square data member is meant to represent the position of a given piece relative to the layout of the
    board ('a1' for example).

    piece_type is meant to represent what type of piece a given piece is ('rook' for example)

    color is meant to differentiate between the white and black pieces ('white' for example)

    This class has 5 methods: __init__, get_current_square, set_current_square, get_piece_type, and get_color

    Upon initialization of this class, a ChessPiece object is created with all of its data members define by the args
    passed in.

    This class is meant to be used within the ChessVar class for creating chess pieces, and moving chess pieces.
    """
    def __init__(self, current_square, piece_type, color):
        """
        :param current_square: a string that represents the position of a chess piece relative to the board
        :param piece_type: a string that represents the type of piece
        :param color: a string that differentiates between the white and black chess pieces
        """
        self._current_square = current_square
        self._piece_type = piece_type
        self._color = color

    def get_current_square(self):
        """
        :return: current_square string data member
        """
        return self._current_square

    def set_current_square(self, new_square):
        """
        :param new_square: a string that represents a square on the chess board

        This will set the current_square data member equal to the argument passed in.
        """
        self._current_square = new_square

    def get_piece_type(self):
        """
        :return: piece_type string data member
        """
        return self._piece_type

    def get_color(self):
        """"
        :return: color string data member
        """
        return self._color


class ChessVar:
    """
    This class has 4 data members: game_state (a string), white_pieces (a list), black_pieces (a list), current_player
    (a string).

    game_state is meant to represent whether the game is still going or if a player won ('UNFINISHED' for example)

    white_pieces is meant to represent all the white chess pieces that have not been captured and are still on the
    board.

    black_pieces is meant to represent all the black chess pieces that have not been captures and are still on the
    board.

    current_player is meant to keep track of which player's turn it is ('white' for example)

    This class has 10 methods: __init__, get_game_state, add_white_piece, remove_white_piece, add_black_piece,
    remove_black_piece, is_legal, game_over, make_move, and start_game

    Upon initialization of this class, the game_state is initialized to 'UNFINISHED', white_pieces and black_pieces
    are initialized to empty lists, current_player is initialized to 'white', and the start_game method is called to
    create all the chess pieces and initialize their positions on the board, and add them to the white_pieces and
    black_pieces lists.

    This class uses the ChessPiece class to create new chess pieces and move chess pieces.
    """
    def __init__(self):
        """
        This will initialize game_state to 'UNFINISHED', initialize the white_pieces and black_pieces to empty lists,
        sets the first player to 'white', and calls start_game to start the game.
        """
        self._game_state = 'UNFINISHED'
        self._white_pieces = []
        self._black_pieces = []
        self._current_player = 'white'
        self.start_game()


    def get_game_state(self):
        """
        :return: game_state string data member
        """
        return self._game_state

    def add_white_piece(self, piece):
        """
        :param piece: a ChessPiece object that has its color data member set to 'white'

        This method will add ChessPiece objects to this class's white_pieces list to keep track of active white chess
        pieces on the board.
        """
        self._white_pieces.append(piece)

    def remove_white_piece(self, piece):
        """
        :param piece: a ChessPiece object that has its color data member set to 'white'

        This method will remove ChessPiece objects from this class's white_pieces list when a piece is captured
        """
        self._white_pieces.remove(piece)

    def add_black_piece(self, piece):
        """
        :param piece: a ChessPiece object that has its color data member to 'black'

        This method will add ChessPiece objects to this class's black_pieces list to keep track of active black chess
        pieces on the board.
        """
        self._black_pieces.append(piece)

    def remove_black_piece(self, piece):
        """
        :param piece: a Chess piece object that has its color data member set to 'black'

        This method will remove ChessPiece objects from this class's black_pieces list when a piece is captured
        """
        self._black_pieces.remove(piece)

    def is_legal(self, piece_type, to_square, row, column):
        """
        :param piece_type: a string that represents the type of chess piece
        :param to_square: a string that represents the square that the chess piece will move to
        :param row: a string that represents the row that the chess piece is currently in
        :param column: a string that represents the column that the chess piece is currently in
        :return: True or False

        This method will check to see if a move is legal before a chess piece officially moves on the board.

        If the move is determined to be illegal, then it'll return False. If the move is determined to be legal, then
        it'll return True.
        """
        if piece_type == 'rook':
            # if it's not staying in the same column and not staying in the same row
            if to_square[0] != column and int(to_square[1]) != row:
                return False

            # if it's staying in same column (moving across rows)
            elif to_square[0] == column:
                row_destination = int(to_square[1])
                row_source = row

                # moving north
                if row_destination > row_source:

                    # check for pieces along its path
                    for i in range(row_source + 1, row_destination):
                        square_along_path = column + str(i)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False

                # moving south
                else:
                    # check for pieces along its path
                    for i in range(row_destination - 1, row_source, -1):
                        square_along_path = column + str(i)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False

            # if it's staying in same row (moving across columns)
            elif int(to_square[1]) == row:
                column_destination = ord(to_square[0])
                column_source = ord(column)

                # moving east
                if column_destination > column_source:
                    #check for pieces along its path
                    for i in range(column_source + 1, column_destination):
                        square_along_path = chr(i) + str(row)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False

                # moving west
                else:
                    #check for pieces along its path
                    for i in range(column_destination - 1, column_source, -1):
                        square_along_path = chr(i) + str(row)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False


        elif piece_type == 'knight':
            if ord(to_square[0]) == (ord(column) + 1) or ord(to_square[0]) == (ord(column) - 1):
                if int(to_square[1]) != (row + 2) and int(to_square[1]) != (row - 2):
                    return False

            elif int(to_square[1]) == (row + 1) or int(to_square[1]) == (row - 1):
                if ord(to_square[0]) != (ord(column) + 2) and ord(to_square[0]) != (ord(column) - 2):
                    return False

            else:
                return False

        elif piece_type == 'bishop':
            column_difference = ord(to_square[0]) - ord(column)
            row_difference = int(to_square[1]) - row

            # a bishop's change in column must equal its change in row
            if abs(column_difference) != abs(row_difference):
                return False

            # moving northeast
            elif row_difference > 0 and column_difference > 0:
                row_destination = int(to_square[1])
                row_source = row

                # check its path
                column_counter = 0
                for i in range(row_source + 1, row_destination):
                    column_counter += 1
                    square_along_path = chr(ord(column) + column_counter) + str(i)
                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == square_along_path:
                            return False

                    for black_piece in self._black_pieces:
                        if black_piece.get_current_square() == square_along_path:
                            return False

            # moving southeast
            elif row_difference < 0 < column_difference:
                row_destination = int(to_square[1])
                row_source = row
                # check its path
                column_counter = 0
                for i in range(row_destination - 1, row_source, -1):
                    column_counter += 1
                    square_along_path = chr(ord(column) + column_counter) + str(i)
                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == square_along_path:
                            return False

                    for black_piece in self._black_pieces:
                        if black_piece.get_current_square() == square_along_path:
                            return False

            # moving southwest
            elif row_difference < 0 and column_difference < 0:
                row_destination = int(to_square[1])
                row_source = row

                # check its path
                column_counter = 0
                for i in range(row_destination - 1, row_source, -1):
                    column_counter -= 1
                    square_along_path = chr(ord(column) + column_counter) + str(i)
                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == square_along_path:
                            return False

                    for black_piece in self._black_pieces:
                        if black_piece.get_current_square() == square_along_path:
                            return False

            # moving northwest
            elif column_difference < 0 < row_difference:
                row_destination = int(to_square[1])
                row_source = row

                # check its path
                column_counter = 0
                for i in range(row_source + 1, row_destination):
                    column_counter -= 1
                    square_along_path = chr(ord(column) + column_counter) + str(i)
                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == square_along_path:
                            return False

                    for black_piece in self._black_pieces:
                        if black_piece.get_current_square() == square_along_path:
                            return False


        elif piece_type == 'queen':
            column_difference = ord(to_square[0]) - ord(column)
            row_difference = int(to_square[1]) - row

            # if its moving like a rook
            if abs(column_difference) != abs(row_difference):
                if to_square[0] != column and to_square[1] != row:
                    return False

                elif to_square[0] == column:
                    row_destination = int(to_square[1])
                    row_source = row

                    if row_destination > row_source:
                        # check its path
                        for i in range(row_source + 1, row_destination):
                            square_along_path = column + str(i)
                            for white_piece in self._white_pieces:
                                if white_piece.get_current_square() == square_along_path:
                                    return False

                            for black_piece in self._black_pieces:
                                if black_piece.get_current_square() == square_along_path:
                                    return False

                    else:
                        # check its path
                        for i in range(row_destination - 1, row_source, -1):
                            square_along_path = column + str(i)
                            for white_piece in self._white_pieces:
                                if white_piece.get_current_square() == square_along_path:
                                    return False

                            for black_piece in self._black_pieces:
                                if black_piece.get_current_square() == square_along_path:
                                    return False

                elif int(to_square[1]) == row:
                    column_destination = ord(to_square[0])
                    column_source = ord(column)

                    if column_destination > column_source:
                        # check its path
                        for i in range(column_source + 1, column_destination):
                            square_along_path = chr(i) + str(row)
                            for white_piece in self._white_pieces:
                                if white_piece.get_current_square() == square_along_path:
                                    return False

                            for black_piece in self._black_pieces:
                                if black_piece.get_current_square() == square_along_path:
                                    return False

                    else:
                        # check its path
                        for i in range(column_destination - 1, column_source, -1):
                            square_along_path = chr(i) + str(row)
                            for white_piece in self._white_pieces:
                                if white_piece.get_current_square() == square_along_path:
                                    return False

                            for black_piece in self._black_pieces:
                                if black_piece.get_current_square() == square_along_path:
                                    return False

            # if its moving like a bishop
            elif abs(column_difference) == abs(row_difference):
                # moving northeast
                if row_difference > 0 and column_difference > 0:
                    row_destination = int(to_square[1])
                    row_source = row

                    # check its path
                    column_counter = 0
                    for i in range(row_source + 1, row_destination):
                        column_counter += 1
                        square_along_path = chr(ord(column) + column_counter) + str(i)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False

                # moving southeast
                elif row_difference < 0 < column_difference:
                    row_destination = int(to_square[1])
                    row_source = row
                    # check its path
                    column_counter = 0
                    for i in range(row_destination - 1, row_source, -1):
                        column_counter += 1
                        square_along_path = chr(ord(column) + column_counter) + str(i)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False

                # moving southwest
                elif row_difference < 0 and column_difference < 0:
                    row_destination = int(to_square[1])
                    row_source = row

                    # check its path
                    column_counter = 0
                    for i in range(row_destination - 1, row_source, -1):
                        column_counter -= 1
                        square_along_path = chr(ord(column) + column_counter) + str(i)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False

                # moving northwest
                elif column_difference < 0 < row_difference:
                    row_destination = int(to_square[1])
                    row_source = row

                    # check its path
                    column_counter = 0
                    for i in range(row_source + 1, row_destination):
                        column_counter -= 1
                        square_along_path = chr(ord(column) + column_counter) + str(i)
                        for white_piece in self._white_pieces:
                            if white_piece.get_current_square() == square_along_path:
                                return False

                        for black_piece in self._black_pieces:
                            if black_piece.get_current_square() == square_along_path:
                                return False


        elif piece_type == 'king':
            column_difference = ord(to_square[0]) - ord(column)
            row_difference = int(to_square[1]) - row

            if column_difference != 1 and column_difference != -1:
                if row_difference != 1 and row_difference != -1:
                    return False

        return True


    def game_over(self, piece_removed):
        """
        :param piece_removed: a ChessPiece object that represents a chess piece that got captured and removed
        :return: True or False

        This method will check to see if the game is officially over after a chess piece is captured.

        If it's determined that the capture led to the game ending, then it'll return True, otherwise it'll return
        False.
        """
        if self._current_player == 'white':
            last_piece = True

            for black_piece in self._black_pieces:
                if black_piece.get_piece_type() == piece_removed.get_piece_type():
                    last_piece = False

            return last_piece

        else:
            last_piece = True

            for white_piece in self._white_pieces:
                if white_piece.get_piece_type() == piece_removed.get_piece_type():
                    last_piece = False

            return last_piece


    def make_move(self, from_square, to_square):
        """
        :param from_square: a string that represents the square that a chess piece is currently located
        :param to_square: a string that represents the square that the chess piece is trying to move to
        :return: True or False

        This method will handle checking to see if a chess piece can make a move (based on if the game is finished,
        if it's the player's turn, if the piece being moved is the player's, and calls is_legal to see if the move itself
        is legal).

        If the move is determined to be illegal, then this method will return False. If all the conditions are met and
        the chess piece officially moves, then the method will return True.
        """
        if self._game_state != 'UNFINISHED':
            return False

        if self._current_player == 'white':
            piece = None

            for white_piece in self._white_pieces:
                if from_square == white_piece.get_current_square():
                    piece = white_piece

                # check if there's a white piece on the square it wants to move to
                if to_square == white_piece.get_current_square():
                    return False

            # if there's not a white piece on the square it's supposed to move from
            if piece is None:
                return False

            column = piece.get_current_square()[0]
            row = int(piece.get_current_square()[1])

            # special case: on pawn's first move (can move forward 1 OR 2 rows)
            if piece.get_piece_type() == 'pawn' and row == 2:
                if to_square[0] != column:
                    return False

                if int(to_square[1]) != (row + 1) and int(to_square[1]) != (row + 2):
                    return False

            elif piece.get_piece_type() == 'pawn' and row != 2:
                legal = False

                if ord(to_square[0]) == (ord(column) + 1) or ord(to_square[0]) == (ord(column) - 1):
                    for black_piece in self._black_pieces:
                        # check if pawn can move diagonal one square (if there's an opponent piece there)
                        if black_piece.get_current_square() == to_square:
                            legal = True

                    if not legal:
                        return False

                else:
                    if to_square[0] != column:
                        return False

                if int(to_square[1]) != (row + 1):
                    return False

                elif int(to_square[1]) == (row - 1) and legal == False:
                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == to_square:
                            return False

            # if the piece is anything other than a pawn
            else:
                legal = self.is_legal(piece.get_piece_type(), to_square, row, column)

                if not legal:
                    return False

            # capture opponent piece if necessary
            for black_piece in self._black_pieces:
                if to_square == black_piece.get_current_square():
                    self.remove_black_piece(black_piece)
                    # check if game is over after capture
                    game_over = self.game_over(black_piece)

                    if game_over:
                        self._game_state = 'WHITE_WON'

            # at this point, the move is finally determined to be fully legal and possible
            piece.set_current_square(to_square)
            self._current_player = 'black'
            return True

        else:
            piece = None

            for black_piece in self._black_pieces:
                if from_square == black_piece.get_current_square():
                    piece = black_piece

                if to_square == black_piece.get_current_square():
                    return False

            if piece is None:
                return False

            column = piece.get_current_square()[0]
            row = int(piece.get_current_square()[1])
            if piece.get_piece_type() == 'pawn' and row == 7:
                if to_square[0] != column:
                    return False

                if int(to_square[1]) != (row - 1) and int(to_square[1]) != (row - 2):
                    return False


            elif piece.get_piece_type() == 'pawn' and row != 7:

                legal = False

                if ord(to_square[0]) == (ord(column) + 1) or ord(to_square[0]) == (ord(column) - 1):

                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == to_square:
                            legal = True

                    if not legal:
                        return False

                else:
                    if to_square[0] != column:
                        return False

                if int(to_square[1]) != (row - 1):
                    return False

                elif int(to_square[1]) == (row - 1) and legal == False:
                    for white_piece in self._white_pieces:
                        if white_piece.get_current_square() == to_square:
                            return False

            else:
                legal = self.is_legal(piece.get_piece_type(), to_square, row, column)

                if not legal:
                    return False

            for white_piece in self._white_pieces:
                if to_square == white_piece.get_current_square():
                    self.remove_white_piece(white_piece)
                    game_over = self.game_over(white_piece)

                    if game_over:
                        self._game_state = 'BLACK_WON'

            piece.set_current_square(to_square)
            self._current_player = 'white'
            return True


    def start_game(self):
        """
        This method is only called once and is automatically called upon initialization of the ChessVar class.

        This method will essentially create all the chess pieces on the board, initialize their starting position, and
        add the ChessPiece objects to the white_pieces and black_pieces data member lists in the ChessVar class.
        """
        ascii_code = (ord('a'))
        # create and initialize all the pawns
        for i in range(8):
            white_pawn = ChessPiece(chr(ascii_code) + '2', 'pawn', 'white')
            black_pawn = ChessPiece(chr(ascii_code) + '7', 'pawn', 'black')
            ascii_code += 1
            self.add_white_piece(white_pawn)
            self.add_black_piece(black_pawn)

        # create and initialize all the rooks
        white_rook_1 = ChessPiece('a1', 'rook', 'white')
        white_rook_2 = ChessPiece('h1', 'rook', 'white')
        self.add_white_piece(white_rook_1)
        self.add_white_piece(white_rook_2)

        black_rook_1 = ChessPiece('a8', 'rook', 'black')
        black_rook_2 = ChessPiece('h8', 'rook', 'black')
        self.add_black_piece(black_rook_1)
        self.add_black_piece(black_rook_2)

        # create and initialize all the knights
        white_knight_1 = ChessPiece('b1', 'knight', 'white')
        white_knight_2 = ChessPiece('g1', 'knight', 'white')
        self.add_white_piece(white_knight_1)
        self.add_white_piece(white_knight_2)

        black_knight_1 = ChessPiece('b8', 'knight', 'black')
        black_knight_2 = ChessPiece('g8', 'knight', 'black')
        self.add_black_piece(black_knight_1)
        self.add_black_piece(black_knight_2)

        # create and initialize all the bishops
        white_bishop_1 = ChessPiece('c1', 'bishop', 'white')
        white_bishop_2 = ChessPiece('f1', 'bishop', 'white')
        self.add_white_piece(white_bishop_1)
        self.add_white_piece(white_bishop_2)

        black_bishop_1 = ChessPiece('c8', 'bishop', 'black')
        black_bishop_2 = ChessPiece('f8', 'bishop', 'black')
        self.add_black_piece(black_bishop_1)
        self.add_black_piece(black_bishop_2)

        # create and initialize the kings and queens
        white_queen = ChessPiece('d1', 'queen', 'white')
        white_king = ChessPiece('e1', 'king', 'white')
        self.add_white_piece(white_queen)
        self.add_white_piece(white_king)

        black_queen = ChessPiece('d8', 'queen', 'black')
        black_king = ChessPiece('e8', 'king', 'black')
        self.add_black_piece(black_queen)
        self.add_black_piece(black_king)
