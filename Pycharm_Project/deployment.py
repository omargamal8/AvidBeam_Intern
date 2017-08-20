from computing import ComputingModule
from media import MediaSource


class DeploymentScenario:
    def __init__(self, comp_mod, media, name, no_streams):
        self._computing_module = comp_mod
        self._media_source = media
        self._name = name
        self._no_streams = no_streams
