import pygetwindow as gw

def get_active_app():

    try:

        window = gw.getActiveWindow()

        if window:
            return window.title

        return "No Active Window"

    except Exception as e:

        return "Unavailable"