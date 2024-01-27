from barcode import EAN8
from barcode import ImageWriter
number = '5901234123457'
my_code = EAN8(number)
my_code.save("new_code")