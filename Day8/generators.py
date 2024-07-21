def my_generator():
    x = 1
    while True:
        yield x
        x += 1


practice_generator = my_generator()

print(next(practice_generator))  # 1
print(next(practice_generator))  # 2
print(next(practice_generator))  # 3



def my_generator():
    lives = 3
    while lives > 0:
        yield f"You have {lives} lives left"
        lives -= 1
    yield "Game Over"


lose_live = my_generator()



def my_generator():
    lives = 3
    while lives > 0:
        yield f"You have {lives} {'lives' if lives > 1 else 'live'} left"
        lives -= 1
    yield "Game Over"


lose_live = my_generator()



