# ytboy_widgets.py - Custom widgets for ytboy
from textual.widget import Widget
from rich.console import RenderableType

class ImageWidget(Widget):
    def __init__(self, image: RenderableType, name: str = None):
        super().__init__(name=name)
        self.image = image

    def render(self) -> RenderableType:
        return self.image

from rich_pixels import Pixels
from PIL import Image

def get_logo():
    with Image.open("assets/logo_large.png") as image:
        new_size = (30, 8)
        resized_image = image.resize(new_size, Image.NEAREST)
        pixels = Pixels.from_image(resized_image)
    return pixels