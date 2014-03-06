#!/usr/bin/python
import sys
import subprocess
import os

#To be used as a Launchbar action
#Usage: Pass as command line args unique abbreviations of the tags to add, separated by spaces
#       e.g. 'ca' or 'cal' for :calm: and 'co' or 'cool' for :cool:, but 'c' won't be recognized as neither.
#       pass 'reset' to reset the tags

SCRIPT_FOLDER = os.path.dirname(os.path.realpath(__file__))
SCRIPT_PROGRAM = 'osascript'
RESET_SCRIPT = 'resetTags.scpt'
ADD_TAG_SCRIPT = 'AddTag.scpt'
TAG_PATTERN = ':{}:'

TAGS = [
    'cool',
    'jump',
    'feel',
    'rise',
    'heavy',
    'calm',
    'happy',
    'sad',
    'evil',
    'dark',
    'dance',
    'beat',
    'instrument',
    'lol',
    'not',
    'game'
]

def main(args):
    split_args = [actual_arg for sublist in [each_arg.split(' ') for each_arg in args] for actual_arg in sublist]

    #Launchbar passes args as one string only. We need to split!
    if 'reset' in split_args:
        subprocess.call([SCRIPT_PROGRAM, os.path.join(SCRIPT_FOLDER, RESET_SCRIPT)])
    else:
        tags_to_add = []
        for prefix in split_args:

            matches = [word for word in TAGS if word.startswith(prefix)]
            if len(matches) == 1: #EXACTLY 1 match
                tags_to_add.append(TAG_PATTERN.format(matches[0]))
            #else, warn the user

        if tags_to_add != []:
            for tag in tags_to_add: #TODO: change the script so it accepts multiple tags at once
                subprocess.call([SCRIPT_PROGRAM, os.path.join(SCRIPT_FOLDER, ADD_TAG_SCRIPT), tag])


if __name__ == '__main__':
    main(sys.argv[1:])
