# See https://github.com/argosopentech/argos-translate-gui/blob/main/bin/argos-translate-gui

import os
os.environ['ARGOS_PACKAGES_DIR'] = 'packages'
os.environ['ARGOS_DEVICE_TYPE'] = 'cpu'

from argostranslategui import gui

gui.main()