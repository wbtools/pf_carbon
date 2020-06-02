# -*- coding: utf-8 -*-
from weibo.weibo_login import wblogin
from weibo.weibo_sender import WeiboSender
from weibo.weibo_message import WeiboMessage

if __name__ == '__main__':
    (wei_session, uid) = wblogin()
    if uid is not None:
        wei_session.get('http://weibo.com/')
        weibo = WeiboMessage("考一建二建的联系我【17621166911】")
        WeiboSender(wei_session, uid).send_weibo(weibo)
