import webbrowser
import time

total_breaks = 3

break_count = 0

print ("Program Has Commenced on" + " " +time.ctime())

while (break_count < total_breaks):

    print ("Loop has begun on" + " " +time.ctime())

    time.sleep(10)

    webbrowser.open("https://youtu.be/uxi73RQlLB8")

    break_count = break_count + 1

    print ("Loop has ended on" + " " +time.ctime())

    time.sleep(10*60)


print ("The Program has ended on"+" " +time.ctime())
