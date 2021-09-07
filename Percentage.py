import pygame
import time
from pygame.constants import K_KP_ENTER, K_RETURN, MOUSEBUTTONDOWN

#Game colors
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
RED = (255, 0, 0)
DARK_WHITE = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (150, 150, 150)

#Window setup
WIDTH, HEIGHT = 700, 500
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("App%")
bg_image = pygame.image.load(r"C:\Users\gmegremis\Desktop\Giorgos\Python\VScode\Percentage\Assets\Math.jpg")

#Icon setup
icon = pygame.image.load(r"C:\Users\gmegremis\Desktop\Giorgos\Python\VScode\Percentage\Assets\icon.ico")
pygame.display.set_icon(icon)


def draw_window():
    wn.blit(bg_image, (0, 0))
    
    rect1 = pygame.Rect(240, 45, 210, 40)
    rect2 = pygame.Rect(100, 150, 200, 100)
    rect3 = pygame.Rect(400, 150, 200, 100)
    rect4 = pygame.Rect(250, 350, 200, 100)

    pygame.draw.rect(wn, DARK_WHITE, rect1)
    pygame.draw.rect(wn, DARK_WHITE, (90, 140, 220, 120))
    pygame.draw.rect(wn, RED, rect2)  
    pygame.draw.rect(wn, DARK_WHITE, (390, 140, 220, 120))   
    pygame.draw.rect(wn, RED, rect3)  
    pygame.draw.rect(wn, DARK_WHITE, (240, 340, 220, 120)) 
    pygame.draw.rect(wn, RED, rect4)    

    #Initializing font
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 35)

    #Headline
    headln = font.render("Μάθε ποσοστά!", 1, RED)
    wn.blit(headln, (250, 50))

    #First box
    text1a = font.render("Πόσο % του ... ", 1, BLACK)
    text1b = font.render("είναι το ...", 1, BLACK)

    wn.blit(text1a, (110, 170))
    wn.blit(text1b, (110, 200))

    #Second box
    text2a = font.render("Ποιανού το ...% ", 1, BLACK)
    text2b = font.render("είναι το ...", 1, BLACK)

    wn.blit(text2a, (410, 170))
    wn.blit(text2b, (410, 200))

    #Third box
    text3a = font.render("Ποιο είναι το ", 1, BLACK)
    text3b = font.render("...% του ...", 1, BLACK)

    wn.blit(text3a, (275, 370))
    wn.blit(text3b, (275, 400))

    font2 = pygame.font.SysFont("comicsans", 20)
    credit_text = font2.render("by Giorgos Megremis", 1, GREEN)
    wn.blit(credit_text, (550, 480))       

def case1():
    wn.blit(bg_image, (0, 0)) 
    print("Case1")
    pygame.font.init()
    pygame.draw.rect(wn, DARK_WHITE, (50, 50, 380, 35))
    font = pygame.font.SysFont("comicsans", 35)
    formula = font.render("Η φόρμουλα είναι: α/β = x/100", 1, RED)
    wn.blit(formula, (50, 50))

    #A input
    pygame.draw.rect(wn, BLACK, (50, 220, 160, 40))
    text1 = font.render("Δώσε το α: ", 1, WHITE)
    wn.blit(text1, (60, 225))

    pygame.draw.rect(wn, RED, (50, 270, 200, 50))
    rect1 = pygame.Rect(55, 275, 190, 40)
    pygame.draw.rect(wn, WHITE, rect1)

    #B input
    pygame.draw.rect(wn, BLACK, (50, 370, 160, 40))
    text2 = font.render("Δώσε το β: ", 1, WHITE)
    wn.blit(text2, (60, 375))

    pygame.draw.rect(wn, RED, (50, 420, 200, 50))
    rect2 = pygame.Rect(55, 425, 190, 40)
    pygame.draw.rect(wn, WHITE, rect2)

def case2():
    wn.blit(bg_image, (0, 0)) 
    print("Case2")
    pygame.font.init()
    pygame.draw.rect(wn, DARK_WHITE, (50, 50, 380, 35))
    font = pygame.font.SysFont("comicsans", 35)
    formula = font.render("Η φόρμουλα είναι: α/x = β/100", 1, RED)
    wn.blit(formula, (50, 50))

    #A input
    pygame.draw.rect(wn, BLACK, (50, 220, 160, 40))
    text1 = font.render("Δώσε το α: ", 1, WHITE)
    wn.blit(text1, (60, 225))

    pygame.draw.rect(wn, RED, (50, 270, 200, 50))
    rect1 = pygame.Rect(55, 275, 190, 40)
    pygame.draw.rect(wn, WHITE, rect1)

    #B input
    pygame.draw.rect(wn, BLACK, (50, 370, 160, 40))
    text2 = font.render("Δώσε το β: ", 1, WHITE)
    wn.blit(text2, (60, 375))

    pygame.draw.rect(wn, RED, (50, 420, 200, 50))
    rect2 = pygame.Rect(55, 425, 190, 40)
    pygame.draw.rect(wn, WHITE, rect2)

