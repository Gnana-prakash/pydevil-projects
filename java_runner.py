'''
Hi friends
This package helps you run the java programs
But the jdk must be installed
note:
unable to give input

Author:
    Gnana prakash
'''
import subprocess as s
import time as t
def Create_file_for(code):
    '''
        Its takes program as parameter and creates file with the class name automatically
        It is mandatory to call this function
        It automatically Saves the file when you directly call the "Run" method
    '''
    a=code.split()
    i=a.index('class')
    f=open(a[i+1]+'.java','w')
    f.write(code)
    f.close()
def Compile(code):
    '''
        Compiles the code by passing the program as an parameter
        It is mandatory to compile your program
        This package takes care of saving and compiling
        
    '''
    Create_file_for(code)
    a=code.split()
    i=a.index('class')
    try:
        s.check_output(['javac',a[i+1]+'.java'],shell=True)
        print('Compiled sucessfully')
        return '#sucess'
    except:
        print('Errors found in your program')
        return '#error'
    
def Run(code,*args):
    '''
        This method will run the java program
        It is compulsory to call this method in order to run your programm
    '''
    status=Compile(code)
    if status=='#error':
        return
    else:
        t.sleep(1)
        print('Output\n-------------\n')
        a=code.split()
        i=a.index('class')
        l=['java',a[i+1]]
        for item in args:
            l.append(str(item))
        
        try:
            output=s.check_output(l,shell=True)
            print(output.decode('utf-8'))
        except:
            print('Run time error')
      

    
