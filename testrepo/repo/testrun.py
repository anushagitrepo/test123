import os,sys,fnmatch
the_path=raw_input("Enter the path: ")
count=len(fnmatch.filter(os.listdir(the_path),'*'))
if(count == 0):
 new_file=os.path.join(the_path,'dummy.txt')
 f=open(new_file,'w')
 f.write("Auto generated file")
 f.close()
else:
 user_response=raw_input("Do you want new file in specified location ? y/n ")
 if(user_reponse=="y"):
  new_file=os.path.join(the_path,'dummy.txt')
  f=open(new_file,'w')
  f.write("Autogenerated file")
  f.close() 
