#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
import sys
import requests
import lxml.html
from time import sleep

def nya(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

N = 200

players = set()

for i in xrange(3):
    if i:
        sleep(1.1)
    nya('{}ページめをやります ... '.format(i+1))
    url = 'https://community.topcoder.com/tc?cc=392&sc=&sd=&cc=392&module=AlgoRank&nr={}&sr={}'.format(N, i*N+1)
    res = requests.get(url)
    if res.status_code != 200:
        nya('(ΦωΦ)＜not 200\n')
        exit(1)
    res0 = res.content.decode('utf-8')
    doc = lxml.html.fromstring(res0)
    ele = doc.xpath("//table[contains(@class, 'stat')]/tbody/tr/td[2]/a")
    for e in ele:
        players.add(e.text)
    nya('完了\n')

with open('japan', 'r') as fleobj:
    for line in fleobj.readlines():
        players.add(line.rstrip())

players = sorted(list(players))

with open('japan', 'w') as fleobj:
    for p in players:
        fleobj.write(p + '\n')

nya('(ΦωΦ)＜gitにコミット->プッシュを忘れずに！\n')
