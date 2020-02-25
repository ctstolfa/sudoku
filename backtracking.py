
board = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
		 [2, 8, 9, 0, 0, 4, 0, 0, 0],
		 [3, 4, 6, 2, 0, 5, 0, 9, 0],
		 [6, 0, 2, 0, 0, 0, 0, 1, 0],
		 [0, 3, 8, 0, 0, 6, 0, 4, 7],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 9, 0, 0, 0, 0, 0, 7, 8],
		 [7, 0, 3, 4, 0, 0, 5, 6, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def backtrack(grid):
	# iterates through board
	for i in range(0, 81):
		row = i // 9
		col = i % 9
		# next unsolved point
		if grid[row][col] == 0:
			break

	# check if grid complete
	if grid[row][col] != 0:
		return True

	# tries each number at the point
	for num in range(1, 10):
		# checks if row contains num
		if num not in grid[row]:
			# checks if col contains num
			if num not in [c[col] for c in grid]:
				# block that contains the current point
				block = [c[slice(col - col % 3, (col - col % 3) + 3)] for c in
						 board[slice(row - row % 3, (row - row % 3) + 3)]]
				# checks if num is in the block
				if num not in block:
					# changes point to current num
					grid[row][col] = num
					# recurse to next unsolved point
					if backtrack(grid):
						return True
					# if its not solved undo
					grid[row][col] = 0
	# backtrack
	return False


backtrack(board)
print()
for r in board:
	print(r)
