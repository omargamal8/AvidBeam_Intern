class ComputingModule:
    def __init__(self, name, ram, threads, core_counts, physical_core_counts,
                 max_freq, fps, path):
        self._name = name
        self._exp_ram = ram
        self._exp_threads = threads
        self._exp_core_counts = core_counts
        self._exp_physical_core_counts = physical_core_counts
        self._exp_max_freq = max_freq
        self._exp_fps = fps
        self._path = path
        