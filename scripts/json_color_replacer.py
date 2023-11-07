import argparse
import os.path
import re
import math


class ColorReplacer():
    def __init__(self, data_path):
        self.data_path = data_path
        self.master_colors = [
            "#171b1c",
            "#24282a",
            "#3c4549",
            "#555c61",
            "#adafb1",
            "#c6c7c8",
            "#0d4662",
            "#07628f",
            "#017dbb",
            "#bb4542",
            "#bb6742",
            "#bc955c"
        ] 
     
    def __hex2rgb(self, color):
        assert type(color) is str
        assert (len(color) == 7 or len(color) == 9) and color.startswith("#")
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        return (r, g, b)   
    
    def __distance(self, color1, color2):
        return math.sqrt(abs(color1[0]-color2[0])**2 +
        abs(color1[1]-color2[1])**2 +
        abs(color1[2]-color2[2])**2)

    def __find_closest_color(self, color):
        color = self.__hex2rgb(color)
        distances = []
        for master_color in self.master_colors:
            master_color = self.__hex2rgb(master_color)
            distances.append(self.__distance(color, master_color))
        return self.master_colors[distances.index(min(distances))]

    def replace(self):
        data_colors = []

        with open(data_path, 'r') as data:
            for line in data.readlines():
                colors = re.findall("\#[A-Fa-f0-9]{6}", line)
                colors += re.findall("\#[A-Fa-f0-9]{8}", line)
                for color in colors:
                    data_colors.append(color)

        data_colors = list(set(data_colors))
        replacement_colors = []

        for color in data_colors:
            replacement_colors.append(self.__find_closest_color(color))

        for i in range(len(replacement_colors)):
            with open(data_path, 'r') as data:
                data_str = data.read()
                data_str = data_str.replace(data_colors[i], replacement_colors[i])
            with open(data_path, 'w') as data:
                data.write(data_str)


if __name__ == '__main__':
    """
    Main method.  
    
    Parses run arguments.
    """

    # Set up argparse arguments
    parser = argparse.ArgumentParser(description='Run color replacement.')
    parser.add_argument('path', metavar='PATH', type=str, help='The path to the file that will be parsed & have its colors replaced.')
    args = parser.parse_args()

    # You can access args with the dot operator like so:
    data_path = os.path.expanduser(args.path)

    replacer = ColorReplacer(data_path)
    replacer.replace()