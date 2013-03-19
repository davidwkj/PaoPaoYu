# -*- coding: utf-8 -*-
import urllib
import cookielib
import urllib2
import BeautifulSoup

email = ""
pwd = ""
def getCookie(email,pwd):
    print ("强烈要求GM还我们公平的钓鱼环境")
    print ("当前版本 0.04,最后更新时间为20091107")
    print ("下载:http://code.google.com/p/paopaoyu/")
    try:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        exheaders = [("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.3) Gecko/20090824 waigua")]
        print(exheaders)
        opener.addheaders=exheaders
        url_login = 'http://passport.renren.com/PLogin.do'
        body = (('email',email), ('password',pwd))
        print(body)
        req1 = opener.open(url_login, urllib.urlencode(body))
        # req1=  opener.open("http://apps.renren.com/paopaoyu/?origin=104")

        soup = BeautifulSoup(req1.read())
        print(soup)
        url=soup.find('iframe')
        print(url)
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
        print ( u"%s %s已经登陆成功 " % (email,uid) )
        print (u"请不要关闭此窗口，耐心等待10分钟")
        return (cookie[0:-1],uid,reffer)
    except:
        print (u"账号密码不对，你丫认真检查")
        return(None,None,None)


getCookie("wangkaijunwkj@126.com","wangxiao")