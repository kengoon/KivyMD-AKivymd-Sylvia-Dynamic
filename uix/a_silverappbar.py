from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior

Builder.load_string(
    """
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
<M_AKSilverAppbarContent>
    canvas.before:
        Color:
            rgba: root.md_bg_color if root.md_bg_color else root.theme_cls.bg_normal
        RoundedRectangle:
            pos: self.pos
            size : self.size
            radius: root.parent.parent.parent.parent.radius

<M_AKSilverAppbar>
    t_opacity:1

    FloatLayout:
        id: float_box
        BoxLayout:
            canvas.after:
                Color:
                    rgba: 0,0,0,0
                    a: root._darkness
                Rectangle:
                    pos: self.pos
                    size: self.size
            id: header
            size_hint_y: None
            height: root.max_height +  root.radius[0]
            pos: self.x, root.height-root.max_height- root.radius[0]

        M_NewScrollView:
            effect_cls:ScrollEffect

            MDBoxLayout:
                id: scroll_box
                adaptive_height: True
                orientation: 'vertical'

                BoxLayout:
                    size_hint_y: None
                    height: root.max_height

        MDToolbar:
            id: toolbar
            pos: self.x, float_box.height-self.height
            right_action_items: root.right_action_items
            left_action_items: root.left_action_items
            title: root.title
            anchor_title: root.anchor_title
            md_bg_color: root.toolbar_bg if root.toolbar_bg else root.theme_cls.primary_color
            elevation: 0.01 if root.elevation==0 else root.elevation
            opacity: root.t_opacity

    """
)


class M_AKSilverAppbarContent(ThemableBehavior, BoxLayout, RectangularElevationBehavior):
    md_bg_color = ListProperty()


class M_AKSilverAppbarHeader(BoxLayout):
    pass


class M_NewScrollView(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda x: self._update())

    def on_vbar(self, *args):
        toolbar_percent = (self.parent.parent.ids.toolbar.height /
                           self.parent.parent.ids.scroll_box.height) * 100
        current_percent = (self.vbar[0] + self.vbar[1]) * 100
        banner_percent_min = (1 - self.parent.parent.max_height /
                              self.parent.parent.ids.scroll_box.height) * 100 + toolbar_percent
        if self.parent.parent.hide_toolbar:
            if banner_percent_min <= current_percent:
                current_percent_in_banner = current_percent - banner_percent_min
                opacity = current_percent_in_banner / \
                          (100 - banner_percent_min)

                self.parent.parent._darkness = self.parent.parent.header_max_darkness * \
                                               (1 - opacity)

                if not self.parent.parent.pin_top:
                    self.parent.parent.toolbar_bg = self.parent.parent.toolbar_bg[0:3] + [0]
                    self.parent.parent.ids.toolbar.opacity = opacity
                else:
                    self.parent.parent.toolbar_bg = self.parent.parent.toolbar_bg[0:3] + [
                        1 - opacity]
                    self.parent.parent.ids.toolbar._hard_shadow_a = 1 - opacity
                    self.parent.parent.ids.toolbar._soft_shadow_a = 1 - opacity

            else:
                if not self.parent.parent.pin_top:
                    self.parent.parent.ids.toolbar.opacity = 0
                else:
                    self.parent.parent.toolbar_bg = self.parent.parent.toolbar_bg[0:3] + [1]

    def _update(self):
        self.parent.parent = self.parent.parent


class M_AKSilverAppbar(ThemableBehavior, BoxLayout):
    max_height = NumericProperty(300)
    left_action_items = ListProperty()
    right_action_items = ListProperty()
    title = StringProperty()
    toolbar_bg = ListProperty()
    anchor_title = StringProperty("left")
    pin_top = BooleanProperty(True)
    hide_toolbar = BooleanProperty(True)
    elevation = NumericProperty(6)
    radius = ListProperty([dp(20), dp(20), 0, 0])
    header_max_darkness = NumericProperty(0.7)

    _darkness = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_widget(self, widget, index=0, canvas=None):

        if issubclass(widget.__class__, M_AKSilverAppbarContent):
            self.ids.scroll_box.add_widget(widget)
        elif issubclass(widget.__class__, M_AKSilverAppbarHeader):
            self.ids.header.add_widget(widget)
        else:
            super().add_widget(widget, index=index, canvas=canvas)
