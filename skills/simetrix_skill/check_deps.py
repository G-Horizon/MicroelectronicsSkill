import sys

try:
    import pywinauto
    print('pywinauto: OK')
except ImportError as e:
    print(f'pywinauto: {e}')

try:
    import matplotlib
    print('matplotlib: OK')
except ImportError as e:
    print(f'matplotlib: {e}')

try:
    import numpy
    print('numpy: OK')
except ImportError as e:
    print(f'numpy: {e}')