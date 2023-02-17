from . import visual_helper

animation = visual_helper.VisualHelper()


def write_list_to_file(filename, array, message):
    f = open(filename, "w")
    animation.print_information(message)
    for data in array:
        f.write(data + "\n")
    f.close()
