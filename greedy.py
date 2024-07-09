from collections import deque as queue


class Board:
  """ Provides common utilities
      for iterating over the board
  """

  def __init__(self, n, m, board):
    self.n = n
    self.m = m
    self.board = board


  def is_valid(self):
    """ Checks the below parameters in the input:
        - the board is a valid nested list
        - input n conforms with board dimensions
        - all values lie in [1, m]
        If at least one of the above conditions don't meet
        then returns False, else returns True.
    """
    if not isinstance(self.board, list) or len(self.board) != self.n:
      return False

    # Check if all rows have the same length and the length is n
    for row in self.board:
        if not isinstance(row, list) or len(row) != self.n:
            return False
        for color in row:
          if color > self.m or color < 1:
            return False

    return True


  def get_distinct_colors(self):
    """ Returns unique colors present in the board
    """

    colors = {number for row in self.board for number in row}
    return len(colors)

  def is_valid_position(self, x, y, vis):
    """ Checks if the given position (x, y) is valid
        and not previously visited
    """
    if min(x, y) < 0 or max(x, y) >= len(self.board):
      return False

    if vis[x][y]:
      return False

    return True

  def get_connected_tiles(self, color, apply_color=False):
    """ Runs a BFS over the board and returns number of
        connected tiles when origin is coloured with
        `color`. Also, applies the `color` to the connected
        tiles when `apply_color` is set to True
    """

    initial_color = self.board[0][0]
    connected_nodes = 0

    # Direction vectors
    dx = [ -1, 0, 1, 0]
    dy = [ 0, 1, 0, -1]

    # initialize the queue
    q = queue()
    vis = [[False for i in range(self.n)] for i in range(self.n)]

    # insert origin node into the queue
    # node is represented by - (x, y, True if node was previously connected)
    q.append((0, 0, True))
    vis[0][0] = True

    while(len(q) > 0):
      cell = q.popleft()
      x = cell[0]
      y = cell[1]
      previously_connected = cell[2]

      connected_nodes += 1
      if apply_color:
        self.board[x][y] = color

      # check all four sides of current tile
      for i in range(4):
        adjx = x + dx[i]
        adjy = y + dy[i]

        if self.is_valid_position(adjx, adjy, vis):
          if self.board[adjx][adjy] == initial_color and previously_connected:
            q.append((adjx, adjy, True))
            vis[adjx][adjy] = True
          elif self.board[adjx][adjy] == color:
            q.append((adjx, adjy, False))
            vis[adjx][adjy] = True

    return connected_nodes

class GreedySolution:

  def __init__(self, n, m, matrix):
    self.board = Board(n, m, matrix)

  def get_moves(self):
    """ Returns a list of moves taken greedily,
        raises a ValueError when board dimension and color
        don't conform with board values.
    """

    if not self.board.is_valid():
      raise ValueError("the given size or color doesn't conforms with the board")

    moves = []

    while(self.board.get_distinct_colors() > 1):
      best_color = 0
      best_count = -1

      for color in range(1, self.board.m + 1):
        count = self.board.get_connected_tiles(color)
        if best_count < count:
          best_count = count
          best_color = color

      self.board.get_connected_tiles(best_color, apply_color=True)
      moves.append(best_color)

    return moves


if __name__ == "__main__":
  n = int(input("n: "))
  m = int(input("m: "))

  board = []
  for i in range(n):
    input_str = input(f"give row {i + 1}: ")
    board.append([int(x) for x in input_str.split()])


  greedy = GreedySolution(n, m, board)

  moves = greedy.get_moves()
  print(f"number of moves: {len(moves)}")
  print(f"moves: {moves}")
