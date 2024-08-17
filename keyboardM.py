import pygame as pg

def init():
    pg.init()
    win = pg.display .set_mode((40,40))

def getKey(keyName):
    result = False
    for events in pg.event.get(): pass
    keyInput = pg.key.get_pressed()
    myKey = getattr(pg, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        result = True
    pg.display.update()
    return result

def main():
    print(getKey("s"))



if __name__ == '__main__':
    init()
    while True:
        main()
