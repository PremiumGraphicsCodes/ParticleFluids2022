# ParticleFluids Tutorial 3 Hello, Obstacles!

2022/03/31 

本アドオンでは，障害物の設定もFluidと同様に行うことができます．

[![](https://img.youtube.com/vi/ZdV1nFPjT_k/0.jpg)](https://www.youtube.com/watch?v=ZdV1nFPjT_k)

## Fluidの作成
チュートリアル1と同じ手順でFluidを作成します．

## Obstacleの設定

- [Add]->[Mesh]->[Plane]で床にする平面を新たに作成します．
- [Object Properties]から[Scale]を[20,20,1], Locationを[0,0,-20]とします．
- [Voxelize]を実行してParticlesに変換します．
- [Object.001]を選択し，[Physics Properties]->[PFFluid]ボタンを押します．
- [FluidType]を[Obstacle]に設定します．

## シミュレーションの開始
 - [PFSolver]タブを開きます．
 - [Min]を[-100,100,-100]とします．
 - [Start]ボタンでシミュレーションが開始されます．
 
[![](https://img.youtube.com/vi/FxPfhIqnM1U/0.jpg)](https://www.youtube.com/watch?v=FxPfhIqnM1U)

## VDBボリュームへの変換
このステップはチュートリアル1と同じです．

## Meshing
このステップはチュートリアル1と同じです．

## レンダリング
このステップはチュートリアル1と同じです．
