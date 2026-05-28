import time

class ScreenTracker:

    def __init__(self):

        self.start_time = time.time()

    def get_screen_time(self):

        current = time.time()

        total_seconds = int(current - self.start_time)

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return hours, minutes, seconds