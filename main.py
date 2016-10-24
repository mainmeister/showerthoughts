import os
import praw

def toaster(title, message):
    cmd = 'notify-send "%s" "%s"' % (title, message)
    os.system(cmd)

if __name__ == '__main__':
    toaster("This is a test", "Hello World!")
