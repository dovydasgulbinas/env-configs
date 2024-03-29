#!/bin/bash

# If you want Touchegg to handle 2 finger gestures, deactivate
# 2 finger gestures in synaptics:
synclient TapButton2=1
synclient TapButton1=1

# Same for 3 finger gestures:
synclient TapButton3=1

# Same for 2 finger clicks:
synclient ClickFinger2=0

# And for 3 finger clicks:
synclient ClickFinger3=0

# If Touchegg shall take care for scrolling, 
# deactivate it in synaptics:
#synclient HorizTwoFingerScroll=0
#synclient VertTwoFingerScroll=0


synclient PalmDetect=1
synclient PalmMinWidth=5
synclient PalmMinZ=100
synclient HorizTwoFingerScroll=1
synclient HorizHysteresis=14
synclient VertHysteresis=14

