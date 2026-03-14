import pygame
from robot_core import Robot, execute_command

pygame.init()

# 地圖大小
GRID_W = 5
GRID_H = 3
CELL_SIZE = 100

HUD_HEIGHT = 170
SCREEN_WIDTH = (GRID_W + 1) * CELL_SIZE
SCREEN_HEIGHT = (GRID_H + 1) * CELL_SIZE + HUD_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Robot Lost")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Microsoft JhengHei", 28)
small_font = pygame.font.SysFont("Microsoft JhengHei", 24)

robot = Robot(0, 0, 'N')
scents = set()

# 額外狀態資訊
robot_count = 1
latest_event = "就緒"
history = []


def record_frame():
    """紀錄目前畫面狀態，之後可作為 replay 基礎"""
    history.append({
        "robot_index": robot_count,
        "x": robot.x,
        "y": robot.y,
        "direction": robot.direction,
        "lost": robot.lost,
        "scent_count": len(scents),
        "event": latest_event,
    })


def grid_to_screen(x, y):
    screen_x = x * CELL_SIZE + CELL_SIZE // 2
    screen_y = (GRID_H - y) * CELL_SIZE + CELL_SIZE // 2
    return screen_x, screen_y


def draw_grid():
    for x in range(GRID_W + 1):
        for y in range(GRID_H + 1):
            rect = pygame.Rect(
                x * CELL_SIZE,
                (GRID_H - y) * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, (180, 180, 180), rect, 1)


def draw_robot():
    px, py = grid_to_screen(robot.x, robot.y)

    pygame.draw.circle(screen, (0, 120, 255), (px, py), 25)

    if robot.direction == 'N':
        tip = (px, py - 30)
    elif robot.direction == 'S':
        tip = (px, py + 30)
    elif robot.direction == 'E':
        tip = (px + 30, py)
    else:
        tip = (px - 30, py)

    pygame.draw.line(screen, (255, 255, 255), (px, py), tip, 5)


def draw_scents():
    for sx, sy, _ in scents:
        px, py = grid_to_screen(sx, sy)
        pygame.draw.circle(screen, (255, 100, 100), (px, py), 10)


def draw_hud():
    hud_rect = pygame.Rect(0, SCREEN_HEIGHT - HUD_HEIGHT, SCREEN_WIDTH, HUD_HEIGHT)
    pygame.draw.rect(screen, (35, 45, 55), hud_rect)

    status_text = "存活"
    if robot.lost:
        status_text = "LOST"

    line1 = f"機器人 #{robot_count}：({robot.x}, {robot.y}) {robot.direction} {status_text}"
    line2 = f"最新事件：{latest_event}"
    line3 = f"Scent 數量：{len(scents)}"
    line4 = f"回放影格數：{len(history)}"
    line5 = "L/R/F 操作  N 新機器人  C 清除  ESC 離開"

    surface1 = font.render(line1, True, (255, 255, 255))
    surface2 = small_font.render(line2, True, (255, 255, 255))
    surface3 = small_font.render(line3, True, (255, 255, 255))
    surface4 = small_font.render(line4, True, (255, 255, 255))
    surface5 = small_font.render(line5, True, (255, 255, 0))

    screen.blit(surface1, (20, SCREEN_HEIGHT - HUD_HEIGHT + 10))
    screen.blit(surface2, (20, SCREEN_HEIGHT - HUD_HEIGHT + 48))
    screen.blit(surface3, (20, SCREEN_HEIGHT - HUD_HEIGHT + 82))
    screen.blit(surface4, (20, SCREEN_HEIGHT - HUD_HEIGHT + 112))
    screen.blit(surface5, (20, SCREEN_HEIGHT - HUD_HEIGHT + 140))


record_frame()

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                latest_event = "離開遊戲"
                running = False

            elif event.key == pygame.K_l:
                old_dir = robot.direction
                execute_command(robot, 'L', GRID_W, GRID_H, scents)
                latest_event = f"左轉：{old_dir} -> {robot.direction}"
                record_frame()

            elif event.key == pygame.K_r:
                old_dir = robot.direction
                execute_command(robot, 'R', GRID_W, GRID_H, scents)
                latest_event = f"右轉：{old_dir} -> {robot.direction}"
                record_frame()

            elif event.key == pygame.K_f:
                before_x, before_y, before_dir = robot.x, robot.y, robot.direction
                before_lost = robot.lost
                before_scent_count = len(scents)

                execute_command(robot, 'F', GRID_W, GRID_H, scents)

                if robot.lost and not before_lost:
                    latest_event = f"機器人掉出地圖，於 ({before_x}, {before_y}) {before_dir} 留下 scent"
                elif len(scents) > before_scent_count and (robot.x, robot.y) == (before_x, before_y):
                    latest_event = f"危險前進，已 LOST"
                elif (robot.x, robot.y) == (before_x, before_y) and not robot.lost:
                    latest_event = "偵測到 scent，忽略這次危險前進"
                else:
                    latest_event = f"前進到 ({robot.x}, {robot.y})"

                record_frame()

            elif event.key == pygame.K_n:
                robot = Robot(0, 0, 'N')
                robot_count += 1
                latest_event = f"建立新機器人 #{robot_count}"
                record_frame()

            elif event.key == pygame.K_c:
                scents.clear()
                latest_event = "已清除所有 scent"
                record_frame()

    draw_grid()
    draw_scents()
    draw_robot()
    draw_hud()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()