chicken = 0
while True:
    rabbit = 35 - chicken
    if 2 * chicken + 4 * rabbit == 100:
        print('雞有 {} 隻, 兔有 {} 隻'.format(chicken, rabbit))
        break
    chicken += 1