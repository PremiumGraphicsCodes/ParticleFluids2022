#include "PhotonCloudScene.h"
#include "Photon.h"

#include "PhotonCloudPresenter.h"

using namespace Crystal::Math;
using namespace Crystal::Scene;
using namespace Crystal::Photon;

PhotonCloudScene::PhotonCloudScene(const int id, const std::string& name) :
	IShapeScene(id, name)
{
	presenter = std::make_unique<PhotonCloudPBVRPresenter>(this);
}

Box3dd PhotonCloudScene::getBoundingBox() const
{
	if (photons.empty()) {
		return Box3dd::createDegeneratedBox();
	}
	Box3d bb(photons.front()->getPosition());
	for (auto p : photons) {
		bb.add(p->getPosition());
	}
	return bb;
}

void PhotonCloudScene::addPhoton(Photon* p)
{
	photons.push_back(p);
}


/*
std::vector<Vector3dd> PhotonScene::getPositions() const
{
	std::vector<Vector3dd> positions;
	for (auto p : photons) {
		positions.push_back(p->getPosition());
	}
	return positions;
}
*/