from . import visual_helper
import os

animation = visual_helper


def write_list_to_file(filename, array, message):
    file_path = os.path.join("Output", filename)
    with open(file_path, "w") as f:
        animation.print_information(message)
        for data in array:
            f.write(data + "\n")
        f.close()
