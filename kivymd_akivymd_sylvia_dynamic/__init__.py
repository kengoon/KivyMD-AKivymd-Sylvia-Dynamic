import os

from kivy import Logger
from kivy.factory import Factory

from kivymd_akivymd_sylvia_dynamic.tools.iconfonts import register

r = Factory.register

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, f"icont{os.sep}")
Logger.info("KASD: 0.1.1")

# registered fonts
register('fontello', f'{fonts_path}/fontello.ttf', f'{fonts_path}/fontello.fontd')
register("icomoon", f"{fonts_path}/icomoon.ttf", f"{fonts_path}/icomoon.fontd")
register("icomoon2", f"{fonts_path}/icomoon2.ttf", f"{fonts_path}/icomoon2.fontd")

# register classes
r("MsCard", module="kivymd_akivymd_sylvia_dynamic.uix.card")
r("M_AKBottomNavigation", module="kivymd_akivymd_sylvia_dynamic.uix.a_bottomnavigation")
r("M_AKSilverAppbar", module="kivymd_akivymd_sylvia_dynamic.uix.a_silverappbar")
r("M_MDIconButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDFloatingActionButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDFlatButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDRaisedButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDRectangleFlatButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDRectangleFlatIconButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDRoundFlatButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDRoundFlatIconButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDFillRoundFlatButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDFillRoundFlatIconButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDTextButton", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
r("M_MDFloatingActionButtonSpeedDial", module="kivymd_akivymd_sylvia_dynamic.uix.m_mdbuttons")
