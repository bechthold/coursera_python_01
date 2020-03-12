#https://www.coursera.org/learn/diving-in-python/programming/sypSV/fail-s-maghichieskimi-mietodami

import tempfile
import os.path

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        with open(self.path_to_file, 'w') as f:
            pass 
        
    def __str__(self):
        return self.path_to_file
    
    def read(self):
        with open(self.path_to_file, 'r') as f:
            return f.read()
        
    def readlines(self):
        with open(self.path_to_file, 'r') as f:
            return f.readlines()
        
    def write(self, text):
        with open(self.path_to_file, 'w') as f:
            return f.write(text)
        
    def __add__(self, other):
        path_to_file = os.path.join(tempfile.gettempdir(), 'file')
        text = self.read() + other.read()
        file = File(path_to_file)
        file.write(text)
        return file
    
    def __getitem__(self, index):
            return self.readlines()[index]
        
#--------------------------------------------------
path_to_file = os.path.join(tempfile.gettempdir(), 'file')
print(os.path.exists(path_to_file))

file_obj = File(path_to_file)
print(os.path.exists(path_to_file))

print(file_obj.read())

print(file_obj.write('some text'))

print(file_obj.read())

print(file_obj.write('other text'))

print(file_obj.read())

file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
print(file_obj_1.write('line 1\n'))

print(file_obj_2.write('line 2\n'))

new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))

print(new_file_obj)

for line in new_file_obj:
    print(ascii(line))  


