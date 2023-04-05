from util.section import Layout, Section
from default import *

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
            layout = Layout(
                Section(
                    self.presets["solid_blue"],
                    Part(EVERYTHING)
                )
            )
        elif estopped:
            layout = Layout(
                Section(
                    self.presets["solid_red"],
                    Part(EVERYTHING)
                )
            )
        else:
            body_pattern = "whole_rainbow"
            uarm_pattern = "armrainbow"
            darm_pattern = "armrainbow2"
            panel_pattern = "whole_rainbow"
            
            # if alliance == "red":
            #     body_pattern = "solid_red"
            # elif alliance == "blue":
            #     body_pattern = "solid_blue"
            
            if stage == "teleop":
                uarm_pattern = piece
                darm_pattern = piece
            
            layout = Layout(
                Section(
                    self.presets[body_pattern],
                    Part(BODY1),
                    Part(BODY2),
                    Part(BODY3),
                    Part(BODY4),
                    Part(BODY5),
                    Part(BODY6),
                    Part(BODY7),
                    Part(BODY8)
                ),
                Section(
                    self.presets[uarm_pattern],
                    Part(RB_UP),
                    Part(LB_UP)
                ),
                Section(
                    self.presets[darm_pattern],
                    Part(RB_DOWN),
                    Part(LB_DOWN)
                ),
                Section(
                    self.presets[panel_pattern],
                    Part(PANEL)
                )
            )

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
