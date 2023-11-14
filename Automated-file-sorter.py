import os,shutil 
from platform import python_version

#example: C:/----/----/----/--/
path = r'parse the path here'



file_names = os.listdir(path)



# the files name
folder_names = ['Sheets files', 'Text files', 'Document files','Pdf files','Image files', 'PowerPoint files']
choose_files = [0, 1, 2, 3, 4, 5, 6]
print('Select the type of folders:\n 0: Sheets files\n 1: Text files\n 2: Document files\n 3: Pdf files\n 4: Image files\n 5: PowerPoint files')
print('---------------------------\n')
print('Enter -1 to finish. \nNote:  Enter the numbers one by one.\n')

numbers = set()
inpt = None
while(inpt != -1):
    inpt = int(input('Enter: '))
    if inpt != -1:
     (numbers.add(inpt))if inpt>=0 and inpt <len(folder_names) else print('Please enter an acceptable value.')
     
for loob in range(0,6):
    if not os.path.exists(path + folder_names[loob]) and loob in numbers:
        print(path + folder_names[loob])  
        os.makedirs(path + folder_names[loob])
        
        
        
        
        
           
for file in file_names:
    if '.csv' in file and not os.path.exists(path + folder_names[0]+'/' + file):
        shutil.move(path + file, path +  folder_names[0]+'/' + file)
    elif '.xlsx' in file and not os.path.exists(path + folder_names[0]+'/' + file):
        shutil.move(path + file, path +folder_names[0]+'/' + file)
        
    elif '.txt' in file and not os.path.exists(path + folder_names[1]+'/' + file):
        shutil.move(path + file, path + folder_names[1]+'/' + file)
        
    elif '.docx' in file and not os.path.exists(path +  folder_names[2]+'/' + file):
        shutil.move(path + file, path + folder_names[2]+'/' + file)
        
    elif '.pdf' in file and not os.path.exists(path + folder_names[3]+'/' + file):
        shutil.move(path + file, path +folder_names[3]+'/' + file)
        
    elif '.png' in file and not os.path.exists(path + folder_names[4]+'/' + file):
        shutil.move(path + file, path + folder_names[4]+'/' + file)
        
    elif '.pptx' in file and not os.path.exists(path + folder_names[5]+'/' + file):
        shutil.move(path + file, path + folder_names[5]+'/' + file)
        
print(' Done. ')
    ## if you want add more types just add the name file in 'folder_name' if you like and be sure to index it here 
    #  put the type like these codes
    
