import asyncio
import datetime
from typing import Any

from kivy.uix.button import Button
from kivymd.app import MDApp


class KivyApp(MDApp):
    title = 'Task Distributor'

    def build(self) -> Any:
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.material_style = "M3"
        return Button(text=str(datetime.datetime.now()))


if __name__ == '__main__':
    asyncio.run(KivyApp().async_run(async_lib='asyncio'))
