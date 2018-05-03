# import httplib
# httplib.HTTPConnection.debuglevel = 1 
# import urllib

# data = urllib.urlopen('http://diveintomark.org/xml/atom.xml').read()    
# print data

# import httplib
# httplib.HTTPConnection.debuglevel = 1                             
# import urllib2
# request = urllib2.Request('http://google.com') 
# opener = urllib2.build_opener()                                   
# feeddata = opener.open(request).read()   


# import urllib2, httplib
# httplib.HTTPConnection.debuglevel = 1
# request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
# request.add_header('Accept-encoding', 'gzip')        
# opener = urllib2.build_opener()
# f = opener.open(request)
# compresseddata = f.read()    
# len(compresseddata)


def openAnything(source, etag=None, lastmodified=None, agent=USER_AGENT):
    # non-HTTP code omitted for brevity
    if urlparse.urlparse(source)[0] == 'http':                                       
        # open URL with urllib2                                                     
        request = urllib2.Request(source)                                           
        request.add_header('User-Agent', agent)                                      
        if etag:                                                                    
            request.add_header('If-None-Match', etag)                                
        if lastmodified:                                                            
            request.add_header('If-Modified-Since', lastmodified)                    
        request.add_header('Accept-encoding', 'gzip')                                
        opener = urllib2.build_opener(SmartRedirectHandler(), DefaultErrorHandler()) 
        return opener.open(request)                   