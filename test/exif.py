import exifread

f = open(r'C:\Source\1\192409110.jpg', 'rb')
 
# Return Exif tags
tags = exifread.process_file(f)

print(type(tags['Image DateTime'].values))
print('date:',tags['Image DateTime'].values)

print('date_part_of_str:',str(tags['Image DateTime'])[:4])

print('theclass',dir(tags['Image DateTime']))



data_arry=tags['Image DateTime'].values.split(" ")

print([x.split(":") for x in data_arry])