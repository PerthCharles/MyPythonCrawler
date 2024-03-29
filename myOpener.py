import http.cookiejar
import urllib.request
import urllib

# Disguised as a Browser
# Please read the references in README for more details
def makeMyOpener(head = {
    'Connection' : 'Keep-Alive',
    'Accept' : 'text/html, application/xhtml+xml, */*',
    'Accept-Language' : \
            'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q= 0.3',
    'User-Agent' : \
            'Mozilla/5.0 (Windows NT 6.3; WOW64; \
            Trident/7.0; rv:11.0) like Gecko'
    }):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener( \
                urllib.request.HTTPCookieProcessor(cj) \
             )
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)

    opener.addheaders = header
    return opener
