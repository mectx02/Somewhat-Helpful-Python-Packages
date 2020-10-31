#  Copyright (c) 2020. Mitchell Case ("mectx02")

# TODO: add a way to import pieces to the board
#       add some error checking for pieceSet parameter


"""
Allows for the creation of an X by Y game board.

Contains multiple functions for ease of use when developing with this program.
"""

'''
MIT License

Copyright (c) 2020 Mitchell Case ("mectx02")

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


def display(board):

    """Iterates through a list and prints it out."""

    for i in board:
        line = ""
        for j in i:
            line += j

        print(line)
    print()


def makeBoard(x, y, pieceSet=""):

    """
    Creates a board with specified length and width (in empty spaces).
    Printed board size does not reflect available spaces of play.

    Final output will be double the size (but have the same amount of spaces).

    OPTIONAL: a map of the current field can be added during the display of the board.
    This works best when the pieces are one character in width (no autosizing of the array yet).
    """

    # First double the sizes and add one (so it looks better)
    xLength = x * 2 + 1
    yLength = y * 2 + 1

    board = []

    for i in range(xLength):

        # Create the board line by line
        line = []

        if i == 0 or i == xLength - 1:
            line.append("+ ")
        else:
            line.append("| ")

        if i % 2 == 1:

            for j in range(yLength - 1):
                if j == yLength - 1:
                    line.append("| ")
                else:
                    if j % 2 == 0:
                        if pieceSet != "":
                            line.append(str(pieceSet[int((i - 1) / 2)][int((j - 1) / 2)]) + " ")
                        else:
                            line.append("  ")
                    else:
                        line.append("| ")

        else:

            for j in range(yLength - 1):

                if j == yLength - 1:
                    line.append("| ")
                else:
                    if j != yLength - 2:
                        line.append("- ")

                    else:
                        line.append("| ")

            if i == 0 or i == xLength - 1:
                line.remove(line[len(line) - 1])
                line.append("+")


        # Append each line to the final result
        board.append(line)

    return board
