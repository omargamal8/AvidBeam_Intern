class MediaSource:
    def __init__(self, roi_x, roi_y, width,height, name, path):
        self._roi_x = roi_x
        self._roi_y = roi_y
        self._roi_width = width
        self._roi_height = height
        self._name = name
        self._path = path
