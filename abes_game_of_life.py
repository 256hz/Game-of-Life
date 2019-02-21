'''
play Conway's Game of Life with given cells
'''

# list of inputs - enter keys during wait() to switch
listOfPatterns = {
	'beehive' : [[0,1], [1,2], [2,2], [3,1], [2,0], [1,0]],
	'blinker' : [[-1,0], [0,0], [1,0]],
	'eater1' : [[0,0], [1,0], [0,1], [2,1], [2,2], [2,3], [2,4], [3,4]],
	'mango' : [[1,0],[2,0], [0,1], [3,1], [1,2], [4,2], [2,3], [3,3]],
	'new' : [[1,2], [2,2], [3,2], [2,3], [3,3], [4,3], [13,2], [13,3], [12,3], [13,4]],
	'switch_engine' : [[0,0], [2,0], [2,1], [5,2], [5,3], [7,3], [5,4], [7,4], [8,4], [7,5]]
}

# grid for checking neighbors
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0,-1), (1, -1), (1, 0), (1, 1)]

def getArea(gameState):
	'''makes the grid to check 1 larger on each side than all current cells.
	Takes x,y pairs from gameState and records the highs & lows.
	I feel like there is a way to clean this up, but haven't found it yet'''
	minX, minY, maxX, maxY = 0, 0, 0, 0
	for i in gameState:
		if i[0] < minX: minX = i[0]
		if i[0] > maxX: maxX = i[0]
		if i[1] < minY: minY = i[1]
		if i[1] > maxY: maxY = i[1]
	minX -= 1
	minY -= 1
	maxX += 2
	maxY += 2
	return [(minX, minY), (maxX, maxY)]

def wait(gameState):
	'''pause between turns'''
	# print('gameState: {}'.format(gameState))
	s = input('\nenter: increment turn\nq: quit\nl: list patterns\nor input name of new pattern: ')
	if s == 'q': quit()
	elif s == '': turn(gameState)
	elif s == 'l':
		for pattern in listOfPatterns:
			print(pattern.keys())
		wait(gameState)
	else: 
		if s in listOfPatterns.keys():
			firstTurn(listOfPatterns[s])
		else: 
			print('pattern not found')
			wait(gameState)
def checkNeighbors(row, cell, gameState):
	'''does what it says on the tin'''
	friends = 0
	for friend in neighbors:
		if [row+friend[0], cell+friend[1]] in gameState:
			friends += 1
	return friends
	
def turn(gameState):
	'''increment board according to Conway's rules'''
	if gameState == '':
		print('No more cells. Game over')
		wait()
	gameState = sorted(gameState)
	area = getArea(gameState)
	minX, minY, maxX, maxY = area[0][0], area[0][1], area[1][0], area[1][1]
	rowPrint, dieList, bornList = [], [], []
	
	#game rules

	for row in range(minX, maxX):
		for cell in range(minY, maxY):
			friends = checkNeighbors(row, cell, gameState)
			if friends == 2:
				pass
			elif friends > 3 or friends < 2: 
				if [row, cell] in gameState:
					dieList.append([row, cell])
					# print('{},{} should die'.format(row, cell))
				else:
					pass
			elif friends == 3:
				if [row, cell] not in gameState:
					bornList.append([row, cell])
					# print('{},{} to be born'.format(row, cell))
	if len(dieList) > 0:
		for cell in reversed(dieList): gameState.remove(cell)
	if len(bornList) > 0: 
		for cell in bornList: gameState.append(cell)

	#update graphics and wait
	
	drawGame(gameState)
	wait(gameState)

def firstTurn(gameState):
	'''on first turn, show board only'''
	gameState = sorted(gameState)
	drawGame(gameState)	
	wait(gameState)

def drawGame(gameState):
	'''output board to text'''
	area = getArea(gameState)
	minX, minY, maxX, maxY = area[0][0], area[0][1], area[1][0], area[1][1]
	rowPrint = []
	for y in range(minY, maxY):
		rowPrint.append('')
	for x, row in enumerate(range(minX, maxX)):
		for y, cell in enumerate(range(minY, maxY)):
			if [row, cell] in gameState: rowPrint[y] += 'o '
			else: rowPrint[y] += '. '
	for x in rowPrint:
		print(x)
	
firstTurn(listOfPatterns['eater1'])
