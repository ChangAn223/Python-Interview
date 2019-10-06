## Flask请求流程

http请求-->Ngix-->WSGI-->web框架

请求进入Flask，flask调用__call__方法：
```python
    def __call__(self, environ, start_response):
        """The WSGI server calls the Flask application object as the
        WSGI application. This calls :meth:`wsgi_app` which can be
        wrapped to applying middleware."""
        return self.wsgi_app(environ, start_response)
```

实际调用wsgi_app方法：
```python
    def wsgi_app(self, environ, start_response):
        """..."""
        ctx = self.request_context(environ)
        error = None
        try:
            try:
                ctx.push()
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:  # noqa: B001
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)
```

首先调用request_context方法创建请求上下文ctx。然后做相应的处理，最后请求上下文ctx出栈。
可任意看到其实request_contect方法实际上就是创建返回的请求上下文对象RequestContext。

```python
    def request_context(self, environ):
        """..."""
        return RequestContext(self, environ)
```

进入RequestContext去看，就是封装了一个Request对象，并提供了push，pop方法。

```python
class RequestContext(object):
    def __init__(self, app, environ, request=None, session=None):...

    def push(self):...
    
    def pop(self, exc=_sentinel):...
```

创建了请求上下文对象，接下来调用 ctx.push()方法将它推入栈中，full_dispatch_request()方法就是对请求进行分发，更具请求调用相应的视图函数做处理，得到响应内容，再将响应返回。最后是调用ctx.auto_pop方法将这个请求上下文推出栈(auto_pop方法进行了异常处理然后调用pop方法出栈)。

再视图函数或其他地方需要用到当前请求相关内容时，是从flask导入request。用到session也是从flask导入，如下：
```python
from flask import session, request
```
实际上是从flask框架的globals.py里导入的。这个模块里有如下全局变量：
```python
# context locals
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, "request"))
session = LocalProxy(partial(_lookup_req_object, "session"))
g = LocalProxy(partial(_lookup_app_object, "g"))
```

导入request实际上是导入的一个代理对象，对request的操作都是通过这个代理对象去操作的。类似threading.Local()，这个代理对象也实现了线程隔离。