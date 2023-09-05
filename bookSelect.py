'''Written by F231337 on 5/Dec/2022
produce a recommend list: provide the budget find out popular book titles, recommend genres to purchase new book titles
#suggest how many book copies the library would purchase for each genre, based on budget
#Based on this log, the system can suggest the purchase list.
'''
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import database



#fig=plt.figure()  #inside can do figsize=(5,5)
#plt.style.use("")
#plt.savefig('myplot.png')
#most checkout and returned
#most pop genres: 10% of budget to fiction
#graph for genres, top bk yitles 
#explanation of test function on learn: 
#main app v3 shows how to make graph pop up
#main app v4 shows how to embed graph nto tkinter interface


#2 different graphs: bar chart for how many times certain book genres AND then book titles were loaned

def getinfo(budget):
    '''Takes the budget as input from the GUI, calls each function and uses the budget in calc_budget_perc().
    This function uses information from Book_Info.txt and logfile.txt to create a 
    list of unique book titles and genres, then map them to how many times each book
    has been loaned or reserved. The keys are the unique books and the values represent 
    their popularity. These are passed into another function to make the graph.
    '''
    #GET INFO FOR BOOK TITLE CHART
    book_info_lines = database.getBookInfo()
    booktitles=[(title.split("/"))[2] for title in book_info_lines]
    uniquetitles=list(set(booktitles))
    dictTitleFreq = dict.fromkeys(uniquetitles, 0)
    bookIDs=[(ids.split("/"))[0] for ids in book_info_lines]
    log_lines = database.getLogInfo()

    for book in bookIDs:
        #use transaction log to determine popular titles
        bookid_loglines=[log for log in log_lines if log.startswith(book+"/") == True and ('LOANED' in log or 'RESERVED' in log)]  
        bookline=[line for line in book_info_lines if line.startswith(book+"/") == True ]
        splitln=bookline[0].split("/")
        booktitle=splitln[2] #book title field        
        dictTitleFreq[booktitle] = dictTitleFreq.get(booktitle) + len(bookid_loglines)

    #GET INFO FOR BOOK GENRE CHART
    loansForBktl=[*dictTitleFreq.values()]
    #using dictionary to map values together: x and y values on the bar chart
    bookgenres=[(genre.split("/"))[1] for genre in book_info_lines]
    uniquegenres=list(set(bookgenres))
    dictGenreFreq = dict.fromkeys(uniquegenres, 0)

    for book in bookIDs:
        #use transaction log to determine popular genres
        bookid_loglines=[log for log in log_lines if log.startswith(book+"/") == True and ('LOANED' in log or 'RESERVED' in log)]  #gets all transactions for book usng book id
        bookline=[line for line in book_info_lines if line.startswith(book+"/") == True]
        splitln=bookline[0].split("/")
        bookgenre=splitln[1] #book genre field       
        dictGenreFreq[bookgenre] = dictGenreFreq.get(bookgenre) + len(bookid_loglines)
    
    loansforBgGnr=[*dictGenreFreq.values()]

    create_graph(uniquetitles,loansForBktl,uniquegenres,loansforBgGnr,budget)

def create_graph(a:list,b:list,c:list,d:list,budg):
    '''Ths function takes lists of unique book titles and book genres with the 
    lists of how many times each title and genre has been loaned or reserved: as arguments.
    Using this, it creates 2 bar graphs displaying the popularity of book titles and genres
    '''
    width = 0.4
    #first subplot
    plt.subplot(1, 2, 1)
    plt.bar(a, b, width=width)
    plt.xlabel("Book Titles")
    plt.ylabel("Number of Books Loaned and Reserved")
    plt.title("Popularity of Book Titles")
    plt.xticks(rotation=55)
    plt.grid(True)
    #second subplot
    plt.subplot(1, 2, 2)
    plt.bar(c, d, width=width)
    plt.xlabel("Book Genres")
    plt.ylabel("Number of Books Loaned and Reserved")
    plt.title("Popularity of Book Genres")
    plt.grid(True)
    plt.show()
    calc_budget_perc(budg,a,b,c,d)


def calc_budget_perc(budg,listttls,ttlsvals,listgnrs,gnrsvals):
    '''calculates % of budget to a genre, calc % of that % to a book title, from 
    that find how many copies for each book title'''
    budget=int(budg)
    #PERC OF BUDGET TO EACH GENRE
    #get sum of loansforBgGnr
    #find fraction of each genre: (each val in dictGenreFreq/total) *100 to get percetage
    #assign percentage to that key
    #plot is listgnrs against percentagesgenres
    dictGenrePerc = dict.fromkeys(listgnrs, 0)
    sumofValues=sum(gnrsvals)
    for gen in listgnrs:
        val_indict=listgnrs.get(gen)
        frac=val_indict/sumofValues
        perc=frac*100
        dictGenrePerc[gen] = dictGenrePerc.get(gen) + perc  #map genres to their budget percentages
    percentagesgenres=[*dictGenrePerc.values()]


    


    plt.subplot(2, 1, 1)
    #how many book copies for each genre
    
    #PERC OF BUDGET TO EACH GENRE
    plt.subplot(2, 2, 1)


    #PERC TO EACH BOOK TITLE FOR FANTASY, store in diff variables: how many copies of each book title based on price
    plt.subplot(2, 2, 2)


    #PERC TO EACH BOOK TITLE FOR MYSTERY
    plt.subplot(2, 2, 2)

    #PERC TO EACH BOOK TITLE FOR SCIFI
    plt.subplot(2, 2, 2)
    



'''%of budget is shown using pie chart'''

'''
'''
