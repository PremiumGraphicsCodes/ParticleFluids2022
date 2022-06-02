#pragma once

#include "Crystal/Shape/IParticle.h"
#include "Crystal/Graphics/SpotLight.h"
#include "CrystalSpace/CrystalSpace/CompactSpaceHash3d.h"

namespace Crystal {
	namespace Photon {
		class Photon;

class PhotonTransporter
{
public:
	void add(Shape::IParticle* particle);

	void addPhoton(Photon* photon);

	void build(const double searchRadius, const size_t tableSize);

	void transport(const float length);

private:
	std::vector<Shape::IParticle*> particles;
	std::vector<Photon*> photons;
	Crystal::Space::CompactSpaceHash3d spaceHash;
};
	}
}