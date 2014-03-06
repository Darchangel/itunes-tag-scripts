#!/usr/bin/python
import sys
import subprocess
from os import path
import json

#To be used as a Launchbar action
#Usage: Pass as command line args unique abbreviations of the tags to add, separated by spaces
#       e.g. 'ca' or 'cal' for :calm: and 'co' or 'cool' for :cool:, but 'c' won't be recognized as neither.
#       pass 'reset' to reset the tags

SCRIPT_FOLDER = path.dirname(path.realpath(__file__))
SCRIPT_PROGRAM = 'osascript'
RESET_SCRIPT = 'resetTags.scpt'
ADD_TAG_SCRIPT = 'AddTag.scpt'
LIST_TAGS_SCRIPT = 'ListTags.scpt'
FILTER_SCRIPT = 'filter.py'

TAGS_FILE = 'tags.json'

TAG_REGEX = '[a-zA-Z0-9-_]+'

def main(args):

    #Launchbar passes args as one string only. We need to split!
    split_args = [actual_arg for sublist in [each_arg.split(' ') for each_arg in args] for actual_arg in sublist]

    if 'reset' in split_args:
        subprocess.call([SCRIPT_PROGRAM, path.join(SCRIPT_FOLDER, RESET_SCRIPT)])
    else:
        json_file = open(path.join(SCRIPT_FOLDER, TAGS_FILE))
        json_data = json.load(json_file)

        TAG_PATTERN = json_data['pattern']
        TAGS = json_data['tags']

        if len(args) == 0: #No arguments: list tags
            regex_pattern = '(' + TAG_PATTERN.format(TAG_REGEX) + ')'
            subprocess.call([SCRIPT_PROGRAM, path.join(SCRIPT_FOLDER, LIST_TAGS_SCRIPT), path.join(SCRIPT_FOLDER, FILTER_SCRIPT), regex_pattern])


        tags_to_add = []
        for prefix in split_args:

            matches = [word for word in TAGS if word.startswith(prefix)]
            if len(matches) == 1: #EXACTLY 1 match
                tags_to_add.append(TAG_PATTERN.format(matches[0]))
            #else, warn the user

        if tags_to_add != []:
            for tag in tags_to_add: #TODO: change the script so it accepts multiple tags at once
                subprocess.call([SCRIPT_PROGRAM, path.join(SCRIPT_FOLDER, ADD_TAG_SCRIPT), tag])


if __name__ == '__main__':
    main(sys.argv[1:])
