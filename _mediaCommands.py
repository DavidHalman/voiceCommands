from dragonfly import (
    Grammar,
    MappingRule,
    Key
)

class MediaRule(MappingRule):

    mapping = {
        #Scrolling
        "media (play | pause)":     Key("playpause"),
        "media next":               Key("tracknext"),
        "media (prev | previous)":  Key("trackprev"),
        "volume mute":              Key("volumemute"),
        "volume up":                Key("volumeup"),
        "volume down":              Key("volumedown")
    }

grammar = Grammar("Media")
grammar.add_rule(MediaRule())
grammar.load()