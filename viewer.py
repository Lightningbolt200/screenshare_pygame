import socket
import pygame
import numpy
from PIL import Image
import math
from pickle import loads


def main(host='127.0.0.1',port=8000):
    hieght =1920
    width = 1080
    pygame.init()
    screen=pygame.display.set_mode((width,hieght))
    clock = pygame.time.Clock()
    watching=True

    sock = socket.socket()
    sock.connect((host,port))
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            rwh = sock.recv(50).decode()
            rwh=eval(rwh)
            print(rwh)
            repeat=rwh[0]
            width=rwh[1]
            height=rwh[2]
            print(repeat)
            b=bytearray()
            flag=0
            for i in range(repeat):
                im = sock.recv(1024)
                b.extend(im)
                flag=flag+1
            print(flag,len(b))
            img = pygame.image.fromstring(bytes(b), (width, height), 'RGB')
            screen.blit(img,(0,0))
            pygame.display.flip()
            clock.tick(60)
    finally:
        sock.close()

        
if __name__ == '__main__':
    main()
