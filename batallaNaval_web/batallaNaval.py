import random

def initialiseGrid():
    x_cord = 4
    y_cord = 5
    grid = [["O"] * y_cord] * x_cord  #tablero de 4 lineas por 5 columnas 
    for i in range(x_cord):      #para evitar aliasing
        grid[i] = ["O"] * y_cord
    return grid

def displayGrid(grid):
    for row in grid:
        print("\t".join(row))
    print()

def validateRow(row):
    if not row.isdigit(): #check de presencia y rango
        return False
    if int(row) < 0 or int(row) > 3: #rango check
        return False
    return True

def validateCol(col):
    if not col.isdigit(): #check de presencia y rango
        return False
    if int(col) < 0 or int(col) > 4: #rango check
        return False
    return True

def checkResult(grid, row, col, ship_row, ship_col, won):
    if ship_row == row and ship_col == col: #el jugador adivino correctamente
        grid[row][col] = "S"
        won = True
    else:
        grid[row][col] = "X" #adivino erroneamente

    return won