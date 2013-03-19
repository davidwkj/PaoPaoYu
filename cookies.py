__author__ = 'baby'
# -*- coding: gbk -*-
from __future__ import with_statement
import ConfigParser, os,time
import cookielib, urllib2,urllib
from BeautifulSoup import BeautifulSoup
import re
def getCookie(email,pwd,loginweb):
#try:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    exheaders = [("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.3) Gecko/20101201 zhangsan")]
    opener.addheaders=exheaders
    cfg = ConfigParser.ConfigParser()
    with open("param.ini") as fobj:
        cfg.readfp( fobj)
    url_login=cfg.get(loginweb,"loginurl")
    if loginweb == 'renrenurl':
        body = (('email',email), ('password',pwd))
        req1 = opener.open(url_login, urllib.urlencode(body))
        req1=  opener.open("http://apps.renren.com/paopaoyu/?origin=104")

        soup = BeautifulSoup(req1.read())
        url=soup.find('iframe')
        surl=url['src'].replace("xiaonei.paopaoyu.cn","xiaonei.paopaoyu.cn/")
        req1=  opener.open(surl)


        soup = BeautifulSoup(req1.read())
        obj= soup.find('object')
        str= obj.contents[3]['value']
        index=str.find('&')
        uid=str[0:index].replace("my_id=","")
        reffer=obj.contents[1]['value']
        cookie =""
        for c in cj:
            cookie+=c.name+"="+c.value+";"
        print u"%s %s已经登陆成功 " % (email,uid)
        print u"请不要关闭此窗口，请耐心等待"
        print  (cookie[0:-1],uid[5:],reffer)
        return (cookie[0:-1],uid[5:],reffer)
    elif loginweb == 'baiduurl':
        '''test'''
        body = (('username',email), ('password',pwd))
        req1 = opener.open(url_login, urllib.urlencode(body))
        req1=  opener.open("http://apps.hi.baidu.com/paopaoyu/")
        print '开始登陆，请稍后1'
        pagedate=req1.read()
        print '开始登陆，请稍后2'
        indexb=pagedate.find(',flashvars:"')
        pagedate=pagedate[indexb+12:indexb+1000]
        indexb=pagedate.find(',id:"bd_swf_')
        pagedate=pagedate[:indexb-1]
        list=pagedate.split('&')
        d={}
        for aa in list:
            d[aa.split('=')[0]]=aa.split('=')[1]
        cookie =""

        for c in cj:
            cookie+=c.name+"="+c.value+";"
        uid=d['bd_sig_session_key'] +","+d['bd_sig_user'] +","+d['bd_sig_portrait'];
        print "%s 已经登陆成功 " % email
        print u"请不要关闭此窗口，请耐心等待"
        cfg = ConfigParser.ConfigParser()
        with open("param.ini") as fobj:
            cfg.readfp( fobj)
        reffer=cfg.get(loginweb,"reffer")
        fileName=d['bd_sig_user']
        fileName= 'vira/%s.txt' % fileName
        print u'参数下载到%s中' % fileName
        s=open(fileName,"w")
        s.write(ch_key(uid))
        s.close()
        return (cookie[0:-1],ch_key(uid),reffer)
        #except:
        #print u"账号密码不对，你丫认真检查,10秒后自动关闭"
        #time.sleep(10)
        #return(None,None,None)
def ch_key( s ):
    s = "%2B" + s
    r = ''
    for t in s.split('%'):
        if t <> '':
            ch = chr(int(t[:2],16))
            r = r + ch + t[2:]
    return r[1:]
if __name__ =='__main__':
    print ch_key('%2Basdhoi%2Bsadfas%2F')






