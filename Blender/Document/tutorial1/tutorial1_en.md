# Tutorial1 Hello Fluids!

2022/03/31 

[![](https://img.youtube.com/vi/bpvUeji3b_A/0.jpg)](https://www.youtube.com/watch?v=bpvUeji3b_A)

## Create Fluid

- Select [Cube] in Blender's default mesh.
- Select [Object Properties]，and change [Scale] to [10,10,10], [Location] to [0,0,10]
- Keep selecting [Cube]，push [VDBTools]->[MeshToPS]->[Voxelize]．
- New object [Object], which has no faces, will be appeared．

- Select [Object]，and open [Physics Properties] tab．
- Push [PFFluid] button．
- Change [FluidType] to [Fluid].
- In this case, use default value.

## Start Simulation

 - Open [PFSolver] tab．
 - Set [Min] to [-100,-100,-3]．
 - Set export directory on [ExportPath].
 - Press [Start] button, then simulation starts.
 - If you check [Render] checkbox, you can check particle's movements.

 [![](https://img.youtube.com/vi/vOi4NsNg4R8/0.jpg)](https://www.youtube.com/watch?v=vOi4NsNg4R8)


## Convert to VDB volume
 - Set [PFSolver]->[ImportDir] which specified the above．
 - Press [Start], and convert to vdb files starts．

## Meshing
Using blender's default function, you can import vbd files.

- [Add]->[Volume]->[ImportOpenVDB](On Blender, you can select all files with Ctrl+A)．
- Select [Cube].
- Open tab [Modifier Properties]
- [AddModifier]->[VolumeToMesh]
- Change [Object] to volume name which you imported.

## Rendering
Rendering step is same as stadard Blender's operation.
Please refer blender's manual.