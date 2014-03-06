iTunes Tag script
===

Small set of scripts to add tags to songs on iTunes.
Started by @carlosefonseca

To use as a Launchbar (Mac only) action (this is why I created this):

Create a link to the `addTags.py` script in the `~/Library/Application Support/LaunchBar/Actions folder`.
Example:
```bash
ln -s ~/your/code/folder/addTags.py ~/Library/Application\ Support/LaunchBar/Actions/Add\ Tags\ To\ Song.py
```

To work in Launchbar, the `addTags.py` script must be executable.

#Usage
Call the action and press `space` to allow passing arguments.
Pass unique prefixes to the tags you want to add (e.g. 'co j' for adding the tags :cool: and :jump:, but not 'c', because it is ambiguous between :cool: and :calm:) to add them to the current song

Pass nothing (don't press `space`) to list the tags of the current song

Configure available tags in the `tags.json` file (copy from `tags.json.sample`)
