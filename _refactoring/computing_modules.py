import Storage
class ComputingModule:
    def __init__(self, name, ram, threads, core_counts, physical_core_counts,
                 max_input_res, max_freq, fps, version, path, context = {}):
        self._name = name
        self._exp_ram = ram
        self._exp_threads = threads
        self._exp_core_counts = core_counts
        self._exp_physical_core_counts = physical_core_counts
        self._exp_max_input_res = max_input_res
        self._exp_max_freq = max_freq
        self._exp_fps = fps
        self._version = version
        self._path = path
        self._context = context
        self._storage = Storage.Storage()
    

    def extract_data_as_dict(self):
        return{
        "algo_name": self._name,
        "plugin_path": self._path,
        "max_inp_res": self._exp_max_input_res,
        "algo_ver": self._version,
        "pcores_count": self._exp_physical_core_counts,
        "ram_req": self._exp_ram,
        "plugin_context": self._context,
        "threads": self._exp_threads,
        "fps":self._exp_fps,
        "cores": self._exp_core_counts,
        "max_fr": self._exp_max_freq
        }
    @staticmethod    
    def create_module(info):
        new_CM =  ComputingModule(*info)
        ComputingModule.store(new_CM)
    @staticmethod
    def store(computingModule):
        storage = Storage.Storage()
        storage.insert_data(computingModule.extract_data_as_dict(), "comp_mod")
    @staticmethod
    def delete_module(algo_name):
        storage = Storage.Storage()
        storage.delete( "comp_mod", {"algo_name":algo_name})