import time

first_chrorus = """
It's stuck with you forever
So promise you won't let it go
I'll trust the universe will always bring me to you
"""

second_chorus = """
I'll imagine we fell in love
I'll nap under moonlight skies with you
"""

third_chorus = """
I think I'll picture us, you with the waves
The ocean's colors on your face
"""

fourth_chorus = """
I'll leave my heart with your air
So let me fly with you
"""

fifth_chorus = """
Will you
be forever
with me?
"""

def time_sleep(sec):
    time.sleep(sec)

for char in first_chrorus:
    print(char, end="", flush=True) 
    time_sleep(0.08 if char != " " else 0.1)  

    if char == "\n":
        time_sleep(0.6)

time_sleep(2.0)

for char in second_chorus:
    print(char, end="", flush=True)
    time_sleep(0.07 if char != " " else 0.1)  

    if char == "\n":
        time_sleep(0.5)

time_sleep(0.35)

for char in third_chorus:
    print(char, end="", flush=True)
    time_sleep(0.06 if char != " " else 0.1)  

    if char == "\n":
        time_sleep(0.5)

time_sleep(0.4)

for char in fourth_chorus:
    print(char, end="", flush=True)
    time_sleep(0.09 if char != " " else 0.1) 

    if char == "\n":
        time_sleep(0.5)

time_sleep(0.5)

for char in fifth_chorus:
    print(char, end="", flush=True)
    time_sleep(0.1 if char != " " else 0.2) 

    if char == "\n":
        time_sleep(0.5)

print() 
