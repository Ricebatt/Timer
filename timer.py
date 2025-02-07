import os
from pygame import mixer
from button import *
import sys

pygame.init()
screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("Timer")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


def main():
    mixer.music.load("alarm.mp3")

    clock = pygame.time.Clock()
    running = True

    timer = 0
    header = JustText("Timer", 200, 50, 200, 180, "Ink Free", 80)
    teaHeader = JustText("Tea", 200, 50, 200, 180, "Ink Free", 80)
    napHeader = JustText("Nap", 200, 50, 200, 180, "Ink Free", 80)
    workHeader = JustText("Work", 200, 50, 200, 180, "Ink Free", 80)
    customHeader = JustText("Enter Time:", 200, 50, 200, 180, "Ink Free", 80)

    timeText = JustText("", 100, 200, 400, 180, "Ink Free", 120)

    timeEntered = "000"

    teaImage = pygame.image.load(os.path.join("tea.png"))
    teaImage = pygame.transform.scale(teaImage, (150, 150))
    napImage = pygame.image.load(os.path.join("cat.png"))
    napImage = pygame.transform.scale(napImage, (150, 150))
    workImage = pygame.image.load(os.path.join("work.png"))
    workImage = pygame.transform.scale(workImage, (130, 130))

    returnImage = pygame.image.load(os.path.join("return.png"))
    returnImage = pygame.transform.scale(returnImage, (35, 35))

    teaButton = Button("", 66, 250, (60, 179, 113, 255), 200, 100)
    napButton = Button("", 333, 250, (60, 179, 113, 255), 200, 100)
    workButton = Button("", 66, 420, (60, 179, 113, 255), 200, 100)
    customButton = Button("Custom", 333, 420, (60, 179, 113, 255), 200, 100)

    returnButton = Button("", 0, 0, (60, 179, 113, 255), 50, 50)
    startButton = Button("Start", 200, 400, (60, 179, 113, 255), 200, 100)

    state = "menu"
    lastState = state

    workCycle = "working"

    dt = 0
    while running:
        timeText.text = f"{int(timer // 60)}:{int(timer % 60):02}"

        #pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and state == "customMenu":
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    timeEntered += "0"
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    timeEntered += "1"
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    timeEntered += "2"
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    timeEntered += "3"
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    timeEntered += "4"
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    timeEntered += "5"
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    timeEntered += "6"
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    timeEntered += "7"
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    timeEntered += "8"
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    timeEntered += "9"
                if event.key == pygame.K_BACKSPACE and len(timeEntered) > 3:
                    timeEntered = timeEntered[:-1]
                print(timeEntered)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if teaButton.click(pos) and state == "menu":
                    teaButton.setColor((119, 209, 159, 255))
                    teaButton.selected = True
                elif workButton.click(pos) and state == "menu":
                    workButton.setColor((119, 209, 159, 255))
                    workButton.selected = True
                elif napButton.click(pos) and state == "menu":
                    napButton.setColor((119, 209, 159, 255))
                    napButton.selected = True
                elif customButton.click(pos) and state == "menu":
                    customButton.setColor((119, 209, 159, 255))
                    customButton.selected = True
                elif startButton.click(pos):
                    startButton.setColor((119, 209, 159, 255))
                    customButton.selected = True
                elif returnButton.click(pos):
                    returnButton.setColor((119, 209, 159, 255))
                    returnButton.selected = True

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if teaButton.click(pos) and state == "menu":
                    state = "teaMenu"
                    timer = 150
                elif napButton.click(pos) and state == "menu":
                    state = "napMenu"
                    timer = 60 * 15
                elif workButton.click(pos) and state == "menu":
                    state = "workMenu"
                    workCycle = "working"
                    timer = 60 * 50
                elif customButton.click(pos) and state == "menu":
                    state = "customMenu"

                elif startButton.click(pos) and (state == "teaMenu" or state == "napMenu" or state == "workMenu" or state == "customMenu"):
                    lastState = state
                    state = "timer"
                    print(state)

                elif returnButton.click(pos) and (state == "teaMenu" or state == "napMenu" or state == "workMenu" or state == "customMenu"):
                    lastState = "menu"
                    state = "menu"

                elif returnButton.click(pos) and state == "timer":
                    state = lastState
                    if state == "teaMenu":
                        timer = 150
                    if state == "napMenu":
                        timer = 60*15
                    if state == "workMenu":
                        timer = 60*50
                    if state == "customMenu":
                        timer = 0

                elif returnButton.click(pos) and state == "finishedTimer":
                    state = "menu"
                    mixer.music.stop()

                teaButton.selected = False
                workButton.selected = False
                napButton.selected = False
                customButton.selected = False
                startButton.selected = False
                returnButton.selected = False
                teaButton.setColor((60, 179, 113, 255))
                napButton.setColor((60, 179, 113, 255))
                workButton.setColor((60, 179, 113, 255))
                customButton.setColor((60, 179, 113, 255))
                startButton.setColor((60, 179, 113, 255))
                returnButton.setColor((60, 179, 113, 255))




        screen.fill((124, 205, 124, 255))

        if state == "menu":
            header.draw(screen)
            teaButton.draw(screen)
            workButton.draw(screen)
            napButton.draw(screen)
            customButton.draw(screen)

            screen.blit(teaImage, (100,232))
            screen.blit(napImage, (380,245))
            screen.blit(workImage, (110,403))

        elif state == "teaMenu":
            teaHeader.draw(screen)
            startButton.draw(screen)
            returnButton.draw(screen)
            timeText.draw(screen)
            screen.blit(returnImage, (7,7))

        elif state == "napMenu":
            napHeader.draw(screen)
            startButton.draw(screen)
            returnButton.draw(screen)
            timeText.draw(screen)
            screen.blit(returnImage, (7, 7))

        elif state == "workMenu":
            if workCycle == "working":
                workHeader.setText("Work")
            else:
                workHeader.setText("Rest")
            workHeader.draw(screen)
            startButton.draw(screen)
            returnButton.draw(screen)
            timeText.draw(screen)
            screen.blit(returnImage, (7, 7))

        elif state == "customMenu":
            customHeader.draw(screen)
            startButton.draw(screen)
            returnButton.draw(screen)
            timer = int(timeEntered[len(timeEntered) - 2:]) + (int(timeEntered[0:len(timeEntered) - 2]) * 60)
            timeText.draw(screen)
            screen.blit(returnImage, (7, 7))

        elif state == "timer":
            if lastState == "teaMenu":
                teaHeader.draw(screen)
            elif lastState == "napMenu":
                napHeader.draw(screen)
            elif lastState == "workMenu":
                workHeader.draw(screen)
            elif lastState == "customMenu":
                header.draw(screen)

            returnButton.draw(screen)
            timeText.draw(screen)
            screen.blit(returnImage, (7, 7))
            timer -= dt
            if timer <= 0:
                #alarm
                if lastState != "workMenu":
                    timer = 0
                    state = "finishedTimer"
                else:
                    if workCycle == "working":
                        workCycle = "resting"
                        timer = 10*60
                    else:
                        workCycle = "working"
                        timer = 50*60
                mixer.music.play()

        elif state == "finishedTimer":
            returnButton.draw(screen)
            timeText.draw(screen)
            screen.blit(returnImage, (7, 7))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    pygame.quit()