def case3():
    wn.blit(bg_image, (0, 0)) 
    print("Case3")
    pygame.font.init()
    pygame.draw.rect(wn, DARK_WHITE, (50, 50, 380, 35))
    font = pygame.font.SysFont("comicsans", 35)
    formula = font.render("Η φόρμουλα είναι: x/α = β/100", 1, RED)
    wn.blit(formula, (50, 50))

    #A input
    pygame.draw.rect(wn, BLACK, (50, 220, 160, 40))
    text1 = font.render("Δώσε το α: ", 1, WHITE)
    wn.blit(text1, (60, 225))

    pygame.draw.rect(wn, RED, (50, 270, 200, 50))
    rect1 = pygame.Rect(55, 275, 190, 40)
    pygame.draw.rect(wn, WHITE, rect1)

    #B input
    pygame.draw.rect(wn, BLACK, (50, 370, 160, 40))
    text2 = font.render("Δώσε το β: ", 1, WHITE)
    wn.blit(text2, (60, 375))

    pygame.draw.rect(wn, RED, (50, 420, 200, 50))
    rect2 = pygame.Rect(55, 425, 190, 40)
    pygame.draw.rect(wn, WHITE, rect2)

def display_answer(a, b, case):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 30)

    if case == 1:
        try:
            answer = (a*100)/b
        except ZeroDivisionError:
            error = font.render("Το ποσό δε μπορεί να είναι 0.", 2, RED)
            wn.blit(error, (300, 300))

    elif case == 2:
        try:
            answer = (a*100)/b
        except ZeroDivisionError:
            error = font.render("Το ποσό δε μπορεί να είναι 0.", 2, RED)
            wn.blit(error, (300, 300))

    else:
        try:
            answer = (a*b)/100
        except ZeroDivisionError:
            error = font.render("Το ποσό δε μπορεί να είναι 0.", 2, RED)
            wn.blit(error, (300, 300))


    pygame.draw.rect(wn, BLACK, (52, 122, 400, 35))
    if case == 1:
        dis_an = font.render("Η απάντηση είναι " + str(answer) + "% !", 2, WHITE)
    else:
        dis_an = font.render("Η απάντηση είναι " + str(answer) + "!", 2, WHITE)
    wn.blit(dis_an, (55, 125))

def back_button():
    pygame.draw.rect(wn, DARK_WHITE, (615, 45, 70, 50))
    pygame.draw.rect(wn, RED, (620, 50, 60, 40))
    arrow = pygame.image.load(r"C:\Users\gmegremis\Desktop\Giorgos\Python\VScode\Percentage\Assets\arrow.png")
    arrow = pygame.transform.scale(arrow, (40, 40))
    wn.blit(arrow, (630, 50))

def main():
    
    flag = True
    redraw_win = True

    pygame.font.init()
    font = pygame.font.Font(None, 32)
    input_box1 = pygame.Rect(55, 275, 160, 40)
    input_box2 = pygame.Rect(55, 425, 200, 40)
    color_inactive = (255, 0, 0)
    color_active = (0, 0, 0)
    color = color_inactive
    active1 = False
    active2 = False
    text1 = ''
    text2 = ''

    clock = pygame.time.Clock()
    FPS = 60

    while flag:
        pygame.display.update()
        pygame.time.delay(FPS)
        clock.tick(10)  

        if redraw_win == True:
            draw_window()
        else:
            back_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if redraw_win == True:

                    mx, my = pygame.mouse.get_pos()

                    if mx > 100 and mx < 300 and my > 150 and my < 250:
                        time.sleep(0.6)
                        redraw_win = False
                        case1() 
                        c = 1

                    elif mx > 400 and mx < 600 and my > 150 and my < 250:
                        time.sleep(0.6)
                        redraw_win = False
                        case2()
                        c = 2

                    elif mx > 250 and mx < 450 and my > 350 and my < 450:
                        time.sleep(0.6)
                        redraw_win = False
                        case3()
                        c = 3
                else:
                    mx, my = pygame.mouse.get_pos()

                    if mx > 625 and mx < 675 and my > 55 and my < 85:
                        time.sleep(0.4)
                        text1 = ''
                        text2 = ''
                        redraw_win = True

                if input_box1.collidepoint(event.pos):
                    active1 = not active1 
                else:
                    active1 = False

                if input_box2.collidepoint(event.pos):
                    active2 = not active2
                else:
                    active2 = False

                color = color_active if active1 or active2 else color_inactive

            elif event.type == pygame.KEYDOWN:
                if active1:
                    #if event.key == pygame.K_RETURN:
                      #  text1 = ''
                    if event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode

                elif active2:
                    #if event.key == pygame.K_RETURN:
                     #   text2 = ''
                    if event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode

                if event.key == pygame.K_RETURN:
                    a = float(text1)
                    b = float(text2)
                    display_answer(a, b, c)
                    print(text1)
                    print(text2)

        txt_surface1 = font.render(text1, True, color)
        txt_surface2 = font.render(text2, True, color)
        wid = max(200, txt_surface1.get_width()+10)
        input_box1.w = wid
        input_box2.w = wid
        wn.blit(txt_surface1, (input_box1.x+5, input_box1.y+5))
        wn.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        
        if redraw_win == False:
            pygame.draw.rect(wn, color, input_box1, 2)
            pygame.draw.rect(wn, color, input_box2, 2)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()