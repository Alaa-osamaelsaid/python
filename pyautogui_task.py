import pyautogui
from time import sleep

pyautogui.hotkey('win')
sleep(2)
pyautogui.write("vscode")
pyautogui.hotkey('enter')
sleep(2)
pyautogui.hotkey('ctrl','shift','x') #extensions menu
sleep(2)

def install_ext(name):
 pyautogui.write(name)
 sleep(3)
 pyautogui.click(x=244,y=219) #locate first option (install button)
 sleep(2)
 pyautogui.click(x=173,y=140) #return back to search 
 pyautogui.hotkey('ctrl','a','del')
 sleep(2)

#enter the extensions you want to install
install_ext("clangd")
install_ext("c++ testmate")
install_ext("c++ helper")
install_ext("cmake")
install_ext("cmake tools")


#pyautogui.click(x=229,y=295) #locate second option (install button)