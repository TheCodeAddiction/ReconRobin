import threading
import time


class VisualHelper:
    show_loading_bar = True

    def play_loading_animation(self):
        while self.show_loading_bar:
            for c in '|/-\\':
                print('\r' + 'Loading please wait ' + c, end='', flush=True)
                time.sleep(0.1)

    def start_loading(self):
        self.show_loading_bar = True
        loading_thread = threading.Thread(target=self.play_loading_animation)
        loading_thread.start()
        return loading_thread

    def stop_loading(self):
        self.show_loading_bar = False
        print('\r' + 'Done!')
