# input must contain faces in this order: white, red, green, orange, blue, yellow
from CubeMover import CubeMover
import random
import numpy as np


class CubeSolver:

    def __init__(self, cube):
        self.mover = CubeMover(cube)
        self.cube = cube
        self.yellow_crossed = False
        self.yellow_vertexes = False
        self.solve_cube()

    def sexy_moves(self):
        self.mover.R()
        self.mover.U()
        self.mover.inv_R()
        self.mover.inv_U()

    def anti_sexy_moves(self):
        self.mover.U()
        self.mover.R()
        self.mover.inv_U()
        self.mover.inv_R()

    def adjust_white_edge(self, name):
        c = self.mover.cube_encoder.edges[name].coordinates
        cube = self.mover.cube
        kleur_vlak = name[1]

        if c == (1, 0, -1):
            if cube[2][1][0] == kleur_vlak:
                self.mover.F()
            else:
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
        elif c == (-1, 0, -1):
            if cube[4][1][2] == kleur_vlak:
                self.mover.inv_F()
            else:
                self.mover.inv_D()
                self.mover.L()
                self.mover.D()
        elif c == (0, 1, -1):
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()
        elif c == (1, 1, 0):
            self.mover.U()
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()
        elif c == (0, 1, 1):
            self.mover.U()
            self.mover.U()
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()
        elif c == (-1, 1, 0):
            self.mover.inv_U()
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (1, 0, 1):
            self.mover.B()
            self.mover.U()
            self.mover.U()
            self.mover.inv_B()
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (-1, 0, 1):
            self.mover.inv_B()
            self.mover.U()
            self.mover.U()
            self.mover.B()
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (0, -1, -1):
            if cube[1][2][1] == kleur_vlak:
                self.mover.inv_F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()

        elif c == (-1, -1, 0):
            self.mover.inv_L()
            if cube[4][1][2] == kleur_vlak:
                self.mover.inv_F()
            else:
                self.mover.inv_D()
                self.mover.L()
                self.mover.D()

        elif c == (0, -1, 1):
            self.mover.B()
            self.mover.B()
            self.mover.U()
            self.mover.U()
            if cube[1][0][1] == kleur_vlak:
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (1, -1, 0):
            self.mover.R()
            if cube[2][1][0] == kleur_vlak:
                self.mover.F()
            else:
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()

    def solve_white_cross(self):
        self.adjust_white_edge('WR')
        self.mover.inv_D()
        self.adjust_white_edge('RG')
        self.mover.inv_D()
        self.adjust_white_edge('RU')
        self.mover.inv_D()
        self.adjust_white_edge('GY')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'

    def solve_vertex_base_case(self, cube):
        if cube[5][2][2] == 'W':
            self.sexy_moves()
            self.sexy_moves()
            self.sexy_moves()
        elif cube[2][0][0] == 'W':
            self.sexy_moves()
        else:
            self.anti_sexy_moves()

    def adjust_white_vertex(self, name):
        c = self.mover.cube_encoder.vertexes[name].coordinates
        cube = self.mover.cube

        if c == (1, 1, -1):
            self.solve_vertex_base_case(cube)

        elif c == (1, 1, 1):
            self.mover.U()
            self.solve_vertex_base_case(cube)

        elif c == (-1, 1, 1):
            self.mover.U()
            self.mover.U()
            self.solve_vertex_base_case(cube)

        elif c == (-1, 1, -1):
            self.mover.inv_U()
            self.solve_vertex_base_case(cube)

        elif c == (1, -1, -1):
            if not cube[0][0][2] == 'W':
                self.sexy_moves()
                self.solve_vertex_base_case(cube)

        elif c == (1, -1, 1):
            self.mover.B()
            self.mover.U()
            self.mover.inv_B()
            self.solve_vertex_base_case(cube)

        elif c == (-1, -1, 1):
            self.mover.L()
            self.mover.U()
            self.mover.U()
            self.mover.inv_L()
            self.solve_vertex_base_case(cube)

        elif c == (-1, -1, -1):
            self.mover.F()
            self.mover.inv_U()
            self.mover.inv_F()
            self.mover.inv_U()
            self.solve_vertex_base_case(cube)

    def finish_white_face(self):
        self.adjust_white_vertex('WRG')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_white_vertex('WGO')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_white_vertex('WOU')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_white_vertex('WRU')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'

    def R_to_G(self):
        self.anti_sexy_moves()
        self.mover.inv_U()
        self.mover.inv_F()
        self.mover.U()
        self.mover.F()

    def R_to_U(self):
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.U()
        self.mover.L()
        self.mover.U()
        self.mover.F()
        self.mover.inv_U()
        self.mover.inv_F()

    def G_to_R(self):
        self.mover.inv_U()
        self.mover.inv_F()
        self.mover.U()
        self.mover.F()
        self.mover.U()
        self.mover.R()
        self.mover.inv_U()
        self.mover.inv_R()

    def G_to_O(self):
        self.mover.U()
        self.mover.B()
        self.mover.inv_U()
        self.mover.inv_B()
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.U()
        self.mover.R()

    def O_to_G(self):
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.U()
        self.mover.R()
        self.mover.U()
        self.mover.B()
        self.mover.inv_U()
        self.mover.inv_B()

    def O_to_U(self):
        self.mover.U()
        self.mover.L()
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.inv_U()
        self.mover.inv_B()
        self.mover.U()
        self.mover.B()

    def U_to_O(self):
        self.mover.inv_U()
        self.mover.inv_B()
        self.mover.U()
        self.mover.B()
        self.mover.U()
        self.mover.L()
        self.mover.inv_U()
        self.mover.inv_L()

    def U_to_R(self):
        self.mover.U()
        self.mover.F()
        self.mover.inv_U()
        self.mover.inv_F()
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.U()
        self.mover.L()

    def adjust_RG(self):
        c = self.mover.cube_encoder.edges['OU'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'U':
                self.G_to_R()
            else:
                self.mover.U()
                self.R_to_G()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'O':
                self.R_to_G()
            else:
                self.mover.inv_U()
                self.G_to_R()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'O':
                self.mover.inv_U()
                self.R_to_G()
            else:
                self.mover.U()
                self.mover.U()
                self.G_to_R()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'U':
                self.mover.U()
                self.G_to_R()
            else:
                self.mover.U()
                self.mover.U()
                self.R_to_G()

        elif c == (1, 0, -1):
            if cube[1][1][2] == 'U':
                self.R_to_G()
                self.mover.U()
                self.mover.U()
                self.R_to_G()

        elif c == (1, 0, 1):
            self.G_to_O()
            if cube[4][0][1] == 'O':
                self.mover.inv_U()
                self.R_to_G()
            else:
                self.mover.U()
                self.mover.U()
                self.G_to_R()

        elif c == (-1, 0, 1):
            self.O_to_U()
            if cube[1][0][1] == 'O':
                self.R_to_G()
            else:
                self.mover.inv_U()
                self.G_to_R()

        elif c == (-1, 0, -1):
            self.U_to_R()
            if cube[2][0][1] == 'U':
                self.G_to_R()
            else:
                self.mover.U()
                self.R_to_G()

    def adjust_GO(self):
        c = self.mover.cube_encoder.edges['WG'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'G':
                self.mover.inv_U()
                self.O_to_G()
            else:
                self.G_to_O()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'G':
                self.mover.U()
                self.mover.U()
                self.O_to_G()
            else:
                self.mover.inv_U()
                self.G_to_O()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'G':
                self.mover.U()
                self.O_to_G()
            else:
                self.mover.U()
                self.mover.U()
                self.G_to_O()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'G':
                self.O_to_G()
            else:
                self.mover.U()
                self.G_to_O()

        elif c == (1, 0, -1):
            self.R_to_G()
            if cube[3][0][1] == 'G':
                self.O_to_G()
            else:
                self.mover.U()
                self.G_to_O()

        elif c == (1, 0, 1):
            if cube[2][1][2] == 'G':
                self.G_to_O()
                self.mover.U()
                self.mover.U()
                self.G_to_O()

        elif c == (-1, 0, 1):
            self.O_to_U()
            if cube[1][0][1] == 'G':
                self.mover.U()
                self.mover.U()
                self.O_to_G()
            else:
                self.mover.inv_U()
                self.G_to_O()

        elif c == (-1, 0, -1):
            self.U_to_R()
            if cube[2][0][1] == 'G':
                self.mover.inv_U()
                self.O_to_G()
            else:
                self.G_to_O()

    def adjust_OU(self):
        c = self.mover.cube_encoder.edges['RY'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'R':
                self.mover.U()
                self.mover.U()
                self.U_to_O()
            else:
                self.mover.inv_U()
                self.O_to_U()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'R':
                self.mover.U()
                self.U_to_O()
            else:
                self.mover.U()
                self.mover.U()
                self.O_to_U()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'R':
                self.U_to_O()
            else:
                self.mover.U()
                self.O_to_U()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'R':
                self.mover.inv_U()
                self.U_to_O()
            else:
                self.O_to_U()

        elif c == (1, 0, -1):
            self.R_to_G()
            if cube[3][0][1] == 'R':
                self.mover.inv_U()
                self.U_to_O()
            else:
                self.O_to_U()

        elif c == (1, 0, 1):
            self.G_to_O()
            if cube[4][0][1] == 'R':
                self.U_to_O()
            else:
                self.mover.U()
                self.O_to_U()

        elif c == (-1, 0, 1):
            if cube[3][1][2] == 'R':
                self.O_to_U()
                self.mover.U()
                self.mover.U()
                self.O_to_U()

        elif c == (-1, 0, -1):
            self.U_to_R()
            if cube[2][0][1] == 'R':
                self.mover.U()
                self.mover.U()
                self.U_to_O()
            else:
                self.mover.inv_U()
                self.O_to_U()

    def adjust_RU(self):
        c = self.mover.cube_encoder.edges['UY'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'U':
                self.mover.U()
                self.R_to_U()
            else:
                self.mover.U()
                self.mover.U()
                self.U_to_R()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'U':
                self.R_to_U()
            else:
                self.mover.U()
                self.U_to_R()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'U':
                self.mover.inv_U()
                self.R_to_U()
            else:
                self.U_to_R()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'U':
                self.mover.U()
                self.mover.U()
                self.R_to_U()
            else:
                self.mover.inv_U()
                self.U_to_R()

        elif c == (1, 0, -1):
            self.R_to_G()
            if cube[3][0][1] == 'U':
                self.mover.U()
                self.mover.U()
                self.R_to_U()
            else:
                self.mover.inv_U()
                self.U_to_R()

        elif c == (1, 0, 1):
            self.G_to_O()
            if cube[4][0][1] == 'U':
                self.mover.inv_U()
                self.R_to_U()
            else:
                self.U_to_R()

        elif c == (-1, 0, 1):
            self.O_to_U()
            if cube[1][0][1] == 'U':
                self.R_to_U()
            else:
                self.mover.U()
                self.U_to_R()

        elif c == (-1, 0, -1):
            if cube[4][1][2] == 'U':
                self.U_to_R()
                self.mover.U()
                self.mover.U()
                self.U_to_R()

    def solve_second_layer(self):
        self.adjust_RG()
        self.mover.moves = self.mover.moves
        self.adjust_GO()
        self.mover.moves = self.mover.moves
        self.adjust_OU()
        self.mover.moves = self.mover.moves
        self.adjust_RU()
        self.mover.moves = self.mover.moves + '\n'

    def find_situation(self):
        cube = self.mover.cube
        position_WO = self.mover.cube_encoder.edges['WO'].coordinates
        position_OY = self.mover.cube_encoder.edges['OY'].coordinates
        color_5_0_0 = cube[5][0][0]
        color_5_0_1 = cube[5][0][1]
        color_5_0_2 = cube[5][0][2]
        color_5_1_0 = cube[5][1][0]
        color_5_1_2 = cube[5][1][2]
        color_5_2_0 = cube[5][2][0]
        color_5_2_1 = cube[5][2][1]
        color_5_2_2 = cube[5][2][2]
        color_1_0_0 = cube[1][0][0]
        color_1_0_2 = cube[1][0][2]
        color_2_0_0 = cube[2][0][0]
        color_2_0_2 = cube[2][0][2]
        color_3_0_0 = cube[3][0][0]
        color_3_0_2 = cube[3][0][2]
        color_4_0_0 = cube[4][0][0]
        color_4_0_2 = cube[4][0][2]
        if (
            (color_5_0_1 == 'U' and color_5_1_0 == 'G' and color_5_1_2 == 'W' and color_5_2_1 == 'O') or
            (color_5_0_1 == 'U' and color_5_1_0 == 'G' and color_5_1_2 == 'O' and color_5_2_1 == 'W') or
            (color_5_0_1 == 'U' and color_5_1_0 == 'W' and color_5_1_2 == 'O' and color_5_2_1 == 'G') or
            (color_5_0_1 == 'U' and color_5_1_0 == 'W' and color_5_1_2 == 'G' and color_5_2_1 == 'O') or
            (color_5_0_1 == 'U' and color_5_1_0 == 'O' and color_5_1_2 == 'G' and color_5_2_1 == 'W') or
            (color_5_0_1 == 'U' and color_5_1_0 == 'O' and color_5_1_2 == 'W' and color_5_2_1 == 'G') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'G' and color_5_1_2 == 'U' and color_5_2_1 == 'W') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'G' and color_5_1_2 == 'W' and color_5_2_1 == 'U') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'U' and color_5_1_2 == 'G' and color_5_2_1 == 'W') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'U' and color_5_1_2 == 'W' and color_5_2_1 == 'G') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'W' and color_5_1_2 == 'U' and color_5_2_1 == 'G') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'W' and color_5_1_2 == 'G' and color_5_2_1 == 'U') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'W' and color_5_1_2 == 'O' and color_5_2_1 == 'U') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'W' and color_5_1_2 == 'U' and color_5_2_1 == 'O') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'U' and color_5_1_2 == 'W' and color_5_2_1 == 'O') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'U' and color_5_1_2 == 'O' and color_5_2_1 == 'W') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'O' and color_5_1_2 == 'W' and color_5_2_1 == 'U') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'O' and color_5_1_2 == 'U' and color_5_2_1 == 'W') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'O' and color_5_1_2 == 'U' and color_5_2_1 == 'G') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'O' and color_5_1_2 == 'G' and color_5_2_1 == 'U') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'U' and color_5_1_2 == 'O' and color_5_2_1 == 'G') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'U' and color_5_1_2 == 'G' and color_5_2_1 == 'O') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'G' and color_5_1_2 == 'O' and color_5_2_1 == 'U') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'G' and color_5_1_2 == 'U' and color_5_2_1 == 'O')
        ):
            if color_5_0_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == 'Y' and color_1_0_2 == 'Y' and color_3_0_0 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y' and color_2_0_2 == 'Y' and color_4_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_4_0_0 == 'Y' and color_4_0_2 == 'Y' and color_1_0_2 == 'Y' and color_3_0_0 == 'Y':
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.R()
                elif color_1_0_0 == 'Y' and color_1_0_2 == 'Y' and color_2_0_2 == 'Y' and color_4_0_0 == 'Y':
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.B()
                elif color_2_0_0 == 'Y' and color_2_0_2 == 'Y' and color_1_0_0 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.L()
                elif color_3_0_0 == 'Y' and color_3_0_2 == 'Y' and color_2_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.F()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_1_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_2_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_4_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()

            elif color_5_0_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y':
                if color_2_0_2 == 'Y' and color_1_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.B()
                elif color_3_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.F()
            elif color_5_0_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                if color_2_0_0 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.L()
                elif color_4_0_0 == 'Y' and color_1_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.R()

            elif color_5_0_2 == 'Y' and color_5_2_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y':
                if color_1_0_0 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.D()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_D()
                    self.mover.inv_B()
                    self.mover.inv_B()
                elif color_4_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.F()
                    self.mover.D()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_D()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_F()
            elif color_5_0_0 == 'Y' and color_5_0_2 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.D()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_D()
                    self.mover.L()
                    self.mover.L()
                elif color_1_0_0 == 'Y' and color_1_0_2 == 'Y':
                    self.mover.R()
                    self.mover.R()
                    self.mover.D()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_D()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_R()
            elif color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_0_2 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_2 == 'Y' and color_3_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.D()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_D()
                    self.mover.inv_F()
                    self.mover.inv_F()
                elif color_2_0_0 == 'Y' and color_2_0_2 == 'Y':
                    self.mover.B()
                    self.mover.B()
                    self.mover.D()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_D()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_B()
            elif color_5_2_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_2_0_2 == 'Y' and color_4_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.D()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_D()
                    self.mover.R()
                    self.mover.R()
                elif color_3_0_0 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.L()
                    self.mover.D()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_D()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_L()
        elif (
            (color_5_0_1 == 'U' and color_5_2_1 == 'O' and position_OY == (0, 1, -1) and
             (color_5_1_0 not in ('G', 'W') and color_5_1_2 not in ('G', 'W'))) or
            (color_5_0_1 == 'U' and color_5_2_1 == 'W' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0))) and
             color_5_1_0 != 'G' and color_5_1_2 != 'G') or
            (color_5_0_1 == 'U' and color_5_2_1 == 'G' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0))) and
             color_5_1_0 != 'W' and color_5_1_2 != 'W') or
            (color_5_0_1 == 'G' and color_5_2_1 == 'W' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0))) and
             position_WO == (0, 1, -1) and
             color_5_1_0 != 'U' and color_5_1_2 != 'U') or
            (color_5_0_1 == 'G' and color_5_2_1 == 'O' and position_OY == (0, 1, -1) and ((color_5_1_2 != 'W' and
             position_WO == (1, 1, 0)) or
             (color_5_1_0 != 'W' and position_WO == (-1, 1, 0))) and color_5_1_0 != 'U' and color_5_1_2 != 'U') or
            (color_5_0_1 == 'O' and color_5_2_1 == 'W' and position_OY == (0, 1, 1) and position_WO == (0, 1, -1) and
             color_5_1_0 not in ('U', 'G') and
             color_5_1_2 not in ('U', 'G')) or
            (color_5_0_1 == 'O' and color_5_2_1 == 'U' and position_OY == (0, 1, 1) and
             (color_5_1_0 not in ('G', 'W') and color_5_1_2 not in ('G', 'W'))) or
            (color_5_0_1 == 'W' and color_5_2_1 == 'U' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0))) and
             color_5_1_0 != 'G' and color_5_1_2 != 'G') or
            (color_5_0_1 == 'G' and color_5_2_1 == 'U' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0))) and
             color_5_1_0 != 'W' and color_5_1_2 != 'W') or
            (color_5_0_1 == 'W' and color_5_2_1 == 'G' and position_WO == (0, 1, 1) and
             ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)))
             and color_5_1_0 != 'U' and color_5_1_2 != 'U') or
            (color_5_0_1 == 'O' and color_5_2_1 == 'G' and position_OY == (0, 1, 1) and ((
             color_5_1_2 != 'W' and position_WO == (1, 1, 0)) or
             (color_5_1_0 != 'W' and position_WO == (-1, 1, 0))) and color_5_1_0 != 'U' and color_5_1_2 != 'U') or
            (color_5_0_1 == 'W' and color_5_2_1 == 'O' and position_OY == (0, 1, -1) and position_WO == (0, 1, 1)
             and color_5_1_0 not in ('U', 'G') and
             color_5_1_2 not in ('U', 'G'))
        ):
            if color_5_0_0 == 'Y' and color_5_0_2 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
            elif color_5_0_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
            elif color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_0_2 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.R()
                elif color_1_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_0_2 == 'Y' and color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.L()
                elif color_3_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_0_2 == 'Y' and color_5_2_2 == 'Y':
                self.mover.B()
                self.mover.U()
                self.mover.inv_B()
                self.mover.inv_U()
                self.mover.F()
                self.mover.inv_B()
                self.mover.R()
                self.mover.B()
                self.mover.inv_R()
                self.mover.inv_F()
            elif color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y' and color_2_0_2 == 'Y' and color_4_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.R()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                elif color_2_0_0 == 'Y' and color_2_0_2 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.R()
                elif color_4_0_0 == 'Y' and color_4_0_2 == 'Y' and color_1_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.L()
                elif color_1_0_2 == 'Y' and color_1_0_0 == 'Y' and color_3_0_0 == 'Y' and color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_F()
                elif color_4_0_2 == color_2_0_0 == color_3_0_0 == color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                elif color_4_0_0 == color_2_0_2 == color_1_0_0 == color_1_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
            elif color_5_2_0 != 'Y' and color_5_2_2 == 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_4_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_4_0_0 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 == 'Y' and color_5_0_2 != 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_2_0_0 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
            elif color_5_2_0 == 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_2_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 == 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_1_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
            elif color_5_0_2 == color_5_2_0 == 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.F()
                elif color_4_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.B()
            elif color_5_0_0 == color_5_2_2 == 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_F()
        elif (
            (color_5_1_0 == 'U' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and
             (color_5_2_1 not in ('G', 'W') and color_5_0_1 not in ('G', 'W'))) or
            (color_5_1_0 == 'U' and color_5_1_2 == 'W' and ((color_5_2_1 == 'Y' and position_OY == (0, 1, -1)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             (color_5_2_1 != 'G' and color_5_0_1 != 'G')) or
            (color_5_1_0 == 'U' and color_5_1_2 == 'G' and ((color_5_2_1 == 'Y' and position_OY == (0, 1, -1))
             or (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_2_1 != 'W' and color_5_0_1 != 'W') or
            (color_5_1_0 == 'G' and color_5_1_2 == 'W' and ((color_5_2_1 == 'Y' and position_OY == (0, 1, -1)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             position_WO == (1, 1, 0) and
             color_5_2_1 != 'U' and color_5_0_1 != 'U') or
            (color_5_1_0 == 'G' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and (
             (color_5_0_1 != 'W' and position_WO == (0, 1, 1)) or
             (color_5_2_1 != 'W' and position_WO == (0, 1, -1))) and color_5_2_1 != 'U' and color_5_0_1 != 'U') or
            (color_5_1_0 == 'O' and color_5_1_2 == 'W' and position_OY == (-1, 1, 0) and position_WO == (1, 1, 0)
             and color_5_2_1 not in ('U', 'G') and
             color_5_0_1 not in ('U', 'G')) or
            (color_5_1_0 == 'O' and color_5_1_2 == 'U' and position_OY == (-1, 1, 0) and
             (color_5_2_1 not in ('G', 'W') and color_5_0_1 not in ('G', 'W'))) or
            (color_5_1_0 == 'W' and color_5_1_2 == 'U' and ((color_5_2_1 == 'Y' and position_OY == (0, 1, -1)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_2_1 != 'G' and color_5_0_1 != 'G') or
            (color_5_1_0 == 'G' and color_5_1_2 == 'U' and ((color_5_2_1 == 'Y' and position_OY == (0, 1, -1)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_2_1 != 'W' and color_5_0_1 != 'W') or
            (color_5_1_0 == 'W' and color_5_1_2 == 'G' and position_WO == (-1, 1, 0) and
             ((color_5_2_1 == 'Y' and position_OY == (0, 1, -1)) or (color_5_0_1 == 'Y' and position_OY == (0, 1, 1)))
             and color_5_2_1 != 'U' and color_5_0_1 != 'U') or
            (color_5_1_0 == 'O' and color_5_1_2 == 'G' and position_OY == (-1, 1, 0) and (
             (color_5_0_1 != 'W' and position_WO == (0, 1, 1)) or
             (color_5_2_1 != 'W' and position_WO == (0, 1, -1))) and color_5_2_1 != 'U' and color_5_0_1 != 'U') or
            (color_5_1_0 == 'W' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and position_WO == (-1, 1, 0)
             and color_5_2_1 not in ('U', 'G') and
             color_5_0_1 not in ('U', 'G'))
        ):
            if color_5_0_0 != 'Y' and color_5_0_2 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
            elif color_5_0_0 == 'Y' and color_5_0_2 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
            elif color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_0_2 != 'Y' and color_5_2_2 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.B()
                elif color_2_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_0_2 == 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.F()
                elif color_4_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_B()
            elif color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_0_2 == 'Y' and color_5_2_2 == 'Y':
                self.mover.R()
                self.mover.U()
                self.mover.inv_R()
                self.mover.inv_U()
                self.mover.L()
                self.mover.inv_R()
                self.mover.F()
                self.mover.R()
                self.mover.inv_F()
                self.mover.inv_L()
            elif color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_2 != 'Y':
                if color_3_0_0 == 'Y' and color_3_0_2 == 'Y' and color_1_0_0 == 'Y' and color_1_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.F()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                elif color_1_0_0 == 'Y' and color_1_0_2 == 'Y' and color_2_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.F()
                elif color_3_0_0 == 'Y' and color_3_0_2 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.B()
                elif color_2_0_2 == 'Y' and color_2_0_0 == 'Y' and color_4_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_L()
                elif color_1_0_2 == color_3_0_0 == color_4_0_0 == color_4_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                elif color_1_0_0 == color_3_0_2 == color_2_0_0 == color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
            elif color_5_2_0 == 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_4_0_0 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 == 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                elif color_1_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_2_0 != 'Y' and color_5_2_2 == 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_3_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 == 'Y' and color_5_0_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_1_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
            elif color_5_0_0 == color_5_2_2 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.R()
                elif color_1_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.L()
            elif color_5_2_0 == color_5_0_2 == 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_1_0_2 == 'Y':
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_R()
        elif (
          color_5_0_1 not in ('G', 'U') and color_5_1_0 not in ('G', 'U') and
          color_5_1_2 not in ('G', 'U') and color_5_2_1 not in ('G', 'U') and
          ((color_5_1_2 != 'W' and position_WO == (1, 1, 0)) or (color_5_1_0 != 'W' and position_WO == (-1, 1, 0)) or
           (color_5_0_1 != 'W' and position_WO == (0, 1, 1)) or (color_5_2_1 != 'W' and position_WO == (0, 1, -1)))
          and ((color_5_0_1 == 'Y' and position_OY == (0, 1, 1)) or (
           color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
           (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or (color_5_2_1 == 'Y' and position_OY == (0, 1, -1)))
        ):
            if color_5_2_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_0 == 'Y' and color_5_0_2 == 'Y':
                self.mover.inv_L()
                self.mover.R()
                self.mover.B()
                self.mover.R()
                self.mover.B()
                self.mover.inv_R()
                self.mover.inv_B()
                self.mover.inv_L()
                self.mover.inv_L()
                self.mover.R()
                self.mover.R()
                self.mover.F()
                self.mover.R()
                self.mover.inv_F()
                self.mover.inv_L()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_2_0_0 == 'Y' and color_2_0_2 == 'Y' and color_4_0_0 == 'Y' and color_4_0_2 == 'Y':
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                elif color_1_0_0 == color_1_0_2 == color_3_0_0 == color_3_0_2 == 'Y':
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                elif color_4_0_0 == color_3_0_0 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                elif color_3_0_0 == color_2_0_0 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                elif color_2_0_0 == color_1_0_0 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                elif color_1_0_0 == color_4_0_0 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 == 'Y' and color_5_0_2 != 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
            elif color_5_2_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 == 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_2_0 != 'Y' and color_5_2_2 == 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_2_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_2_0 == 'Y' and color_5_2_2 != 'Y' and color_5_0_0 != 'Y' and color_5_0_2 != 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_1_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_0 == color_5_0_2 == 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.R()
                    self.mover.B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                elif color_1_0_0 == 'Y':
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_F()
            elif color_5_0_2 == color_5_2_2 == 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.F()
                    self.mover.R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                elif color_4_0_2 == 'Y':
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_L()
            elif color_5_2_0 == color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.L()
                    self.mover.F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                elif color_3_0_2 == 'Y':
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_B()
            elif color_5_0_0 == color_5_2_0 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.B()
                    self.mover.L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                elif color_2_0_2 == "Y":
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_R()
            elif color_5_0_0 == color_5_2_2 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                elif color_2_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
            elif color_5_0_2 == color_5_2_0 == 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
        elif (
            (color_5_0_1 == 'U' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and
             (color_5_1_0 not in ('G', 'W') and color_5_2_1 not in ('G', 'W'))) or
            (color_5_0_1 == 'U' and color_5_1_2 == 'W' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_0 != 'G' and color_5_2_1 != 'G') or
            (color_5_0_1 == 'U' and color_5_1_2 == 'G' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_0 != 'W' and color_5_2_1 != 'W') or
            (color_5_0_1 == 'G' and color_5_1_2 == 'W' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             position_WO == (1, 1, 0) and
             color_5_1_0 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'G' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and ((color_5_1_0 != 'W' and
             position_WO == (-1, 1, 0)) or
             (color_5_2_1 != 'W' and position_WO == (0, 1, -1))) and color_5_1_0 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'O' and color_5_1_2 == 'W' and position_OY == (0, 1, 1) and position_WO == (1, 1, 0) and
             color_5_1_0 not in ('U', 'G') and
             color_5_2_1 not in ('U', 'G')) or
            (color_5_0_1 == 'O' and color_5_1_2 == 'U' and position_OY == (0, 1, 1) and
             (color_5_1_0 not in ('G', 'W') and color_5_2_1 not in ('G', 'W'))) or
            (color_5_0_1 == 'W' and color_5_1_2 == 'U' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_0 != 'G' and color_5_2_1 != 'G') or
            (color_5_0_1 == 'G' and color_5_1_2 == 'U' and ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_0 != 'W' and color_5_2_1 != 'W') or
            (color_5_0_1 == 'W' and color_5_1_2 == 'G' and position_WO == (0, 1, 1) and
             ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or (color_5_2_1 == 'Y' and position_OY == (0, 1, -1)))
             and color_5_1_0 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'O' and color_5_1_2 == 'G' and position_OY == (0, 1, 1) and ((
             color_5_1_0 == 'O' and position_WO == (-1, 1, 0)) or
             (color_5_2_1 == 'O' and position_WO == (0, 1, -1))) and color_5_1_0 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'W' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and position_WO == (0, 1, 1)
             and color_5_1_0 not in ('U', 'G') and
             color_5_2_1 not in ('U', 'G'))
        ):
            if color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_L()
                elif color_3_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.F()
            elif color_5_0_0 == color_5_2_2 == 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y':
                if color_4_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                elif color_1_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
            elif color_5_0_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                self.mover.B()
                self.mover.L()
                self.mover.inv_F()
                self.mover.inv_L()
                self.mover.inv_B()
                self.mover.F()
                self.mover.U()
                self.mover.F()
                self.mover.inv_U()
                self.mover.inv_F()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                elif color_4_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.F()
            elif color_5_0_2 == 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                elif color_1_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                elif color_3_0_2 == 'Y':
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                if color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == color_2_0_2 == color_1_0_0 == color_3_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                elif color_3_0_0 == color_3_0_2 == color_2_0_0 == color_4_0_2 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_4_0_0 == color_4_0_2 == color_1_0_2 == color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                elif color_1_0_0 == color_1_0_2 == color_4_0_0 == color_2_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_1_0_0 == color_1_0_2 == color_3_0_0 == color_3_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.R()
                elif color_4_0_0 == color_4_0_2 == color_2_0_0 == color_2_0_2 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_B()
            elif color_5_0_0 == 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.inv_B()
                elif color_3_0_0 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_0_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.B()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_B()
                elif color_3_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.F()
                    self.mover.R()
        elif (
            (color_5_2_1 == 'U' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and
             (color_5_1_0 not in ('G', 'W') and color_5_0_1 not in ('G', 'W'))) or
            (color_5_2_1 == 'U' and color_5_1_2 == 'W' and (
             (color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_0 != 'G' and color_5_0_1 != 'G') or
            (color_5_2_1 == 'U' and color_5_1_2 == 'G' and (
             (color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_0 != 'W' and color_5_0_1 != 'W') or
            (color_5_2_1 == 'G' and color_5_1_2 == 'W' and (
             (color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             position_WO == (1, 1, 0) and
             color_5_1_0 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'G' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and ((color_5_1_0 != 'W' and
             position_WO == (-1, 1, 0)) or (color_5_0_1 != 'W' and position_WO == (0, 1, 1))) and
             color_5_1_0 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'O' and color_5_1_2 == 'W' and position_OY == (0, 1, -1) and position_WO == (1, 1, 0) and
             color_5_1_0 not in ('U', 'G') and color_5_0_1 not in ('U', 'G')) or
            (color_5_2_1 == 'O' and color_5_1_2 == 'U' and position_OY == (0, 1, -1) and
             (color_5_1_0 not in ('G', 'W') and color_5_0_1 not in ('G', 'W'))) or
            (color_5_2_1 == 'W' and color_5_1_2 == 'U' and (
             (color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_0 != 'G' and color_5_0_1 != 'G') or
            (color_5_2_1 == 'G' and color_5_1_2 == 'U' and (
             (color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_0 != 'W' and color_5_0_1 != 'W') or
            (color_5_2_1 == 'W' and color_5_1_2 == 'G' and position_WO == (0, 1, -1) and
             ((color_5_1_0 == 'Y' and position_OY == (-1, 1, 0)) or (
              color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and color_5_1_0 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'O' and color_5_1_2 == 'G' and position_OY == (0, 1, -1) and ((
             color_5_1_0 != 'W' and position_WO == (-1, 1, 0)) or (color_5_0_1 != 'W' and position_WO == (0, 1, 1)))
             and color_5_1_0 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'W' and color_5_1_2 == 'O' and position_OY == (1, 1, 0) and position_WO == (0, 1, -1)
             and color_5_1_0 not in ('U', 'G') and
             color_5_0_1 not in ('U', 'G'))
        ):
            if color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.L()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.inv_B()
                elif color_2_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.L()
            elif color_5_0_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                elif color_4_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
            elif color_5_0_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                self.mover.R()
                self.mover.B()
                self.mover.inv_L()
                self.mover.inv_B()
                self.mover.inv_R()
                self.mover.L()
                self.mover.U()
                self.mover.L()
                self.mover.inv_U()
                self.mover.inv_L()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 == 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                elif color_3_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.L()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                elif color_4_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_4_0_2 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                elif color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_0_2 == 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                if color_1_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_1_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == color_1_0_2 == color_4_0_0 == color_2_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                elif color_2_0_0 == color_2_0_2 == color_1_0_0 == color_3_0_2 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_3_0_0 == color_3_0_2 == color_4_0_2 == color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                elif color_4_0_0 == color_4_0_2 == color_3_0_0 == color_1_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_4_0_0 == color_4_0_2 == color_2_0_0 == color_2_0_2 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.F()
                elif color_1_0_0 == color_1_0_2 == color_3_0_0 == color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_R()
            elif color_5_0_0 != 'Y' and color_5_0_2 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_0_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.R()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.L()
                    self.mover.F()
        elif (
            (color_5_2_1 == 'U' and color_5_1_0 == 'O' and position_OY == (-1, 1, 0) and
             (color_5_1_2 not in ('G', 'W') and color_5_0_1 not in ('G', 'W'))) or
            (color_5_2_1 == 'U' and color_5_1_0 == 'W' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_2 != 'G' and color_5_0_1 != 'G') or
            (color_5_2_1 == 'U' and color_5_1_0 == 'G' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_2 != 'W' and color_5_0_1 != 'W') or
            (color_5_2_1 == 'G' and color_5_1_0 == 'W' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             position_WO == (-1, 1, 0) and
             color_5_1_2 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'G' and color_5_1_0 == 'O' and position_OY == (-1, 1, 0) and ((color_5_1_2 != 'W' and
             position_WO == (1, 1, 0)) or (color_5_0_1 != 'W' and position_WO == (0, 1, 1))) and
             color_5_1_2 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'O' and color_5_1_0 == 'W' and position_OY == (0, 1, -1) and position_WO == (-1, 1, 0) and
             color_5_1_2 not in ('U', 'G') and
             color_5_0_1 not in ('U', 'G')) or
            (color_5_2_1 == 'O' and color_5_1_0 == 'U' and position_OY == (0, 1, -1) and
             (color_5_1_2 not in ('G', 'W') and color_5_0_1 not in ('G', 'W'))) or
            (color_5_2_1 == 'W' and color_5_1_0 == 'U' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_2 != 'G' and color_5_0_1 != 'G') or
            (color_5_2_1 == 'G' and color_5_1_0 == 'U' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and
             color_5_1_2 != 'W' and color_5_0_1 != 'W') or
            (color_5_2_1 == 'W' and color_5_1_0 == 'G' and position_WO == (0, 1, -1) and
             ((color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or (
              color_5_0_1 == 'Y' and position_OY == (0, 1, 1))) and color_5_1_2 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'O' and color_5_1_0 == 'G' and position_OY == (0, 1, -1) and ((
             color_5_1_2 != 'W' and position_WO == (1, 1, 0)) or (color_5_0_1 != 'W' and position_WO == (0, 1, 1)))
             and color_5_1_2 != 'U' and color_5_0_1 != 'U') or
            (color_5_2_1 == 'W' and color_5_1_0 == 'O' and position_OY == (-1, 1, 0) and position_WO == (0, 1, -1)
             and color_5_1_2 not in ('U', 'G') and
             color_5_0_1 not in ('U', 'G'))
        ):
            if color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_2_0_0 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.B()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.inv_R()
                elif color_1_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.B()
            elif color_5_0_0 == color_5_2_2 == 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                elif color_3_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
            elif color_5_0_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                self.mover.F()
                self.mover.R()
                self.mover.inv_B()
                self.mover.inv_R()
                self.mover.inv_F()
                self.mover.B()
                self.mover.U()
                self.mover.B()
                self.mover.inv_U()
                self.mover.inv_B()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.L()
                elif color_2_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.B()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                elif color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                elif color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                if color_4_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
            elif color_5_0_2 == 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_4_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_4_0_0 == color_4_0_2 == color_3_0_0 == color_1_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                elif color_1_0_0 == color_1_0_2 == color_4_0_0 == color_2_0_2 == 'Y':
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_2_0_0 == color_2_0_2 == color_3_0_2 == color_1_0_0 == 'Y':
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                elif color_3_0_0 == color_3_0_2 == color_2_0_0 == color_4_0_2 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                elif color_3_0_0 == color_3_0_2 == color_1_0_0 == color_1_0_2 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.L()
                elif color_4_0_0 == color_4_0_2 == color_2_0_0 == color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_F()
            elif color_5_0_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_4_0_2 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.inv_F()
                elif color_1_0_0 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_0 == 'Y' and color_5_0_2 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_4_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.F()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_F()
                elif color_1_0_0 == 'Y':
                    self.mover.inv_L()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.B()
                    self.mover.L()
        elif (
            (color_5_0_1 == 'U' and color_5_1_0 == 'O' and position_OY == (-1, 1, 0) and
             (color_5_1_2 not in ('G', 'W') and color_5_2_1 not in ('G', 'W'))) or
            (color_5_0_1 == 'U' and color_5_1_0 == 'W' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_2 != 'G' and color_5_2_1 != 'G') or
            (color_5_0_1 == 'U' and color_5_1_0 == 'G' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_2 != 'W' and color_5_2_1 != 'W') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'W' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             position_WO == (-1, 1, 0) and
             color_5_1_2 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'O' and position_OY == (-1, 1, 0) and ((color_5_1_2 != 'W' and
             position_WO == (1, 1, 0)) or (color_5_2_1 != 'W' and position_WO == (0, 1, -1)) and
             color_5_1_2 != 'U' and color_5_2_1 != 'U')) or
            (color_5_0_1 == 'O' and color_5_1_0 == 'W' and position_OY == (0, 1, 1) and position_WO == (-1, 1, 0) and
             color_5_1_2 not in ('U', 'G') and
             color_5_2_1 not in ('U', 'G')) or
            (color_5_0_1 == 'O' and color_5_1_0 == 'U' and position_OY == (0, 1, 1) and
             (color_5_1_2 not in ('G', 'W') and color_5_2_1 not in ('G', 'W'))) or
            (color_5_0_1 == 'W' and color_5_1_0 == 'U' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_2 != 'G' and color_5_2_1 != 'G') or
            (color_5_0_1 == 'G' and color_5_1_0 == 'U' and (
             (color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or
             (color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and
             color_5_1_2 != 'W' and color_5_2_1 != 'W') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'G' and position_WO == (0, 1, 1) and
             ((color_5_1_2 == 'Y' and position_OY == (1, 1, 0)) or (
              color_5_2_1 == 'Y' and position_OY == (0, 1, -1))) and color_5_1_2 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'O' and color_5_1_0 == 'G' and position_OY == (0, 1, 1) and ((
             color_5_1_2 != 'W' and position_WO == (1, 1, 0)) or (color_5_2_1 != 'W' and position_WO == (0, 1, -1)))
             and color_5_1_2 != 'U' and color_5_2_1 != 'U') or
            (color_5_0_1 == 'W' and color_5_1_0 == 'O' and position_OY == (-1, 1, 0) and position_WO == (0, 1, 1)
             and color_5_1_2 not in ('U', 'G') and
             color_5_2_1 not in ('U', 'G'))
        ):
            if color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_1_0_0 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.R()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.inv_R()
                    self.mover.inv_F()
                elif color_4_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.R()
            elif color_5_0_0 != 'Y' and color_5_2_2 != 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                if color_1_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.inv_R()
                elif color_2_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
            elif color_5_0_0 == 'Y' and color_5_2_2 == 'Y' and color_5_0_2 == 'Y' and color_5_2_0 == 'Y':
                self.mover.L()
                self.mover.F()
                self.mover.inv_R()
                self.mover.inv_F()
                self.mover.inv_L()
                self.mover.R()
                self.mover.U()
                self.mover.R()
                self.mover.inv_U()
                self.mover.inv_R()
            elif color_5_0_2 == 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_4_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.B()
                elif color_1_0_0 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.F()
                    self.mover.R()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.U()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                elif color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_3_0_0 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_0_2 != 'Y' and color_5_0_0 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_2_0_2 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                elif color_3_0_0 == 'Y':
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
                    self.mover.inv_L()
                    self.mover.B()
                    self.mover.L()
                    self.mover.inv_B()
                    self.mover.L()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_L()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                if color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
            elif color_5_0_2 == 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 == 'Y':
                if color_4_0_0 == 'Y':
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.inv_U()
                    self.mover.inv_F()
                    self.mover.U()
                    self.mover.U()
                    self.mover.F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.inv_L()
                elif color_3_0_2 == 'Y':
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.inv_U()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
            elif color_5_0_2 != 'Y' and color_5_0_0 != 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_3_0_0 == color_3_0_2 == color_2_0_0 == color_4_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.inv_F()
                    self.mover.inv_U()
                    self.mover.F()
                    self.mover.U()
                    self.mover.R()
                elif color_4_0_0 == color_4_0_2 == color_3_0_0 == color_1_0_2 == 'Y':
                    self.mover.F()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.R()
                    self.mover.U()
                    self.mover.inv_R()
                    self.mover.inv_U()
                    self.mover.inv_F()
                elif color_1_0_0 == color_1_0_2 == color_2_0_2 == color_4_0_0 == 'Y':
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.inv_L()
                    self.mover.F()
                elif color_2_0_0 == color_2_0_2 == color_1_0_0 == color_3_0_2 == 'Y':
                    self.mover.B()
                    self.mover.U()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.B()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.R()
                    self.mover.B()
                    self.mover.U()
                    self.mover.inv_B()
                    self.mover.inv_U()
                    self.mover.inv_R()
                elif color_2_0_0 == color_2_0_2 == color_4_0_0 == color_4_0_2 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.B()
                elif color_1_0_0 == color_1_0_2 == color_3_0_0 == color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_L()
            elif color_5_0_0 != 'Y' and color_5_0_2 != 'Y' and color_5_2_0 == 'Y' and color_5_2_2 != 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_F()
                    self.mover.inv_F()
                    self.mover.inv_L()
                elif color_4_0_0 == 'Y':
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
                    self.mover.U()
                    self.mover.B()
                    self.mover.L()
                    self.mover.U()
                    self.mover.inv_L()
                    self.mover.inv_U()
                    self.mover.inv_B()
            elif color_5_0_0 != 'Y' and color_5_0_2 == 'Y' and color_5_2_0 != 'Y' and color_5_2_2 != 'Y':
                if color_3_0_2 == 'Y':
                    self.mover.inv_R()
                    self.mover.L()
                    self.mover.L()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.L()
                    self.mover.F()
                    self.mover.F()
                    self.mover.inv_L()
                    self.mover.F()
                    self.mover.R()
                    self.mover.inv_L()
                elif color_4_0_0 == 'Y':
                    self.mover.inv_B()
                    self.mover.inv_R()
                    self.mover.F()
                    self.mover.inv_R()
                    self.mover.inv_F()
                    self.mover.R()
                    self.mover.R()
                    self.mover.B()

    def aa_perm(self):
        self.mover.inv_R()
        self.mover.F()
        self.mover.inv_R()
        self.mover.B()
        self.mover.B()
        self.mover.R()
        self.mover.inv_F()
        self.mover.inv_R()
        self.mover.B()
        self.mover.B()
        self.mover.R()
        self.mover.R()

    def e_perm(self):
        self.mover.R()
        self.mover.inv_B()
        self.mover.inv_R()
        self.mover.F()
        self.mover.R()
        self.mover.B()
        self.mover.inv_R()
        self.mover.inv_F()
        self.mover.R()
        self.mover.B()
        self.mover.inv_R()
        self.mover.F()
        self.mover.R()
        self.mover.inv_B()
        self.mover.inv_R()
        self.mover.inv_F()

    def vertex_pll(self):
        cube = self.mover.cube
        color_1_0_0 = cube[1][0][0]
        color_1_0_2 = cube[1][0][2]
        color_2_0_0 = cube[2][0][0]
        color_2_0_2 = cube[2][0][2]
        color_3_0_0 = cube[3][0][0]
        color_3_0_2 = cube[3][0][2]
        color_4_0_0 = cube[4][0][0]
        color_4_0_2 = cube[4][0][2]
        if color_1_0_0 == color_1_0_2 == 'R' and color_3_0_0 == color_3_0_2 == 'O':
            pass
        elif color_2_0_0 == color_2_0_2 == 'R' and color_4_0_0 == color_4_0_2 == 'O':
            self.mover.U()
        elif color_3_0_0 == color_3_0_2 == 'R' and color_1_0_0 == color_1_0_2 == 'O':
            self.mover.U()
            self.mover.U()
        elif color_4_0_0 == color_4_0_2 == 'R' and color_2_0_0 == color_2_0_2 == 'O':
            self.mover.inv_U()
        elif color_1_0_0 == 'R' == color_1_0_2 == 'R':
            self.mover.U()
            self.mover.U()
            self.aa_perm()
            self.mover.U()
        elif color_1_0_0 == 'G' == color_1_0_2 == 'G':
            self.mover.U()
            self.mover.U()
            self.aa_perm()
        elif color_1_0_0 == 'B' == color_1_0_2 == 'B':
            self.mover.U()
            self.mover.U()
            self.aa_perm()
            self.mover.U()
            self.mover.U()
        elif color_1_0_0 == 'O' == color_1_0_2 == 'O':
            self.mover.U()
            self.mover.U()
            self.aa_perm()
            self.mover.inv_U()
        elif color_2_0_0 == 'R' == color_2_0_2 == 'R':
            self.mover.inv_U()
            self.aa_perm()
            self.mover.U()
        elif color_2_0_0 == 'G' == color_2_0_2 == 'G':
            self.mover.inv_U()
            self.aa_perm()
        elif color_2_0_0 == 'B' == color_2_0_2 == 'B':
            self.mover.inv_U()
            self.aa_perm()
            self.mover.U()
            self.mover.U()
        elif color_2_0_0 == 'O' == color_2_0_2 == 'O':
            self.mover.inv_U()
            self.aa_perm()
            self.mover.inv_U()
        elif color_3_0_0 == 'R' == color_3_0_2 == 'R':
            self.aa_perm()
            self.mover.U()
        elif color_3_0_0 == 'G' == color_3_0_2 == 'G':
            self.aa_perm()
        elif color_3_0_0 == 'B' == color_3_0_2 == 'B':
            self.aa_perm()
            self.mover.U()
            self.mover.U()
        elif color_3_0_0 == 'O' == color_3_0_2 == 'O':
            self.aa_perm()
            self.mover.inv_U()
        elif color_4_0_0 == 'R' == color_4_0_2 == 'R':
            self.mover.U()
            self.aa_perm()
            self.mover.U()
        elif color_4_0_0 == 'G' == color_4_0_2 == 'G':
            self.mover.U()
            self.aa_perm()
        elif color_4_0_0 == 'B' == color_4_0_2 == 'B':
            self.mover.U()
            self.aa_perm()
            self.mover.U()
            self.mover.U()
        elif color_4_0_0 == 'O' == color_4_0_2 == 'O':
            self.mover.U()
            self.aa_perm()
            self.mover.inv_U()
        else:
            self.e_perm()

    def ua_perm(self):
        self.mover.L()
        self.mover.L()
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.inv_U()
        self.mover.L()
        self.mover.U()
        self.mover.L()
        self.mover.U()
        self.mover.L()
        self.mover.inv_U()
        self.mover.L()

    def ub_perm(self):
        self.mover.R()
        self.mover.R()
        self.mover.U()
        self.mover.R()
        self.mover.U()
        self.mover.inv_R()
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.U()
        self.mover.inv_R()

    def z_perm(self):
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()
        self.mover.D()
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()
        self.mover.U()
        self.mover.L()
        self.mover.inv_R()
        self.mover.F()
        self.mover.F()
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()
        self.mover.B()
        self.mover.B()
        self.mover.L()
        self.mover.inv_R()
        self.mover.U()
        self.mover.U()

    def h_perm(self):
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()
        self.mover.D()
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()
        self.mover.U()
        self.mover.U()
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()
        self.mover.D()
        self.mover.L()
        self.mover.L()
        self.mover.R()
        self.mover.R()

    def edges_pll(self):
        cube = self.mover.cube
        color_5_0_1 = cube[5][0][1]
        color_5_1_0 = cube[5][1][0]
        color_5_1_2 = cube[5][1][2]
        color_5_2_1 = cube[5][2][1]
        if color_5_2_1 == 'O' and color_5_1_0 == 'G' and color_5_1_2 == 'W':
            pass
        elif color_5_2_1 == 'O' and color_5_1_0 == 'W' and color_5_0_1 == 'G':
            self.mover.U()
            self.mover.U()
            self.ua_perm()
            self.mover.U()
            self.mover.U()
        elif color_5_2_1 == 'O' and color_5_1_2 == 'G' and color_5_1_0 == 'U':
            self.mover.U()
            self.mover.U()
            self.ub_perm()
            self.mover.U()
            self.mover.U()
        elif color_5_1_2 == 'W' and color_5_2_1 == 'U' and color_5_1_0 == 'O':
            self.mover.inv_U()
            self.ua_perm()
            self.mover.U()
        elif color_5_1_2 == 'W' and color_5_0_1 == 'O' and color_5_2_1 == 'G':
            self.mover.inv_U()
            self.ub_perm()
            self.mover.U()
        elif color_5_0_1 == 'U' and color_5_1_2 == 'G':
            self.ua_perm()
        elif color_5_0_1 == 'U' and color_5_1_0 == 'W':
            self.ub_perm()
        elif color_5_1_0 == 'G' and color_5_0_1 == 'O' and color_5_1_2 == 'U':
            self.mover.U()
            self.ua_perm()
            self.mover.inv_U()
        elif color_5_1_0 == 'G' and color_5_2_1 == 'U' and color_5_0_1 == 'W':
            self.mover.U()
            self.ub_perm()
            self.mover.inv_U()
        elif color_5_0_1 == 'O' and color_5_2_1 == 'U':
            self.h_perm()
        elif color_5_0_1 == 'G' and color_5_1_0 == 'U' and color_5_1_2 == 'O':
            self.z_perm()
        elif color_5_1_0 == 'O' and color_5_2_1 == 'G' and color_5_0_1 == 'W':
            self.mover.U()
            self.z_perm()
            self.mover.inv_U()

    def generator(self):
        random_300 = random.randint(200, 300)
        for i in range(random_300):
            random_6 = random.randint(0, 5)
            if random_6 == 0:
                self.mover.U()
            elif random_6 == 1:
                self.mover.F()
            elif random_6 == 2:
                self.mover.R()
            elif random_6 == 3:
                self.mover.B()
            elif random_6 == 4:
                self.mover.L()
            elif random_6 == 5:
                self.mover.D()
        print(self.mover.cube)
        self.mover.moves = self.mover.moves + '\n'

    def error_check(self):
        if not np.array_equal([[['W', 'R', 'W'],
                                ['Y', 'W', 'G'],
                                ['W', 'U', 'W']],
                               [['R', 'Y', 'R'],
                                ['U', 'R', 'O'],
                                ['R', 'W', 'R']],
                               [['G', 'O', 'G'],
                                ['U', 'G', 'W'],
                                ['G', 'R', 'G']],
                               [['O', 'W', 'O'],
                                ['G', 'O', 'Y'],
                                ['O', 'R', 'O']],
                               [['U', 'O', 'U'],
                                ['R', 'U', 'Y'],
                                ['U', 'G', 'U']],
                               [['Y', 'U', 'Y'],
                                ['G', 'Y', 'W'],
                                ['Y', 'O', 'Y']]], self.mover.cube):
            print('error1')

    def solve_cube(self):
        self.generator()
        self.solve_white_cross()
        self.finish_white_face()
        self.solve_second_layer()
        self.find_situation()
        self.mover.moves = self.mover.moves + '\n'
        self.vertex_pll()
        self.mover.moves = self.mover.moves + '\n'
        self.vertex_pll()
        self.mover.moves = self.mover.moves + '\n'
        self.edges_pll()
        self.mover.moves = self.mover.moves + '\n'
        print(self.mover.moves)
        self.error_check()
