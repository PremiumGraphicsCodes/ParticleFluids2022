import bpy

from .filter import VDB_TOOLS_Filter_UI
from .resampling import VDB_TOOLS_Resampling_UI
from .composite import VDB_TOOLS_Composite_UI
from .points_to_volume import VDB_TOOLS_VolumeToPoints_UI
from .mesh_to_volume import VDB_TOOLS_MeshToVolume_UI
from .volume_to_points import VDB_TOOLS_VolumeToPoints_UI
from .mesh_to_points import VDB_TOOLS_MeshToPoints_UI

bl_info = {
    "name": "VDBToolsForBlender",
    "author": "PremiumGraphicsInc",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "",
    "description": "",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object"
}

def register():
    VDB_TOOLS_Filter_UI.register()
    VDB_TOOLS_Resampling_UI.register()
    VDB_TOOLS_Composite_UI.register()
    VDB_TOOLS_VolumeToPoints_UI.register()
    VDB_TOOLS_MeshToVolume_UI.register()
    #VDB_TOOLS_VolumeToPoints_UI.register()
    VDB_TOOLS_MeshToPoints_UI.register()

def unregister():
    VDB_TOOLS_MeshToPoints_UI.unregister()
    #VDB_TOOLS_VolumeToPoints_UI.unregister()
    VDB_TOOLS_MeshToVolume_UI.unregister()
    VDB_TOOLS_VolumeToPoints_UI.unregister()
    VDB_TOOLS_Composite_UI.unregister()
    VDB_TOOLS_Resampling_UI.unregister()
    VDB_TOOLS_Filter_UI.unregister()

if __name__ == "__main__":
    register()