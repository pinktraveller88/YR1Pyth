The book_info file holds information about books purchased by for libary, sorted into:
Book_id/MemberID/Genre/Title/Author/Price/PurchaseDate

The log file holds trasnaction info, sorted into:
Book_id/MemberID/LoanedToMemberID/CheckoutDate/ReturnDate/ReservationInfo/ReservationDate

The MemberID field logs the member who performed the transaction. 
The LoanedToMemberID logs the member who has the book on loan.

Loaned Book transactions do not log a reservation date or a return date (as the book is currently on loan and not AVAILABLE yet) so these fields are not filled. 
Reserved book transactions do not log a return date (as the book is currently on loan and not AVAILABLE yet) or a checkout date (the book is on loan so cannot 
be checked out) so these fields are not filled. 
AVAILABLE book transactions do not log a LoanedToMemberID (as the book is AVAILABLE, it is no longer on loan) or a reservation date so these fields are not filled. 


