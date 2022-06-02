#pragma once

#include "CrystalScene/Scene/IParticleSystemScene.h"
//#include "ParticleAttribute.h"

//#include "IParticleSystemScene.h"
#include "CrystalScene/Scene/ParticleSystemPresenter.h"

namespace Crystal {
	namespace Photon {
		class Photon;

class PhotonCloudScene : public Scene::IShapeScene
{
public:
	//PhotonScene();

	PhotonCloudScene(const int id, const std::string& name);

	~PhotonCloudScene() {};

	void translate(const Math::Vector3dd& v) override { ; }

	void transform(const Math::Matrix3dd& m) override { ; }

	void transform(const Math::Matrix4dd& m) override { ; }

	static Scene::SceneType getTypeName() { return Scene::SceneType("photon"); }

	Scene::SceneType getType() const override { return getTypeName(); }

	Math::Box3dd getBoundingBox() const override;

	void addPhoton(Photon* p);

	std::vector<Photon*> getPhotons() const { return photons; }

	//std::vector<Math::Vector3dd> getPositions() const override;

	Scene::IPresenter* getPresenter() override { return presenter.get(); }

private:
	std::vector<Photon*> photons;
	//std::unique_ptr< Shape::ParticleSystem<ParticleAttribute> > shape;
	std::unique_ptr< Scene::IPresenter > presenter;
};

	}
}