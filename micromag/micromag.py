#!/usr/bin/env python3


import re
import numpy as np
import matplotlib.pyplot as plt
import argparse


class HysteresisCurve:

    def __init__(self, filename):
        with open(filename, "r", encoding="iso-8859-1") as fh:
            lines = map(lambda x: x.strip(), fh.readlines())

        self.params = {}
        param_regex = re.compile("^(.*)    +(.*)$")
        loop_regex_part = r"[+-][0-9.]{8}E[+-]\d\d"
        loop_regex = \
            re.compile("({0}),({0}),({0}),({0})".format(loop_regex_part))

        # Sections: -1 = before loop data; 0, 1, 2 = loop sections
        current_section = -1
        loop_rows = [[]]
        for line in lines:
            param_match = param_regex.fullmatch(line)
            if param_match is not None:
                self.params[param_match.group(1).strip()] = param_match.group(2)

            loop_match = loop_regex.fullmatch(line)
            if loop_match is not None:
                loop_rows[-1].append(list(map(float, loop_match.groups())))
                if current_section == -1:
                    current_section = 0

            if 0 <= current_section < 2 and line == "":
                # Loop sections are separated by blank lines.
                current_section += 1
                loop_rows.append([])

        self.loops = list(map(lambda x: np.array(x).transpose(), loop_rows))

    def plot(self):
        mass = float(self.params["Mass"])
        colors = ["blue", "black", "green"]
        for part in 0, 1, 2:
            plt.plot(self.loops[part][2], self.loops[part][3] / mass,
                     color=colors[part])


def main():
    args = argparse.ArgumentParser()
    args.add_argument("filename", type=str, nargs="+")
    opts = args.parse_args()
    curves = [HysteresisCurve(f) for f in opts.filename]
    for curve in curves:
        curve.plot()
    plt.show()


if __name__ == "__main__":
    main()
