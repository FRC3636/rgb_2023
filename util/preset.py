class Preset:
    # type is unused, but helps to document
    def __init__(self, type, name, run, slots=[]):
        self.type = type
        self.name = name
        self.slots = slots
        self.run = run
    
    def activate(self):
        return ActivePreset(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.type}, {self.slots})"

class ActivePreset:
    def __init__(self, preset):
        self.preset = preset
        self.children = {}
        self.current_layout = None
    
    def set_slot(self, name, preset):
        if name not in self.preset.slots:
            raise KeyError(f"no such slot {name} found in preset {self.preset.name}")
        elif self.children.get(name) != None and self.children[name].preset != preset:
            return
        self.current_layout = None
        self.children[name] = preset.activate()
    
    def layout(self):
        if self.current_layout == None:
            self.current_layout = self.preset.run(
                map(
                    lambda x: x.layout(),
                    filter(
                        lambda x: x != None,
                        self.children.values()
                    )
                )
            )
        return self.current_layout

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.preset}, {self.children})"