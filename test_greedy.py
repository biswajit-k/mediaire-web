import pytest
from greedy import GreedySolution


class TestInvalidBoard:
  """ Test if board dimension or colors don't
      match with values of board
  """
  def test_empty_boad(self):
    n = 2
    m = 1
    board = []
    soln = GreedySolution(n, m, board)

    with pytest.raises(ValueError, match="the given size or color doesn't conforms with the board"):
      soln.get_moves()

  def test_invalid_size(self):
    n = 3
    m = 2
    board = [[1, 2], [1, 1]]
    soln = GreedySolution(n, m, board)

    with pytest.raises(ValueError, match="the given size or color doesn't conforms with the board"):
      soln.get_moves()

  def test_invalid_color(self):
    n = 2
    m = 2
    board = [[1, 2], [3, 1]]
    soln = GreedySolution(n, m, board)

    with pytest.raises(ValueError, match="the given size or color doesn't conforms with the board"):
      soln.get_moves()


class TestFullyConnectedBoard:
  """ Test when board is fully-connected
  """
  def test_empty_board(self):
    n = 0
    m = 0
    board = []
    soln = GreedySolution(n, m, board)

    assert soln.get_moves() == []

  def test_board(self):
    n = 2
    m = 4
    board = [[3, 3], [3, 3]]
    soln = GreedySolution(n, m, board)

    assert soln.get_moves() == []


def test_empty_board():
  n = 0
  m = 0
  board = []
  soln = GreedySolution(n, m, board)

  assert soln.get_moves() == []


def test_1x1_board():
  n = 1
  m = 3
  board = [[2]]
  soln = GreedySolution(n, m, board)

  assert soln.get_moves() == []


def test_chose_minimum_rank():
  n = 2
  m = 3
  board = [
    [1, 3],
    [2, 1]
  ]
  soln = GreedySolution(n, m, board)

  assert soln.get_moves() == [2, 1, 3]


def test_2x2_board():
  n = 2
  m = 4
  board = [
    [1, 2],
    [2, 4]
  ]
  soln = GreedySolution(n, m, board)

  assert soln.get_moves() == [2, 4]


def test_distinct_color():
  n = 3
  m = 10
  board = [
    [4, 1, 2],
    [3, 5, 9],
    [7, 6, 8]
  ]
  soln = GreedySolution(n, m, board)

  assert soln.get_moves() == [1, 2, 3, 5, 6, 7, 8, 9]

def test_challenge_example():
  n = 6
  m = 3
  board = [
    [1, 2, 1, 3, 1, 2],
    [3, 1, 3, 2, 3, 2],
    [3, 3, 2, 3, 3, 3],
    [3, 2, 1, 3, 1, 2],
    [3, 2, 1, 2, 2, 2],
    [1, 3, 1, 2, 3, 1]
  ]
  soln = GreedySolution(n, m, board)

  assert soln.get_moves() == [3, 2, 3, 1, 2, 3, 1]

