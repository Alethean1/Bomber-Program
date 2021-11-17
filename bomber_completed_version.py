
import time
import random
bomber_health = 100
munitions = 16


print("You are the pilot of a B-21 Raider over the Pacific.")
time.sleep(3)
print("You must perform bombing runs over several island airstrips and neutralize them all.")
time.sleep(3)
print("The first target is aproaching")
time.sleep(3)
print("Happy Hunting...")
time.sleep(3)
print("Ten seconds until target is in range ")
time.sleep(3)
print("...")
time.sleep(3)
print("...")
time.sleep(3)
print("...")
time.sleep(3)

def Bomb(bomber_health):
	rand_num = random.randint(1,11)
	if rand_num < 9:
		print("Target destroyed!")
		
	else:
		print("Taking enemy fire. We've been hit!")
		bomber_health -= 50
	return bomber_health
                
while True:
        print(f"Bomber Health: {bomber_health}  Munitions Remaining: {munitions}")
        pilot = input("Targets within range. Deploy missiles? Yes/No")
        if pilot =="Yes":
                bomber_health = Bomb(bomber_health)
                munitions = munitions-4
        if munitions == 0:
                time.sleep(1)
                print("ALL TARGETS DESTROYED!!!  Return to base!")
                break
        time.sleep(3)
        print("Adjusting course")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(3)
else:
        print("Mission aborted.  Returning to base.")
	        

	



