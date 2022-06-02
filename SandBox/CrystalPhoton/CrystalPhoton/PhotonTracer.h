#pragma once

#include "Crystal/Shape/IParticle.h"
#include "Crystal/Graphics/SpotLight.h"
#include "CrystalSpace/CrystalSpace/CompactSpaceHash3d.h"

namespace Crystal {
	namespace Photon {
		class Photon;
		class PhotonCloudScene;

class PhotonTracer
{
public:
	void add(Shape::IParticle* particle);

	void build(const double searchRadius, const size_t tableSize);

	std::vector<Photon*> generatePhotons(const Graphics::SpotLight& light);

	void trance(PhotonCloudScene* photonCloud, const float length);

private:
	std::vector<Shape::IParticle*> particles;
	Crystal::Space::CompactSpaceHash3d spaceHash;
};
	}
}