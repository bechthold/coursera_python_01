# https://www.coursera.org/learn/diving-in-python/programming/W3QfI/riealizatsiia-prostogho-klassa-dlia-chtieniia-iz-faila

class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def read(self):
        try:
            with open(self.filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
                return ''
            