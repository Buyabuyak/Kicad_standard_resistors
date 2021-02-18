#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

import csv

# well, It aint beautifull but it should work
# fell free to fill the arrays with whatever you need in order to create your custom generic resistor lib
# the naming and description comes from eurocircuit, it should be compatible but it's untested...

# E192 + E24 series, cannot compute it cause there's f*****g exceptions
# from https://en.wikipedia.org/wiki/E_series_of_preferred_numbers

# values = [1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11,
#          1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24, 1.26,
#          1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42,
#          1.43, 1.45, 1.47, 1.49, 1.50, 1.52, 1.54, 1.56, 1.58, 1.60,
#          1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.80,
#          1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2.00, 2.03,
#          2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.20, 2.21, 2.23, 2.26,
#          2.29, 2.32, 2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55,
#          2.58, 2.61, 2.64, 2.67, 2.70, 2.71, 2.74, 2.77, 2.80, 2.84,
#          2.87, 2.91, 2.94, 2.98, 3.00, 3.01, 3.05, 3.09, 3.12, 3.16,
#          3.20, 3.24, 3.28, 3.30, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52,
#          3.57, 3.60, 3.61, 3.65, 3.70, 3.74, 3.79, 3.83, 3.88, 3.90,
#          3.92, 3.97, 4.02, 4.07, 4.12, 4.17, 4.22, 4.27, 4.30, 4.32,
#          4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70, 4.75, 4.81, 4.87,
#          4.93, 4.99, 5.05, 5.10, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42,
#          5.49, 5.56, 5.60, 5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04,
#          6.12, 6.19, 6.20, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73,
#          6.80, 6.81, 6.90, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.50,
#          7.59, 7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.20, 8.25, 8.35,
#          8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.09, 9.10, 9.20, 9.31,
#          9.42, 9.53, 9.65, 9.76, 9.88]

# E24
# values = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6,
#           1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
#           3.3, 3.6, 3.9, 4.3, 4.7, 5.1,
#           5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

# E24 + E96
values = [1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.20, 1.21,
          1.24, 1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54,
          1.58, 1.60, 1.62, 1.65, 1.69, 1.74, 1.78, 1.80, 1.82, 1.87,
          1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.20, 2.21, 2.26, 2.32,
          2.37, 2.40, 2.43, 2.49, 2.55, 2.61, 2.67, 2.70, 2.74, 2.80,
          2.87, 2.94, 3.00, 3.01, 3.09, 3.16, 3.24, 3.30, 3.32, 3.40,
          3.48, 3.57, 3.60, 3.65, 3.74, 3.83, 3.90, 3.92, 4.02, 4.12,
          4.22, 4.30, 4.32, 4.42, 4.53, 4.64, 4.70, 4.75, 4.87, 4.99,
          5.10, 5.11, 5.23, 5.36, 5.49, 5.60, 5.62, 5.76, 5.90, 6.04,
          6.19, 6.20, 6.34, 6.49, 6.65, 6.80, 6.81, 6.98, 7.15, 7.32,
          7.50, 7.68, 7.87, 8.06, 8.20, 8.25, 8.45, 8.66, 8.87, 9.09,
          9.10, 9.31, 9.53, 9.76]

# used to set the decades
multipliers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]

# used the set the package size and the matching power(s)
sizes = {
    "0201_0603": ["1/20W"],
    "0402_1005": ["1/16W"],
    "0603_1608": ["1/10W"],
    "0805_2012": ["1/8W" ],
    "1206_3216": ["1/4W" ],
    "1210_3225": ["1/2W" ],
    "1218_3246": ["1/1W" ],
    "2010_4516": ["3/4W" ],
    "2512_6332": ["1W"   ]
}

# used the set the tolerance(s)
tolerances = ["1.0%"]

filename = "GenericResSMD"

if __name__ == "__main__":

    with open('%s.lib' % filename, 'w') as lib:
        with open('%s.dcm' % filename, 'w') as dcm:

            lib.writelines(
                ["EESchema-LIBRARY Version 2.4\n", "#encoding utf-8\n", "#\n"])
            dcm.writelines(["EESchema-DOCLIB  Version 2.0\n", "#\n"])

            # iterate over everything
            for package, powers in sizes.items():
                for power in powers:
                    for tolerance in tolerances:
                        for value in values:
                            for multiplier in multipliers:
                                
                                # create the resistor value from the values and decade
                                # transform it to a human string with the correct "decade corresponding metric system letter"
                                val = ""
                                if multiplier <= 100:
                                    val = "%.2f" % (value * multiplier)
                                    val = val.replace('.', 'R')
                                    val = val.rstrip('0')
                                elif multiplier <= 100000:
                                    val = "%.2f" % (value * multiplier / 1000)
                                    val = val.replace('.', 'K')
                                    val = val.rstrip('0')
                                else:
                                    val = "%.2f" % (
                                        value * multiplier / 1000000)
                                    val = val.replace('.', 'M')
                                    val = val.rstrip('0')
                                name = "GPR%s%s" % (
                                    package[0:4] ,val, )
                                    # creates the symbol
                                lib.writelines([
                                    "#\n",
                                    "# %s" % name,
                                    "#\n",
                                    "DEF %s R 0 0 N Y 1 F N\n" % name,
                                    "F0 \"R\" 80 0 50 V V C CNN\n",
                                    "F1 \"%s\" 0 0 50 V I C CNN\n" % name,
                                    "F2 \"Resistor_SMD:R_%sMetric\" -70 0 50 V I C CNN\n" % package,
                                    "F3 \"\" 0 0 50 H I C CNN\n",
                                    "F4 \"%s\" 0 0 50 H V C CNN \"Resistance\"\n" % val,
                                    "F5 \"%s\" 0 0 25 H V C CNN \"Package\"\n" % package[:4],
                                    "F6 \"%s\" 0 0 25 H I C CNN \"Tolerance\"\n" % tolerance,
                                    "F7 \"%s\" 0 0 25 H I C CNN \"Power\"\n" % power,
                                    "$FPLIST\n",
                                    " R_*\n",
                                    "$ENDFPLIST\n",
                                    "DRAW\n",
                                    "S -40 -100 40 100 0 1 10 N\n",
                                    "X ~ 1 0 150 50 D 50 50 1 1 P\n",
                                    "X ~ 2 0 -150 50 U 50 50 1 1 P\n",
                                    "ENDDRAW\n",
                                    "ENDDEF\n"
                                ])
                                # do the same for the complementary file
                                dcm.writelines([
                                    "$CMP %s\n" % name,
                                    "D Resistor\n",
                                    "K %s, %s, Res %sOhm, %s, %s,\n" % (
                                    package[:4], package[5:], val, tolerance, power),
                                    "F ~\n",
                                    "$ENDCMP\n",
                                    "#\n"

                                ])

            # the end of the line
            lib.writelines(["#End Library\n"])
            dcm.writelines(["#End Doc Library\n"])
