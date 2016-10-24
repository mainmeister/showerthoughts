import os
import praw
import time

def toaster(title, message):
    cmd = 'notify-send "%s" "%s"' % (title, message)
    os.system(cmd)

def reddit():
    r = praw.Reddit('ThoughtsInShower by u/mainmeister ver 0.1 see https://github.com/mainmeister/showerthoughts for source')
    processed_subs = []
    while True:
        subr = r.get_subreddit('Showerthoughts')
        for message in subr.get_new():
            if not message.id in processed_subs:
                toaster(message.author.name, message.title)
                processed_subs.append(message.id)
        time.sleep(5)

if __name__ == '__main__':
    reddit()