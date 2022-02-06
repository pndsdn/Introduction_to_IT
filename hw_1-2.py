def does_brick_fit(br_h, br_w, br_d, h, w):
    brick = [br_h, br_w, br_d]
    hole = [h, w]
    brick.remove(max(brick))
    return min(brick) <= min(hole) and max(brick) <= max(hole)


brick_h = int(input('brick height: '))
brick_w = int(input('brick width: '))
brick_d = int(input('brick depth: '))
h = int(input('hole height: '))
w = int(input('hole width: '))
print(does_brick_fit(brick_h, brick_w, brick_d, h, w))
