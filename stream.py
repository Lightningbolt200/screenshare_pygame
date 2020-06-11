import socket
import pyscreenshot as ImageGrab
import math
from pickle import dumps


def take_screenshot(conn):
    while 'recording':
        im = ImageGrab.grab()
        convbyte=bytearray(im.tobytes())
        size=len(convbyte)
        repeat=size/1024
        repeat=math.ceil(repeat)
        c=0
        d=1024
        flag=0
        print(repeat)
        width,height=im.size
        rwh = (repeat, width, height)
        rwh = str(rwh)
        rwh+= ' '*(50-len(rwh))
        conn.send(str(rwh).encode())
        for i in range(repeat):
            tosend=convbyte[c:d]
            conn.send(tosend+b'\x00'*(1024-len(tosend)))
            c=c+1024
            d=d+1024
            flag=flag+1
        print(flag,len(convbyte))
        

def main(host='127.0.0.1',port=8000):
    sock=socket.socket()
    sock.bind((host,port))
    try:
        sock.listen(1)
        print('server initialized')
        while 'connected':
            conn,addr=sock.accept()
            print('Client connected IP:', addr)
            take_screenshot(conn)
    finally:
        sock.close()

        
if __name__ == '__main__':
    main()
