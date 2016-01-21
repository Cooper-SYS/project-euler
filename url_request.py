# coding:utf-8
import urllib2
import socket
import cookielib
import gzip
import StringIO


def unzip(data):
    data = StringIO.StringIO(data)
    gz = gzip.GzipFile(fileobj=data)
    data = gz.read()
    gz.close()
    return data

class Ajax:
    enable_proxy = False
    proxy_protocol = 'http'
    proxy_dom = '127.0.0.1:8888'
    timeout = 5
    '''
    def __init__(self,enable_proxy,proxy_protocol,proxy_dom,timeout):
        if enable_proxy:
            self.proxy_protocol = proxy_protocol
            self.proxy_dom = proxy_dom
        else:
            enable_proxy = False
        self.timeout = timeout
    '''        
        
    def ajax(self,url):
        
        if self.enable_proxy:
            proxy_handler = urllib2.ProxyHandler({self.proxy_protocol:self.proxy_dom})
        else:
            proxy_handler = urllib2.ProxyHandler({})
        
        
        '''
        使用 urllib2.install_opener() 会设置 urllib2 的全局 opener 。
        这样后面的使用会很方便，但不能做更细粒度的控制，比如想在程序中使用两个不同的 Proxy 设置等。
        比较好的做法是不使用 install_opener 去更改全局的设置，
        而只是直接调用 opener 的 open 方法代替全局的 urlopen 方法。
        '''
        opener = urllib2.build_opener(proxy_handler)
        '''
        使用 urllib2 时，可以通过下面的方法把 debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试，
        有时可以省去抓包的工作
        
        
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)

        urllib2.install_opener(opener)
        '''
        
        #在老版 Python 中，urllib2 的 API 并没有暴露 Timeout 的设置，要设置 Timeout 值，只能更改 Socket 的全局 Timeout 值。
        #socket.setdefaulttimeout(10) # 10 秒钟后超时
        urllib2.socket.setdefaulttimeout(self.timeout) # 另一种方式

        #在 Python 2.6 以后，超时可以通过 urllib2.urlopen() 的 timeout 参数直接设置。
        #response = urllib2.urlopen('http://www.google.com', timeout=10)
        
        '''
        要加入 header，需要使用 Request 对象：
        对有些 header 要特别留意，服务器会针对这些 header 做检查
        User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
        Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。常见的取值有：
            application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
            application/json ： 在 JSON RPC 调用时使用
            application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
        在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
        '''
        request = urllib2.Request(url)
        #request.add_header('User-Agent', 'fake-client')
        
        '''
        对于 200 OK 来说，只要使用 urlopen 返回的 response 对象的 getcode() 方法就可以得到 HTTP 的返回码。但对其它返回码来说，urlopen 会抛出异常。这时候，就要检查异常对象的 code 属性了：
        '''
        encoding = 'gbk'
        try:
            resp = urllib2.urlopen(request)
            header = resp.info()
            if 'Content-Encoding' in header and header['Content-Encoding'] == 'gzip':
                content = unzip(resp.read()).decode(encoding,'ignore')
            else:
                content = resp.read().decode(encoding,'ignore')
            print content
        except urllib2.URLError, e:
            print 'urllib2.URLError:' + str(e.reason)
        except urllib2.HTTPError, e:
            print 'urllib2.HTTPError:' + str(e.code)
        
        

        
url = 'http://www.4493.com/siwameitui/'  
ajax = Ajax()
ajax.ajax(url)

'''
urllib2 默认情况下会针对 HTTP 3XX 返回码自动进行 redirect 动作，无需人工配置。要检测是否发生了 redirect 动作，只要检查一下 Response 的 URL 和 Request 的 URL 是否一致就可以了。
response = urllib2.urlopen('http://www.google.cn')
redirected = response.geturl() == 'http://www.google.cn'
'''

'''
urllib2 对 Cookie 的处理也是自动的。如果需要得到某个 Cookie 项的值，可以这么做：
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.google.com')
for item in cookie:
    if item.name == 'some_cookie_item_name':
        print item.value
'''
        
'''                
urllib2 只支持 HTTP 的 GET 和 POST 方法，如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。虽然如此，我们还是能通过下面的方式，使 urllib2 能够发出 PUT 或 DELETE 的请求，这种做法虽然属于 Hack 的方式，但实际使用起来也没什么问题。：
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)
'''


'''
如果不想自动 redirect，除了使用更低层次的 httplib 库之外，还可以自定义 HTTPRedirectHandler 类。
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass

opener = urllib2.build_opener(RedirectHandler)
opener.open('http://www.google.cn')
'''