### Weather Advisor Task ###
def weatherAdvisor():
    temp = float(input("Please enter the current temperature in Celsius: "))
    
    if(temp >= 30):
        print("It's a hot day. Stay hydrated!")
    elif(temp>=20 and temp<= 29 ):
        print("It's a warm day. Enjoy the weather!")
    elif(temp>=10 and temp <=19):
        print("It's a cool day. Wear a jacket!")
    elif(temp<10):
        print("It's a cold day. Stay warm!")
    

### Filter and Transform a List Task ###
def filterAndTransform():
    myList=[]
    for i in range(1, 21):
        myList.append(i)
    for i in myList:
        if(i%3==0):
            print(f"{i} is divisible by 3!")


def main():
    print("### Welcome to Task 2 solution ###")
    choose = int(input("Chose 1 for Weather Advisor Solution OR Chose 2 for Filter And Transform Solution: "))
    if(choose == 1):
        weatherAdvisor()
    elif(choose == 2):
      filterAndTransform()

main()