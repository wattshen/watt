#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

#python tkinter
#python version 3.3.2  
 from tkinter import * 
 '''
    �ж�
    ����С��
    {
        Բ�ģ�A(x1,y1)  �뾶��r  X���ٶȣ�Vax  Y���ٶȣ�Vay
        Բ�ģ�B(x2,y2)  �뾶��R  X���ٶȣ�Vbx  Y���ٶȣ�Vby
    }
    ��ײ�������ǣ�
    1.����С���Բ�ľ��벻������С��뾶֮��(r+R)������
    {
        (x2 - x1)^2 + (y2 - y1)^2 <= (r + R)^2
    }
    2.С����ײ����С������Ƚ���������
    {
        tempVax = Vax
        tempVay = Vay
        Vax = Vbx
        Vay = Vby
        Vbx = tempVax
        Vby = tempVay
        ��
        Vax = Vax + Vbx
        Vbx = Vax - Vbx
        Vax = Vax - Vbx
        Vay = Vay + Vby
        Vby = Vay - Vby
        Vay = Vay - Vby
    } 
     ��Ϸ����
    ��С���ڻ������ƶ�������֮��������ײ����ȻС����������Ҷ��������ײ
    ��ײ��С���ı䷽�򷵻�
    ����������α������ڵ���С����ƶ��ٶȣ��α�ķ�Χ��[-100, 100]

    ȱ�ݻ�BUG��
    1.���޸��α����ݴӶ��ı�С���ƶ��ٶȵ�ʱ��С���ƶ��ľ���ò�����ʱ�ĸ���
    ����С����ܻ����뻭��
    2.С�����˶��Ĺ����У���ʱ��Ҳ�п������뻭�� 
     �ܽ᣺
    ��������Ϸ������һ�����ڵ��°�ʱ�䡣����������в�����ȥѧϰ�˸��е���ѧ֪ʶ��
    ����֪ʶ���ܶණ�������ò���ˣ������ܿ���ѧ�������ˡ�
    ��Ϸ��ʵ�ܶ������ѧ���⡣

    ��Ϸ�л�����ȱ�ݻ�BUG��ϣ��־ͬ�����߿��Թ�ͬ���ơ�
''' 
 __author__ = {'author' : 'Hongten',
              'Email' : 'hongtenzone@foxmail.com',
              'Blog' : 'http://www.cnblogs.com/hongten/',
              'Created' : '2013-09-28',
              'Version' : '1.0'} 
 class Pong(Frame):
    def createWidgets(self):
        ## ����
        self.draw = Canvas(self, width="5i", height="5i", bg='white') 
         ## �α�(����С���ƶ��ٶȣ���Χ��[-100, 100])
        self.speed = Scale(self, orient=HORIZONTAL, label="ball speed",
                           from_=-100, to=100) 
         self.speed.pack(side=BOTTOM, fill=X) 
         #С����ײǽ�ڵķ�Χ
        self.scaling_right = 4.8
        self.scaling_left = 0.2
        #С��ֱ��
        self.ball_d = 0.4
        #�α����
        self.scale_value = self.speed.get()
        #������
        self.scaling = 100.0 
         #���С������
        self.balls = []
        #���С��x��������
        self.ball_x = []
        #���С��y��������
        self.ball_y = []
        #���С��x�᷽���ٶ�����
        self.ball_v_x = []
        #���С��y�᷽���ٶ�����
        self.ball_v_y = [] 
         # ���С��
        self.ball = self.draw.create_oval("0.10i", "0.10i", "0.50i", "0.50i",
                                          fill="red")
        self.second_ball = self.draw.create_oval("0.70i", "0.70i", "1.10i", "1.10i",
                                                 fill='black')
        self.three_ball = self.draw.create_oval("1.30i", "1.30i", "1.70i", "1.70i",
                                                 fill='brown')
        self.four_ball = self.draw.create_oval("2.0i", "2.0i", "2.40i", "2.40i",
                                                 fill='green')
        self.five_ball = self.draw.create_oval("3.0i", "3.0i", "3.40i", "3.40i",
                                                 fill='gray') 
         #�����С���������
        self.balls.append(self.ball)
        self.balls.append(self.second_ball)
        self.balls.append(self.three_ball)
        self.balls.append(self.four_ball)
        self.balls.append(self.five_ball) 
         #��һ��С�򣬼�self.ball��Բ������(self.x, self.y),��������˷���,Ŀ����Ϊ��
        #��С���ƶ��Ĺ����и�������
        self.x = 0.3        
        self.y = 0.3
        #��һ��С����ٶȷ���
        self.velocity_x = -0.2
        self.velocity_y = 0.5 
         self.second_ball_x = 0.9
        self.second_ball_y = 0.9
        self.second_ball_v_x = 0.4
        self.second_ball_v_y = -0.5 
         self.three_ball_x = 1.5
        self.three_ball_y = 1.5
        self.three_ball_v_x = -0.3
        self.three_ball_v_y = -0.5 
         self.four_ball_x = 2.2
        self.four_ball_y = 2.2
        self.four_ball_v_x = 0.1
        self.four_ball_v_y = -0.5 
         self.five_ball_x = 3.2
        self.five_ball_y = 3.2
        self.five_ball_v_x = 0.3
        self.five_ball_v_y = 0.5 
         
        #����С�������
        self.update_ball_x_y()
        self.draw.pack(side=LEFT) 
     def update_ball_x_y(self, *args):
        '''����С������꣬���Ѹ���С���Բ��������Ϣ�Լ��ٶ���Ϣ��ŵ������У�
           �����ں���ѭ��������ʱ��ʹ�á�'''
        #��һ��С����Ϣ
        self.ball_x.append(self.x)
        self.ball_y.append(self.y)
        self.ball_v_x.append(self.velocity_x)
        self.ball_v_y.append(self.velocity_y) 
         self.ball_x.append(self.second_ball_x)
        self.ball_y.append(self.second_ball_y)
        self.ball_v_x.append(self.second_ball_v_x)
        self.ball_v_y.append(self.second_ball_v_y) 
         self.ball_x.append(self.three_ball_x)
        self.ball_y.append(self.three_ball_y)
        self.ball_v_x.append(self.three_ball_v_x)
        self.ball_v_y.append(self.three_ball_v_y) 
         self.ball_x.append(self.four_ball_x)
        self.ball_y.append(self.four_ball_y)
        self.ball_v_x.append(self.four_ball_v_x)
        self.ball_v_y.append(self.four_ball_v_y) 
         self.ball_x.append(self.five_ball_x)
        self.ball_y.append(self.five_ball_y)
        self.ball_v_x.append(self.five_ball_v_x)
        self.ball_v_y.append(self.five_ball_v_y)

    def update_ball_velocity(self, index, *args):
        '''���¸���С���ٶ���Ϣ����С����ײ�����ܺ������С����Ҫ���µ��ٶ���Ϣ'''
        #�α�ֵ
        self.scale_value = self.speed.get()
        #��ײǽ��
        if (self.ball_x[index] > self.scaling_right) or (self.ball_x[index] < self.scaling_left):
            self.ball_v_x[index] = -1.0 * self.ball_v_x[index]
        if (self.ball_y[index] > self.scaling_right) or (self.ball_y[index] < self.scaling_left):
            self.ball_v_y[index] = -1.0 *  self.ball_v_y[index] 
         '''
        #TEST:
        for n in range(len(self.balls)):
            #print((self.ball_x[index] - self.ball_x[n])**2)
            #print(round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2))
            print(round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2))
        '''
        for n in range(len(self.balls)):
            #С����ײ����������(x2 - x1)^2 + (y2 - y1)^2 <= (r + R)^2
            if (round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2)):
                #��С���ٶȽ���
                temp_vx = self.ball_v_x[index]
                temp_vy = self.ball_v_y[index]
                self.ball_v_x[index] = self.ball_v_x[n]
                self.ball_v_y[index] = self.ball_v_y[n]
                self.ball_v_x[n] = temp_vx
                self.ball_v_y[n] = temp_vy
        #print(self.ball_v_x, self.ball_v_y)

        '''
        #WRONG:
        for n in range(len(self.balls)):            
            if (((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2) <= self.ball_d**2):
                #��С���ٶȽ���
                self.ball_v_x[index] = self.ball_v_x[index] + self.ball_v_x[n]
                self.ball_v_x[n] = self.ball_v_x[0] - self.ball_v_x[n]
                self.ball_v_x[index] = self.ball_v_x[index] - self.ball_v_x[n]
                self.ball_v_y[index] = self.ball_v_y[index] + self.ball_v_y[n]
                self.ball_v_y[n] = self.ball_v_y[index] - self.ball_v_y[n]
                self.ball_v_y[index] = self.ball_v_y[index] - self.ball_v_y[n]
        print(self.ball_v_x, self.ball_v_y)
        '''

    def get_ball_deltax(self, index, *args):
        '''��ȡС��X�������ƶ����벢�Ҹ���С���Բ��X���꣬����X�������ƶ�����'''
        deltax = (self.ball_v_x[index] * self.scale_value / self.scaling)
        self.ball_x[index] = self.ball_x[index] + deltax
        return deltax 
     def get_ball_deltay(self, index, *args):
        '''��ȡС��Y�������ƶ����벢�Ҹ���С���Բ��Y���꣬����Y�������ƶ�����'''
        deltay = (self.ball_v_y[index] * self.scale_value / self.scaling)
        self.ball_y[index] = self.ball_y[index] + deltay
        return deltay

    def moveBall(self, *args):
        '''�ƶ���һ��С�򣬱��Ϊ��0,���Ǹ������飺self.ballsȷ���ġ�'''
        self.update_ball_velocity(0)       
        deltax = self.get_ball_deltax(0)
        deltay = self.get_ball_deltay(0)
        #С���ƶ�
        self.draw.move(self.ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.moveBall) 
     def move_second_ball(self, *args):
        self.update_ball_velocity(1)       
        deltax = self.get_ball_deltax(1)
        deltay = self.get_ball_deltay(1)        
        self.draw.move(self.second_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_second_ball) 
 
    def move_three_ball(self, *args):
        self.update_ball_velocity(2)       
        deltax = self.get_ball_deltax(2)
        deltay = self.get_ball_deltay(2)
        self.draw.move(self.three_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_three_ball) 
     def move_four_ball(self, *args):
        self.update_ball_velocity(3)       
        deltax = self.get_ball_deltax(3)
        deltay = self.get_ball_deltay(3)
        self.draw.move(self.four_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_four_ball) 
     def move_five_ball(self, *args):
        self.update_ball_velocity(4)       
        deltax = self.get_ball_deltax(4)
        deltay = self.get_ball_deltay(4)
        self.draw.move(self.five_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_five_ball) 
             
    def __init__(self, master=None):
        '''��ʼ������'''
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        self.after(10, self.moveBall)
        self.after(10, self.move_three_ball)
        self.after(10, self.move_four_ball)
        self.after(10, self.move_five_ball)
        self.after(10, self.move_second_ball)

        
game = Pong() 
 game.mainloop()
 