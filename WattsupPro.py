import os, serial
import datetime, time
import argparse
import curses
from platform import uname

EXTERNAL_MODE = 'E'
INTERNAL_MODE = 'I'
TCPIP_MODE = 'T'
FULLHANDLING = 2

class WattsUp(object):
    def __init__(self, port, interval):

        self.s = serial.Serial(port, 115200 )
        self.logfile = None
        self.interval = interval
        # initialize lists for keeping data
        self.t = []
        self.power = []
        self.potential = []
        self.current = []

    def mode(self, runmode):
        temp = '#L,W,3,%s,,%d;' % (runmode, self.interval)
        self.s.write( str.encode(temp))
        if runmode == INTERNAL_MODE:
            self.s.write('#O,W,1,%d' % FULLHANDLING)

    def log(self, logfile = None):
        print('Logging...')
        self.mode(EXTERNAL_MODE)
        if logfile:
            self.logfile = logfile
            o = open(self.logfile,'w')

        line = self.s.readline()
        n = 0
        timeout_start = time.time()
        

        while time.time() < timeout_start + args.timeout:
            if line.startswith( str.encode('#d') ):
                if args.raw:
                    r.write(line)
                fields = line.split(str.encode(','))
                if len(fields)>5:
                    W = float(fields[3]) / 10;
                    V = float(fields[4]) / 10;
                    A = float(fields[5]) / 1000;
                   
                    if self.logfile:
                        o.write('%s %d %3.1f %3.1f %5.3f\n' % (datetime.datetime.now(), n, W, V, A))  # SAVE TO LOG
                    n += self.interval
            line = self.s.readline()

        try:
            o.close()
        except:
            pass
        if args.raw:
            try:
                r.close()
            except:
                pass

def main(args):
    if not args.port:
        system = uname()[0]
        if system == 'Darwin':          # Mac OS X
            args.port = '/dev/tty.usbserial-A1000wT3'
        elif system == 'Linux':
            args.port = '/dev/ttyUSB1'
    meter = WattsUp(args.port, args.interval)
    if args.log:
        meter.log(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get data from Watts Up power meter.')
    parser.add_argument('-r', '--raw', dest='raw', action='store_true', help='output raw file')
    parser.add_argument('-o', '--outfile', dest='outfile', default='log.out', help='Output file')
    parser.add_argument('-s', '--sample-interval', dest='interval', default=1.0, type=float, help='Sample interval (default 1 s)')
    parser.add_argument('-p', '--port', dest='port', default=None, help='USB serial port')
    parser.add_argument('-t', '--timeout', dest='timeout', default=10.0, type=float, help='Timeout for experiment (default 10 s)')
    parser.add_argument('-l', '--log', dest='log', action='store_true', help='log data in real time')
    parser.add_argument('-m', '--simulation-mode', dest='sim', action='store_true', help='simulate logging by reading serial data from disk with delay of sample interval between lines')

    args = parser.parse_args()
    main(args)
