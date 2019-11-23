from dragonfly import AppContext, Grammar, CompoundRule, Key

# Voice command rule combining spoken form and recognition processing.
class ExampleRule(CompoundRule):
    spec = "do something computer"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        a1 = Key("k")
        a1.execute()

# Create a grammar which contains and loads the command rule.
grammar = Grammar("example grammar", context = AppContext(executable='Notepad'))                # Create a grammar to contain the command rule.
grammar.add_rule(ExampleRule())                     # Add the command rule to the grammar.
grammar.load()                                      # Load the grammar.