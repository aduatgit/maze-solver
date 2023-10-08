from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(100, 100, 25, 25, 10, 10, win)
    maze.solve()
    win.wait_for_close()

main()