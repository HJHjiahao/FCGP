'''config file'''
import os


# FPS
FPS = 100
# 屏幕大小
SCREENSIZE = (640, 480)
# 游戏图片路径
IMAGE_PATHS = {
                'rabbit': os.path.join(os.getcwd(), 'G1/resources/images/dude.png'),
                'grass': os.path.join(os.getcwd(), 'G1/resources/images/grass.png'),
                'castle': os.path.join(os.getcwd(), 'G1/resources/images/castle.png'),
                'arrow': os.path.join(os.getcwd(), 'G1/resources/images/bullet.png'),
                'badguy': os.path.join(os.getcwd(), 'G1/resources/images/badguy.png'),
                'healthbar': os.path.join(os.getcwd(), 'G1/resources/images/healthbar.png'),
                'health': os.path.join(os.getcwd(), 'G1/resources/images/health.png'),
                'gameover': os.path.join(os.getcwd(), 'G1/resources/images/gameover.png'),
                'youwin': os.path.join(os.getcwd(), 'G1/resources/images/youwin.png')
            }
# 游戏声音路径
SOUNDS_PATHS = {
                'hit': os.path.join(os.getcwd(), 'G1/resources/audio/explode.wav'),
                'enemy': os.path.join(os.getcwd(), 'G1/resources/audio/enemy.wav'),
                'shoot': os.path.join(os.getcwd(), 'G1/resources/audio/shoot.wav'),
                'moonlight': os.path.join(os.getcwd(), 'G1/resources/audio/moonlight.wav')
            }