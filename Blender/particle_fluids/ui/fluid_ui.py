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

import bpy
from bpy.props import FloatProperty, StringProperty, BoolProperty

from physics.fluid_scene import FluidScene
from ui.model.bl_fluid import BLFluid
from ui.prop.fluid_prop import PARTICLE_FLUID_FluidProperty

class PARTICLE_FLUID_OT_Activate(bpy.types.Operator):
    bl_idname = "object.sample27_nop"
    bl_label = "NOP"
    bl_description = "何もしない"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
      is_active = bpy.context.active_object.ps_fluid.is_active_prop
      bpy.context.active_object.ps_fluid.is_active_prop = not is_active
      return {'FINISHED'}

class PARTICLE_FLUID_PT_FluidPanel(bpy.types.Panel) :
  bl_space_type = "PROPERTIES"
  bl_region_type = "WINDOW"
  bl_context = "physics"
  bl_category = "ParticleFluid"
  bl_label = "ParticleFluid"
 
  def draw(self, context):
    layout = self.layout
    layout.operator(PARTICLE_FLUID_OT_Activate.bl_idname, text="PFFluid")    
    if bpy.context.active_object.ps_fluid.is_active_prop == True :
      fluid_property = bpy.context.active_object.ps_fluid
      layout.prop(fluid_property, "type_prop", text="FluidType")
      layout.prop(fluid_property, "particle_radius_prop", text="ParticleRadius")
      layout.prop(fluid_property, "stiffness_prop", text="Stiffness")
      layout.prop(fluid_property, "viscosity_prop", text="Viscosity")
      #  layout.prop(fluid_property, "is_static_prop", text="Static")
      layout.prop(fluid_property, "temperature_prop", text="Temperature")
      layout.prop(fluid_property, "heat_diffuse_prop", text="HeatDiffuse")
      layout.prop(fluid_property, "drag_force_prop", text="DragForce")
      layout.prop(fluid_property, "drag_heat_prop", text="DragHeat")
      if fluid_property.type_prop == "Emitter" :
        layout.prop(fluid_property, "start_step_prop", text="StartStep")
        layout.prop(fluid_property, "end_step_prop", text="EndStep")
        layout.prop(fluid_property, "interval_prop", text="Interval")
        layout.prop(fluid_property, "initial_velocity_prop", text="Velocity")
        layout.prop(fluid_property, "lifetime_prop", text="LifeTime")

classes = [
  PARTICLE_FLUID_OT_Activate,
  PARTICLE_FLUID_PT_FluidPanel,  
  PARTICLE_FLUID_FluidProperty,
]

class PARTICLE_FLUIDS_FluidUI :
  def register():
    for c in classes:
      bpy.utils.register_class(c)
    bpy.types.Object.ps_fluid = bpy.props.PointerProperty(name="PSFluid", type=PARTICLE_FLUID_FluidProperty)
    
  def unregister() :
    del bpy.types.Object.ps_fluid
    for c in classes:
      bpy.utils.unregister_class(c)
 