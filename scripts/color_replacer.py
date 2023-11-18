'''
Written by John Mays.
Free for any use covered under MIT License.
Description:
    This script is for the purpose of parsing config files (in a text format)
    and altering all of the colors in the file to be one of the colors in a color
    palette.

Functionality:
    Pass a text file to this script, then it will look through the file for colors
    of a specified format (e.g. hex (default)) and replace them with a color from
    the palette that is the least distance away.  Once it is finished, it will
    save the file.

Instructions:
    Run the script as so:
        python color_replacer.py <path>
    The path is mandatory.
    Run with -h argument for more information on arguments and options.

'''

import argparse
import os.path
import re
import math

class ColorReplacer():
    def __init__(self, data_path, protocol, color_mode):
        self.data_path = data_path
        self.color_mode = color_mode
        if protocol == "syntax":
            # a color list for syntax highlighting (no dark greys)
            self.master_colors = [
                # "#020303",
                # "#03100f",
                "#032825",
                # "#031c1a",
                "#023737",
                "#027873",
                "#046458",
                "#02aa9c",
                "#01cfc0",
                "#cefbfe",
                "#99f8f8",
                #
                "#ab87c3",
                "#bd293c",
                "#ff8753",
                "#ff9d6d",
                "#ffe68e"
            ]
        else: # (if protocol == "program")
            # a color list for programs in general (grays, but no greens)
            self.master_colors = [
                "#020303",
                "#03100f",
                "#032825",
                "#031c1a",
                "#023737",
                "#027873",
                "#046458",
                "#02aa9c",
                "#01cfc0",
                "#cefbfe",
                "#99f8f8"
            ]
     
    def __hex2rgb(self, color: str) -> tuple:
        '''
            @ param: color in hex format (w/ or w/o alpha)
                e.g. "#ffffff", "#ffffff00"
            @ return: color in tuple (r,g,b) or (r,g,b,a) format
         '''
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
    
    def __rofi2rgb(self, color:str) -> tuple:
        '''
            @ param: color in rofi format (as str): "( r, g, b, a % )"
            @ return: color in tuple (r,g,b) or (r,g,b,a) format
        '''
        assert type(color) is str # "( r, g, b, a % )"
        return tuple(map(lambda x: int(x), re.findall("[0-9]+", color)))

    def __rgb2rofi(self, color:tuple) -> str:
        '''
            @ param: color in tuple (r,g,b) or (r,g,b,a) format
            @ return: color in rofi format (as str): "( r, g, b, a % )"
        '''
        assert type(color) is tuple # (r,g,b) or (r,g,b,a)
        assert (len(color) == 3 or len(color) == 4)
        if len(color) == 3:
            r,g,b = color
            return "( {r}, {g}, {b}, 100 % )".format(r=r, g=g, b=b)
        else:
            r,g,b,a = color
            return "( {r}, {g}, {b}, {a} % )".format(r=r, g=g, b=b, a=a)

    def __hex2rofi(self, color:str) -> str:
        '''color = ""
            @ param: color in hex format (w/ or w/o alpha)
                e.g. "#ffffff", "#ffffff00+++"
            @ return: color in rofi format (as str): "( r, g, b, a % )"
        '''
        assert type(color) is str
        return self.__rgb2rofi(self.__hex2rgb(color))

    def __distance(self, color1:tuple, color2:tuple)->float:
        '''
            Finds the euclidean distance between two colors
            (Only considers r, g, b, and not alpha)
            @param color1: color in rgb(a) format
            @param color2: color in rbg(a) format
            @return: numeric distance value
        '''
        return math.sqrt(
            abs(color1[0]-color2[0])**2 +
            abs(color1[1]-color2[1])**2 +
            abs(color1[2]-color2[2])**2
        )

    def __find_closest_color(self, color):
        '''
            Finds the color in the palette that is closest to the input color,
            and returns it.  Maintains alpha if there is one in the input color.
            @param: color in any format
            @return: matching color from palette in same format.
        '''
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
        '''
            This method scans through the input file, looks for colors in
            the specified format, then replaces them and closes the file.
        '''
        data_colors = set([])
        # opens file, scans for existing colors, adds to list.
        with open(data_path, 'r') as data:
            if color_mode == "hex":
                for line in data.readlines():
                    colors = re.findall("\#[A-Fa-f0-9]{6}", line)
                    colors += re.findall("\#[A-Fa-f0-9]{8}", line)
                    for color in colors:
                        data_colors.add(color)
            else:
                for line in data.readlines():
                    colors = re.findall("\( [0-9]*, [0-9]*, [0-9]*, [0-9]* \% \)", line)
                    for color in colors:
                        data_colors.add(color)

        replacement_colors = [] # not a set: there may be duplicate replacement colors

        data_colors = list(data_colors)
        
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
    parser.add_argument('path', metavar='PATH', type=str,
                        help='The path to the file that will be parsed & have its colors replaced.')
    parser.add_argument('-p', '--palette', dest='protocol', type=str, required=False,
                        help='Color palette. Accepted: \"program\", \"syntax\".')
    parser.add_argument('-f', '--color-format', dest='color_mode', type=str, required=False,
                        help='The format colors are written in. Accepted: \"hex\", \"rofi\".')
    args = parser.parse_args()

    data_path = os.path.expanduser(args.path)

    protocol = ""
    if args.protocol is None:
        protocol = "program" # default if nothing is specified
    elif args.protocol in ["program", "syntax"]:
        protocol = args.protocol
    else:
        raise(ValueError("Invalid Argument: please set palette to either \"syntax\" or \"program\". "))
    color_mode = ""
    if args.color_mode is None:
        color_mode = "hex" # default if nothing is specified
    elif args.color_mode in ["hex", "rofi"]:
        color_mode = args.color_mode
    else:
        raise(ValueError("Invalid Argument: please set format to either \"hex\" or \"rofi\". "))

    print("Running replacer of type: {p}\nand color format: {c}".format(p=protocol, c = color_mode))
    replacer = ColorReplacer(data_path, protocol, color_mode)
    replacer.replace()