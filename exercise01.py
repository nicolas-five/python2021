"""
练习01：　使用浏览器访问服务端代码，得到
一个图片展示出来。图片可自行选择
注意：图片格式响应内容格式使用
　　　Content-Type:image/jpeg
"""
from socket import *

#　接收ｈｔｔｐ请求，回复响应
def handle(connfd):
    # 接收到了浏览器发送的http请求
    request = connfd.recv(1024)
    # 请求内容
    info = request.decode().split(' ')[1]
    if info == "/1":
        filename = "1.jpeg"
    elif info == "/2":
        filename = "2.jpeg"
    elif info == "/3":
        filename = "3.jpeg"
    else:
        filename = "404.jpeg"

    # 组织ｈｔｔｐ响应格式
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:image/jpeg\r\n"
    response += "\r\n"
    with open(filename,'rb') as f:
        data = f.read()
    response = response.encode() + data
    # 　发送给浏览器
    connfd.send(response)


def main():
    sock = socket()
    sock.bind(("0.0.0.0", 8002))
    sock.listen(5)
    while True:
        # 接收浏览器连接请求
        connfd, addr = sock.accept()
        print("Connect from", addr)
        # 　处理浏览器请求
        handle(connfd)
        connfd.close()
    sock.close()


if __name__ == '__main__':
    main()
