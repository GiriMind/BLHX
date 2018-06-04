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
CCC_BGR2BGRA = 0
CCC_RGB2RGBA = CCC_BGR2BGRA
CCC_BGRA2BGR = 1
CCC_RGBA2RGB = CCC_BGRA2BGR

# Image matchTemplate method
MTM_SQDIFF = 0
MTM_SQDIFF_NORMED = 1
MTM_CCORR = 2
MTM_CCORR_NORMED = 3
MTM_CCOEFF = 4
MTM_CCOEFF_NORMED = 5

# Image rectangle lineType
RLT_FILLED = -1
RLT_LINE_4 = 4
RLT_LINE_8 = 8
RLT_LINE_AA = 16

# Image normalize normType
NNT_MINMAX = 32
