import threading
import time


class VisualHelper:
    show_loading_bar = True

    def play_loading_animation(self, message):
        while self.show_loading_bar:
            for c in '|/-\\':
                print('\r' + message + c, end='', flush=True)
                time.sleep(0.1)

    def start_loading(self, message):
        self.show_loading_bar = True
        loading_thread = threading.Thread(target=self.play_loading_animation(message))
        loading_thread.start()
        return loading_thread

    def stop_loading(self):
        self.show_loading_bar = False
        print('\r' + 'Done!')

    def print_information(self, message):
        print("==== " + message + " ====")
