from maze import Maze
import unittest

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Number of columns are different"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Number of rows are different"
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Number of columns are different"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Number of rows are different"
        )

    def test_maze_removes_exit_and_entrance(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
            "Entrance wasn't opened"
        )
        self.assertEqual(
             m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
             False,
             "Exit wasn't opened"
        )

    def test_maze_reset_visited(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=0)
        self.assertEqual(
             m1._cells[0][0].visited,
             False,
             "visited does not reset on first loop"
        )
        m1._cells[0][0].visited = True
        m1._reset_cells_visited()
        self.assertEqual(
             m1._cells[0][0].visited,
             False,
             "visited does not reset on second loop"
        )

    def test_reset_visited_all_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
        unittest.main()