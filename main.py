import pyxel
import enum
import time
import random

love_count = 0

class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3
    IDLE = 4
    ENTER = 5

class State(enum.Enum):
    IDLE_0 = 0
    IDLE_1 = 1

class Interact(enum.Enum):
    NULL = 0
    WATER = 1
    MAH = 2
    PTINTIN = 3
    PMAW = 4
    PLANIL = 5
    SOMSOM = 6
    MANGU = 7
    HERB = 8
    CHEST = 9
    MAIN = 10
    NONGTAN = 11
    NONGARW = 12
    PERIN = 13
    NONGPAT = 14
    PERIN_GAME = 15
    NONGYEEN = 16
    ENDING = 17

class Water:
    def __init__ (self):
        self.x = 0
        self.y = 132
        self.w = 124
        self.h = 140

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Flower:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 72
            sprite_y = 24
        else :
            sprite_x = 80
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class GPU:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 136
            sprite_y = 16
        else :
            sprite_x = 144
            sprite_y = 16
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Bottle:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 168
            sprite_y = 16
        else :
            sprite_x = 176
            sprite_y = 16
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Chest:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.found = False

    def draw(self, state, is_ending):
        if self.found :
            if(state == State.IDLE_0):
                sprite_x = 64
                sprite_y = 0
            else :
                sprite_x = 72
                sprite_y = 0
        else :
            if(state == State.IDLE_0):
                sprite_x = 80
                sprite_y = 0
            else :
                sprite_x = 104
                sprite_y = 0
        if is_ending :
            if(state == State.IDLE_0):
                sprite_x = 64
                sprite_y = 0
            else :
                sprite_x = 208
                sprite_y = 0
        
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Herb:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 88
            sprite_y = 24
        else :
            sprite_x = 96
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Carrot:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 120
            sprite_y = 24
        else :
            sprite_x = 72
            sprite_y = 16
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Cake:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16

    def draw(self, state, is_blow):
        if not is_blow :
            if(state == State.IDLE_0):
                sprite_x = 216
                sprite_y = 0
            else :
                sprite_x = 232
                sprite_y = 0
        else :
            if(state == State.IDLE_0):
                sprite_x = 216
                sprite_y = 16
            else :
                sprite_x = 232
                sprite_y = 16
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Tree:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 16

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 8
            sprite_y = 8
        else :
            sprite_x = 56
            sprite_y = 32
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)

    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects
    
class Charlotte :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 7
        self.h = 8

    def draw(self, direction, state, land):
        if (land) :
            self.h = 8
            if(state == State.IDLE_0):
                sprite_x = 9
                sprite_y = 0
                if(direction == Direction.LEFT):
                    sprite_y = 0
                    sprite_x = 1
                if(direction == Direction.RIGHT):
                    sprite_x = 17
                    sprite_y = 0
                pyxel.blt(self.x, self.y, 1, sprite_x, sprite_y, self.w, self.h)
            else :
                self.h = 7
                sprite_x = 25
                sprite_y = 1
                pyxel.blt(self.x, self.y+1, 1, sprite_x, sprite_y, self.w, self.h)
        else :
            self.h = 6
            if(state == State.IDLE_0):
                sprite_x = 41
                sprite_y = 0
                if(direction == Direction.LEFT):
                    sprite_x = 33
                    sprite_y = 0
                if(direction == Direction.RIGHT):
                    sprite_x = 49
                    sprite_y = 0
                pyxel.blt(self.x, self.y, 1, sprite_x, sprite_y, self.w, self.h)
            else :
                self.h = 5
                sprite_x = 57
                sprite_y = 1
                pyxel.blt(self.x, self.y+1, 1, sprite_x, sprite_y, self.w, self.h)
            # pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h)

class Fish :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 0
            sprite_y = 24
        else :
            sprite_x = 48
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class Mah :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 0
            sprite_y = 32
        else :
            sprite_x = 8
            sprite_y = 32
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class PTinTin :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            self.h = 8
            sprite_x = 16
            sprite_y = 32
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
        else :
            self.h = 6
            sprite_x = 24
            sprite_y = 34
            pyxel.blt(self.x, self.y+2, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class PMaw :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 16
            sprite_y = 40
        else :
            sprite_x = 24
            sprite_y = 40
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class PlaNil :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 7
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            self.h = 5
            sprite_x = 9
            sprite_y = 27
            pyxel.blt(self.x+1, self.y+3, 0, sprite_x, sprite_y, self.w, self.h)
        else :
            self.h = 8
            sprite_x = 57
            sprite_y = 24
            pyxel.blt(self.x+1, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class SomSom :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 7
        self.h = 7

    def draw(self, state):
        if(state == State.IDLE_0):
            self.h = 7
            sprite_x = 0
            sprite_y = 41
            pyxel.blt(self.x, self.y+8, 0, sprite_x, sprite_y, self.w, self.h)
        else :
            self.h = 6
            sprite_x = 8
            sprite_y = 42
            pyxel.blt(self.x, self.y+9, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y+8 and self.y+8 + self.h > v) :
            is_intersects = True
        return is_intersects

class Mangu :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 40
            sprite_y = 40
        else :
            sprite_x = 48
            sprite_y = 40
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class nongTan :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 104
            sprite_y = 24
        else :
            sprite_x = 112
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class nongArw :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 136
            sprite_y = 24
        else :
            sprite_x = 144
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class PErin :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 152
            sprite_y = 24
        else :
            sprite_x = 160
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class nongPat :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self, state):
        if(state == State.IDLE_0):
            sprite_x = 192
            sprite_y = 24
        else :
            sprite_x = 200
            sprite_y = 24
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

class nongYeen :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 5
        self.h = 6

    def draw(self, state):
        if(state == State.IDLE_0):
            self.h = 6
            sprite_x = 176
            sprite_y = 26
            pyxel.blt(self.x, self.y+2, 0, sprite_x, sprite_y, self.w, self.h)
        else :
            self.h = 5
            sprite_x = 184
            sprite_y = 27
            pyxel.blt(self.x, self.y+3, 0, sprite_x, sprite_y, self.w, self.h)
    
    def intersects(self,u ,v, w, h):
        is_intersects = False
        if (u + w > self.x and self.x + self.w > u and v + h > self.y and self.y + self.h > v) :
            is_intersects = True
        return is_intersects

def draw_text(text, title):
    if title :
        y = 104
        count_x = 2
    else :
        y = 128
        count_x = 10
    max_count_x = 188
    for i in range(len(text)):
        if (ord(text[i])>=3585 and ord(text[i])<=3616):
            sprite_x = (ord(text[i]) - 3585)*8
            sprite_y = 50
        elif (ord(text[i])>=3617 and ord(text[i])<=3648):
            sprite_y = 58
            sprite_x = (ord(text[i]) - 3617)*8
        elif (ord(text[i])>=3649):
            sprite_y = 66
            sprite_x = (ord(text[i]) - 3649)*8
        elif (33 <= ord(text[i]) <= 64):
            sprite_y = 74
            sprite_x = (ord(text[i]) - 33)*8
        elif (65 <= ord(text[i]) <= 96):
            sprite_y = 82
            sprite_x = (ord(text[i]) - 65)*8

        if text[i] in ["ต","ท","น","บ","ป","ผ","ฝ","พ","ฟ","ภ","ๆ","ห","M", "N", "T", "O","ณ","/","W","Y","X","ซ","ศ"] :
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 7, 6)
            count_x += 6
        # elif text[i] in ["ณ"]:
        #     pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 7, 6)
        #     count_x += 7
        elif text[i] in ["ญ"]:
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 7, 6)
            pyxel.blt(count_x, y+6, 0, 128, 56, 7, 3)
            count_x += 6
        elif text[i] in ["ง","แ","า","3",">","I","L","E","1","ธ","-"]:
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 7, 6)
            count_x += 4
        elif text[i] in ["(",")","ะ"]:
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 7, 6)
            count_x += 3
        elif text[i] in ["เ","!",":",".",";"]:
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 7, 6)
            count_x += 2
        elif text[i] in ["ั","ิ","ี","์","่","้","็","ึ","๋","ื","๊"]:
            if text[i-1] in ("ั","ิ","ี","ึ","ื") :
                pyxel.blt(count_x-5, y-6, 0, sprite_x, sprite_y-2, 7, 3)
            else:
                if text[i-1] in ["ป"] or (text[i-2] in ["ป"] and text[i-1] in ["ุ"]):
                    pyxel.blt(count_x-6, y-3, 0, sprite_x, sprite_y-2, 7, 3)
                else :
                    pyxel.blt(count_x-5, y-3, 0, sprite_x, sprite_y-2, 7, 3)
            if i+1 != len(text) and text[i+1] in ["ำ"]:
                pyxel.blt(count_x-5, y-6, 0, sprite_x, sprite_y-2, 7, 3)
        elif text[i] in ["ุ","ู"]:
            pyxel.blt(count_x-4, y+6, 0, sprite_x, sprite_y+2, 7, 4)
        elif text[i] in ["ใ","ไ","โ"]:
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y-2, 6, 6)
            count_x += 4
        elif text[i] in ["ำ"]:
            pyxel.blt(count_x-5, y-3, 0, sprite_x, sprite_y-2, 7, 3)
            pyxel.blt(count_x, y, 0, sprite_x-8, sprite_y, 7, 6)
            count_x += 4
        elif text[i] == " ":
            count_x += 2
        elif text[i] == "❤":
            pyxel.blt(count_x, y, 0, 16, 50, 7, 6)
            count_x += 6
        elif text[i] == "|":
            count_x = 1
            y += 12
        else :
            pyxel.blt(count_x, y, 0, sprite_x, sprite_y, 6, 6)
            count_x += 5
        if (count_x >= max_count_x):
            count_x = 1
            y += 12

