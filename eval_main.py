import numpy as np
import torch

import utils

from info.game_info import GameInfo


class Evaluator(object):
    def __init__(self):
        self.player = None
        self.enemy = None
        self.monitor = None
        pass

    def get_action(self, root_id, board, turn, enemy_turn):

        action, action_index = 0, 0

        if turn != enemy_turn:
            choice = input("move or block\n")
            if choice == 'm':
                action = 0
                direction = input("dir?\n")
                if direction == 'u':
                    action_index = 0
                elif direction == 'r':
                    action_index = 1
                elif direction == ' ':
                    action_index = 2
                else:
                    action_index = 3
        else:
            pass

        return action, action_index


evaluator = Evaluator()


def main():
    turn = 0
    enemy_turn = 1

    board = np.zeros([17, 17])
    root_id = (0,)
    win_index = 0
    action_index = None

    GameInfo.game_board = board

    # 게임이 시작된  후 끝날때까지 진행되는 메인 코드
    while win_index == 0:
        utils.render_str(board)  # 콘솔에 보드 상태 출력

        # 다음 액션에 대한 입력을 대기
        action, action_index = evaluator.get_action(root_id,
                                                    board,
                                                    turn,
                                                    enemy_turn)
        # 액션 실행
        if turn != enemy_turn:
            root_id = evaluator.player.root_id + action + (action_index,)
        else:

        # 승패 판독


if __name__ == '__main__':
    main()
