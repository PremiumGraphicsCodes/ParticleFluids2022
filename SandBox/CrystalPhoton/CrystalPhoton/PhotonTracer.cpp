#include "PhotonTracer.h"

#include "Photon.h"
#include "PhotonCloudScene.h"

using namespace Crystal::Math;
using namespace Crystal::Shape;
using namespace Crystal::Graphics;
using namespace Crystal::Photon;

void PhotonTracer::add(IParticle* particle)
{
	spaceHash.add(particle);
}

std::vector<Photon*> PhotonTracer::generatePhotons(const SpotLight& l)
{
	Photon* photon = new Photon(l.getPosition(), ColorRGBAf(1, 1, 1, 1), 20.0f);
	photon->setDirection(l.getDirection());
	return { photon };
}

void PhotonTracer::build(const double searchRadius, const size_t tableSize)
{
	spaceHash.setup(searchRadius * 2.0, tableSize);
}

void PhotonTracer::trance(PhotonCloudScene* photonCloud, const float length)
{
	// photon‚ðparticle‚É‚Ô‚Â‚©‚é‚Ü‚Å‚·‚·‚ß‚Ä‚¢‚­
	const auto& photons = photonCloud->getPhotons();
	for (auto p : photons) {
		if (p->isAbserved()) {
			continue;
		}

		p->setPosition( p->getPositionf() + p->getDirection() * length );
	}
	for (auto p : photons) {
		auto neighbors = spaceHash.findNeighbors( p->getPosition() );
		if (!neighbors.empty()) {
			p->setAbserved(true);
		}
	}
}
