class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        return "Current floor: {}".format(self.current)
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current + 1 <= self.top:
            self.current = self.current + 1
        return self.current
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current - 1 >= self.bottom:
            self.current = self.current - 1
        return self.current
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        return self.current

elevator = Elevator(-1, 10, 0)
