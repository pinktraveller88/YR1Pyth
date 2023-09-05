'''Written by F231337 on 5/Dec/2022
This module contains shared functions which allow the other modules to interact with the data files: Book_Info.txt and logfile.txt
code from today's lecture has info about testing db funcs: 
'''

def getBookInfo():
    '''explain func'''
    bookinfo=open("Book_Info.txt")
    text=bookinfo.read()
    searchInLines = text.split("\n")  #returns a list containing each line in file as list item
    bookinfo.close()
    return searchInLines

def getLogInfo():
    '''explain func'''
    loginfo=open("logfile.txt")
    text=loginfo.read()
    searchInLines = text.split("\n")
    loginfo.close()
    return searchInLines

def addLogInfo(add_item):
    '''explain func'''
    loginfo=open("logfile.txt","a")
    loginfo.write(add_item+'\n')
    loginfo.close()



