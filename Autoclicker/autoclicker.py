import pyautogui as auto
import keyboard
print('The autoclicker is now ready for use!')
while True:
    
    if keyboard.is_pressed('space'):
        auto.click()
        print('The SPACE key is pressed') #Attention there could be spamming in the console
    if keyboard.is_pressed('enter'):
        print ('END OF THE AUTOCLICKER ')
        break