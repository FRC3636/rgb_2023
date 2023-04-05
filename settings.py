from util.section import RootSection
from default import patterns, sections

class Settings:
    def __init__(self):
        self.properties = {
            "enabled": True
        }
        
        self.gameinfo = {
            "stage": None,
            "alliance": None,
            "piece": None,
            "matchtype": None,
            "time": None,
            "estopped": None
        }
        self.update_pattern()

    def update_pattern(self):
        stage = self.gameinfo.get("stage")
        piece = self.gameinfo.get("piece")
        estopped = self.gameinfo.get("estopped")
        alliance = self.gameinfo.get("alliance")

        layout = None

        if stage == None:
            layout = sections.ALL(patterns.solid_blue)
        elif estopped:
            layout = sections.ALL(patterns.solid_red)
        else:
            body = sections.BODY(patterns.whole_rainbow)
            arms = sections.ARMS(patterns.whole_rainbow)
            panel = sections.PANEL(patterns.whole_rainbow)
            
            # if alliance == "red":
            #     body_pattern = "solid_red"
            # elif alliance == "blue":
            #     body_pattern = "solid_blue"
            
            if stage == "teleop":
                arms = sections.ARMS(patterns.cube if piece == "cube" else patterns.cone)
            
            layout = RootSection(body, arms, panel)

        self.pattern = layout.pattern()

    def get_pattern(self):
        return self.pattern

    def update(self, lights, gameinfo):
        new_props = {}
        new_info = {}
        for k, v in self.properties.items():
            new_props[k] = lights.getValue(k, v)
        for k, v in self.gameinfo.items():
            new_info[k] = gameinfo.getValue(k, v)
        props_updated = new_props != self.properties
        info_updated = new_info != self.gameinfo

        self.properties = new_props
        self.gameinfo = new_info

        if info_updated or props_updated:
            self.update_pattern()

    def push(self, nwtable):
        for k, v in self.properties.items():
            if v != None:
                nwtable.putValue(k, v)
