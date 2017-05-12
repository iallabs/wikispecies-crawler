import urllib.request
# https://docs.python.org/3/howto/urllib2.html

def curl(website):
    # website shoulb at the form 'http://google.com/'
    R = urllib.request.urlopen(website)
    return R.readlines()



# values = dict()
def request(website, values):
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(website, data)
    R = urllib.request.urlopen(req)
    return R.readlines()
    
    
