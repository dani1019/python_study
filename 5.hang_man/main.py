import picture as pic
import words as wd
import method as md
import random

#start the hang_man
print(pic.hang_man)

#select randomly answer
answer = random.choice(wd.words).lower()
print(answer)

#guess the answer and enter the letter
letter= input("Guess a letter: ").lower()

"""
１．ユーザが入力したalphabetが表示された単語に含まれているか判断する
　・どう判断するか
　・ユーザーが入力したalaphabetが単語に存在する場合、画面に表示される単語と正解の単語を別々作成する
　・入力するたびに画面に表示される単語にユーザーが入力したalphabetが反映されるようにする
　→画面表示の単語をどこかに入れ、ユーザがalphabet入力処理に使われるようにする
"""
display_first_string =list(answer)
#check if letter entered include in words
while True:
    md.match_letter(display_first_string,letter)



"""
2.ユーザーが入力したalphabetが提示された単語に含まれている場合、
　・ユーザーが入力したalphabetの単語の一部分として表示される
  →単語のalphabetが表示されるとYou Winで終了。
　
　ユーザーが入力したalphabetが提示された単語に含まれていない場合、
　・5回未満
　　１。の処理が繰り返される
    hang_manの絵が表示される
  ・5回
    Game overが画面に表示される
"""


display_string = []



#if alphabet include in words and display the letter

#if alphabet don't include in words 
#You guesed a {alphabet}, that's not in the word. You lose a life
#display the picture