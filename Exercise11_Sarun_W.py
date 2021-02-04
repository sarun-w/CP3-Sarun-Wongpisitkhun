"""
# Example Output display when user enter input value = 5
>>> User Input: 5

1. >>>_-_-*                     
2. >>>_-_***                  
3. >>>_-*****                   
4. >>>_*******                  
5. >>>*********                 
"""

userInput = int(input("User Input: "))
for i in range(userInput):
    print(" " * (userInput - i - 1) + ("*" * (2 * i + 1)))