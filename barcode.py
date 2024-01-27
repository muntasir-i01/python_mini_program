from barcode import EAN13
from barcode import ImageWriter
number : '5901234123457'
my_code = EAN13(number, ImageWriter())
my_code.save("new_code 1")