class Hud:
    def __init__(self):
        self.love_count = 0
        self.is_ขยร้ = None
        self.is_หูกระจง = None
        self.answer = True
        self.x = random.randint (0,184)
        self.y = random.randint (0,160)
        self.grill_tail = None
        self.is_spicy_tail = None
    
    def main_story_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == -1) :
            draw_text("กดปุ่ม G เพื่อ INTERACT",False)
        if (c == 0) :
            draw_text("อะแฮ่ม.. ในเช้าที่สดใสของวันเสาร์รองสุดท้ายของปี |2022 จอมมารคนสวยผู้ยิ่งใหญ่และใหญ่ยิ่งเดินออกมา|ซู๊ดอากาศภายนอกปราสาท",False)
        elif (c==1) :
            draw_text("แต่เช้าที่ควรจะสงบเงียบไม่รู้ทำไมถึงมีสิงสาราสัตว์|อะไรเยอะแยะก็ไม่รู้",False)
        elif (c==2) :
            draw_text("จอมมารยืนอยู่ใต้ต้นไม้ต้นนึงที่ดูห่างไกลจากความ|วุ่นวายมากที่สุด เพื่อตรวจสอบสถานการณ์",False)
        elif (c==3) :
            draw_text("SOME อีกา",True)
            draw_text("แฮร่!!",False)
        elif (c==4) :
            draw_text("SOME อีกา",True)
            draw_text("ไหว้ย่อท่านจอมมารคนสวยค่ะ",False)
        elif (c==5) :
            draw_text("SOME อีกา",True)
            draw_text("เห็นว่ามีกล่องสมบัติซ่อนอยู่ที่นี่ ทุกคนก็เลยมา|วุ่นวายอยู่ที่นี่กันหมด",False)
        elif (c==6) :
            draw_text("SOME อีกา",True)
            draw_text("ท่านจอมมารเองก็ลองไปสำรวจดูสิคะ",False)
        elif (c==7) :
            draw_text("SOME อีกา",True)
            draw_text("แต่ก่อนจะไป หนูให้ขนอีกาสีขาวนี่นะคะ เผื่อเอาไป|ใช้ในอนาคต",False)
        elif (c==8) :
            draw_text("กล่องสมบัติที่ดูเหมือนต้องวางของลงไป 11 อย่าง ถึงจะเปิดดูภายในกล่องได้",False)
        elif (c==9) :
            draw_text("ลองถามคน(?)อื่นๆดูดีกว่า",False)
        elif (c==10) :
            draw_text("ทุกคน",True)
            draw_text("เย้!!!",False)
        elif (c==11) :
            draw_text("ทุกคน",True)
            draw_text("สุขสันต์วันเกิดนะท่านจอมมาร!!",False)
        elif (c==12) :
            draw_text("ทุกคน",True)
            draw_text("นี่เป็นของขวัญที่เราเตรียมไว้ให้",False)
        elif (c==13) :
            draw_text("ทุกคน",True)
            draw_text("อย่าลืมขอพรก่อนเป่าเค้กนะครับ/ค่ะ",False)
        elif (c==15) :
            draw_text("ทุกคน",True)
            draw_text("เย้!!!",False)
        elif (c==16) :
            draw_text("เอาเค้กไปแบ่งกับทุกคนกันเถอะ",False)
        elif (c==17) :
            draw_text("และแล้ววันเกิดของท่านจอมมารผู้ยิ่งใหญ่และใหญ่ยิ่ง|ก็ผ่านไปอีกปี",False)
        elif (c==18) :
            draw_text("เข้าสู่ช่วง END CREDIT อิอิ",False)
        elif (c==19) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("อิย๊ากกกก ขอบคุณทุกคนมากฮะ ที่มามีส่วนร่วมในเกมนี้",False)
        elif (c==20) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("ขอบคุณพรี่ตินติน พรี่เอริน พรี่แมว น้องแพท มะงึ |น้องทัล สมชาย น้องยีนส์ อาว ปลานิล ที่มามีส่วนร่วมในเกมนี้นะครับ ขอบคุณมากๆ",False)
        elif (c==21) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("อาจจะชวนเด็กๆในปราสาทมาได้ไม่ครบทุกคนต้อง|ขออภัยด้วยฮะ แล้วก็ขออภัยในความล่าช้าและข้อผิด|พลาดที่อาจเกิดขึ้นในเกมด้วยฮะ ;-;",False)
        elif (c==22) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("สุดท้ายนี้ คนที่ต้องขอบคุณมากที่สุดก็คือจอมมารของเรา เกมนี้ก็เหมือนเป็น RECAP เล็กๆน้อยๆสำหรับความทรงจำที่เราได้สร้างร่วมกันในปีนี้",False)
        elif (c==23) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("ขอบคุณที่มาเป็นส่วนสำคัญในชีวิตของทุกๆคนนะฮะ ปีหน้าก็มาสร้างความทรงจำด้วยกันอีกนะ❤",False)
        elif (c==24) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("จบเกมแล้วฮะ จอมมารกดออกได้เลยฮะ อะหิ",False)
            
    def draw_mah_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME หม๋า",True)
            draw_text("ฟุดฟิดๆได้กลิ่นคนสวย",False)
        elif (c==2) :
            draw_text("SOME หม๋า",True)
            draw_text("แต่ง่วงจังเยยขอนอนอีกหน่อยน้า คร่อก",False)
        elif (c==3) :
            draw_text("คลิกหัวจุยบอกรักหม๋าห้าครั้งเพื่อปลุก อิอิ",False)
            pyxel.mouse(True)
            if self.love_count < 5:
                pyxel.blt(self.x, self.y, 0, 15, 49, 9, 8)
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if (self.x <= pyxel.mouse_x <= self.x+9) and (self.y <= pyxel.mouse_y <= self.y+7):
                        self.x = random.randint (0,184)
                        self.y = random.randint (0,160)
                        self.love_count += 1
            else:
                pyxel.mouse(False)
                pyxel.rect(0, 100, 192, 168, 14)
                draw_text("MISSION COMPLETE",False)
        elif (c==4) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("ฮ้าวว แผล่บๆ อยุนสวัสดิ์คับท่านจอมมาร",False)
        elif (c==5) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("ขอบคุณที่ช่วยปลุกนะฮะ เมื่อกี้อยู่ดีๆก็มีกระดูกตกใส่|หัวหม๋า ผมนี่วูบเลย",False)
        elif (c==6) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("แต่ผมไม่กินกระดูกอะ ยกให้ท่านจอมมารละกันฮับ |เผื่อจะใช้ประโยชน์อะไรได้ อะจิ๊ม๊วฟ",False)
        elif (c==7) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("รักจอมมารเหมือนกันนะฮะ",False)
        elif (c==8) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("ขอบคุณสำหรับทุกสิ่งทุกอย่าง ขอบคุณที่ใจดีกับหม๋า|เสมอ จอมมารเป็นกำลังใจที่สำคัญให้ตลอดเลย ทั้งให้|อ้อน ทั้งคอยปลอบใจ อยู่ข้างๆกัน ขอบคุณนะฮะ",False)
        elif (c==9) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("จอมมารบอกเสมอให้หม๋ารักตัวเอง จอมมารก็ต้องรักตัวเองด้วยนะคับบ ดูแลตัวเองดีๆนะ อย่าให้ใครมาเอา|ความสุขจากเราไปได้ อย่าแคร์ใครมากกว่าตัวเอง",False)
        elif (c==10) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("รวมถึงหม๋าด้วย จำสัญญาของเราได้ใช่ไหมครับ ถ้า|มีอะไรต้องบอกกันตรงๆนะ จอมมารสำคัญกับหม๋า หม๋าไม่อยากทำร้ายจอมมารโดยที่ไม่รู้ตัว",False)
        elif (c==11) :
            draw_text("หม๋า (KAM7411)",True)
            draw_text("สุขสันต์วันเกิดและวันครบรอบเดบิ้วนะค้าบ รักจอม|มารนะ หวังว่าจะชอบของขวัญชิ้นนี้นะฮับ ถึงจะไม่ได้|ออกมาดีมาก แต่ก็ตั้งใจทำนะฮับ เยิฟ",False)

    def draw_PTinTin_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME อุ๋งๆ",True)
            draw_text("หวัดดรฮะคนสวบ เอ้ย คนสวย อย่าบู้บี้ผม",False)
        elif (c==2) :
            draw_text("SOME อุ๋งๆ",True)
            draw_text("อยู่ต่อหน้าจอมมารแล้วพิมพ์ผิเตลอดเลน",False)
        elif (c==3) :
            draw_text("SOME อุ๋งๆ",True)
            draw_text("ต้องให้จอมมารสอย เอ้ย สอน",False)
        elif (c==4 and self.is_ขยร้ is None) :
            draw_text("SOME อุ๋งๆ",True)
            draw_text("คำว่า \"ขยี้\" ต้องเขียนยังไงฮะ",False)
            pyxel.mouse(True)
            pyxel.rect(28, 140, 48, 16, 3)
            pyxel.blt(44,140, 0, 32, 12, 16, 12)
            pyxel.rect(120, 140, 48, 16, 8)
            pyxel.blt(136, 142, 0, 48, 14, 20, 10)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (28 <= pyxel.mouse_x <= 28+48) and (140 <= pyxel.mouse_y <= 140+16):
                    self.is_ขยร้ = False
                elif (120 <= pyxel.mouse_x <= 120+48) and (140 <= pyxel.mouse_y <= 140+16):
                    self.is_ขยร้ = True
        elif (c==4) and not (self.is_ขยร้):
            draw_text("หม๋า",True)
            draw_text("หม๋าว่ามันบ่ใช่",False)
        elif (c==5) and not (self.is_ขยร้):
            draw_text("SOME อุ๋งๆ",True)
            draw_text("คำว่า \"ขยี้\" ต้องเขียนยังไงฮะ",False)
            pyxel.mouse(True)
            pyxel.rect(28, 140, 48, 16, 13)
            pyxel.blt(44,140, 0, 32, 28, 16, 12)
            pyxel.rect(120, 140, 48, 16, 8)
            pyxel.blt(136, 142, 0, 48, 14, 20, 10)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (120 <= pyxel.mouse_x <= 120+48) and (140 <= pyxel.mouse_y <= 140+16):
                    self.is_ขยร้ = True
        elif (self.is_ขยร้ and c<6):
            draw_text("ตินติน (TINTIN)",True)
            draw_text("อย่าบู้บี้ผม",False)
        elif (c==7):
            pyxel.rect(0, 100, 192, 168, 14)
            draw_text("MISSION COMPLETE",False)
        elif (c==8):
            draw_text("ตินติน (TINTIN)",True)
            draw_text("ขอบคุณฮะ นี่ผมให้เต้า...หู้",False)
        elif (c==10):
            draw_text("ตินติน (TINTIN)",True)
            draw_text("สุขสันต์​วันเกิดและวันครบรอบ 1 ปี ฮะ ขออวยพร|ให้จอมมารร่างกายแข็ง​แรง ได้ทำในสิ่งที่รัก มีเด็กเด็ก|เพิ่มขึ้นจนล้นปราสาทเลย",False)
             
    def draw_PMaw_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME แมว",True)
            draw_text("เมี้ยว เมี้ยว หิวจังเลยเมี้ยว",False)
        elif (c == 2) :
            draw_text("SOME แมว",True)
            draw_text("จอมมารคนสวยมีปลาไหมเมี้ยว", False)
        elif (c == 3) :
            draw_text("SOME แมว",True)
            draw_text("จอมมารจับปลาให้ตัวนึงหน่อยสิเมี้ยวๆๆ",False)
        elif (c == 4) :
            draw_text("แมว (NITHI)",True)
            draw_text("ขอบคุณมากเมี้ยว",False)
        elif (c == 5) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 6) :
            draw_text("แมว (NITHI)",True)
            draw_text("จอมมารอุตส่าห์จับปลามาให้ แมวให้หนวดแมวนะ |จะช่วยป้องกันโชคร้ายและนำพาโชคลาภมาให้นะเมี้ยว ",False)
        elif (c == 7) :
            draw_text("แมว (NITHI)",True)
            draw_text("ยินดีด้วยที่ก้าวมาถึงจุดนี้ ขอให้ก้าวต่อไปเรื่อยๆ|อย่างมั่นคงและสวยงามอย่างนี้ตลอดไปนะเมี้ยว",False)
        
    def draw_PlaNil_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME ปลา",True)
            draw_text("ท่านจอมมาร คิดถึงจัง ขอชิมแขนคำนึงคับ สวบๆๆ",False)
        elif (c == 2) :
            draw_text("SOME ปลา",True)
            draw_text("ปลาหิว ปลาอยากสวบดอกไม้ แต่ปลาขึ้นไปเก็บดอกไม้ไม่ได้", False)
        elif (c == 3) :
            draw_text("SOME ปลา",True)
            draw_text("ท่านจอมมารช่วยเก็บดอกไม้สีฟ้าตรงนั้นให้ปลาสัก|สิบดอกหน่อยสิคั้บ",False)
        elif (c == 4) :
            draw_text("ปลานิล (PLANIL)",True)
            draw_text("สวบๆๆๆ ขอบคุณคั้บท่านจอมมาร",False)
        elif (c == 5) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 6) :
            draw_text("ปลานิล (PLANIL)",True)
            draw_text("ขอบคุณคับท่านจอมมาร ปลาให้ลูกอมนะ",False)
        elif (c == 7) :
            draw_text("ปลานิล (PLANIL)",True)
            draw_text("ยินดีกับท่านจอมมารด้วยนะครับสำหรับการเดินทางมาตลอดหนึ่งปี! ท่านจอมมารของเราจากเติบโตขึ้นมา|มากๆๆๆเลยยย!! เป็นคนน่ารักที่เก่งที่สุดด",False)
        elif (c == 8) :
            draw_text("ปลานิล (PLANIL)",True)   
            draw_text("แล้วต่อจากนี้ผมก็ขอHBDให้วันคล้ายวันเกิดของท่านจอมมารนะครับ ผมขอให้ท่านจอมมารสุขภาพร่างกาย|แข็งแรงมีพลังงานเต็มเปี่ยมฟิตปั๋งๆเลย",False)
        elif (c == 9) :
            draw_text("ปลานิล (PLANIL)",True)   
            draw_text("พักผ่อนเยอะๆกินข้าวให้ครบ3มื้อดื่มน้ำให้เพียงพอ|ไม่โหมงานหนักเกินไป มีความสุขให้มากๆยิ้มให้เยอะๆ|ท่านจอมมารของเราเหมาะกับรอยยิ้มที่สุดแล้วล่ะครับ>:D",False)

    def draw_Somsom_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME ส้ม",True)
            draw_text("ว้า ทำไมไม่หล่นใส่นมนะ สงสัยจะเล็งผิด แย่จัง" ,False)
        elif (c == 2) :
            draw_text("SOME ส้ม",True)
            draw_text("ได้ยินว่าท่านมีปราสาท แล้วที่ปราสาทปลูกต้นไม้|หรือไม่", False)
        elif (c == 3) :
            draw_text("SOME ส้ม",True)
            draw_text("แต่ก็นะใช่ว่าทุกต้นจะปลูกใกล้ปราสาทได้ เดี๋ยว|ปราสาทจะพัง",False)
        elif (c == 4) :
            draw_text("SOME ส้ม",True)
            draw_text("เอาล่ะนะ ฮะแฮ่ม",False)
        elif (c == 5 and self.is_หูกระจง is None) :
            draw_text("SOME ส้ม",True)
            draw_text("ต้นอะไรควรปลูกให้ห่างจากปราสาท ติ้กต้อกๆ",False)
            pyxel.mouse(True)
            pyxel.rect(28, 140, 54, 16, 5)
            pyxel.blt(30,143, 0, 96, 32, 50, 11)
            pyxel.rect(120, 140, 48, 16, 4)
            pyxel.blt(128,145, 0, 64, 34, 32, 9)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (28 <= pyxel.mouse_x <= 28+54) and (140 <= pyxel.mouse_y <= 140+16):
                    self.is_หูกระจง = True
                elif (120 <= pyxel.mouse_x <= 120+48) and (140 <= pyxel.mouse_y <= 140+16):
                    self.is_หูกระจง = False
        elif (c==5) and not (self.is_หูกระจง):
            draw_text("SOME ส้ม",True)
            draw_text("อะจิ๊มิ๊ เด็กน้อยตอบผิดแล้วจ้ะ หุหุ||  (เลียนแบบท่านผู้หนึ่งมา แค่กๆ)",False)
        elif (c==6) and not (self.is_หูกระจง):
            draw_text("SOME ส้ม",True)
            draw_text("ต้นอะไรควรปลูกให้ห่างจากปราสาท ติ้กต้อกๆ",False)
            pyxel.mouse(True)
            pyxel.rect(28, 140, 54, 16, 5)
            pyxel.blt(30,143, 0, 96, 32, 50, 11)
            pyxel.rect(120, 140, 48, 16, 13)
            pyxel.blt(128,145, 0, 152, 34, 32, 9)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (28 <= pyxel.mouse_x <= 28+54) and (140 <= pyxel.mouse_y <= 140+16):
                    self.is_หูกระจง = True
        elif (self.is_หูกระจง and c<7):
            pyxel.mouse(False)
            draw_text("สมชาย (SOMCHANG)",True)
            draw_text("ถะ ถะ ถูกต้องนะคร้าบบ",False)
        elif (c==7):
            pyxel.rect(0, 100, 192, 168, 14)
            draw_text("MISSION COMPLETE",False)
        elif (c==8):
            draw_text("สมชาย (SOMCHANG)",True)
            draw_text("กินส้มมั้ยคะเบ้บบี้ ผมเอาตัวเองให้เลย",False)
        elif (c==10):
            draw_text("สมชาย (SOMCHANG)",True)
            draw_text("ยินดีกับจอมมารทั้งครบรอบเดบิวต์และสุขสันต์วัน|เกิดนะคะ ขอให้ในทุกวันของจอมมารมีแต่ความน่ารัก|สดใสและมีรอยยิ้มอยู่เสมอ สมชายหัวใจจอมมาร❤",False)

    def draw_Mangu_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME มะงึ",True)
            draw_text("สวัสดีท่านจอมมาร มีอะไรให้มะงึรับใช้มั้ย",False)
        elif (c == 2) :
            draw_text("SOME มะงึ",True)
            draw_text("โอ้มะงึมีหาง ท่านต้องการหางมะงึหรอ", False)
        elif (c == 3) :
            draw_text("SOME มะงึ",True)
            draw_text("ได้สิแต่ท่านต้องช่วยอะไรมะงึอย่างนึงนะ ช่วยไปเก็บ|สมุนไพรในตำนานแล้วท่านจะได้หางมะงึไป",False)
        elif (c == 4) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 5 and self.grill_tail is None) :
            draw_text("มะงึ (PAWEEKORN)",True)
            draw_text("โอ้ ขอบคุณมาก รับนี่ไปสิ หางมะงึ 1 EA จะว่าไปจะรับแบบย่างมั้ย",False)
            pyxel.mouse(True)
            pyxel.rect(28, 148, 48, 16, 3)
            pyxel.blt(44,151, 0, 184, 32, 16, 8)
            pyxel.rect(120, 148, 48, 16, 8)
            pyxel.blt(138, 151, 0, 200, 32, 12, 8)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (28 <= pyxel.mouse_x <= 28+48) and (148 <= pyxel.mouse_y <= 148+16):
                    self.grill_tail = True
                elif (120 <= pyxel.mouse_x <= 120+48) and (148 <= pyxel.mouse_y <= 148+16):
                    self.grill_tail = False
        elif (c == 5 and self.grill_tail) :
            draw_text("มะงึ (PAWEEKORN)",True)
            draw_text("ย่างก็...มีสูตรธรรมดากับสูตรเผ็ด",False)
            pyxel.mouse(True)
            pyxel.rect(28, 140, 48, 16, 3)
            pyxel.blt(38,144, 0, 184, 40, 32, 8)
            pyxel.rect(120, 140, 48, 16, 8)
            pyxel.blt(138, 142, 0, 216, 38, 16, 10)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (28 <= pyxel.mouse_x <= 28+48) and (140 <= pyxel.mouse_y <= 148+16):
                    self.is_spicy_tail = False
                    pyxel.mouse(False)
                elif (120 <= pyxel.mouse_x <= 120+48) and (140 <= pyxel.mouse_y <= 148+16):
                    self.is_spicy_tail = True
                    pyxel.mouse(False)
                print (self.is_spicy_tail)
        elif (c == 5 and not self.grill_tail) :
            pyxel.mouse(False)
            draw_text("มะงึ (PAWEEKORN)",True)
            draw_text("ไม่หรอ...",False)
        elif (c == 6) :
            draw_text("มะงึ (PAWEEKORN)",True)
            draw_text("ขอให้โลกใบนี้ใจดีกับจอมมารมากๆ มีความสุขเยอะๆครับจอมมาร มะงึจะเป็นกำลังใจให้จอมมารนะ เจอกัน|ครับ",False)
        elif (c == 7) :
            draw_text("มะงึ (PAWEEKORN)",True)
            draw_text("ขอให้โลกใบนี้ใจดีกับจอมมารมากๆ มีความสุขเยอะๆครับจอมมาร มะงึจะเป็นกำลังใจให้จอมมารนะ เจอกัน|ครับ",False)

    def draw_Herb_text(self, c, r):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == r):
            draw_text("หม๋า เอ๊ย ต้นสมุนไพร",True)
            draw_text("อิย๊าา จอมมารดึงแรงจังเลยครับผมชอบ เอาสมุนไพรในตำนานไปได้เลยฮะ ผมยกให้ด้วยความเต็มใจ อิอิ",False)
        else:
            draw_text("ต้นสมุนไพร",True)
            draw_text(["ต้นสมุนไพรดูยังอ่อนเกินกว่าจะใช้ได้","ต้นสมุนไพรแห้งเหี่ยวเหมือนไม่ได้น้ำมาแปดปี","ต้นสมุนไพรแก่งั่กหายใจรวยริน","ต้นสมุนไพรเล่นตัวไม่ยอมให้จับให้ทัช","ไม่ใช่ต้นสมุนไพรแค่มาเนียนเฉยๆ"][r-c-1],False)
    
    def draw_nongTan_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME กระต่าย",True)
            draw_text("สวัสดีค่ะท่านจอมมาร",False)
        elif (c == 2) :
            draw_text("SOME กระต่าย",True)
            draw_text("ท่านจอมมารหาของอยู่หรอคะ หนูก็กำลังหาแครอท|สีทองอยู่เหมือนกัน แต่แครอทที่นี่กระจายไปทั่วเลยแถมยังปนกับแครอทธรรมดาด้วย", False)
        elif (c == 3) :
            draw_text("SOME กระต่าย",True)
            draw_text("ถ้าท่านจอมมารช่วยเก็บให้หนูสัก 4 อัน ไม่รู้ว่าจะมี|ประโยชน์ไหม แต่จะแบ่งให้ท่านจอมมารด้วยนะ",False)
        elif (c == 4) :
            draw_text("กระตุ่ย (TANYARAT RIN)",True)
            draw_text("ขอบคุณค่ะท่านจอมมาร",False)
        elif (c == 5) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 6) :
            draw_text("กระตุ่ย (TANYARAT RIN)",True)
            draw_text("หนูแบ่งแครอททองคำให้อันนึงนะ โชคดีค่ะ",False)
        elif (c == 7) :
            draw_text("กระตุ่ย (TANYARAT RIN)",True)
            draw_text("ขอให้ท่านจอมมาร มีผู้ติดตามที่เยอะขึ้นจนได้ แครอททองคำตามที่ต้องการเลยนะ",False)

    
    def draw_nongArw_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME จิ้งจอก",True)
            draw_text("นึกว่าใคร ท่านจอมมารคนสวยนี่เอง",False)
        elif (c == 2) :
            draw_text("SOME จิ้งจอก",True)
            draw_text("เกี่ยวกับหีบสมบัติหรอ หนูไม่รู้เรื่องหรอก หนูมาตามหาการ์ดจอ", False)
        elif (c == 3) :
            draw_text("SOME จิ้งจอก",True)
            draw_text("ท่านจอมมารช่วยหนูหาการ์ดจอหน่อยจิ เดี๋ยวหนูจะ|ให้ของตอบแทน",False)
        elif (c == 4) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 5) :
            draw_text("อาว (ARX-7 ARBALEST)",True)
            draw_text("เย้ ท่านจอมมารหาเจอจริงๆด้วย",False)
        elif (c == 6) :
            draw_text("อาว (ARX-7 ARBALEST)",True)
            draw_text("ได้ท่านจอมมารช่วยไว้แท้ๆเลย นี่หนูให้อมยิ้ม",False)
        elif (c == 7) :
            draw_text("อาว (ARX-7 ARBALEST)",True)
            draw_text("ไหนๆก็ครบรอบ1ปีแล้ว ขอให้ท่านจอมมารสุขภาพ|แข็งแรงแล้วก็ มีกำลังใจและใจสู้ในการทำวีต่อไปด้วยนะครับ",False)

    def draw_pErin_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME สาว",True)
            draw_text("สวัสดีค่ะท่านจอมมาร ไม่ได้เจอกันตั้งนาน เป็นไงบ้าง สบายดีใช่มั้ยคะ ท่านดูสวยและสง่างามเสมอเลยนะคะ❤",False)
        elif (c == 2) :
            draw_text("SOME สาว",True)
            draw_text("ท่านจอมมารสะดวกไหมคะ มีเรื่องอยากให้ช่วยเหลือ|สักเล็กน้อยน่ะค่ะ", False)
        elif (c == 3) :
            draw_text("SOME สาว",True)
            draw_text("พอดีแก้พัซเซิลอันนี้มาได้สักพักแล้ว แก้ไม่ได้สักที |ปวดหัวมากเลยค่ะ ท่านจอมมารพอจะแก้ให้ได้ไหมคะ ;-;",False)
        elif (c == 4) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 5) :
            draw_text("เอริน (ERIN)",True)
            draw_text("ในที่สุดก็แก้ได้สักที!! ถ้าไม่ได้ท่านจอมมารคงปวดหัวยาวแน่ๆ ขอบคุณท่านมากจริงๆ",False)
        elif (c == 6) :
            draw_text("เอริน (ERIN)",True)
            draw_text("อันนี้เป็นของแทนคำขอบคุณเล็กน้อยจากเราค่ะ เป็น|กาแฟที่ดื่มเป็นประจำ หวังว่าท่านจะชอบนะคะ❤",False)
        elif (c == 8) :
            draw_text("เอริน (ERIN)",True)
            draw_text("ยินดีสำหรับครอบรอบเดบิวต์ 1 ปีด้วยนะคะจอมมาร เย้!!!❤️ ขอให้จอมมารมียอดผู้ติดตามมากขึ้นไปอีก",False)
        elif (c == 9) :
            draw_text("เอริน (ERIN)",True)
            draw_text("ชอบงานของจอมมารมากๆ ผลิตงานวาดและงาน|เพลงต่อไปนะคะ จะคอยติดตามไปเรื่อยๆเลยค่ะ❤️",False)

    def draw_nongPat_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("SOME เด็ก",True)
            draw_text("ฮือ...ฮือ",False)
        elif (c == 2) :
            draw_text("SOME เด็ก",True)
            draw_text("ฮือ...หนูทำขวดนมหาย หนูนอนไม่ได้ ถ้าไม่ได้กินนม", False)
        elif (c == 3) :
            draw_text("SOME เด็ก",True)
            draw_text("ฮือ...;-;",False)
        elif (c == 4) :
            draw_text("MISSION COMPLETE",False)
        elif (c == 5) :
            draw_text("แพท (PATTRIKA)",True)
            draw_text("ฮึก ขอบคุณค่ะพี่สาว นี่คือของรางวัลแทนคำขอบคุณ|นะ",False)
        elif (c == 6) :
            draw_text("ได้รับ ปิ่นโตที่ใส่เก้นเอ็บวุ้นสุ้ง เอ้ย จุ้งเอ็บวุ้นเด้น เอ้ย ดุ้งกุ้งอ่มบุ๊นเจ้น เอ้ย อุ้งเจ็บดุ้งจุ้ง เอ้ย ดุ้งอมยุ้นเจ้น เอ้ย |เจ้นเอ็บวุ้นดุ้ง เอ้ย กุ้งอบวุ้นเส้น เอ้ย ถูกแล้ว!",False)
        elif (c == 8) :
            draw_text("แพท (PATTRIKA)",True)
            draw_text("ขอให้พี่สาวมีความสุขมากๆ มีแต่คนรักและเอ็นดู เป็นที่รักของทุกคนรอบข้าง",False)
    
    def draw_nongYeen_text(self, c):
        pyxel.rect(0, 100, 192, 168, 14)
        if (c == 1) :
            draw_text("ยีนส์ (YEENNNN)",True)
            draw_text("ขอให้จอมมารพบเจอแต่ความใจดี สุขสันต์วันครบ|รอบนะคะขอให้จอมมารไม่ปวดหลังสุขภาพร่างกายแข็งแรงอยู่เป็นวีทูปแบบนี้ไปนาน ๆ เลยเย้",False)

