#pragma once

#include "CrystalScene/AppBase/IOkCancelView.h"

#include "CrystalScene/Scene/World.h"
#include "CrystalScene/AppBase/Canvas.h"

#include "../CrystalPhoton/PhotonTransporter.h"

#include "CrystalScene/Scene/ParticleSystemScene.h"
#include "../CrystalPhoton/PhotonCloudScene.h"

namespace Crystal {
	namespace UI {

class MovingPhotonView : public UI::IOkCancelView
{
public:
	MovingPhotonView(const std::string& name, Scene::World* world, Canvas* canvas);

private:
	void onBuild();

	void onStep();

	void onOk();

private:
	Button buildButton;
	Button stepButton;

	Photon::PhotonTransporter transporter;
	Scene::ParticleSystemScene* particles;
	Photon::PhotonCloudScene* photonCloud;
};

	}
}