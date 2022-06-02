#pragma once

#include "CrystalScene/Scene/IPresenter.h"

namespace Crystal {
	namespace Scene {
		class PointShaderScene;
	}
	namespace Photon {
		class PhotonCloudScene;
		class PBVRShaderScene;

class IPhotonCloudPresenter : public Scene::IPresenter
{
public:
	IPhotonCloudPresenter(PhotonCloudScene* model) {}
};

class PhotonCloudPresenter : public IPhotonCloudPresenter
{
public:
	explicit PhotonCloudPresenter(PhotonCloudScene* model);

	void createView(Scene::SceneShader* sceneShader) override;

	void removeView(Scene::SceneShader* sceneShader) override;

	void updateView() override;

private:
	void updateScreenView();

	void updateParentIdView();

	void updateChildIdView();

private:
	PhotonCloudScene* model;
	Scene::PointShaderScene* view;
};

class PhotonCloudPBVRPresenter : public IPhotonCloudPresenter
{
public:
	explicit PhotonCloudPBVRPresenter(PhotonCloudScene* model);

	void createView(Scene::SceneShader* sceneShader) override;

	void removeView(Scene::SceneShader* sceneShader) override;

	void updateView() override;

private:
	void updateScreenView();

	void updateParentIdView();

	void updateChildIdView();

private:
	PhotonCloudScene* model;
	PBVRShaderScene* view;
};

	}
}