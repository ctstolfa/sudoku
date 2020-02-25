import pygame

pygame.init()

window = pygame.display.set_mode((572, 642))
pygame.display.set_caption("Sudoku Solver")

board = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
		 [2, 8, 9, 0, 0, 4, 0, 0, 0],
		 [3, 4, 6, 2, 0, 5, 0, 9, 0],
		 [6, 0, 2, 0, 0, 0, 0, 1, 0],
		 [0, 3, 8, 0, 0, 6, 0, 4, 7],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 9, 0, 0, 0, 0, 0, 7, 8],
		 [7, 0, 3, 4, 0, 0, 5, 6, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#		 [5, 2, 0, 0, 0, 0, 0, 0, 0],
#		 [0, 8, 7, 0, 0, 0, 0, 3, 1],
#		 [0, 0, 3, 0, 1, 0, 0, 8, 0],
#		 [9, 0, 0, 8, 6, 3, 0, 0, 5],
#		 [0, 5, 0, 0, 9, 0, 6, 0, 0],
#		 [1, 3, 0, 0, 0, 0, 2, 5, 0],
#		 [0, 0, 0, 0, 0, 0, 0, 7, 4],
#		 [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def draw():
	x = 5
	y = 5
	font = pygame.font.Font('freesansbold.ttf', 56)
	for i in range(0, 81):
		if board[i//9][i%9] != 0:
			text = font.render(f'{board[i//9][i%9]}', True, (0, 0, 0), (255, 255, 255))
			rect = pygame.draw.rect(window, (255, 255, 255), (x, y, 60, 60))
			window.blit(text, rect)
		else:
			pygame.draw.rect(window, (255, 255, 255), (x, y, 60, 60))

		if (i + 1) % 9 != 0:
			y += 62
			if (i + 1) % 3 == 0:
				y += 3
		else:
			y = 5
			x += 62
			if (i + 1) / 9 % 3 == 0:
				x += 3
	font = pygame.font.Font('freesansbold.ttf', 54)
	cap = font.render("Press Space to Solve", True, (255, 255, 255))
	r = pygame.draw.rect(window, (0, 0, 0), (10, 575, 200, 60))
	window.blit(cap, r)

	pygame.display.update()


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
					draw()
					# recurse to next unsolved point
					if backtrack(grid):
						return True
					# if its not solved undo
					grid[row][col] = 0
					draw()
	# backtrack
	return False


on = True
start = False
time = 100
while on:
	pygame.time.delay(time)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			on = False

	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE]:
		time = 1000
		start = True

	if start:
		if time > 50:
			time -= 5
		backtrack(board)
	else:
		draw()
