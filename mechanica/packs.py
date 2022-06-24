"""
Requirements for a Pack:
    - Pack folder should contain keys.json file which describing which keys are associated with which sound.
"""
import json
import pathlib
import sys
import threading
from pydub import AudioSegment
from pydub.playback import play
from io import StringIO


KEYMAPPING_FILE = pathlib.Path("keys.json")
PRESS = "press"
RELEASE = "release"
SOUND_ANCHORS = [PRESS, RELEASE]
DEFAULT_SOUND = "_DEFAULT"

def play_sound_with_threads(soundobj):
    thread = threading.Thread(target=lambda: play(soundobj))
    thread.start()

class Pack:
    def __init__(self, name, audio_dir, show_warnings=False) -> None:
        self.name = name
        self.audio_dir = audio_dir
        self.keymapping = {}

        if show_warnings:
            self.warn_buf = sys.stderr
        
        self.warn_buf = StringIO()

    def load_keymapping(self):
        with open(pathlib.Path(self.audio_dir) / KEYMAPPING_FILE) as f:
            keymapping = json.load(f)

        for anchor in SOUND_ANCHORS:
            try:
                for key, value in keymapping[anchor].items():
                    sound = AudioSegment.from_file(pathlib.Path(self.audio_dir) / value)
                    keymapping[anchor][key] = sound
            except IndexError:
                pass

        self.keymapping = keymapping
        
    
    def _key_util(self, key, anchor):
        try:
            play_sound_with_threads(self.keymapping[anchor][str(key)])
        except KeyError:
            try:
                play_sound_with_threads(self.keymapping[anchor][DEFAULT_SOUND])
            except KeyError:
                print(f"Warning: {anchor} sound for {key} key couldn't found.", file=self.warn_buf)

    def press_key(self, key):
        self._key_util(key, PRESS)

    def release_key(self, key):
        self._key_util(key, RELEASE)

    