#!/usr/bin/python
# Filename: using_list.py

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist), 'items to purchase'

print 'These items are: ', # Notice the comma at end of the line

for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')

print 'My shoplist list is now', shoplist

print 'I will sort my list now'
shoplist.sort()
print 'sorted list is ', shoplist

print 'The first item I will buy is ',  shoplist[0]
oldItem = shoplist[0]
del shoplist[0]
print 'I bought the ', oldItem

print 'My shoplist list is now', shoplist
