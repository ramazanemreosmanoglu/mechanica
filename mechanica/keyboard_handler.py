from pynput import keyboard


class KeyboardHandler:
    def __init__(self, pack) -> None:
        self.pressing_keys = []
        self.pack = pack

    def on_press(self, key):
        if key in self.pressing_keys:
            return
        
        self.pressing_keys.append(key)
        try:
            self.pack.press_key(str(key.char))
        except AttributeError:
            self.pack.press_key(str(key))

    def on_release(self, key):
        self.pack.release_key(str(key)) 
        try:
            self.pressing_keys.remove(key)
        except ValueError:
            pass


def main(pack):
    handler = KeyboardHandler(pack)

    try:

        with keyboard.Listener(
                on_press=handler.on_press,
                on_release=handler.on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        exit(0)

