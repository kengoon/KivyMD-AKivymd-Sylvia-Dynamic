import os

from kivy import Logger

from kivymd_akivymd_sylvia_dynamic.tools.iconfonts import register

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, f"icont{os.sep}")
Logger.info("KASD: 0.1")
register('fontello', f'{fonts_path}/fontello.ttf', f'{fonts_path}/fontello.fontd')
register("icomoon", f"{fonts_path}/icomoon.ttf", f"{fonts_path}/icomoon.fontd")
register("icomoon2", f"{fonts_path}/icomoon2.ttf", f"{fonts_path}/icomoon2.fontd")
