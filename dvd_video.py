import pygame, os

WIDTH:int = 1280
HEIGHT:int = 720

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    deltaTime = 0

    dvd_logos:list = []

    dir_path:str = "assets"
    for i in os.listdir(dir_path):
        dvd_logos.append(pygame.image.load(f"./assets/{i}"))

    current_logo = dvd_logos[0]

    dvd_rect = current_logo.get_rect()
    dvd_speed = [5, 5]

    def change_logo(l):
        logo = l
        curr = dvd_logos.index(logo)
        print(curr, logo)

        if curr + 2 > len(dvd_logos):
            logo = dvd_logos[0]
        else:
            logo = dvd_logos[curr + 1]

        return logo


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        if dvd_rect.left < 0 or dvd_rect.right > WIDTH:
            dvd_speed[0] = -dvd_speed[0]
            current_logo = change_logo(current_logo)

        if dvd_rect.top < 0 or dvd_rect.bottom > HEIGHT:
            dvd_speed[1] = -dvd_speed[1]
            current_logo = change_logo(current_logo)

        screen.blit(current_logo, dvd_rect)

        dvd_rect = dvd_rect.move(dvd_speed)

        pygame.display.flip()

        deltaTime = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()