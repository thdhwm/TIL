from hw_4_4_list import list_of_book
from hw_4_4_list import rental_book

missing_book = [book for book in rental_book if book not in list_of_book]   

[print('모든 도서가 대여 가능한 상태입니다.') if missing_book == False else print(f'{book} 을 보충하여야 합니다.') for book in missing_book] 



