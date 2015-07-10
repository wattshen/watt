
#python tkinter
#python version 3.3.2  
 from tkinter import * 
 '''
    ÅÐ¶Ï
    Á½¸öÐ¡Çò
    {
        Ô²ÐÄ£ºA(x1,y1)  °ë¾¶£ºr  XÖáËÙ¶È£ºVax  YÖáËÙ¶È£ºVay
        Ô²ÐÄ£ºB(x2,y2)  °ë¾¶£ºR  XÖáËÙ¶È£ºVbx  YÖáËÙ¶È£ºVby
    }
    Åö×²µÄÌõ¼þÊÇ£º
    1.Á½¸öÐ¡ÇòµÄÔ²ÐÄ¾àÀë²»´óÓÚÁ½Ð¡Çò°ë¾¶Ö®ºÍ(r+R)£¬¼´£º
    {
        (x2 - x1)^2 + (y2 - y1)^2 <= (r + R)^2
    }
    2.Ð¡ÇòÅö×²ºó£¬Á½Ð¡ÇòµÄÊý¶È½»»»£¬¼´£º
    {
        tempVax = Vax
        tempVay = Vay
        Vax = Vbx
        Vay = Vby
        Vbx = tempVax
        Vby = tempVay
        »ò£º
        Vax = Vax + Vbx
        Vbx = Vax - Vbx
        Vax = Vax - Vbx
        Vay = Vay + Vby
        Vby = Vay - Vby
        Vay = Vay - Vby
    } 
     ÓÎÏ·¹æÔò£º
    ÎåÐ¡ÇòÔÚ»­²¼ÖÐÒÆ¶¯£¬ËûÃÇÖ®¼ä»á²úÉúÅö×²£¬µ±È»Ð¡ÇòºÍÉÏÏÂ×óÓÒ¶¼»á²úÉúÅö×²
    Åö×²ºó£¬Ð¡Çò»á¸Ä±ä·½Ïò·µ»Ø
    ¶ø×îÏÂÃæµÄÓÎ±êÔòÓÃÓÚµ÷½ÚÐ¡ÇòµÄÒÆ¶¯ËÙ¶È£¬ÓÎ±êµÄ·¶Î§ÊÇ[-100, 100]

    È±ÏÝ»òBUG£º
    1.ÔÚÐÞ¸ÄÓÎ±êÊý¾Ý´Ó¶ø¸Ä±äÐ¡ÇòÒÆ¶¯ËÙ¶ÈµÄÊ±ºò£¬Ð¡ÇòÒÆ¶¯µÄ¾àÀëµÃ²»µ½¼°Ê±µÄ¸üÐÂ
    µ¼ÖÂÐ¡Çò¿ÉÄÜ»áÌÓÀë»­²¼
    2.Ð¡ÇòÔÚÔË¶¯µÄ¹ý³ÌÖÐ£¬ÓÐÊ±ºòÒ²ÓÐ¿ÉÄÜÌÓÀë»­²¼ 
     ×Ü½á£º
    Íê³ÉÕâ¸öÓÎÏ·£¬»¨ÁËÒ»¸öÐÇÆÚµÄÏÂ°àÊ±¼ä¡£ÔÚÕâ¸ö¹ý³ÌÖÐ²»½ö»ØÈ¥Ñ§Ï°ÁË¸ßÖÐµÄÊýÑ§ÖªÊ¶£¬
    ÎïÀíÖªÊ¶£¬ºÜ¶à¶«Î÷¶¼ÍüµÃ²î²»¶àÁË£¬²»¹ýºÜ¿ìÓÖÑ§·µ»ØÀ´ÁË¡£
    ÓÎÏ·ÆäÊµºÜ¶à¾ÍÊÇÊýÑ§ÎÊÌâ¡£

    ÓÎÏ·ÖÐ»¹´æÔÚÈ±ÏÝ»òBUG£¬Ï£ÍûÖ¾Í¬µÀºÏÕß¿ÉÒÔ¹²Í¬ÍêÉÆ¡£ 
     ÐÞ¸Ä¼ÇÂ¼£º
    1.µ÷Õû»­²¼´óÐ¡
    2.µ÷ÕûÁËÐ¡ÇòµÄ°ë¾¶,ÒÔ¼°Ð¡ÇòµÄËÙ¶È³õÊ¼Öµ£¬Ð¡Çò³õÊ¼Ô²ÐÄ×ø±ê
    3.ÓÎ±êµÄ·¶Î§ÐÞ¸ÄÎª£º[-200, 200]
    ÕâÐ©ÐÞ¸ÄÖ÷ÒªÊÇÕë¶ÔÉÏÃæµÄÈ±ÏÝ¶ø½øÐÐµÄ¡£ 
     ÓÅµã£º
    1.Ð¡ÇòÒÆ¶¯µÄ¹ý³Ì¸üÖ±¹Û
    2.Ð¡ÇòµÄÒÆ¶¯ËÙ¶È±äÐ¡£¬µ«ÊÇ¿ÉÒÔ¸ù¾ÝÓÎ±êÀ´ÐÞ¸ÄÐ¡ÇòÒÆ¶¯ËÙ¶È
    3.½çÃæ±ÈÖ®Ç°¸ü¼ÓÓÑºÃ
''' 
 __author__ = {'author' : 'Hongten',
              'Email' : 'hongtenzone@foxmail.com',
              'Blog' : 'http://www.cnblogs.com/hongten/',
              'Created' : '2013-09-28',
              'Version' : '1.1'} 
 class Pong(Frame):
    def createWidgets(self):
         #·ÅËõÂÊ
        self.scaling = 100.0
        #»­²¼±ÈÀý
        self.canvas_width = 10
        self.canvas_height = 5.6
        ## »­²¼
        self.draw = Canvas(self, width=(self.canvas_width * self.scaling),
                           height=(self.canvas_height * self.scaling),
                           bg='white') 
         ## ÓÎ±ê(¿ØÖÆÐ¡ÇòÒÆ¶¯ËÙ¶È£¬·¶Î§£º[-100, 100])
        self.speed = Scale(self, orient=HORIZONTAL, label="ball speed",
                           from_=-200, to=200)

        self.speed.pack(side=BOTTOM, fill=X) 
         #Ð¡ÇòÖ±¾¶
        self.ball_d = 1.0
        #Ð¡ÇòÅö×²Ç½±ÚµÄ·¶Î§
        self.scaling_left = round(self.ball_d / 2, 1)
        self.scaling_right = self.canvas_width - self.scaling_left
        self.scaling_bottom = self.canvas_height - self.scaling_left
        self.scaling_top = self.scaling_left

        #ÓÎ±ê¶ÈÊý
        self.scale_value = self.speed.get() * 0.1

        #´æ·ÅÐ¡ÇòÊý×é
        self.balls = []
        #´æ·ÅÐ¡Çòx×ø±êÊý×é
        self.ball_x = []
        #´æ·ÅÐ¡Çòy×ø±êÊý×é
        self.ball_y = []
        #´æ·ÅÐ¡ÇòxÖá·½ÏòËÙ¶ÈÊý×é
        self.ball_v_x = []
        #´æ·ÅÐ¡ÇòyÖá·½ÏòËÙ¶ÈÊý×é
        self.ball_v_y = [] 
         # Îå¸öÐ¡Çò
        self.ball = self.draw.create_oval("0.60i", "0.60i", "1.60i", "1.60i",
                                          fill="red")
        self.second_ball = self.draw.create_oval("2.0i", "2.0i", "3.0i", "3.0i",
                                                 fill='black')
        self.three_ball = self.draw.create_oval("4.0i", "4.0i", "5.0i", "5.0i",
                                                 fill='brown')
        self.four_ball = self.draw.create_oval("6.0i", "2.0i", "7.0i", "3.0i",
                                                 fill='green')
        self.five_ball = self.draw.create_oval("8.0i", "3.0i", "9.0i", "4.0i",
                                                 fill='gray') 
         #°ÑÎå¸öÐ¡Çò·ÅÈëÊý×é
        self.balls.append(self.ball)
        self.balls.append(self.second_ball)
        self.balls.append(self.three_ball)
        self.balls.append(self.four_ball)
        self.balls.append(self.five_ball) 
         #µÚÒ»¸öÐ¡Çò£¬¼´self.ballµÄÔ²ÐÄ×ø±ê(self.x, self.y),ÕâÀï½øÐÐÁË·ÅËõ,Ä¿µÄÊÇÎªÁË
        #ÔÚÐ¡ÇòÒÆ¶¯µÄ¹ý³ÌÖÐ¸ü¼ÓÁ÷³©
        self.x = 1.1        
        self.y = 1.1
        #µÚÒ»¸öÐ¡ÇòµÄËÙ¶È·½Ïò
        self.velocity_x = -0.2
        self.velocity_y = 0.1 
         self.second_ball_x = 2.5
        self.second_ball_y = 2.5
        self.second_ball_v_x = 0.1
        self.second_ball_v_y = -0.2 
         self.three_ball_x = 4.5
        self.three_ball_y = 4.5
        self.three_ball_v_x = -0.1
        self.three_ball_v_y = -0.2 
         self.four_ball_x = 6.5
        self.four_ball_y = 2.5
        self.four_ball_v_x = 0.1
        self.four_ball_v_y = -0.2 
         self.five_ball_x = 8.5
        self.five_ball_y = 3.5
        self.five_ball_v_x = 0.1
        self.five_ball_v_y = 0.2 
         
        #¸üÐÂÐ¡ÇòµÄ×ø±ê
        self.update_ball_x_y()
        self.draw.pack(side=LEFT) 
     def update_ball_x_y(self, *args):
        '''¸üÐÂÐ¡ÇòµÄ×ø±ê£¬¼´°Ñ¸÷¸öÐ¡ÇòµÄÔ²ÐÄ×ø±êÐÅÏ¢ÒÔ¼°ËÙ¶ÈÐÅÏ¢´æ·Åµ½Êý×éÖÐ£¬
           ±ãÓÚÔÚºóÃæÑ­»·±éÀúµÄÊ±ºòÊ¹ÓÃ¡£'''
        #µÚÒ»¸öÐ¡ÇòÐÅÏ¢
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
        '''¸üÐÂ¸÷¸öÐ¡ÇòËÙ¶ÈÐÅÏ¢£¬¼´Ð¡ÇòÅö×²µ½ËÄÖÜºÍÁíÍâµÄÐ¡ÇòË÷Òª¸üÐÂµÄËÙ¶ÈÐÅÏ¢'''
        #ÓÎ±êÖµ
        self.scale_value = self.speed.get() * 0.1
        #Åö×²Ç½±Ú
        if (self.ball_x[index] > self.scaling_right) or (self.ball_x[index] < self.scaling_left):
            self.ball_v_x[index] = -1.0 * self.ball_v_x[index]
        if (self.ball_y[index] > self.scaling_bottom) or (self.ball_y[index] < self.scaling_top):
            self.ball_v_y[index] = -1.0 *  self.ball_v_y[index] 
         '''
        #TEST:
        for n in range(len(self.balls)):
            #print((self.ball_x[index] - self.ball_x[n])**2)
            #print(round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2))
            print(round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2))
        '''
        for n in range(len(self.balls)):
            #Ð¡ÇòÅö×²Ìõ¼þ£¬¼´£º(x2 - x1)^2 + (y2 - y1)^2 <= (r + R)^2
            if (round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2)):
                #Á½Ð¡ÇòËÙ¶È½»»»
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
                #Á½Ð¡ÇòËÙ¶È½»»»
                self.ball_v_x[index] = self.ball_v_x[index] + self.ball_v_x[n]
                self.ball_v_x[n] = self.ball_v_x[0] - self.ball_v_x[n]
                self.ball_v_x[index] = self.ball_v_x[index] - self.ball_v_x[n]
                self.ball_v_y[index] = self.ball_v_y[index] + self.ball_v_y[n]
                self.ball_v_y[n] = self.ball_v_y[index] - self.ball_v_y[n]
                self.ball_v_y[index] = self.ball_v_y[index] - self.ball_v_y[n]
        print(self.ball_v_x, self.ball_v_y)
        '''

    def get_ball_deltax(self, index, *args):
        '''»ñÈ¡Ð¡ÇòXÖá×ø±êÒÆ¶¯¾àÀë²¢ÇÒ¸üÐÂÐ¡ÇòµÄÔ²ÐÄX×ø±ê£¬·µ»ØXÖáËùÐèÒÆ¶¯¾àÀë'''
        deltax = (self.ball_v_x[index] * self.scale_value / self.scaling)
        self.ball_x[index] = self.ball_x[index] + deltax
        return deltax 
     def get_ball_deltay(self, index, *args):
        '''»ñÈ¡Ð¡ÇòYÖá×ø±êÒÆ¶¯¾àÀë²¢ÇÒ¸üÐÂÐ¡ÇòµÄÔ²ÐÄY×ø±ê£¬·µ»ØYÖáËùÐèÒÆ¶¯¾àÀë'''
        deltay = (self.ball_v_y[index] * self.scale_value / self.scaling)
        self.ball_y[index] = self.ball_y[index] + deltay
        return deltay

    def moveBall(self, *args):
        '''ÒÆ¶¯µÚÒ»¸öÐ¡Çò£¬±àºÅÎª£º0,ÕâÊÇ¸ù¾ÝÊý×é£ºself.ballsÈ·¶¨µÄ¡£'''
        self.update_ball_velocity(0)       
        deltax = self.get_ball_deltax(0)
        deltay = self.get_ball_deltay(0)
        #Ð¡ÇòÒÆ¶¯
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
        '''³õÊ¼»¯º¯Êý'''
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
 