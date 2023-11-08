import argparse
import os.path
import re
import math


class ColorReplacer():
    def __init__(self, data_path, protocol, color_mode):
        self.data_path = data_path
        self.color_mode = color_mode
        if protocol == "syntax":
            self.master_colors = [
                "#555c61",
                "#adafb1",
                "#c6c7c8",
                "#0d4662",
                "#07628f",
                "#017dbb",
                "#bb4542",
                "#bb6742",
                "#bc955c",
                "#3d683b",
                "#647c50",
                "#4a3957"
            ]
        else: # (if protocol == "program")
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
        if len(color) == 7:
            return (r, g, b)   
        else:
            a = int(color[7:9], 16)
            return(r, g, b, a)
    
    def __rofi2rgb(self, color):
        assert type(color) is str # "(r, g, b, a % )"
        return tuple(list(map(lambda x: int(x), re.findall("[0-9]+", color))))

    def __rgb2rofi(self, color):
        assert type(color) is tuple # (r,g,b) or (r,g,b,a)
        assert (len(color) == 3 or len(color) == 4)
        if len(color) == 3:
            r,g,b = color
            return "( {r}, {g}, {b}, 100 % )".format(r=r, g=g, b=b)
        else:
            r,g,b,a = color
            return "( {r}, {g}, {b}, {a} % )".format(r=r, g=g, b=b, a=a)

    def __hex2rofi(self, color):
        assert type(color) is str # "#ffffff" or "#ffffffff"
        return self.__rgb2rofi(self.__hex2rgb(color))

    def __distance(self, color1, color2):
        return math.sqrt(abs(color1[0]-color2[0])**2 +
        abs(color1[1]-color2[1])**2 +
        abs(color1[2]-color2[2])**2)

    def __find_closest_color(self, color):
        if self.color_mode == "hex":
            color_tuple = self.__hex2rgb(color)
        else:
            color_tuple = self.__rofi2rgb(color)
        distances = []
        for master_color in self.master_colors:
            master_color_tuple = self.__hex2rgb(master_color)
            distances.append(self.__distance(color_tuple, master_color_tuple))
        if self.color_mode == "hex":
            if len(color) == 7:
                return self.master_colors[distances.index(min(distances))]
            else:
                return self.master_colors[distances.index(min(distances))] + color[-2:]
        else:
            return self.__hex2rofi(self.master_colors[distances.index(min(distances))])

    def replace(self):
        data_colors = []

        with open(data_path, 'r') as data:
            if color_mode == "hex":
                for line in data.readlines():
                    colors = re.findall("\#[A-Fa-f0-9]{6}", line)
                    colors += re.findall("\#[A-Fa-f0-9]{8}", line)
                    for color in colors:
                        data_colors.append(color)
            else:
                for line in data.readlines():
                    colors = re.findall("\( [0-9]*, [0-9]*, [0-9]*, [0-9]* \% \)", line)
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
    parser.add_argument('-p', '--protocol', dest='protocol', type=str, required=False)
    parser.add_argument('-m', '--color-mode', dest='color_mode', type=str, required=False)
    args = parser.parse_args()

    # You can access args with the dot operator like so:
    data_path = os.path.expanduser(args.path)
    protocol = ""
    if args.protocol is None:
        protocol = "program" # default if nothing is specified
    elif args.protocol in ["program", "syntax"]:
        protocol = args.protocol
    else:
        raise(ValueError("Invalid Argument: please set protocol to either 'syntax' or 'program'"))
    color_mode = ""
    if args.color_mode is None:
        color_mode = "hex" # default if nothing is specified
    elif args.color_mode in ["hex", "rofi"]:
        color_mode = args.color_mode
    else:
        raise(ValueError("Invalid Argument: please set protocol to either 'syntax' or 'program'"))

    print("Running replacer of type: {p}\n and color mode: {c}".format(p=protocol, c = color_mode))
    replacer = ColorReplacer(data_path, protocol, color_mode)
    replacer.replace()