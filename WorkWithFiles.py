with open('raj.jpeg','rb') as rf:
    with open('raj_copy.jpeg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



#with open('raj1.jpg','rb') as rf:
#    with open('raj1_copy.jpg','wb') as wf:
#        for line in rf:
#            wf.write(line)



#with open('file.txt','r') as rf:
#    with open('file_copy.txt','w') as wf:
#        for line in rf:
#            wf.write(line)
        
        
    
    
#with open('file.txt','r') as f:    
#    size_to_read = 10
#    f_content =f.read(size_to_read)
#    print(f_content, end='')
#    
#    f.seek(0)
#    
#    f_content =f.read(size_to_read)
#    print(f_content, end='')
    
    
#with open('file.txt','r') as f:    
#    size_to_read = 10    
#    while len(f_content) >0:
#        print(f_content, end='*')
#        f_content = f.read(size_to_read)
#    
    

    


#f_contents = f.read()
#f_contents = f.readlines()
#    for line in f:
#        print(line, end='')    
#    