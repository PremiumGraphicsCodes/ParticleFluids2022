# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from venv import create
import bpy
import json

import os
import subprocess

class VDB_TOOLS_OT_PointsToVolumeOperator(bpy.types.Operator) :
  bl_idname = "pg.pointstovolume"
  bl_label = "PointsToVolume"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context) :
      points_file_prop = context.scene.points_to_volume_property.points_file_prop
      name = context.scene.points_to_volume_property.name_prop
      radius = context.scene.points_to_volume_property.radius_prop
      voxel_size = context.scene.points_to_volume_property.voxel_size_prop
      filepath = bpy.path.abspath( points_file_prop )

      print(filepath)

      export_dir_path = os.path.dirname(filepath)
      export_file_path = os.path.join(export_dir_path, name)

      j = self.to_json(filepath, radius, voxel_size, export_file_path)
      print(json.dumps(j, ensure_ascii=False, indent=2))

      json_file_path = os.path.join(export_dir_path, "command.json")
      with open(json_file_path, 'w') as f:
        json.dump(j, f, ensure_ascii=False, indent=4)

      addon_dirpath = os.path.dirname(__file__)
      tool_path = os.path.join(addon_dirpath, 'VDBRunner')
      params = []
      params.append(tool_path)
      params.append(json_file_path)        
      
      result = subprocess.run(params, shell=True)
      if result == -1 : 
        return {'CANCELLED'}

      vol = bpy.data.volumes.new(name =name)
      vol.filepath = export_file_path
      ob = bpy.data.objects.new(name, vol)
      bpy.context.collection.objects.link(ob)

      return {'FINISHED'}

  def get_selected_volume(self, context) :
    for o in bpy.data.objects:
      if o.type == 'VOLUME' and o.select_get():
        return o
    return None

  def to_json(self, input_vdb_file, radius, voxel_size, output_vdb_file) :
    read_dict = dict()
    read_dict["FilePath"] =  input_vdb_file
    read_dict["Radius"] = 0.5
    read_command = ["VDBSceneFileRead", read_dict]

    convert_dict = dict()
    convert_dict["SceneId"] = 1
    convert_dict["Radius"] = radius
    convert_dict["VoxelSize"] = voxel_size
    convert_command = ["VDBScenePSToVolume", convert_dict]

    write_dict = dict()
    write_dict["FilePath"] = output_vdb_file
    write_dict["VDBSceneId"] = 2
    write_command = ["VDBSceneFileWrite", write_dict]

    data = dict()
    data = [read_command, convert_command, write_command]
    return data

class PointsToVolumePropertyGroup(bpy.types.PropertyGroup):
  voxel_size_prop : bpy.props.IntProperty(
      name="voxelSize",
      description="",
      default=1,
      min=1
  )
  radius_prop : bpy.props.FloatProperty(
      name="radius",
      description="",
      default=1,
      min=0
  )
  points_file_prop : bpy.props.StringProperty(
    name="points_file",
    description="",
    default="//",
    maxlen=1024,
    subtype='FILE_PATH',
  )
  name_prop : bpy.props.StringProperty(
    name="name",
    description="",
    default="ToVolume",
  )

class VDB_TOOLS_PT_PointsToVolumePanel(bpy.types.Panel) :
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "VDBTools"
  bl_label = "PointsToVolume"
  
  def draw(self, context):
    layout = self.layout
    layout.prop(context.scene.points_to_volume_property, "voxel_size_prop", text="VoxelSize")
    layout.prop(context.scene.points_to_volume_property, "radius_prop", text="Radius")
    layout.prop(context.scene.points_to_volume_property, "points_file_prop", text="PointsFile")
    layout.prop(context.scene.points_to_volume_property, "name_prop", text="Name")
    layout.operator(VDB_TOOLS_OT_PointsToVolumeOperator.bl_idname, text="ToVolume")

classes = [
  VDB_TOOLS_OT_PointsToVolumeOperator,
  VDB_TOOLS_PT_PointsToVolumePanel,
  PointsToVolumePropertyGroup
]

class VDB_TOOLS_VolumeToPoints_UI :
  def register():
    for c in classes:
      bpy.utils.register_class(c)
    bpy.types.Scene.points_to_volume_property = bpy.props.PointerProperty(type=PointsToVolumePropertyGroup)

  def unregister() :
    del bpy.types.Scene.points_to_volume_property
    for c in classes:
      bpy.utils.unregister_class(c)
 