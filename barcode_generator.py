import barcode
from barcode.writer import ImageWriter

BARCODE_TYPE = 'code128'

DATA_TO_ENCODE = "Python le j ni sajilo pardexa yrr!"

barcode_class = barcode.get_barcode_class(BARCODE_TYPE)
generated_barcode = barcode_class(DATA_TO_ENCODE, writer=ImageWriter())

output_filename = generated_barcode.save("my_barcode")

print(f"Barcode saved as: {output_filename}.png")