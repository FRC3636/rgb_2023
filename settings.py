from util.section import RootSection
from default import presets

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
            "estopped": None,
            "balanced": None
        }
        self.active_preset = None
        self.update_pattern()

    def set_preset(self, preset):
        if self.active_preset == None or self.active_preset.preset != preset:
            self.active_preset = preset.activate()

    def update_pattern(self):
        stage = self.gameinfo.get("stage")
        piece = self.gameinfo.get("piece")
        estopped = self.gameinfo.get("estopped")
        alliance = self.gameinfo.get("alliance")
        balanced = self.gameinfo.get("balanced")

        if stage == None:
            self.set_preset(presets.DISCONNECTED)
        elif estopped:
            self.set_preset(presets.ESTOP)
        elif balanced:
            self.set_preset(presets.BALANCED)
            self.active_preset.set_slot("body", presets.HOT_FIRE if alliance == "red" else presets.COLD_FIRE)
        else:
            self.set_preset(presets.DEFAULT)
            
            self.active_preset.set_slot("body", presets.WRAINBOW_BODY)
            self.active_preset.set_slot("panel", presets.WRAINBOW_PANEL)
            if stage == "teleop":
                self.active_preset.set_slot("arms", presets.CUBE if piece == "cube" else presets.CONE)
            else:
                self.active_preset.set_slot("arms", presets.WRAINBOW_ARMS)
        
        self.pattern = self.active_preset.layout().pattern()

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
