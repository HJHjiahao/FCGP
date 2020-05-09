'''
Function:
	经典坦克大战小游戏
'''
import os
import pygame

import G2.cfg as cfg
# from modules import *

from G2.modules.GameLevel import GameLevel
from G2.modules.interfaces.gameEndIterface import gameEndIterface
from G2.modules.interfaces.gameStartInterface import gameStartInterface
from G2.modules.interfaces.switchLevelIterface import switchLevelIterface

'''主函数'''
def main():
	# 游戏初始化
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
	pygame.display.set_caption(cfg.TITLE)
	# 加载游戏素材
	sounds = {}
	for key, value in cfg.AUDIO_PATHS.items():
		sounds[key] = pygame.mixer.Sound(value)
		sounds[key].set_volume(1)
	# 开始界面
	score = 0
	prop_use = False
	is_dual_mode = gameStartInterface(screen, cfg)
	# 关卡数
	levelfilepaths = [os.path.join(cfg.LEVELFILEDIR, filename) for filename in sorted(os.listdir(cfg.LEVELFILEDIR))]
	# 主循环
	for idx, levelfilepath in enumerate(levelfilepaths):
		switchLevelIterface(screen, cfg, idx+1)
		game_level = GameLevel(idx+1, levelfilepath, sounds, is_dual_mode, cfg, score, prop_use)
		is_win = game_level.start(screen)
		score  = game_level.score
		if not is_win: break
	is_quit_game = gameEndIterface(screen, cfg, is_win)
	return is_quit_game
