# ParticleFluids Tutorial 1 Hello, Fluids!

2022/03/31 

[![](https://img.youtube.com/vi/bpvUeji3b_A/0.jpg)](https://www.youtube.com/watch?v=bpvUeji3b_A)


## Fluidの作成

- Blenderデフォルトで生成されている[Cube]を選択します．
- [Object Properties]から，[Scale]を[10,10,10], [Location]を[0,0,10]とします．
- [Cube]を選択したまま，[VDBTools]->[MeshToPS]->[Voxelize]を押します．
- するとツリー上に[Object]という頂点だけのパーティクルオブジェクトが現れます．

- 作成した[Object]を選択し，[Physics Properties]タブを開きます．
- [PFFluid]ボタンを押します．
- パラメータ設定用タブが開きます．
- ここではそのままデフォルト値を用います．

## シミュレーションの開始

 - [PFSolver]タブを開きます．
 - [Min]を[-100,-100,-3]とします．
 - [ExportPath]で出力されるシミュレーションデータのディレクトリを設定します．
 - [Start]ボタンでシミュレーションが開始されます．
 - [Render]チェックボックスにチェックをつけておくと，シミュレーション途中のParticleの動きを確認できます．

 [![](https://img.youtube.com/vi/vOi4NsNg4R8/0.jpg)](https://www.youtube.com/watch?v=vOi4NsNg4R8)


## VDBボリュームへの変換
 - [PFSolver]->[ImportDir]で先ほど出力した[ExportDir]を指定します．
 - [Start]]ボタンを押すとコンバート処理が始まり，同じフォルダにVDB形式のデータが作成されます．

## Meshing
Blender標準の機能で連番のOpenVDBファイルを入力として扱うことができます．

- [Add]->[Volume]->[ImportOpenVDB]で先ほど出力したvdbファイルを選択します(BlenderではCtrl+Aで全選択できます)，．
- [Cube]を選択し，[Modifier Properties]->[AddModifier]->[VolumeToMesh][Object]を先ほどインポートしたvolumeとします．

## レンダリング
あとは通常のMeshと同じです．
詳細はBlenderのマニュアルを参考にしてください．