import os
import shutil

from_dir="D:/f1"
to_dir="D:/Army"

listoffiles= os.listdir(from_dir)
print(listoffiles)

for file in listoffiles:
 name, est= os.path.splitext(file)
 print(name)
 print(est)

 if est== " ":
  continue
 if est in [".gif",".png",".jpg", "jpeg","jfif"]:
  path1=from_dir+"/"+file
  path2=to_dir+"/"+"imagefiles"
  path3=to_dir+"/"+"imagefiles"+"/"+file
  if os.path.exists(path2):
   print("Moving The File!!")
   shutil.move(path1,path3)
  else:
   os.makedirs(path2)
   print("Moving The File!!")
   shutil.move(path1,path3)
