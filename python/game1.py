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
language_option = """\
    Language: Choose the language for System[OPTION]
            -1                    Choose English Language
            -2                    Choose Chinese Language
            """
enter_str = 'please enter an integer:'
#��ʼ��Ϸǰ��˵��
en_game_start_str = 'You choose English language!,Now��Game Start!'
cn_game_start_str = '��ѡ�������ģʽ�����ڣ���ʼ��Ϸ!'
#��Ϸ����
en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the information of the number'
cn_game_rule_str = '������һ��0-9�����֣�ϵͳ���ӡ�������ֵ���Ϣ'
#������Ϸ
en_game_over_str = 'Game Over!'
cn_game_over_str = '��Ϸ������'
print(language_option)
number = int(input(enter_str))

def print_info(num):
    if num == 0:
        print('0 zero ��')
    elif num == 1:
        print('1 one Ҽ')
    elif num == 2:
        print('2 two ��')
    elif num == 3:
        print('3 three ��')
    elif num == 4:
        print('4 four ��')
    elif num == 5:
        print('5 five ��')
    elif num == 6:
        print('6 six ½')
    elif num == 7:
        print('7 seven ��')
    elif num == 8:
        print('8 eight ��')
    elif num == 9:
        print('9 nine ��')
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



#������Ϸ���������Ҫ����������ѡ��1ѡ��Ӣ�2ѡ���������Ĭ��ѡ��Ӣ��
#�������ѡ������������벻ͬ����������
#��Ϸ�����������һ��0-9�����֣�ϵͳ���������������֣���ӡ�����ֵ���Ϣ
#        ��������������ַ�Χ����0-9������ӡ��"Error!"
#�˳���Ϸ����Ϸ�����Ŵ�ӡ��Ϣ�������ʾ�˳���Ϸ
language_option = """\
    Language: Choose the language for System[OPTION]
            -1                    Choose English Language
            -2                    Choose Chinese Language
            """
enter_str = 'please enter an integer:'

#��ʼ��Ϸǰ��˵��
en_game_start_str = 'You choose English language!,Now��Game Start!'
cn_game_start_str = '��ѡ�������ģʽ�����ڣ���ʼ��Ϸ!'

#��Ϸ����
en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the information of the number'
cn_game_rule_str = '������һ��0-9�����֣�ϵͳ���ӡ�������ֵ���Ϣ'

#������Ϸ
en_game_over_str = 'Game Over!'
cn_game_over_str = '��Ϸ������'
print(language_option)

#�����б�
en_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
cn_list = ['��','Ҽ','��','��','��','��','½','��','��','��']

#ѭ����־
FLAG = True

#����Ҫ����?
en_play_again_str = """\
    #############################################
    Do you want play again?
    -1              Play Again
    -2              Exit Game
             """
cn_play_again_str = """\
    #############################################
    �㻹Ҫ��������
    -1              ������
    -2              �˳���Ϸ
             """

number = int(input(enter_str))

#��Ϸ��ӡ��Ϣ
def print_info(num):
    if num in range(0,9):
        print(num,en_list[num],cn_list[num])
    else:
        print('Error!')

#��ʼ��Ϸ
def start_game(num):
    if num == 1:
        print(en_game_rule_str)
    elif num == 2:
        print(cn_game_rule_str)
    else:
        print(en_game_rule_str)
    n = int(input(enter_str))
    print_info(n)

#ѭ������Ϸ
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
        #����ʹ�õ���ȫ�ֱ�����ע�����ﲻҪд�ɣ�global FLAG = False
        global FLAG
        FLAG = False
        
#��Ϸ��ѭ����   
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