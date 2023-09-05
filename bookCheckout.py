import database
from datetime import date

'''Written by F231337 on 5/Dec/2022
This module contains functions used to take books oout for loan, if the book is unavailable it suggests a reservation or to checkout another copy'''


def checkoutOption(book_toloan,id_borrower):
    global lasttransac_list
    global bookid
    bookid=book_toloan
    global membid
    membid=id_borrower
    '''Takes BookID and memberID as input. Checks thatthe input is valid then looks at the book's reseervation history 
    to determine if it can be checked out and returns a message describing reservation info of that book.'''
    book_info_lines = database.getBookInfo()  #get info from txt file
    try:
        given_mID=int(id_borrower)  #if memb id field is non-int string: converting to int raises error
    except:
        return 'Input Invalid'
    #bookid and memberid:check if inputs are valid: interval comparison and looking for any line in book_info.txt that starts with 'bookid/'
    if (1000 <= given_mID <= 9999) and any(item.startswith(book_toloan+"/") for item in book_info_lines):  #CHECK (member is between 1000 and 9999 AND book appears in the bookinfo list)
        today = date.today() 
        todaysdate=today.strftime("%d.%m.%Y")
        log_lines=database.getLogInfo()

        #check if theres been ANY transactions done to the book entered
        if any(log.startswith(book_toloan+"/") for log in log_lines):  #book has had some transactions done with it
            bookid_loglines=[log for log in log_lines if log.startswith(book_toloan+"/")]  #gets all transactions for book usng book id
            global last_transac
            last_transac=bookid_loglines[-1]
            #if book is currently reserved, it is still on loan by someone ELSE and not yet AVAILABLE: cannot be checked out
            if 'LOANED' in last_transac:
                #find out who its loaned to:
                lasttransac_list = last_transac.split("/")
                return 'Book Loaned'
            elif 'RESERVED'in last_transac:
                return 'Book Reserved'
            elif 'AVAILABLE' in last_transac:  
            #check if book was reserved BEFORE AVAILABLE: only the member who RESERVED it, can check out
                second_tolasttransac=bookid_loglines[-2]
                secToLastList=second_tolasttransac.split("/")  
                if ('RESERVED' in second_tolasttransac) and (secToLastList[1]==id_borrower):  #check if the book was reserved by this member
                    new_log_checkout=book_toloan+"/"+id_borrower+"/"+id_borrower+"/"+todaysdate+"/None/LOANED/None"
                    database.addLogInfo(new_log_checkout)
                    return 'Checkout Successful'
                elif 'RESERVED' not in second_tolasttransac:   #the book wasn't reserved while it was on loan: available
                    new_log_checkout=book_toloan+"/"+id_borrower+"/"+id_borrower+"/"+todaysdate+"/None/LOANED/None"
                    database.addLogInfo(new_log_checkout)
                    return 'Checkout Successful'
                else:
                    return 'Book Reserved'
                
        else: #then book must be available for checkout, book has NEVER been loaned, AVAILABLE or reserved
            new_log_checkout=book_toloan+"/"+id_borrower+"/"+id_borrower+"/"+todaysdate+"/None/LOANED/None"
            database.addLogInfo(new_log_checkout)
            return 'Checkout Successful'
    else:
        return 'Input Invalid'
   


def reserve_book():
    '''Runs if the user wants to reserve a book, updates the log file using todays date'''
    today = date.today() 
    todaysdate=today.strftime("%d.%m.%Y")
    res_statement=bookid+"/"+membid+"/"+lasttransac_list[0]+"/None/None/RESERVED/"+todaysdate #append this as new line to logfile
    database.addLogInfo(res_statement)
 


def checkout_other(book_toloan):
    '''looks for another copy using the given bookid as an argument, returns whether copy was found or not'''
    today = date.today() 
    todaysdate=today.strftime("%d.%m.%Y")
    book_info_lines = database.getBookInfo()
    log_lines=database.getLogInfo()
    bID_Line=[x for x in book_info_lines if x.startswith(book_toloan+"/")]   #find line in bookinfo that begins with bookid
    list_of_bookinfo=bID_Line[0].split("/")  #split the line into parts
    #get BOOK TITLE AND AUTHOR OF BOOKID ENTERED 
    booktitle=list_of_bookinfo[2]
    author=list_of_bookinfo[3]
    for line in book_info_lines:
        if ((booktitle in line) and (author in line)) and (line.startswith(book_toloan+"/") == False):   #another copy of book (different id but same title and author)
        #  search LOGFILE up until a line with the bookid of the found line is found: from that line: 
            #check if theres been ANY transactions done to the book entered
            global new_log_checkout
            new_log_checkout = list_of_bookinfo[0] + "/" + membid + "/" + membid + "/" + todaysdate + "/None/LOANED/None"
            if any(log.startswith(book_toloan+"/") for log in log_lines):  #check book has had some transactions done with it
                reversed_loglines=log_lines.reverse()  
                last_transac=next(log for log in reversed_loglines if log.startswith(book_toloan+"/"))  #gets only 1st occurence of a line in list that has bookid
                #the reverse gives us the last occurrence which = latest transaction for bookid = loan availability of book
                if 'AVAILABLE' in last_transac:   #book not loaned or reserved      
                    return 'A Copy'
            else: #then book must be available for checkout, book has NEVER been loaned, AVAILABLE or reserved
                return 'A Copy'

    def checkout_copy():
        '''checkout the other copy'''
        database.addLogInfo(new_log_checkout)



