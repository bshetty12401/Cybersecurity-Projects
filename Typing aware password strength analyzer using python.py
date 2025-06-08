from pynput import keyboard
from time import time

password =""
timestamps = []
def press(key):
    global password,timestamps
    try:
        if key.char!="":
            password=password+key.char
            timestamps.append(time())
    except:
        pass
    if key==keyboard.Key.enter:
        return False
print("type your password and press enter")
with keyboard.Listener(on_press=press) as l:
    l.join()
delays = [round(timestamps[i+1] - timestamps[i], 2) for i in range(len(timestamps)-1)]
avgdelay=round(sum(delays)/len(delays),2)
print("\naverage delay=",avgdelay,"secs")
print("the password you typed =",password)
strength=0
if len(password)==12:
    strenght= strength + 6
elif len(password)>12:
    print("note the password is too long , reccomonded lenth is 12 charcters")
    strength= strength + 5
else:
    print("password is too short")
if any(c.islower() for c in password):
    strength= strength + 1
else:
    print("lower case letter is missing")
if any(c.isupper() for c in password):
    strength= strength + 1
else:
    print("upper case letter is missing")
if any(c.isdigit() for c in password):
    strength= strength + 1
else:
    print("your password is missing a number")
if any(c in "@#$%&*~<>?_+-/ " for c in password):
    strength= strength + 1
else:
    print("your password is missing a special charcter")

if avgdelay>3:
    print("you took a long time between keypresses. This may be hard to remember")
if avgdelay<0.5:
    print("you typed very fast,this might be a reused or copied password")
print("final password strength score",strength,"/10")