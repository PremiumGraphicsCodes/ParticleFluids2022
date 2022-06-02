bl_info = {
    "name": "サンプル 333: 何もしないアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "アドオンの有効化と無効化を試すためのサンプル",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}
import bpy
from bpy.props import *

class TUTORIAL_OT_SayComment(bpy.types.Operator):
  bl_idname = "tutorial.saycomment"
  bl_label = "Say Comment"
  bl_options = {"REGISTER", "UNDO"}

  comment: StringProperty(default="Hello", options={'HIDDEN'})

  def execute(self, context):
    self.report({'INFO'}, self.comment)

    return {'FINISHED'}

class TUTORIAL_PT_SamplePanel(bpy.types.Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "Tutorial"
  bl_label = "PanelTitle"

  def draw(self, context):
    layout = self.layout
    layout.prop(context.scene, "tutorial_comment")

    op_prop = layout.operator(TUTORIAL_OT_SayComment.bl_idname, text="Say")
    op_prop.comment = context.scene.tutorial_comment

classes = [
  TUTORIAL_PT_SamplePanel,
  TUTORIAL_OT_SayComment
]

def register():
  for c in classes:
    bpy.utils.register_class(c)

  bpy.types.Scene.tutorial_comment = StringProperty(default = "")

def unregister():
  for c in classes:
    bpy.utils.unregister_class(c)

  del bpy.types.Scene.tutorial_comment

if __name__ == "__main__":
  register()