import exifread

f = open(r'C:\Source\1\192409110.jpg', 'rb')
 
# Return Exif tags
tags = exifread.process_file(f)

print(tags['Image DateTime'])

print(str(tags['Image DateTime'])[:4])

print(dir(exifread.classes))

print(exifread.classes)