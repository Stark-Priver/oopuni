class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def update(self, target):
        self.x = target.x - self.width // 2
        self.y = target.y - self.height // 2

    def apply(self, entity):
        return (entity.x - self.x, entity.y - self.y)

    def apply_rect(self, rect):
        return rect.move(-self.x, -self.y)

    def apply_xy(self, x, y):
        return (x - self.x, y - self.y)

    def get_offset(self):
        return (self.x, self.y)
