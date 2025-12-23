# from math import fabs
# from turtle import end_fill
# from numpy import true_divide
import pygame
from guitry_functions import *

# 1. הפעלת המנוע של Pygame
pygame.init()

# 2. יצירת חלון בגודל 600 על 600 פיקסלים
screen = pygame.display.set_mode((450, 650))
pygame.display.set_caption("משחק איקס עיגול")
my_font = pygame.font.SysFont('Arial', 30)
end_font = pygame.font.SysFont('Arial',40)

running = True
board = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
turn = 1
sp1=0
sp2=0
game_over=False
font_heb = pygame.font.SysFont('Arial', 40) 

#כפתור כדי לשחק שוב
play_again_msg=end_font.render("click here to play again", True, (0, 0, 0)) 
play_again_button_rect = pygame.Rect(25, 580, 400, 60)
play_again_msg = font_heb.render('press here to play again', True, (0, 0, 0))
play_again_rect = play_again_msg.get_rect(center=play_again_button_rect.center)

#הודעות נוספות בראש המשחק (תור מי ומי ניצח וכו..)
status_font = pygame.font.SysFont('Arial', 40)
status_text = "X turn"
status_color = (0, 0, 0)
status_msg = status_font.render(status_text,True,status_color)
status_rect= status_msg.get_rect(center=(225,60))

#הוספת אפשרות לשחק מול מחשב 
vs_computer= False
pvp_button_rect=pygame.Rect(25, 300, 400, 40)
pvp_button_rect.center =(225,300)
pvp_msg = font_heb.render('play vs player', True, (0, 0, 0))
pvp_rect = pvp_msg.get_rect(center=pvp_button_rect.center)
pvc_button_rect=pygame.Rect(25, 360, 400, 40)
pvc_button_rect.center =(225,360)
pvc_msg = font_heb.render('play vs computer', True, (0, 0, 0))
pvc_rect = pvc_msg.get_rect(center=pvc_button_rect.center)
game_active= False



# 3. לולאת המשחק (Game Loop)
# הלולאה הזו רצה שוב ושוב ושומרת את החלון פתוח
while running:
    # בדיקה האם המשתמש עשה משהו (כמו ללחוץ על ה-X לסגירת החלון)
    if game_active and vs_computer and turn % 2 == 0 and not game_over:
        pygame.time.delay(500)
        smartAI(board, turn, sp1=0, sp2=0)
        turn+=1
        win, sp1, sp2,status_text,status_color = is_win_scores(board, turn, sp1, sp2,  status_text, status_color, apply_score=True)
        if win:
            game_over=True
            if "tie" not in status_text: 
                status_text = 'Computer Won!'
                status_color = (0, 0, 255)
        else:
            status_text = "X turn"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #מקבל את מיקום העכבר בזמן הלחיצה
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            col = pos[0] // 150
            row = (pos[1] - 100) // 150
            # החישוב של מיקום העכבר למפתח במילון
            if game_active:
                if not game_over:
                    key = str((row * 3) + col + 1)
                    if board[key] != "x" and board[key] != "o": # בודק שהמיקום על הלוח ריק
                        if turn % 2 == 0:
                            board[str(key)] = "o"
                            status_text= "X turn"
                        else:
                            board[str(key)] = "x"
                            status_text= "O turn"
                        turn+=1
                        win, sp1, sp2,status_text,status_color = is_win_scores(board, turn, sp1, sp2,  status_text, status_color, apply_score=True)
                        if win:
                            game_over=True
                else:
                    if play_again_button_rect.collidepoint(event.pos):
                        clear_board(board)
                        turn=1
                        status_color = (0, 0, 0)
                        status_text='X turn'
                        game_over=False

            else:
                if pvp_button_rect.collidepoint(event.pos):
                    vs_computer=False
                    game_active=True
                if pvc_button_rect.collidepoint(event.pos):
                    vs_computer=True
                    game_active=True



    # רענון המסך (חשוב מאוד כדי שנראה שינויים)
    screen.fill((255, 255, 255)) # צביעת המסך בלבן
    # ציור המשחק
    if game_active:
        status_msg = status_font.render(status_text,True,status_color)
        status_rect= status_msg.get_rect(center=(225,60))
        pygame.draw.line(screen, (0, 0, 0), (150, 100), (150, 550), 5)
        pygame.draw.line(screen, (0, 0, 0), (300, 100), (300, 550), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, 250), (450, 250), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, 400), (450, 400), 5)
        screen.blit(status_msg,status_rect)
        for row in range(0, 3):
            for col in range(0, 3):
                centerX = col * 150 + 75
                centerY = row * 150 + 175
                key = (row * 3) + col + 1
                if board[str(key)] == "x":
                    pygame.draw.line(screen, (0, 0, 0), (centerX - 40, centerY - 40), (centerX + 40, centerY + 40), 5)
                    pygame.draw.line(screen, (0, 0, 0), (centerX + 40, centerY - 40), (centerX - 40, centerY + 40), 5)
                elif board[str(key)] == "o":
                    pygame.draw.circle(screen, (0,0,0), (centerX, centerY), 50, 5)
        if game_over:
            end_msg = end_font.render("Game Over", True, (0, 0, 0))# מייצר משפט סיום משחק
            screen.blit(end_msg, (140, 550)) #מדפיס את המשפט
            screen.blit(play_again_msg, play_again_rect)
        
        score_msg = end_font.render(f"score: p1:{sp1} p2:{sp2}", True, (0, 0, 0))# מייצר משפט תוצאות
        screen.blit(score_msg, (100, 0)) 
    #ציור מסך הבית 
    else:
        pygame.draw.rect(screen, (200, 200, 200), pvp_button_rect) 
        screen.blit(pvp_msg, pvp_rect)
        pygame.draw.rect(screen, (200, 200, 200), pvc_button_rect) 
        screen.blit(pvc_msg, pvc_rect)
    pygame.display.flip()

# יציאה מסודרת כשיוצאים מהלולאה
pygame.quit()