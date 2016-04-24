vcl 4.0;

# Default backend definition. Set this to point to your content server.
#后端的HTTP服务器IP和端口
backend default {
    .host = "127.0.0.1";
    .port = "8001";
}

#设置清理缓存的IP
acl purgers {
    "127.0.0.1";
}

sub vcl_recv {
    if (req.method == "PURGE") {    # PURGE请求的处理
        if (!client.ip ~ purgers) {
            return(synth(405,"Method not allowed"));
        }
        #清理缓存
        return(purge);
    }

    if (req.method != "GET" && req.method != "HEAD") {
        return (pass);
    }
     #不缓存认证信息
    if (req.http.Authorization ) {
        return (pass);
    }
    #不正常的访问不缓存
    if (req.method != "GET" &&
            req.method != "HEAD" &&
            req.method != "PUT" &&
            req.method != "POST" &&
            req.method != "TRACE" &&
            req.method != "OPTIONS" &&
            req.method != "PATCH" &&
            req.method != "DELETE") {
        return (pipe);
    }
    return (hash);
}

sub vcl_backend_response {
}


sub vcl_deliver {
 if (obj.hits > 0) {
        #如果命中缓存 Response Headers x-cache-lookup= MemCache
        set resp.http.x-cache= "MemCache";
    } else {
        set resp.http.x-cache= "MISS";
    }
    #删除Response Headers 部分信息
    #unset resp.http.Server;
    #unset resp.http.X-Drupal-Cache;
    #unset resp.http.X-Varnish;
    #unset resp.http.Via;
    #unset resp.http.Age;
    #unset resp.http.Link;
}