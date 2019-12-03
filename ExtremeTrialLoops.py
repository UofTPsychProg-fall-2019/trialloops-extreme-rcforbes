#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height')

instr = visual.TextStim(win, color = 'black', height=.05, text="""Rachel Forbes PS6
Extreme Trial Loops

Hope you like cute pets! In this experiment you will be rating different pets on cuteness.

To make a rating click somewhere on the line. To accept your rating, either press 'enter' or click the glowing button.

Press any key to begin (or escape to quit).""")

event.clearEvents()
instr.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
ratingScale = visual.RatingScale(win, textColor = 'black', lineColor = 'black', choices=['cute', 'very cute', 'cutest'], pos=(0, -.45))
text = visual.TextStim(win, text='How cute is this picture?', color = 'black', pos=(0,-.4), height=.05)

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
imageList = ['Pics/Gizmo.jpg', 'Pics/Minnie.jpg', 'Pics/Artemis.jpg']
data = []
alldata = []
bigText = visual.TextStim(win, text='Big value!', color = 'black', height=.05)
smallText = visual.TextStim(win, text='Small value!', color = 'black', height=.05)
midText = visual.TextStim(win, text='Middle value!', color = 'black', height=.05)

rating = ratingScale.getRating()
history = ratingScale.getHistory()
ratingText = visual.TextStim(win, text= print(rating), color = 'black', height=.05)
hisText = visual.TextStim(win, text= history, color = 'black', height=.05)
# make your loop
for image in imageList:
    x, y = ratingScale.win.size
    text = visual.SimpleImageStim(win=win, image=image, units='pix', pos=[0, y//7])
    ratingScale.reset()
    event.clearEvents()
    while ratingScale.noResponse:
         text.draw()
         ratingScale.draw()
         win.flip()
         if event.getKeys(['escape']):
             core.quit()
    data.append([ratingScale.getRating()])
    alldata.append([image, ratingScale.getRating(), ratingScale.getRT()])
    win.flip()
    if data[-1][0] == 'cutest':
        bigText.draw()
    elif data[-1][0] == 'cute':
        smallText.draw()
    else:
        midText.draw()
    win.flip()
    core.wait(1)
summaryText = visual.TextStim(win, text = """Here is a summary of your responses:""", color = 'black', pos=(0, 0.25), height = .05)

GizmoText = visual.TextStim(win, text = 'Rating and reaction time for Trial 1: Gizmo', color = 'black', pos=(-0.2, 0.1), height = .04)
MinnieText = visual.TextStim(win, text = 'Rating and reaction time for Trial 2: Minnie', color = 'black', pos=(-0.2, 0.0), height = .04)
ArtemisText = visual.TextStim(win, text = 'Rating and reaction time for Trial 3: Artemis', color = 'black', pos=(-0.2, -0.1), height = .04)

Gizmo = visual.TextStim(win, text= alldata[0][1:3], color = 'red', pos = (0.35, 0.1),height=.045)
Minnie = visual.TextStim(win, text= alldata[1][1:3], color = 'red', pos = (0.35, 0),height=.045)
Artemis = visual.TextStim(win, text= alldata[2][1:3], color = 'red', pos = (0.35, -0.1),height=.045)

next = visual.TextStim(win, color = 'black', pos = (0, -0.35), height=.05, text='Press any key to continue')
next.draw()
summaryText.draw()
GizmoText.draw()
MinnieText.draw()
ArtemisText.draw()
Gizmo.draw()
Minnie.draw()
Artemis.draw()

win.flip()
if 'escape' in event.waitKeys():
    core.quit()

total = visual.TextStim(win, color = 'black', pos = (0, 0.1), height=.05, text="""Total Cuteness Score:

Big values have a score of 3
Middle values have a score of 2
Small values have a score of 1

Below is your cuteness response score out of 9:""")

cuteCount = 0
for i in range(len(data)):
    if data[i] == ['cutest']:
        cuteCount = cuteCount + 3
    elif data[i] == ['very cute']:
        cuteCount = cuteCount + 2
    elif data[i] == ['cute']:
        cuteCount = cuteCount + 1


count = visual.TextStim(win, text = cuteCount, color = 'red', pos = (0, -0.2), height=.05)
next = visual.TextStim(win, color = 'black', pos = (0, -0.35), height=.05, text='Press any key to continue')
next.draw()
total.draw()
count.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()

    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater 
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!

close = visual.TextStim(win, color = 'black', height=.05, text="""Rachel Forbes PS6
Extreme Trial Loops

You have rated all my pets! 
Press any key to quit. """)

event.clearEvents()
close.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly
win.close()
