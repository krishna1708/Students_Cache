from student import *
from time import sleep

def print_cache(cache):
    for i, item in enumerate(cache.item_list):
        print ("index: {0} "
               "Student: {1}    "
               "Class: {2}      "
               "Marks: {3}      "
               "Entry_Timestamp: {4}".format(i,
                                       item.Student,
                                       item.Class,
                                       item.Marks,
                                       item.timestamp))
one = LRUCacheItem('Jio', 'A-1', '90')
two = LRUCacheItem('Leo', 'A-2', '92')
three = LRUCacheItem('Rup', 'A-3', '64')
four = LRUCacheItem('JoG', 'A-4', '76') 
five = LRUCacheItem('Smt', 'A-3', '81')
six = LRUCacheItem('Ram', 'A-4', '55')

dict_of = {'Jio': one, 'Leo': two, 'Rup': three, 'JoG': four, 'Smt': five, 'Ram': six}

print "Initial cache items."

cache = LRUCache(length=5, delta=5)
cache.insertItem(one)
sleep(1)
cache.insertItem(two)
sleep(1)
cache.insertItem(three)
cache.insertItem(four)
cache.insertItem(five)
cache.insertItem(six)
print_cache(cache)
print "#" * 20
for i in range (100):
    check = raw_input("Do you want to continue (Y/N): ")
    if 'Y' == check:
        name = raw_input("Enter the Existing Student Name: ")
        i = 0
        for k,v in dict_of.items():
            if k == name:
                print "Please check the cache now"
                i = 1
                sleep(1)
                cache.insertItem(v)
                print_cache(cache)
                print "#" * 20
                break
        if i != 1:
            print 'name does not exist in Cache. So Please enter valid name'
    else:
        break
'''
print "Insert a existing Student: {0}.".format(two.Student)
#sleep(1)
cache.insertItem(two)
print_cache(cache)
print "#" * 20

print "Insert another existing item: {0}.".format(two.Student)
cache.insertItem(two)
print_cache(cache)
print "#" * 20

print "Validate items after a period of time"
#sleep(6)
cache.validateItem()
print_cache(cache)
print "#" * 20
'''
