# -*- coding: utf-8 -*-
import database
from datetime import date
'''Written by F231337 on 5/Dec/2022
This module contains functions used to return books that were on loan.'''

def returnOption(book_toloan):
    '''EXPLAIN FUNC'''
    book_info_lines = database.getBookInfo()
    if any(item.startswith(book_toloan+"/") for item in book_info_lines):  #check if bookid entered exists in book_info.txt
        log_lines=database.getLogInfo()
        #check if book is AVAILABLE 
        #check if theres been ANY transactions done to the book entered
        if any(log.startswith(book_toloan+"/") for log in log_lines):  #check book has had some transactions done with it
            reversed_loglines=log_lines.reverse()  
            last_transac=next(log for log in reversed_loglines if log.startswith(book_toloan+"/"))  #gets only 1st occurence of line in logfile that has bookid
            #the reverse gives us the last occurrence which = latest transaction for bookid = latest loan availability of book
            
            if 'LOANED' in last_transac:
                today = date.today() 
                todaysdate=today.strftime("%d.%m.%Y")
                last_tlist=last_transac.split("/")
                id_borrower=last_tlist[1]
                checkout_date=last_tlist[3]
                new_log=book_toloan+"/"+id_borrower+"/None/"+checkout_date+"/"+todaysdate+"/AVAILABLE/None"
                database.addLogInfo(new_log)
                return 'BRet'  #AVAILABLE book successfully
            elif 'RESERVED'in last_transac:
                return 'BRes'   #error msg if book reserved
            elif 'AVAILABLE' in last_transac:   
                return 'BA'  #book is available, last transaction was to return: error msg
        else:
            return 'BA' #book is available, as no transactions done with it: error msg
    else:
        return 'II'  #invalid id: error msg
        
