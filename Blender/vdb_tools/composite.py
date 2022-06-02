import bpy
import os
import json
import subprocess

class VDB_TOOLS_OT_CompositeOperator(bpy.types.Operator) :
  bl_idname = "pg.compositeoperator"
  bl_label = "Composite"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context) :
      name = context.scene.composite_property.name_prop

      #export_dir_path = bpy.path.abspath(context.scene.composite_property.export_directory_prop)
      composite_type = context.scene.composite_property.type_prop

      selected_volumes = self.get_selected_volumes(context)
      if len(selected_volumes) != 2 :
        self.report({'INFO'}, "Please select two volumes")
        return {'CANCELLED'}

      filepath1 = bpy.path.abspath( selected_volumes[0].filepath )
      filepath2 = bpy.path.abspath( selected_volumes[1].filepath )

      export_dir_path = os.path.dirname(filepath1)
      export_file_path = os.path.join(export_dir_path, name)

      j = self.to_json(filepath1, filepath2, composite_type, export_file_path)
      #print(json.dumps(j, ensure_ascii=False, indent=2))

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

  def get_selected_volumes(self, context) :
    volumes = []
    for o in bpy.data.objects:
      if o.type == 'VOLUME' and o.select_get():
        volumes.append(o.data)
    return volumes

  def to_json(self, input_vdb_file1, input_vdb_file2, composit_type, output_vdb_file) :
    read_dict1 = dict()
    read_dict1["FilePath"] =  input_vdb_file1
    read_dict1["Radius"] = 0.5
    read1 = ["VDBSceneFileRead", read_dict1]

    read_dict2 = dict()
    read_dict2["FilePath"] =  input_vdb_file2
    read_dict2["Radius"] = 0.5
    read2 = ["VDBSceneFileRead", read_dict2]

    composite_dict = dict()
    composite_dict["CompositeType"] = composit_type
    composite_dict["SceneId1"] = 1
    composite_dict["SceneId2"] = 2
    composite = ["VDBSceneComposite", composite_dict]

    write_dict = dict()
    write_dict["FilePath"] = output_vdb_file
    write_dict["VDBSceneId"] = 1
    write = ["VDBSceneFileWrite", write_dict]

    data = dict()
    data = [read1, read2, composite, write]
    return data

class CompositePropertyGroup(bpy.types.PropertyGroup):
  type_prop: bpy.props.EnumProperty(
        name="Type",
        description="",
        default='Union',
        items=[
            ('Union', "Union", ""),
            ('Intersection', "Intersection", ""),
            ('Diff', "Diff", "")
        ]
    )
  name_prop : bpy.props.StringProperty(
    name="name",
    description="Name",
    default="composited",
  )


class VDB_TOOLS_PT_Composite_Panel(bpy.types.Panel) :
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "VDBTools"
  bl_label = "Composite"
  
  def draw(self, context):
    layout = self.layout
    layout.prop(context.scene.composite_property, "type_prop", text="Type")
    layout.prop(context.scene.composite_property, "name_prop", text="Name")
    layout.operator(VDB_TOOLS_OT_CompositeOperator.bl_idname, text="Composite")

classes = [
  VDB_TOOLS_OT_CompositeOperator,
  VDB_TOOLS_PT_Composite_Panel,
  CompositePropertyGroup
]

class VDB_TOOLS_Composite_UI :
  def register():
    for c in classes:
      bpy.utils.register_class(c)
    bpy.types.Scene.composite_property = bpy.props.PointerProperty(type=CompositePropertyGroup)

  def unregister() :
    del bpy.types.Scene.composite_property
    for c in classes:
      bpy.utils.unregister_class(c)
 