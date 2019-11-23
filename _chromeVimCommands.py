from dragonfly import (
    AppContext,
    Grammar,
    MappingRule,
    Key
)

class ChromeRule(MappingRule):

    mapping = {
        #Scrolling
        "scroll up":        Key("u"),
        "scroll down":      Key("d"),
        "scroll right":     Key("l:down/5"),
        "scroll left":      Key("h:down/5"),
        "scroll top":       Key("g, g"),
        "scroll bottom":    Key("G"),
        #Url Navigation
        "link new":         Key("F"),
        "link same":        Key("f"),
        "reload":           Key("r"),
        "copy URL":         Key("y, f"),
        #Tab Navigation
        "tab left":         Key("J"),
        "tab right":        Key("K"),
        "tab first":        Key("g, 0"),
        "tab last":         Key("g, $"),
        "tab new":          Key("t"),
        "tab close":        Key("ctrl:down, w, ctrl:up"),
        "tab restore":      Key("X"),
        "tab search":       Key("T"),
        #Marks
        "mark set":         Key("m, a"),
        "mark go":          Key("`, a"),
        "mark back":        Key("`, `"),
        #History
        "history back":     Key("H"),
        "history forward":  Key("L")
    }

# context = AppContext(executable="chrome.exe")
# grammar = Grammar("Chrome", context=context)
grammar = Grammar("Chrome")
grammar.add_rule(ChromeRule())
grammar.load()