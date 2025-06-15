print("    Welcome to Treasure Island.\nYour mission is to find the treasure.")
print(r'''                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("You have to find the hidden treasure")
game_over=False
life_limit=3

while not game_over :
    if life_limit==0:
        game_over=True
        print("You spent all your life.You lose!!!")
    else:    
        print("There is a cross road.Where do you want to go?")
        _1st=input('Left or right? If you wanna go left write "left" or else write "right" :\n').lower()
        if _1st=="left":
            print("You have reached in front of a lake: \n Do you wanna wait for boat or swim? ")
            _2nd=input('Type "wait" if you want to wait and "swim" if you want to swim:\n ').lower()
            if _2nd=="wait":
                print("You have successfully reached an island. \nThere are two door. one blue and another red")
                _3rd=input('Type "blue" for blue door and "red" for red door:\n ').lower()
                if _3rd=="blue":
                    print("You found the treasure. You won!!!\n")
                    game_over=True
                else:
                    print("You ran into the fire. You lose!!!") 
                    life_limit-=1   
                    print(f"You have {life_limit} left\n")
            else:
                print("You are attacked by crocodile. You lose!!!") 
                life_limit-=1   
                print(f"You have {life_limit} left\n")
        else:
            print("You fell into the hole. You lose!!!")
            life_limit-=1   
            print(f"You have {life_limit} left\n")