import psutil

class InternetTracker:

    def __init__(self):

        self.last_sent = psutil.net_io_counters().bytes_sent
        self.last_recv = psutil.net_io_counters().bytes_recv

    def get_usage(self):

        current = psutil.net_io_counters()

        new_sent = current.bytes_sent
        new_recv = current.bytes_recv

        upload_speed = (new_sent - self.last_sent) / 1024
        download_speed = (new_recv - self.last_recv) / 1024

        self.last_sent = new_sent
        self.last_recv = new_recv

        return {
            "upload_speed": round(upload_speed, 2),
            "download_speed": round(download_speed, 2),
            "total_upload_mb": round(new_sent / (1024 * 1024), 2),
            "total_download_mb": round(new_recv / (1024 * 1024), 2)
        }