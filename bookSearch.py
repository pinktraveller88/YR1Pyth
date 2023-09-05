'''Written by F231337 on 5/Dec/2022
This module contains functions used to search for books that have been purchased by the library
the argument is a search term, return output
take book title as search input, return list of books (case insensitive or return similar results)
#each book returned has to have all its data shown with it: title,id,genre,author,loanAv'''

import database

def searchOption(search_term):
    '''takes the argument searched: book title in the GUI, accesses the book info file and returns all the books that have the same title'''
    list_oftuples=[] 
    combList=[]  #log file and book_info file info combined for the search result
    for line in database.getBookInfo():  
        print(line)
        textLine=line.split("/") 
        #search is case insensitive, textLine[2] refers to the book TITLE field 
        print(textLine[2].lower(),search_term.lower())
        if textLine[2].lower().find(search_term.lower()) != -1:   #if the search term is SOMEWHERE within the current book title
            id_string=textLine[0]+"/"  
            fileline=database.getLogInfo() #each line in logfile becomes an elemnt in a list called fileline
            endslice=len(id_string)
            lines_withbookID=[row for row in fileline if row[0:endslice] == id_string]  #get a sublist of items in 'logfile.txt' that begin with bookID+"/"
            if lines_withbookID != []:
                lastelemList=lines_withbookID[-1].split("/")  #returns LATEST transaction for the bookID
                #:shows whether book is now on loan, AVAILABLE or reserved!!
                combList=textLine[0:4] 
                combList.append(lastelemList[5]) #combine info from book_info file:First4Fields WITH log file:ReservationInfo to make 5 FIELDS
            else:   #book result has no logs in log file
                combList=textLine[0:4]
                combList.append("AVAILABLE")
            list_oftuples.append(combList)  
    return list_oftuples  #will be empty if search term wasnt found anywhere




'''NOTE: You can use the following values to test this function.

#both titles contain 'dune', 'AVAILABLE' might be a different state depending on whether checkout/reserve has been used

# searchOption(dune) should return 
#[[1,'Sci-Fi',Dune','Frank Herbert','AVAILABLE'],[26,'Sci-Fi','Son's of Dune','Frank Herbert','AVAILABLE]].   

# searchOption(end) should return 
# [[6,Sci-Fi,Ender's Game,Orson Scott Card,'AVAILABLE'],
[9,Sci-Fi,Ender's Game,Orson Scott Card,'AVAILABLE'],[14,Sci-Fi,Ender's Game,Orson Scott Card, 'LOANED'],
[20,Sci-Fi,Ender's Game,Orson Scott Card,'AVAILABLE']].

#search_term = 'abcdefg'
# searchOption(search_term) should return [].
'''
