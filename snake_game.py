import random

def draw_map(snake, food):
    grid = [['.' for row in range(10)] for col in range(10)]
    for x, y in snake:   #draw snake
        grid[x][y] = 'X'  # x for snake
    for x, y in food:     #draw food
        grid[x][y] = 'F'  # f for food
    for row in grid:
        print(' '.join(row))

def movement(snake, direction, ate_food):
    x, y = snake[-1]  #access to the snake's head, so the snake can move to the given direction
    if direction == 'n':
        x -= 1
    elif direction == 's':
        x += 1
    elif direction == 'e':
        y += 1
    elif direction == 'w':
        y -= 1
    snake.append((x, y))
    if not ate_food:   #if snake did not eat
        snake.pop(0)   #remove snake's tail

def generate_food(snake):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) not in snake:  #because the food cannot be in the snake's body
            return (x, y)

def game():
    grid=[]
    snake = [(0, 0), (0, 1)]  #coordinates for snake (0,0)-> tail, (0,1) ->head
    food = [generate_food(grid)]  # coordinates for food, that appears random
    direction = ''     #initialize the variable direction as empty string
    ate_food = False   # set to false, as snake did not eat food in the beginning
    while direction != 'end':
        draw_map(snake, food)
        direction = input("Enter movement direction (n/s/e/w) or 'end' to stop: ")
        if direction in ['n', 's', 'e', 'w']:
            movement(snake, direction, ate_food)
            if snake[-1] in food:
                food.remove(snake[-1])
                food.append(generate_food(snake))
                ate_food = True
            else:
                ate_food = False
        else:
            print("Wrong direction!")
    print("Game Over!")

game()