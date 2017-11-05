#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:38:01 2017

@author: Marco
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr  
 
# 第三方 SMTP 服务
mail_host="smtp.126.com"  #设置服务器
mail_user="letitwork@126.com"    #用户名
mail_pass="zhangmin1026"   #口令 
 
 
sender = 'letitwork@126.com'
receivers = ['sz547073165@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

def send_email(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host, 25)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

send_email(mail_host,mail_user,mail_pass,receivers,'椭圆曲线数字签名算法（ECDSA）的使用方法，不要告诉别人','非公开，拥有者需安全保管。通常是由随机算法生成的，说白了，就是一个巨大的随机整数，256位、32字节。大小介于1 ~ 0xFFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFE BAAE DCE6 AF48 A03B BFD2 5E8C D036 4141之间的数，都可以认为是一个合法的私钥。于是，除了随机方法外，采用特定算法由固定的输入，得到32字节输出的算法就可以成为得到私钥的方法。于是，便有了迷你私钥(Mini Privkey)，原理很简单，例如，采用SHA256的一种实现：'.encode())