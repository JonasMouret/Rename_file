import os 
import os.path
  
# Function to rename multiple files 

def main(): 
    print("-" * 38)
    print("|    Welcome to RenameFiles Alpha    |")
    print("-" * 38 + "\n")
    
    i = input("Enter the number you would like to start ")
    i = int(i)
    path = input('Enter the path of the folder : ')
    if path.endswith(''):
        path +=('/')
    file_filter = input('Enter a filter to the file to rename (ex: if you would like to rename all the file whose start with test (test0001.jpg) enter "test" Leave it blank for no filter) : ')
    new_name = input('Enter the new name of the file : ')
    file_format = input('Enter the file format (jpg, tif, avi...) : ')

    if (file_filter == '') :
        for filename in os.listdir(path):
            dst = new_name + str(i) + file_format
            src = path + filename 
            dst = path + dst 
            os.rename(src, dst) 
            i += 1
    else:         
        for filename in os.listdir(path):
            if filename.startswith(file_filter):
                dst = new_name + str(i) + file_format
                src = path + filename 
                dst = path + dst 
                os.rename(src, dst) 
                i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 