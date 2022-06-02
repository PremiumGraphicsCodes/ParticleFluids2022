# ParticleFluids Tutorial 3 Hello, Obstacles!

2022/03/31 

On this add-on, obstacles can be created as same as fluids.

[![](https://img.youtube.com/vi/ZdV1nFPjT_k/0.jpg)](https://www.youtube.com/watch?v=ZdV1nFPjT_k)

## Create Fluid
This step is same as Tutorial1.

## Create Obstacle

- Create a mesh by [Add]->[Mesh]->[Plane]．
- Open [Object Properties] tab, and change [Scale] to [20,20,1], [Location] to [0,0,-20]．
- Create particles by　[VDBTools]->[MeshToPS]->[Voxelize]
- Select[Object001]，push [Physics Properties]->[PFFluid] button．
- Change [FluidType] to [Obstacle]．

## Start Simulation
 - Open [PFSolver] tab．
 - Change [Min] to [-100,100,-100]．
 - Press [Start] button, then simulation starts.

[![](https://img.youtube.com/vi/FxPfhIqnM1U/0.jpg)](https://www.youtube.com/watch?v=FxPfhIqnM1U)

## Convert to VDB volume
This step is same as Tutorial1.

## Meshing
This step is same as Tutorial1.
