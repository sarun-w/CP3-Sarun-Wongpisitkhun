"""
# Example Output display when user enter input value = 5
>>> User Input: 5

1. >>>_-_-*                     (4/1)
2. >>>_-_***                    (3/2)
3. >>>_-*****                   (2/3)
4. >>>_*******                  (1/4)
5. >>>*********                 (0/5)
"""

userInput = int(input("User Input: "))
for i in range(userInput):
    print(" " * (userInput - i - 1) + ("*" * (2 * i + 1)))