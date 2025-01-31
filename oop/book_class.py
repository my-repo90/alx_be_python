class Book:
    #   the constructor method
    def __init__(self , title: str , author:str , year:int):
        self.title = title
        self.author = author
        self.year = year
    
    #   the destructor method
    def __del__(self):
        print(f"Deleting {self.title}")

    #string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
        
    #official string representation of an object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"