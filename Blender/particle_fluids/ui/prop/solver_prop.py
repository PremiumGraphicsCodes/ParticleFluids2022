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

from bpy.props import (
    BoolProperty,
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
)

class PARTICLE_FLUIDS_SolverProperty(bpy.types.PropertyGroup) :
    do_render_prop : BoolProperty(
        name ="active",
        description = "Active",
        default = False,
    )
    start_frame_prop : IntProperty(
        name = "start_frame",
        description="StartFrame",
        default=0,
        min=0,
    )
    end_frame_prop : IntProperty(
        name = "end_frame",
        description="EndFrame",
        default=250,
        min=0,
    )
    time_step_prop : FloatProperty(
        name="time_step",
        description="TimeStep",
        default=0.01,
        min=0.0,
        max=1.0,
    )
    external_force_prop : FloatVectorProperty(
        name="external_force",
        description="ExternalForce",
        default=(0.0, 0.0, -9.8)
    )
    buoyancy_prop : FloatVectorProperty(
        name="buoyancy",
        description="Buoyancy",
        default=(0.0, 0.0, 0.1)
    )
    search_radius_prop : FloatProperty(
        name="search_radius",
        description="SearchRadius",
        default = 3.0,
        min = 0.0
    )
    min_prop : bpy.props.FloatVectorProperty(
        name="min",
        description="Min",
        default=(-100.0, -100.0, 0.0)
    )
    max_prop : bpy.props.FloatVectorProperty(
        name="max",
        description="Max",
        default=(100.0, 100.0, 100.0)
    )
    export_directory_prop : bpy.props.StringProperty(
        name="export_dir",
        description="ExportDirectory",
        default="//",
        maxlen=1024,
        subtype='DIR_PATH',
    )
    iteration_prop : bpy.props.IntProperty(
        name="iteration_prop",
        description ="Iteration",
        default =1,
        min = 1,
    )