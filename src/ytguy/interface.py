from rich.console import RenderableType

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.validation import URL
from textual.widgets import Footer, Input, Static, Button
from textual.widget import Widget

from ytboy.src.widgets import ImageWidget, get_logo

class ImageWidget(Widget):
    def __init__(self, image: RenderableType, name: str = None):
        super().__init__(name=name)
        self.image = image

    def render(self) -> RenderableType:
        return self.image

class ytboy(App):

    CSS_PATH = "./ytboy.tcss"
    URL_MESSAGE = "Please enter a URL to download." 

    def compose(self) -> ComposeResult:
        yield Container(
            Vertical(
                ImageWidget(get_logo(), name="logo"),
                Input(
                    placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    validators=[URL()],
                    valid_empty=True,
                    id="url_input"
                ),
                Container(
                    Horizontal(
                        Button("Video download", variant="success"),
                        Button("Audio download", variant="error"),
                        classes="buttons",
                        id="horizontal_button_conainer"
                    ),
                    id="input_buttons_container",
                ),
                Static(self.URL_MESSAGE, id="url_message"),
                id="vertical_container"
            ),
            id="main_container",
        )

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
        if event.validation_result is not None and not event.validation_result.is_valid:  
            self.query_one(Static).update(', '.join(event.validation_result.failure_descriptions))
        else:
            self.query_one(Static).update(self.URL_MESSAGE)  # Use the default URL

if __name__ == "__main__":
    app = ytboy()
    app.run()