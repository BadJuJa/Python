import glob

imdir = r'C:\Users\Guren\Downloads\потом разберусь\Images'
im_formats = ['png', 'jpg', 'jpeg']

files = []
[files.extend(glob.glob(imdir + '\**\*.' + e, recursive=True)) for e in im_formats]
for _path in files[:10]:
    print(_path[:_path.rfind('\\')])
#print(files[0])