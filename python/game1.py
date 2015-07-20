<<<<<<< HEAD
#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

#������Ϸ���������Ҫ����������ѡ��1ѡ��Ӣ�2ѡ���������Ĭ��ѡ��Ӣ��
#�������ѡ������������벻ͬ����������
#��Ϸ�����������һ��0-9�����֣�ϵͳ���������������֣���ӡ�����ֵ���Ϣ
#        ��������������ַ�Χ����0-9������ӡ��"Error!"
#�˳���Ϸ����Ϸ�����Ŵ�ӡ��Ϣ�������ʾ�˳���Ϸ
=======
#运行游戏后，玩家首先要进行语音的选择，1选择英语，2选择汉语，其他则默认选择英语
#根据玩家选择的语音，进入不同的语音环境
#游戏规则：玩家输入一个0-9的数字，系统根据玩家输入的数字，打印出数字的信息
#        如果玩家输入的数字范围不在0-9，则会打印出"Error!"
#退出游戏：游戏会随着打印信息的完成提示退出游戏
>>>>>>> master
language_option = """\
    Language: Choose the language for System[OPTION]
            -1                    Choose English Language
            -2                    Choose Chinese Language
            """
enter_str = 'please enter an integer:'
#开始游戏前的说明
en_game_start_str = 'You choose English language!,Now，Game Start!'
cn_game_start_str = '你选择的中文模式！现在，开始游戏!'
#游戏规则
en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the information of the number'
cn_game_rule_str = '你输入一个0-9的数字，系统会打印出该数字的信息'
#结束游戏
en_game_over_str = 'Game Over!'
cn_game_over_str = '游戏结束！'
print(language_option)
number = int(input(enter_str))

def print_info(num):
    if num == 0:
        print('0 zero 零')
    elif num == 1:
        print('1 one 壹')
    elif num == 2:
        print('2 two 贰')
    elif num == 3:
        print('3 three 叁')
    elif num == 4:
        print('4 four 肆')
    elif num == 5:
        print('5 five 伍')
    elif num == 6:
        print('6 six 陆')
    elif num == 7:
        print('7 seven 柒')
    elif num == 8:
        print('8 eight 捌')
    elif num == 9:
        print('9 nine 玖')
    else:
        print('Error!')

def start_game(num):
    if num == 1:
        print(en_game_rule_str)
    elif num == 2:
        print(cn_game_rule_str)
    else:
        print(en_game_rule_str)
    n = int(input(enter_str))
    print_info(n)
          

if number == 1:
    print(en_game_start_str)
    start_game(1)
    print(en_game_over_str)
    exit()
elif number == 2:
    print(cn_game_start_str)
    start_game(2)
    print(cn_game_over_str)
    exit()
else:
    print(en_game_start_str)
    start_game(number)
    print(en_game_over_str)
    exit()



#运行游戏后，玩家首先要进行语音的选择，1选择英语，2选择汉语，其他则默认选择英语
#根据玩家选择的语音，进入不同的语音环境
#游戏规则：玩家输入一个0-9的数字，系统根据玩家输入的数字，打印出数字的信息
#        如果玩家输入的数字范围不在0-9，则会打印出"Error!"
#退出游戏：游戏会随着打印信息的完成提示退出游戏
language_option = """\
    Language: Choose the language for System[OPTION]
            -1                    Choose English Language
            -2                    Choose Chinese Language
            """
enter_str = 'please enter an integer:'

#开始游戏前的说明
en_game_start_str = 'You choose English language!,Now，Game Start!'
cn_game_start_str = '你选择的中文模式！现在，开始游戏!'

#游戏规则
en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the information of the number'
cn_game_rule_str = '你输入一个0-9的数字，系统会打印出该数字的信息'

#结束游戏
en_game_over_str = 'Game Over!'
cn_game_over_str = '游戏结束！'
print(language_option)

#定义列表
en_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
cn_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']

#循环标志
FLAG = True

#还需要玩吗?
en_play_again_str = """\
    #############################################
    Do you want play again?
    -1              Play Again
    -2              Exit Game
             """
cn_play_again_str = """\
    #############################################
    你还要继续玩吗？
    -1              继续玩
    -2              退出游戏
             """

number = int(input(enter_str))

#游戏打印信息
def print_info(num):
    if num in range(0,9):
        print(num,en_list[num],cn_list[num])
    else:
        print('Error!')

#开始游戏
def start_game(num):
    if num == 1:
        print(en_game_rule_str)
    elif num == 2:
        print(cn_game_rule_str)
    else:
        print(en_game_rule_str)
    n = int(input(enter_str))
    print_info(n)

#循环玩游戏
def play_again(n):
    if n == 1:
        print(en_play_again_str)
    elif n == 2:
        print(cn_play_again_str)
    else:
        print(en_play_again_str)
    again = int(input(enter_str))
    if again == 1:
        pass
    elif again == 2:
        #这里使用的是全局变量，注意这里不要写成：global FLAG = False
        global FLAG
        FLAG = False
        
#游戏的循环体   
while True:
    if FLAG:
        if number == 1:
            print(en_game_start_str)
            start_game(1)
            play_again(1)
        elif number == 2:
            print(cn_game_start_str)
            start_game(2)
            play_again(2)
        else:
           print(en_game_start_str)
           start_game(number)
           play_again(number)
    else:
        print(en_game_over_str)
        break
        #exit()