# -*- coding: utf-8 -*-

# https://github.com/antfu/bopomofo
from bopomofo import to_bopomofo

print('==============================')
print('     輸入「stop」來結束程式')
print('==============================')

while True:
  query = input('請輸入中文: ')
  if query == 'stop':
    break
  print('相對應注音:', to_bopomofo(query))
  print('==============================')