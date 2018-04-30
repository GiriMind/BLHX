# coding: utf-8

# Image read flags
RF_UNCHANGED = -1
RF_GRAYSCALE = 0
RF_COLOR = 1

# Image type
IT_8UC1 = 0
IT_8SC1 = 1
IT_16UC1 = 2
IT_16SC1 = 3
IT_32SC1 = 4
IT_32FC1 = 5
IT_64FC1 = 6
IT_8UC2 = 8
IT_8UC3 = 16
IT_8UC4 = 24

# Image cvtColor code
COLOR_BGR2BGRA = 0
COLOR_RGB2RGBA = COLOR_BGR2BGRA
COLOR_BGRA2BGR = 1
COLOR_RGBA2RGB = COLOR_BGRA2BGR

# Image matchTemplate method
TM_SQDIFF = 0
TM_SQDIFF_NORMED = 1
TM_CCORR = 2
TM_CCORR_NORMED = 3
TM_CCOEFF = 4
TM_CCOEFF_NORMED = 5

# Image rectangle lineType
FILLED = -1
LINE_4 = 4
LINE_8 = 8
LINE_AA = 16

# Image normalize normType
NORM_MINMAX = 32
