import re
import urllib.request
import urllib
from collections import deque
import datetime

from save import saveFile
from myOpener import makeMyOpener


# The whole process is like a BFS in a graph
'''
    queue Q
    set S
    Q.push(Start)
    S.insert(Start)

    while (!Q.empty)
        cur = Q.front()
        Q.pop()
        
        for link in cur'url
            if (link not in S)
                Q.push(link)
                S.insert(link)
'''


url =            # set your start page
LogFile =        # set your log file name
LogPath =        # set your log file path
PageDir =        # set your path to store the pages
'''
    Example:
    url = "http://news.dbanotes.net"
    LogFile = "log"
    LogPath = "/tmp/MyPythonCrawler"
    PageDir = "/tmp/MyPythonCrawler"
'''

linkcnt = 0  
linklimit = 50      # limit the number of visited pages
levelcnt = 0
levellimit = 10     # limit the depth of BFS
levelcurcnt  = 1    # two auxiliary variables
levelnextcnt = 0

ISOFORMAT = '%Y%m%d'
today = datetime.date.today()
saveFile( \
    bytes('Date: ' + today.strftime(ISOFORMAT), 'UTF-8'), \
    LogFile, \
    LogPath, \
    'ab' \
)

queue = deque()
visited = set()
queue.append(url)

oper = makeMyOpener()
while queue:
    url = queue.popleft()
    visited |= {url}
    linkcnt += 1
    if levelcurcnt > 0:
        levelcurcnt -= 1
    else:
        levelcnt += 1
        levelcurcnt = levelnextcnt
        levelnextcnt = 0

    msg = 'Already visited ' + str(linkcnt) + ' pages: \
           visiting <-- ' + url
    saveFile( \
        bytes(msg, 'UTF-8'), \
        LogFile, \
        LogPath, \
        'ab' \
    )
    print(msg)

    uop = oper.open(url, timeout = 2000)
    if 'html' not in uop.getheader('Content-Type'):
        continue

    try:
        data = uop.read().decode('UTF-8')
        saveFile( \
            bytes(data, 'UTF-8'), \
            str(linkcnt) + '.html', \
            PageDir, \
            'wb' \
        )
    except:
        print(type(exception.__name__))
        continue

    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            levelnextcnt += 1
            queue.append(x)
            saveFile( \
                bytes('  adding into queue --> ' + x, 'UTF-8'), \
                LogFile, \
                LogPath, \
                'ab' \
            )
    
    if linkcnt >= linklimit:
        break
    if levelcnt >= levellimit:
        break


