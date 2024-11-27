class Cow:
    def __init__(self, name):
        self.name = name
        self.image = None

    @property
    def get_name(self):
        return self.name

    @property
    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image