class App:
    def __init__(self):
        print ("Game Start")
        
        pyxel.init(192, 168, caption="Charlotte Birthday", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.water = Water()
        self.c_main_story = -1
        self.chest = Chest(72,120)
        self.open_chest = False
        self.flower_1 = Flower(64,64)
        self.flower_2 = Flower(72,64)
        self.flower_3 = Flower(80,64)
        self.flower_4 = Flower(88,64)
        self.flower_5 = Flower(96,64)
        self.flower_6 = Flower(64,72)
        self.flower_7 = Flower(72,72)
        self.flower_8 = Flower(80,72)
        self.flower_9 = Flower(88,72)
        self.flower_10 = Flower(96,72)
        self.pick_flower_1 = False
        self.pick_flower_2 = False
        self.pick_flower_3 = False
        self.pick_flower_4 = False
        self.pick_flower_5 = False
        self.pick_flower_6 = False
        self.pick_flower_7 = False
        self.pick_flower_8 = False
        self.pick_flower_9 = False
        self.pick_flower_10 = False
        self.c_flower = 0
        self.herb_1 = Herb(random.randint(120,180), random.randint(0,30))
        self.herb_2 = Herb(random.randint(120,180), random.randint(0,30))
        self.herb_3 = Herb(random.randint(120,180), random.randint(0,30))
        self.herb_4 = Herb(random.randint(120,180), random.randint(0,30))
        self.herb_5 = Herb(random.randint(120,180), random.randint(0,30))
        self.rand_herb = random.randint(1,5)
        self.c_herb = 0
        self.pick_herb_1 = False
        self.pick_herb_2 = False
        self.pick_herb_3 = False
        self.pick_herb_4 = False
        self.pick_herb_5 = False
        self.carrot_1 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_2 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_3 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_4 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_5 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_6 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_7 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_8 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_9 = Carrot(random.randint(0,140), random.randint(0,114))
        self.carrot_10 = Carrot(random.randint(0,140), random.randint(0,114))
        self.pick_carrot_1 = False
        self.pick_carrot_2 = False
        self.pick_carrot_3 = False
        self.pick_carrot_4 = False
        self.pick_carrot_5 = False
        self.pick_carrot_6 = False
        self.pick_carrot_7 = False
        self.pick_carrot_8 = False
        self.pick_carrot_9 = False
        self.pick_carrot_10 = False
        self.c_gloden_carrot = 0
        self.gloden_carrot = random.sample(range(1,10),4)
        self.gpu = GPU(random.randint(0,140), random.randint(0,114))
        self.bottle = Bottle(random.randint(0,140), random.randint(0,114))
        self.tree = Tree(random.randint(0,120), random.randint(0,112))
        self.somsom = SomSom(self.tree.x+8, self.tree.y)
        self.somsom_drop = False
        self.c_somsom = 0
        self.start_x_somsom= self.somsom.x
        self.start_y_somsom = self.somsom.y
        self.quest_somsom = False
        self.sent_quest_somsom = False
        self.hud = Hud()
        self.interract: Interact = Interact.NULL
        self.charlotte = Charlotte(95, 84)
        self.start_x_charlotte = self.charlotte.x
        self.start_y_charlotte = self.charlotte.y
        self.mah = Mah(20, 20)
        self.start_x_mah = self.mah.x
        self.start_y_mah = self.mah.y
        self.c_mah = 0
        self.quest_mah = False
        self.sent_quest_mah = False
        self.pTinTin = PTinTin(random.randint(0,120), random.randint(132,160))
        self.start_x_pTinTin = self.pTinTin.x
        self.start_y_pTinTin = self.pTinTin.y
        self.c_pTinTin = 0
        self.quest_ptintin = False
        self.sent_quest_ptintin = False
        self.pMaw = PMaw(50, 100)
        self.start_x_pMaw = self.pMaw.x
        self.start_y_pMaw = self.pMaw.y
        self.c_pMaw = 0
        self.quest_pmaw = False
        self.sent_quest_pmaw = False
        self.mangu = Mangu(random.randint(0,120), random.randint(0,114))
        self.start_x_mangu = self.mangu.x
        self.start_y_mangu = self.mangu.y
        self.c_mangu = 0
        self.quest_mangu = False
        self.sent_quest_mangu = False
        self.nongtan = nongTan(random.randint(0,120), random.randint(0,114))
        self.start_x_nongtan = self.nongtan.x
        self.start_y_nongtan = self.nongtan.y
        self.c_nongtan = 0
        self.quest_nongtan = False
        self.sent_quest_nongtan = False
        self.nongarw = nongArw(random.randint(0,120), random.randint(0,114))
        self.start_x_nongarw = self.nongarw.x
        self.start_y_nongarw = self.nongarw.y
        self.c_nongarw = 0
        self.quest_nongarw = False
        self.sent_quest_nongarw = False
        self.found_GPU = False
        self.pErin = PErin(random.randint(0,120), random.randint(0,114))
        self.start_x_pErin = self.pErin.x
        self.start_y_pErin = self.pErin.y
        self.c_pErin = 0
        self.sound_quest = random.choices(range(0,4),k=5)
        print (self.sound_quest)
        self.c_sound = 0
        self.sound_answer = []
        self.play_sound = False
        self.quest_pErin = False
        self.sent_quest_pErin = False
        self.time_since_last_move_s = 0
        self.nongPat = nongPat(random.randint(0,120), random.randint(0,114))
        self.start_x_nongPat = self.nongPat.x
        self.start_y_nongPat = self.nongPat.y
        self.c_nongPat = 0
        self.quest_nongPat = False
        self.sent_quest_nongPat = False
        self.found_bottle = False
        self.plaNil = PlaNil(random.randint(0,120), random.randint(132,160))
        self.start_x_plaNil = self.plaNil.x
        self.start_y_plaNil = self.plaNil.y
        self.c_plaNil = 0
        self.quest_planil = False
        self.sent_quest_planil = False
        self.time_p = 0
        self.time_since_last_move_p = 0
        self.charlotte_land = True
        self.charlotte_direction: Direction = Direction.RIGHT
        self.charlotte_state: State = State.IDLE_0
        self.fish = Fish(random.randint(0,120), random.randint(132,160))
        self.time_fish = 0
        self.time_since_last_move_f = 0
        self.time_last_frame = time.time()
        self.dt = 0
        self.time_since_last_move = 0
        self.speed = 2
        self.c_fish = 0
        self.draw_fish = False
        self.new_fish = True
        self.nongyeen = nongYeen(174,92)
        self.quest_nongyeen = True
        self.c_nongyeen = 0
        self.start_x_nongyeen = self.nongyeen.x
        self.start_y_nongyeen = self.nongyeen.y
        self.sent_quest_nongyeen = False
        self.cake = Cake(106,54)
        self.blow = False
        self.ending = False
        # self.charlotte.x = 72
        # self.charlotte.y = 70
        # self.chest.x = 72
        # self.chest.y = 70
        # self.c_main_story = 17
        # self.interract = Interact.ENDING
        pyxel.run(self.update, self.draw)
        
    def update(self):
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        self.time_since_last_move += self.dt
        self.time_since_last_move_f += self.dt
        self.time_since_last_move_p += self.dt
        self.time_since_last_move_s += self.dt
        self.time_last_frame = time_this_frame
        if self.time_since_last_move_f >= self.time_fish :
            self.draw_fish = True
            self.time_fish = random.randint(0,5)
            self.time_since_last_move_f = 0
            self.fish.x = random.randint(0,120)
            self.fish.y = random.randint(132,160)
            self.new_fish = True
        if self.time_since_last_move_p >= self.time_p :
            self.draw_p = True
            self.time_p = random.randint(0,5)
            self.time_since_last_move_p = 0
            self.plaNil.x = random.randint(0,120)
            self.plaNil.y = random.randint(132,160)
            self.start_x_PlaNil = self.plaNil.x
            self.start_y_PlaNil = self.plaNil.y
        if self.time_since_last_move_s >= 1 and self.play_sound:
            self.time_since_last_move_s = 0
            pyxel.play(0,self.sound_quest[self.c_sound])
            print (self.c_sound,self.sound_quest[self.c_sound])
            self.c_sound += 1
            if self.c_sound == 5 :
                self.c_sound = 0
                self.play_sound = False
        self.check_input()
        if self.time_since_last_move >= 1 / self.speed:
            self.time_since_last_move = 0
            if self.charlotte_state == State.IDLE_0 :
                self.charlotte_state = State.IDLE_1
            else :
                self.charlotte_state = State.IDLE_0
        self.check_colisions()
        if self.interract == Interact.NULL :
            self.move_charlotte()

    def draw(self):
        pyxel.cls(0)
        if self.open_chest and not self.ending:
            pyxel.bltm(-192, 0, 0, 0, 0, 100, 100)
            if self.interract == Interact.MAIN:
                self.hud.main_story_text(self.c_main_story)
            else :
                pyxel.blt(88, 114, 0, 95, 8, 31, 9)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if (88 <= pyxel.mouse_x <= 88+31) and (114 <= pyxel.mouse_y <= 114+9):
                    if(self.quest_mah):
                        self.sent_quest_mah = True
                    if(self.quest_mangu):
                        self.sent_quest_mangu = True
                    if(self.quest_nongtan):
                        self.sent_quest_nongtan = True
                    if(self.quest_nongPat):
                        self.sent_quest_nongPat = True
                    if(self.quest_nongarw):
                        self.sent_quest_nongarw = True
                    if(self.quest_planil) :
                        self.sent_quest_planil = True
                    if(self.quest_pmaw) :
                        self.sent_quest_pmaw = True
                    if(self.quest_ptintin) :
                        self.sent_quest_ptintin = True
                    if(self.quest_pErin) :
                        self.sent_quest_pErin = True
                    if(self.quest_somsom) :
                        self.sent_quest_somsom = True
                    if(self.quest_nongyeen) :
                        self.sent_quest_nongyeen= True
            if self.sent_quest_mah :
                pyxel.blt(48, 40, 0, 112, 0, 8, 8)
            if self.sent_quest_pmaw :
                pyxel.blt(80, 40, 0, 176, 0, 8, 8)
            if self.sent_quest_nongtan :
                pyxel.blt(112, 40, 0, 136, 0, 8, 8)
            if self.sent_quest_nongPat :
                pyxel.blt(144, 40, 0, 152, 0, 8, 8)
            if self.sent_quest_nongarw :
                pyxel.blt(64, 64, 0, 144, 0, 8, 8)
            if self.sent_quest_planil :
                pyxel.blt(96, 64, 0, 168, 0, 8, 8)
            if self.sent_quest_nongyeen :
                pyxel.blt(128, 64, 0, 184, 0, 8, 8)
            if self.sent_quest_mangu :
                if self.hud.is_spicy_tail :
                    pyxel.blt(48, 88, 0, 128, 0, 8, 8)
                else :
                    pyxel.blt(48, 88, 0, 120, 0, 8, 8)
            if self.sent_quest_ptintin :
                pyxel.blt(80, 88, 0, 160, 0, 8, 8)
            if self.sent_quest_pErin :
                pyxel.blt(112, 88, 0, 200, 0, 8, 8)
            if self.sent_quest_somsom :
                pyxel.blt(144, 88, 0, 192, 0, 8, 8)
            if (self.sent_quest_mah and self.sent_quest_pmaw and self.sent_quest_nongtan and self.sent_quest_nongPat and self.sent_quest_nongarw and self.sent_quest_planil and self.sent_quest_nongyeen and self.sent_quest_mangu and self.sent_quest_ptintin and self.sent_quest_pErin and self.sent_quest_somsom) :
                self.ending = True
                self.charlotte.x = 72
                self.charlotte.y = 70
                self.chest.x = 72
                self.chest.y = 70
        elif self.interract == Interact.PERIN_GAME :
            pyxel.bltm(-384, -8, 0, 0, 0, 100, 100)

        else :
            pyxel.bltm(0, 0, 0, 0, 0, 100, 100)
            if self.ending :
                pyxel.bltm(0, -50, 0, 0, 0, 100, 100)
                self.water.y = 78
                self.nongyeen.x = 60
                self.nongyeen.y = 70
                self.pTinTin.x = 66
                self.pTinTin.y = 78
                self.plaNil.x = 74
                self.plaNil.y = 78
                self.nongarw.x = 84
                self.nongarw.y = 70
                self.nongtan.x = 86
                self.nongtan.y = 62
                self.nongPat.x = 86
                self.nongPat.y = 54
                self.mah.x = 78
                self.mah.y = 52
                self.pMaw.x = 70
                self.pMaw.y = 60
                self.pErin.x = 62
                self.pErin.y = 52
                self.mangu.x = 54
                self.mangu.y = 54
                self.somsom.x = 54
                self.somsom.y = 56
                self.chest.x = 72
                self.chest.y = 70
                self.cake.draw(self.charlotte_state, self.blow)
                if (self.c_main_story == 14 and not self.blow) or (self.c_main_story == 17) :
                    pass
                else :
                    self.hud.main_story_text(self.c_main_story)
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if (self.c_main_story == 14 and not self.blow) or self.c_main_story == 17:
                        pass
                    else :
                        self.c_main_story += 1
            if self.interract == Interact.NULL or self.interract == Interact.WATER :
                if not self.ending :
                    if not (self.pick_flower_1) :
                        self.flower_1.draw(self.charlotte_state)
                    if not (self.pick_flower_2) :
                        self.flower_2.draw(self.charlotte_state)
                    if not (self.pick_flower_3) :
                        self.flower_3.draw(self.charlotte_state)
                    if not (self.pick_flower_4) :
                        self.flower_4.draw(self.charlotte_state)
                    if not (self.pick_flower_5) :
                        self.flower_5.draw(self.charlotte_state)
                    if not (self.pick_flower_6) :
                        self.flower_6.draw(self.charlotte_state)
                    if not (self.pick_flower_7) :
                        self.flower_7.draw(self.charlotte_state)
                    if not (self.pick_flower_8) :
                        self.flower_8.draw(self.charlotte_state)
                    if not (self.pick_flower_9) :
                        self.flower_9.draw(self.charlotte_state)
                    if not (self.pick_flower_10) :
                        self.flower_10.draw(self.charlotte_state)
                    self.tree.draw(self.charlotte_state)
                    self.herb_1.draw(self.charlotte_state)
                    self.herb_2.draw(self.charlotte_state)
                    self.herb_3.draw(self.charlotte_state)
                    self.herb_4.draw(self.charlotte_state)
                    self.herb_5.draw(self.charlotte_state)
                else :
                    self.somsom.draw(self.charlotte_state)
                if self.c_nongtan > 0 :
                    if not self.pick_carrot_1 and not self.quest_nongtan :
                        self.carrot_1.draw(self.charlotte_state)
                    if not self.pick_carrot_2 and not self.quest_nongtan :
                        self.carrot_2.draw(self.charlotte_state)
                    if not self.pick_carrot_3 and not self.quest_nongtan :
                        self.carrot_3.draw(self.charlotte_state)
                    if not self.pick_carrot_4 and not self.quest_nongtan :
                        self.carrot_4.draw(self.charlotte_state)
                    if not self.pick_carrot_5 and not self.quest_nongtan :
                        self.carrot_5.draw(self.charlotte_state)
                    if not self.pick_carrot_6 and not self.quest_nongtan :
                        self.carrot_6.draw(self.charlotte_state)
                    if not self.pick_carrot_7 and not self.quest_nongtan :
                        self.carrot_7.draw(self.charlotte_state)
                    if not self.pick_carrot_8 and not self.quest_nongtan :
                        self.carrot_8.draw(self.charlotte_state)
                    if not self.pick_carrot_9 and not self.quest_nongtan :
                        self.carrot_9.draw(self.charlotte_state)
                    if not self.pick_carrot_10 and not self.quest_nongtan :
                        self.carrot_10.draw(self.charlotte_state)
                    if self.c_gloden_carrot > 0 and not self.quest_nongtan :
                        pyxel.blt(179, 160, 0, 90, 16, 4, 8)
                        pyxel.blt(184, 163, 0, 96, 21, 3, 3)
                        pyxel.blt(188, 162, 0, 0+(8*(self.c_gloden_carrot-1)), 91, 4, 5)
                if self.c_nongPat > 0 and not self.found_bottle:
                    self.bottle.draw(self.charlotte_state)
                self.nongyeen.draw(self.charlotte_state)
                self.mah.draw(self.charlotte_state)
                self.pTinTin.draw(self.charlotte_state)
                self.pMaw.draw(self.charlotte_state)
                self.mangu.draw(self.charlotte_state)
                self.chest.draw(self.charlotte_state, self.ending)
                self.nongtan.draw(self.charlotte_state)
                self.nongarw.draw(self.charlotte_state)
                self.pErin.draw(self.charlotte_state)
                self.nongPat.draw(self.charlotte_state)
                if not self.found_GPU and self.c_nongarw > 0:
                    self.gpu.draw(self.charlotte_state)
                if self.somsom_drop :
                    self.somsom.draw(self.charlotte_state)
                if (self.draw_p):
                    self.plaNil.draw(self.charlotte_state)
                if ((self.c_pMaw == 3 ) and self.new_fish and self.draw_fish):
                    self.fish.draw(self.charlotte_state)
                self.charlotte.draw(self.charlotte_direction, self.charlotte_state, self.charlotte_land)
            else: 
                self.charlotte.x = 98
                self.charlotte.y = 92
                if self.interract == Interact.MAIN:
                    self.charlotte.x = 180
                    self.charlotte.y = 92
                    self.hud.main_story_text(self.c_main_story)
                    if (self.c_main_story > 2 ):
                        self.nongyeen.draw(self.charlotte_state)
                elif (self.interract == Interact.MAH):
                    self.mah.x = 90
                    self.mah.y = 92
                    self.hud.draw_mah_text(self.c_mah)
                    self.mah.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.PTINTIN):
                    self.pTinTin.x = 90
                    self.pTinTin.y = 92
                    self.hud.draw_PTinTin_text(self.c_pTinTin)
                    self.pTinTin.draw(self.charlotte_state)
                    self.charlotte_land = False
                    self.charlotte.y += 2
                elif (self.interract == Interact.PMAW):
                    self.pMaw.x = 90
                    self.pMaw.y = 92
                    self.hud.draw_PMaw_text(self.c_pMaw)
                    self.pMaw.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.PLANIL):
                    self.plaNil.x = 90
                    self.plaNil.y = 92
                    self.hud.draw_PlaNil_text(self.c_plaNil)
                    self.plaNil.draw(self.charlotte_state)
                    self.charlotte_land = False
                    self.charlotte.y += 2
                elif (self.interract == Interact.SOMSOM):
                    self.somsom.x = 90
                    self.somsom.y = 85
                    self.hud.draw_Somsom_text(self.c_somsom)
                    self.somsom.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.MANGU):
                    self.mangu.x = 90
                    self.mangu.y = 92
                    self.hud.draw_Mangu_text(self.c_mangu)
                    self.mangu.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.HERB):
                    self.hud.draw_Herb_text(self.c_herb, self.rand_herb)
                elif (self.interract == Interact.NONGTAN):
                    self.nongtan.x = 90
                    self.nongtan.y = 92
                    self.hud.draw_nongTan_text(self.c_nongtan)
                    self.nongtan.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.NONGARW):
                    self.nongarw.x = 90
                    self.nongarw.y = 92
                    self.hud.draw_nongArw_text(self.c_nongarw)
                    self.nongarw.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.PERIN):
                    self.pErin.x = 90
                    self.pErin.y = 92
                    self.hud.draw_pErin_text(self.c_pErin)
                    self.pErin.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.NONGPAT):
                    self.nongPat.x = 90
                    self.nongPat.y = 92
                    self.hud.draw_nongPat_text(self.c_nongPat)
                    self.nongPat.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.NONGYEEN):
                    self.nongyeen.x = 90
                    self.nongyeen.y = 92
                    self.hud.draw_nongYeen_text(self.c_nongyeen)
                    self.nongyeen.draw(self.charlotte_state)
                    self.charlotte_land = True
                elif (self.interract == Interact.ENDING):
                    self.hud.main_story_text(self.c_main_story)
                    self.nongyeen.draw(self.charlotte_state)
                    self.mah.draw(self.charlotte_state)
                    self.pTinTin.draw(self.charlotte_state)
                    self.pMaw.draw(self.charlotte_state)
                    self.mangu.draw(self.charlotte_state)
                    self.chest.draw(self.charlotte_state, self.ending)
                    self.nongtan.draw(self.charlotte_state)
                    self.nongarw.draw(self.charlotte_state)
                    self.pErin.draw(self.charlotte_state)
                    self.nongPat.draw(self.charlotte_state)
                    self.somsom.draw(self.charlotte_state)
                self.charlotte.draw(self.charlotte_direction, self.charlotte_state, self.charlotte_land)

    def move_charlotte(self):
        if self.charlotte_direction == Direction.UP:
            self.charlotte.y -= 1
        elif self.charlotte_direction == Direction.RIGHT:
            self.charlotte.x += 1
        elif self.charlotte_direction == Direction.DOWN:
            self.charlotte.y += 1
        elif self.charlotte_direction == Direction.LEFT:
            self.charlotte.x -= 1
        
    def check_input(self):
        if (pyxel.btn(pyxel.KEY_W)):
            self.charlotte_direction = Direction.UP
        elif (pyxel.btn(pyxel.KEY_D)):
            self.charlotte_direction = Direction.RIGHT
        elif (pyxel.btn(pyxel.KEY_S)):
            self.charlotte_direction = Direction.DOWN
        elif (pyxel.btn(pyxel.KEY_A)):
            self.charlotte_direction = Direction.LEFT
        elif (pyxel.btn(pyxel.KEY_ENTER)):
            self.charlotte_direction = Direction.ENTER
        else :
            self.charlotte_direction = Direction.IDLE
    
    def check_colisions(self):
        self.charlotte_land = True
        if (self.interract == Interact.ENDING):
            if (pyxel.btnp(pyxel.KEY_G)) :
                self.c_main_story += 1
                if(self.c_main_story == 26):
                    self.interract = Interact.NULL
        if (self.water.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
            self.charlotte_land = False
        if (self.chest.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
            if (pyxel.btnp(pyxel.KEY_G)) and not self.chest.found:
                self.chest.found = True
        if (self.c_main_story < 7):
            self.interract = Interact.MAIN
        elif (self.open_chest and self.c_main_story < 10):
            self.interract = Interact.MAIN
        if self.interract == Interact.MAIN:
            if (pyxel.btnp(pyxel.KEY_G)) :
                self.c_main_story += 1
                if self.c_main_story == 8 and not self.open_chest :
                    self.interract = Interact.NULL
                if self.c_main_story == 10 :
                    self.interract = Interact.NULL
                    self.open_chest = False
                    pyxel.mouse(False)
        elif self.chest.found :
            if (self.chest.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) and self.chest.found and not self.open_chest and not self.ending:
                    self.open_chest = True
                    pyxel.mouse(True)
                elif (pyxel.btnp(pyxel.KEY_G)) and self.chest.found and self.open_chest:
                    self.open_chest = False
                    pyxel.mouse(False)
            elif (self.mah.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if ((pyxel.btnp(pyxel.KEY_G)) and not (self.quest_mah)) or ((pyxel.btnp(pyxel.KEY_G)) and (self.ending) and self.c_mah < 12):
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.interract = Interact.MAH
                    self.c_mah += 1
            elif self.interract == Interact.MAH:
                if (pyxel.btnp(pyxel.KEY_G)):
                    if(self.c_mah == 3) and self.hud.love_count < 5:
                        pass
                    else:
                        self.c_mah += 1
                    if(self.c_mah == 7) or (self.c_mah == 12):
                        self.quest_mah = True
                        self.interract = Interact.NULL
                        self.mah.x = self.start_x_mah
                        self.mah.y = self.start_y_mah
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
            elif (self.pTinTin.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.quest_ptintin) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_pTinTin < 11):
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.interract = Interact.PTINTIN
                    self.c_pTinTin += 1
            elif self.interract == Interact.PTINTIN:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if((self.c_pTinTin == 4) and self.hud.is_ขยร้ is None) or ((self.c_pTinTin == 5) and not self.hud.is_ขยร้):
                        pass
                    elif self.c_pTinTin < 6 and (self.hud.is_ขยร้):
                        self.c_pTinTin = 7
                    else :
                        self.c_pTinTin += 1
                    if(self.c_pTinTin == 9) or (self.c_pTinTin == 11):
                        self.quest_ptintin = True
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.pTinTin.x = self.start_x_pTinTin
                        self.pTinTin.y = self.start_y_pTinTin
            elif (self.pMaw.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.quest_pmaw or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_pMaw < 7)) :
                    if self.c_pMaw == 3 and self.c_fish == 0:
                        pass
                    else :
                        self.start_x_charlotte = self.charlotte.x
                        self.start_y_charlotte = self.charlotte.y
                        self.interract = Interact.PMAW
                        self.c_pMaw += 1
            elif self.interract == Interact.PMAW:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if self.c_pMaw == 3 and self.c_fish == 0:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.pMaw.x = self.start_x_pMaw
                        self.pMaw.y = self.start_y_pMaw
                    elif self.c_pMaw == 6 or self.c_pMaw == 7:
                        self.interract = Interact.NULL
                        self.quest_pmaw = True
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.pMaw.x = self.start_x_pMaw
                        self.pMaw.y = self.start_y_pMaw
                    else :
                        self.c_pMaw += 1
            elif (self.plaNil.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) and not (self.quest_planil) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_plaNil < 9):
                    if (self.c_plaNil == 3 and self.c_flower < 10) :
                        pass
                    else :
                        self.c_plaNil += 1
                        self.interract = Interact.PLANIL
                        self.start_x_charlotte = self.charlotte.x
                        self.start_y_charlotte = self.charlotte.y
            elif (self.interract == Interact.PLANIL):
                if (pyxel.btnp(pyxel.KEY_G)):
                    if (self.c_plaNil == 3 and self.c_flower < 10) :
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.plaNil.x = self.start_x_plaNil
                        self.plaNil.y = self.start_y_plaNil
                    elif (self.c_plaNil == 6) or self.c_plaNil == 9:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.plaNil.x = self.start_x_plaNil
                        self.plaNil.y = self.start_y_plaNil
                        self.quest_planil = True
                    else:
                        self.c_plaNil += 1
            elif (self.fish.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.c_fish += 1
                    self.new_fish = False
            elif (self.flower_1.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_1)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_1 = True
                    self.c_flower += 1
            elif (self.flower_2.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_2)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_2 = True
                    self.c_flower += 1
            elif (self.flower_3.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_3)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_3 = True
                    self.c_flower += 1
            elif (self.flower_4.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_4)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_4 = True
                    self.c_flower += 1
            elif (self.flower_5.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_5)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_5 = True
                    self.c_flower += 1
            elif (self.flower_6.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_6)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_6 = True
                    self.c_flower += 1   
            elif (self.flower_7.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_7)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_7 = True
                    self.c_flower += 1   
            elif (self.flower_8.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_8)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_8 = True
                    self.c_flower += 1
            elif (self.flower_9.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_9)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_9 = True
                    self.c_flower += 1 
            elif (self.flower_10.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_flower_10)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_flower_10 = True
                    self.c_flower += 1 
            elif (self.tree.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.somsom_drop):
                    self.somsom_drop = True
            elif (self.somsom.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and self.somsom_drop and not self.quest_somsom) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_somsom < 10):
                    self.c_somsom += 1
                    self.interract = Interact.SOMSOM
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
            elif (self.interract == Interact.SOMSOM):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if((self.c_somsom == 5) and self.hud.is_หูกระจง is None) or ((self.c_somsom == 6) and not self.hud.is_หูกระจง):
                        pass
                    elif self.c_somsom < 7 and (self.hud.is_หูกระจง):
                        self.c_somsom = 8
                    else :
                        self.c_somsom += 1
                    if(self.c_somsom == 9) or self.c_somsom == 11:
                        self.quest_somsom = True
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.somsom.x = self.start_x_somsom
                        self.somsom.y = self.start_y_somsom
            elif (self.mangu.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.quest_mangu) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_mangu < 7) :
                    if self.c_mangu == 3 and self.c_herb < self.rand_herb:
                        pass
                    else :
                        self.start_x_charlotte = self.charlotte.x
                        self.start_y_charlotte = self.charlotte.y
                        self.interract = Interact.MANGU
                        self.c_mangu += 1
            elif self.interract == Interact.MANGU:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if self.c_mangu == 3 and self.c_herb < self.rand_herb:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.mangu.x = self.start_x_mangu
                        self.mangu.y = self.start_y_mangu
                    elif((self.c_mangu == 5) and self.hud.grill_tail is None) :
                        pass
                    elif self.c_mangu == 5 and self.hud.is_spicy_tail is None :
                        if not self.hud.grill_tail :
                            self.interract = Interact.NULL
                            self.quest_mangu = True
                            self.charlotte.x = self.start_x_charlotte
                            self.charlotte.y = self.start_y_charlotte
                            self.mangu.x = self.start_x_mangu
                            self.mangu.y = self.start_y_mangu
                        else :
                            pass
                    elif (self.c_mangu == 5 and not self.hud.grill_tail) or self.c_mangu == 7:
                        self.interract = Interact.NULL
                        self.quest_mangu = True
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.mangu.x = self.start_x_mangu
                        self.mangu.y = self.start_y_mangu
                    else :
                        self.c_mangu += 1
                elif (self.c_mangu == 5 and self.hud.is_spicy_tail is not None) or self.c_mangu == 7 :
                        self.interract = Interact.NULL
                        self.quest_mangu = True
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.mangu.x = self.start_x_mangu
                        self.mangu.y = self.start_y_mangu
            elif (self.herb_1.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_herb_1)):
                if (pyxel.btnp(pyxel.KEY_G) and self.c_herb < 5) :
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.pick_herb_1 = True
                    self.c_herb += 1
                    self.interract = Interact.HERB
            elif (self.herb_2.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_herb_2)):
                if (pyxel.btnp(pyxel.KEY_G) and self.c_herb < 5) :
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.pick_herb_2 = True
                    self.c_herb += 1
                    self.interract = Interact.HERB
            elif (self.herb_3.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_herb_3)):
                if (pyxel.btnp(pyxel.KEY_G) and self.c_herb < 5) :
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.pick_herb_3 = True
                    self.c_herb += 1
                    self.interract = Interact.HERB
            elif (self.herb_4.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_herb_4)):
                if (pyxel.btnp(pyxel.KEY_G) and self.c_herb < 5) :
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.pick_herb_4 = True
                    self.c_herb += 1
                    self.interract = Interact.HERB
            elif (self.herb_5.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_herb_5)):
                if (pyxel.btnp(pyxel.KEY_G) and self.c_herb < 5) :
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.pick_herb_5 = True
                    self.c_herb += 1
                    self.interract = Interact.HERB
            elif self.interract == Interact.HERB:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.interract = Interact.NULL
                    self.charlotte.x = self.start_x_charlotte
                    self.charlotte.y = self.start_y_charlotte
            elif (self.carrot_1.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_1)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_1 = True
                    if (1 in self.gloden_carrot):
                        self.c_gloden_carrot += 1
            elif (self.carrot_2.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_2)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_2 = True
                    if (2 in self.gloden_carrot):
                        self.c_gloden_carrot += 1
            elif (self.carrot_3.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_3)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_3 = True
                    if (3 in self.gloden_carrot):
                        self.c_gloden_carrot += 1
            elif (self.carrot_4.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_4)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_4 = True
                    if (4 in self.gloden_carrot):
                        self.c_gloden_carrot += 1
            elif (self.carrot_5.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_5)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_5 = True
                    if (5 in self.gloden_carrot):
                        self.c_gloden_carrot += 1
            elif (self.carrot_6.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_6)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_6 = True
                    if (6 in self.gloden_carrot):
                        self.c_gloden_carrot += 1   
            elif (self.carrot_7.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_7)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_7 = True
                    if (7 in self.gloden_carrot):
                        self.c_gloden_carrot += 1   
            elif (self.carrot_8.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_8)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_8 = True
                    if (8 in self.gloden_carrot):
                        self.c_gloden_carrot += 1 
            elif (self.carrot_9.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_9)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_9 = True
                    if (9 in self.gloden_carrot):
                        self.c_gloden_carrot += 1   
            elif (self.carrot_10.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h) and not (self.pick_carrot_10)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.pick_carrot_10 = True
                    if (10 in self.gloden_carrot):
                        self.c_gloden_carrot += 1  
            elif (self.nongtan.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if ((pyxel.btnp(pyxel.KEY_G) and not self.quest_nongtan) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_nongtan < 7)) :
                    if self.c_nongtan == 3 and self.c_gloden_carrot < 4:
                        pass
                    else :
                        self.start_x_charlotte = self.charlotte.x
                        self.start_y_charlotte = self.charlotte.y
                        self.interract = Interact.NONGTAN
                        self.c_nongtan += 1
            elif self.interract == Interact.NONGTAN:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if self.c_nongtan == 3 and self.c_gloden_carrot < 4:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongtan.x = self.start_x_nongtan
                        self.nongtan.y = self.start_y_nongtan
                    elif self.c_nongtan == 6 or self.c_nongtan == 7:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongtan.x = self.start_x_nongtan
                        self.nongtan.y = self.start_y_nongtan
                        self.quest_nongtan = True
                    else :
                        self.c_nongtan += 1
            elif (self.nongarw.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.quest_nongarw) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_nongarw < 7):
                    if self.c_nongarw == 3 and not self.found_GPU:
                        pass
                    else :
                        self.start_x_charlotte = self.charlotte.x
                        self.start_y_charlotte = self.charlotte.y
                        self.interract = Interact.NONGARW
                        self.c_nongarw += 1
            elif self.interract == Interact.NONGARW:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if self.c_nongarw == 3 and not self.found_GPU:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongarw.x = self.start_x_nongarw
                        self.nongarw.y = self.start_y_nongarw
                    elif self.c_nongarw == 6 or self.c_nongarw == 7:
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongarw.x = self.start_x_nongarw
                        self.nongarw.y = self.start_y_nongarw
                        self.quest_nongarw = True
                    else :
                        self.c_nongarw += 1
            elif (self.gpu.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.found_GPU = True
            elif (self.pErin.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.quest_pErin) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_pErin < 9):
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.interract = Interact.PERIN
                    self.c_pErin += 1
            elif self.interract == Interact.PERIN:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if(self.c_pErin == 3):
                        self.interract = Interact.PERIN_GAME
                    else :
                        self.c_pErin += 1
                    if(self.c_pErin == 7 or self.c_pErin == 10):
                        self.quest_pErin = True
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.pErin.x = self.start_x_pErin
                        self.pErin.y = self.start_y_pErin
            elif (self.nongPat.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G) and not self.quest_nongPat) or (pyxel.btnp(pyxel.KEY_G) and (self.ending) and self.c_nongPat < 8):
                    if (self.c_nongPat == 3 and not self.found_bottle) :
                        pass
                    else :
                        self.start_x_charlotte = self.charlotte.x
                        self.start_y_charlotte = self.charlotte.y
                        self.interract = Interact.NONGPAT
                        self.c_nongPat += 1
            elif self.interract == Interact.NONGPAT:
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if(self.c_nongPat == 3 ) :
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongPat.x = self.start_x_nongPat
                        self.nongPat.y = self.start_y_nongPat
                    else :
                        self.c_nongPat += 1
                    if(self.c_nongPat == 7 or self.c_nongPat == 9):
                        self.quest_nongPat = True
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongPat.x = self.start_x_nongPat
                        self.nongPat.y = self.start_y_nongPat
            elif (self.bottle.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.found_bottle = True
            elif (self.interract == Interact.PERIN_GAME) :
                pyxel.mouse(True)
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if (8 <= pyxel.mouse_x <= 64) and (8 <= pyxel.mouse_y <= 64): 
                        pyxel.play(0,0)
                        self.sound_answer.append(0)
                    elif (104 <= pyxel.mouse_x <= 168) and (8 <= pyxel.mouse_y <= 64): 
                        pyxel.play(0,1)
                        self.sound_answer.append(1)
                    elif (8 <= pyxel.mouse_x <= 64) and (80 <= pyxel.mouse_y <= 144): 
                        pyxel.play(0,2)
                        self.sound_answer.append(2)
                    elif (104 <= pyxel.mouse_x <= 168) and (80 <= pyxel.mouse_y <= 144): 
                        pyxel.play(0,3)
                        self.sound_answer.append(3)
                    elif (80 <= pyxel.mouse_x <= 104) and (72 <= pyxel.mouse_y <= 88): 
                        print ("play")
                        self.play_sound = True
                    if len(self.sound_answer) > 5:
                        self.sound_answer.pop(0)
                    print (self.sound_answer)
                    if self.sound_answer == self.sound_quest :
                        pyxel.mouse(False)
                        self.interract = Interact.PERIN
                        self.c_pErin += 1
            elif (self.cake.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) :
                    self.blow = True
            elif (self.nongyeen.intersects(self.charlotte.x, self.charlotte.y, self.charlotte.w, self.charlotte.h)):
                if (pyxel.btnp(pyxel.KEY_G)) and self.ending and self.c_nongyeen < 1:
                    self.start_x_charlotte = self.charlotte.x
                    self.start_y_charlotte = self.charlotte.y
                    self.interract = Interact.NONGYEEN
                    self.c_nongyeen += 1
            elif (self.interract == Interact.NONGYEEN) :
                if (pyxel.btnp(pyxel.KEY_G)) :
                    if(self.c_nongyeen == 1 ):
                        self.interract = Interact.NULL
                        self.charlotte.x = self.start_x_charlotte
                        self.charlotte.y = self.start_y_charlotte
                        self.nongyeen.x = self.start_x_nongyeen
                        self.nongyeen.y = self.start_y_nongyeen
                    else: 
                        self.c_nongyeen += 1
            elif (self.blow and self.c_main_story == 17 and self.c_mah == 12 and self.c_pTinTin == 11 and self.c_pMaw == 7 and self.c_plaNil == 9 and self.c_somsom == 11 and self.c_mangu == 7 and self.c_nongtan == 7 and self.c_nongarw == 7 and self.c_pErin == 10 and self.c_nongPat == 9 and self.c_nongyeen == 1):
                self.interract = Interact.ENDING
                self.c_main_story += 1

            
App()