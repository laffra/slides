"""
A PDF player written using PyScript LTK.
"""
import ltk

body = ltk.find("body")

class Player():
    """ A PDF player """
    def __init__(self, page_count):
        self.index = 1
        self.page_count = page_count
        self.image = ltk.Image("slides/page-1.png").addClass("slide")
        ltk.Div(
            self.image
                .on("load", ltk.proxy(lambda event: self.resize_image()))
                .on("mousemove", ltk.proxy(lambda event: self.show_buttons())),
            ltk.Label("<")
                .addClass("button previous")
                .on("click", ltk.proxy(lambda event: self.previous_page())),
            ltk.Label(">")
                .addClass("button next")
                .on("click", ltk.proxy(lambda event: self.next_page())),
        ) \
        .addClass("container") \
        .appendTo(body)

        ltk.find(ltk.window) \
            .on("keydown", ltk.proxy(lambda event: self.handle_key(event.key))) \
            .on("resize", ltk.proxy(lambda event: self.resize_image()))

    def resize_image(self):
        """ Resize the image """
        self.image.css("left", (body.width() - self.image.width()) / 2)

    def handle_key(self, key):
        """ The user pressed a key """
        if key == "f":
            return ltk.window.document.body.requestFullscreen()
        if key in [ "k", "Backspace", "PageUp", "ArrowUp", "ArrowLeft"]:
            return self.previous_page()
        if key in [ " ", "j", "Enter", "PageDown", "ArrowDown", "ArrowRight"]:
            return self.next_page()
        if key == "Home":
            return self.render(1)
        if key == "End":
            return self.render(self.page_count)
        if key >= "1" and key <= "9":
            return self.render(int(key))
        print(f"You pressed {key}")

    def show_buttons(self):
        """ Show the buttons """
        ltk.find(".button").css("opacity", 1)
        ltk.schedule(self.hide_buttons, "hide buttons", 1)
        self.image.css("cursor", "pointer")

    def hide_buttons(self):
        """ Hide the buttons """
        ltk.find(".button").animate(ltk.to_js({
            "opacity": 0,
        }))
        self.image.css("cursor", "none")

    def previous_page(self):
        """ go to the previous page """
        self.render(self.index - 1)

    def next_page(self):
        """ go to the next page """
        self.render(self.index + 1)

    def render(self, index):
        """ show the page at the given index """
        self.index = max(min(index, self.page_count), 1)
        print("goto page", self.index)
        self.image.attr("src", f"slides/page-{self.index}.png")

Player(23)
