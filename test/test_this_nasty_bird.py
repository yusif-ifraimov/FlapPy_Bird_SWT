from unittest import TestCase
import unittest

from src import Bird
from src import MainGame
from src import LoadGame


def isin(pos, rect):
    if pos[0] > rect[0] and pos[0] < rect[0]+rect[2]:
        if pos[1] > rect[1] and pos[1] < rect[1] + rect[3]: return True
        else:
            return False
    else:
        return False

LoadGame = []


class LoadGame:
    def __init__(self, color, rect):
        self.rect = rect
        self.color = color


pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, 0, 32)

load1 = LoadGame((255, 0, 0), [10, 10, 20, 20])
load2 = LoadGame((0, 255, 0), [20, 20, 20, 20])
load3 = LoadGame((0, 0, 255), [30, 30, 20, 20])

tracking = False
posgolb = 0
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if mousepress[0] != 0:
                    pos = pygame.mouse.get_pos()
                    for load in LoadGame:
                        if isin(pos, load.rect):
                            posglob = pos; loadglob = load
                            tracking = True
            if event.type == pygame.MOUSEBUTTONUP:
                posglob = 0; tracking = False; loadglob = 0

        if tracking:
            pos = pygame.mouse.get_pos()
            f = loadglob.rect
            f[0] = pos[0] - 10
            f[1] = pos[1] - 10
            loadglob.rect = f
        pygame.draw.rect(screen, (0,0,0),[0,0,640,480])
        for load in LoadGame:
            pygame.draw.rect(screen, load.color, load.rect)
        pygame.display.flip()
        pygame.display.update()
        
class TestGeneric(TestCase):
    def test_list_behaviour(self):
        my_list = []
        [[my_list.append((j, i)) for i in range(20)] for j in range(20)]
        my_body = [(i, 3) for i in range(10)]

        list_size = len(my_list)
        body_size = len(my_body)

        for segment in my_body:
            if segment in my_list:
                my_list.remove(segment)

        assert len(my_list) == list_size - body_size


class TestBird(TestCase):
    def test_init(self):
        b = Bird()
        assert b.get_position() == (MainGame.size[0] / 2, MainGame.size[1] / 2)

    def test_get_speed_and_turn(self):
        b = Bird()
        assert b.get_speed() == (-1, 0)

        b.turn('lt')
        assert b.get_speed() == (0, -1)  # lt

        b.turn('lt')
        b.turn('rt')
        assert b.get_speed() == (0, -1)

        b.turn('dn')
        assert b.get_speed() == (1, 0)

        b.turn('up')
        assert b.get_speed() == (1, 0)

        b.turn('rt')
        assert b.get_speed() == (0, 1)

        b.turn('up')
        assert b.get_speed() == (-1, 0)

        b.turn('up')
        assert b.get_speed() == (-1, 0)

        b.turn('lt')
        assert b.get_speed() == (0, -1)

    def test_move(self):
        b = Bird()

        x_shift = MainGame.size[1] // 2

        def move_n_cells(n, dest_x, dest_y):
            [b.move() for _ in range(1, n)]

            assert b.get_position() == (dest_y, dest_x)

        n = 100

        b.turn('up')
        move_n_cells(n, x_shift, 0)

    def test_get_body(self):
        b = Bird()

        x_shift = MainGame.size[1] // 2
        y_shift = MainGame.size[0] // 2

        def move_bird_up(n, dest_x, dest_y, direction=(-1, 0), print_flag=False):
            for i in range(1, n+1):
                b.move()
                # print_body(s)

            assert b.get_position() == (dest_y + y_shift, dest_x + x_shift)

            i = 0
            j = 0
            for segment in b.get_body():
                if print_flag:
                    print(segment.pos, "i: ", i, "j: ", j)
                assert segment.pos == (dest_y - i + y_shift, dest_x - j + y_shift)
                i += direction[0]
                j += direction[1]



    def test_self_collision(self):
        b = Bird(length=10)

        x_shift = Playground.size[1] // 2
        y_shift = Playground.size[0] // 2

        def n_moves_to(di, n):
            b.turn(di)
            for _ in range(n):
                if b.move() == Bird.self_collision:
                    assert b.get_position() == (2 + y_shift, 1 + x_shift)

        n_moves_to('rt', 2)
        n_moves_to('dn', 2)
        n_moves_to('lt', 5)

    def test_wall_collision(self):
        b = Bird()

        x_shift = MainGame.size[1] // 2

        def n_moves_to(di, n):
            b.turn(di)
            for _ in range(n):
                if b.move() == Bird.wall_collision:
                    assert b.get_position() == (0, x_shift)

        n_moves_to('up', 100)

    @unittest.skip("Requires manual driving")
    def test_bird_main(self):
        b = Bird()

        def show_bird():
            print("----- Bird -----")
            for segment in b.get_body():
                print(segment.get_pos())
            print("===== Bird =====")
            print("----- Hit -----")
            print(b.__hit.get_pos())

        while(b.cli()):
            b.move()
            display_bird()


class TestPlayground(TestCase):
    def test_init(self):
        p = MainGame()
        assert (-1, 0) in p.borders
        assert (-1, 19) in p.borders

        assert (20, 0) in p.borders
        assert (20, 19) in p.borders

        assert (0, -1) in p.borders
        assert (19, -1) in p.borders

        assert (0, 20) in p.borders
        assert (19, 20) in p.borders


class TestSound(TestCase):
    def test_change_sound(self):
        s = Sound()


        sound_file = s.get_pos()

        assert sound_file[0] < MainGame.size[0]
        assert sound_file[1] < MainGame.size[1]
        assert sound_file[0] >= 0
        assert sound_file[1] >= 0

    def test_sprites_loading(self):
        s = Sprites()
        p = MainGame()

        point1 = (1, 1)
        index1 = s.get_index(p, point1)
        assert index1 == (p.rows + 2) - 1
        assert MainGame.convert_index(s, index1) == point1

