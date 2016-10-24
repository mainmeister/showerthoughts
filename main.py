import os
import praw
import time

def toaster(title, message):
    cmd = 'notify-send "%s" "%s"' % (title, message)
    os.system(cmd)

def reddit():
    processed_subs = []
    r = praw.Reddit('ThoughtsInShower by u/mainmeister ver 0.1 see https://github.com/mainmeister/showerthoughts for source')
    subr = r.get_subreddit('Showerthoughts')
    messages = []
    while True:
        if len(messages) == 0:
            messages = subr.get_new()
            for message in messages:
                if not message.id in processed_subs:
                    toaster(message.author.name, message.title)
                    processed_subs.append(message.id)
                    time.sleep(10)
            messages = []
        time.sleep(10)

if __name__ == '__main__':
    reddit()