#!/usr/bin/python
import sys
import subprocess

#To be used as a Launchbar action
#Usage: Pass as command line args unique abbreviations of the tags to add, separated by spaces
#       e.g. 'ca' or 'cal' for :calm: and 'co' or 'cool' for :cool:, but 'c' won't be recognized as neither.
#       pass 'reset' to reset the tags

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
    'not'
]

def main(args):
    tags_to_add = []

    if 'reset' in args:
        subprocess.call([SCRIPT_PROGRAM, RESET_SCRIPT])
    else:
        for prefix in args:
            matches = [word for word in TAGS if word.startswith(prefix)]
            if len(matches) == 1: #EXACTLY 1 match
                tags_to_add.append(TAG_PATTERN.format(matches[0]))
            #else, warn the user

        if tags_to_add != []:
            for tag in tags_to_add: #TODO: change the script so it accepts multiple tags at once
                print(" ".join([SCRIPT_PROGRAM, ADD_TAG_SCRIPT, tag]))
                subprocess.call([SCRIPT_PROGRAM, ADD_TAG_SCRIPT, tag])


if __name__ == '__main__':
    main(sys.argv[1:])
