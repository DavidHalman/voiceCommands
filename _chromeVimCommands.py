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
        "tab left":         Key("ctrl:down, shift:down, tab, shift:up, ctrl:up"),
        "tab right":        Key("ctrl:down, tab, ctrl:up"),
        "tab first":        Key("g, 0"),
        "tab last":         Key("g, $"),
        "tab new":          Key("t"),
        "tab close":        Key("ctrl:down, w, ctrl:up"),
        "tab restore":      Key("X"),
        "tab search":       Key("T"),

        "tab one":          Key("ctrl:down, 1, ctrl:up"),
        "tab two":          Key("ctrl:down, 2, ctrl:up"),
        "tab three":        Key("ctrl:down, 3, ctrl:up"),
        "tab four":         Key("ctrl:down, 4, ctrl:up"),
        "tab five":         Key("ctrl:down, 5, ctrl:up"),
        "tab six":          Key("ctrl:down, 6, ctrl:up"),
        "tab seven":        Key("ctrl:down, 7, ctrl:up"),
        "tab eight":        Key("ctrl:down, 8, ctrl:up"),
        "tab nine":         Key("ctrl:down, 9, ctrl:up"),
        #Marks
        "mark set":         Key("m, a"),
        "mark go":          Key("`, a"),
        "mark back":        Key("`, `"),
        #History
        "history back":     Key("H"),
        "history forward":  Key("L")
    }

context = AppContext(executable="chrome.exe")
grammar = Grammar("Chrome", context=context)
grammar.add_rule(ChromeRule())
grammar.load()