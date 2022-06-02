#include "PhotonTransporter.h"

#include "Photon.h"
#include <random>

using namespace Crystal::Math;
using namespace Crystal::Shape;
using namespace Crystal::Graphics;
using namespace Crystal::Photon;

void PhotonTransporter::add(IParticle* particle)
{
	spaceHash.add(particle);
}

void PhotonTransporter::addPhoton(Photon* photon)
{
	photons.emplace_back(photon);
}

void PhotonTransporter::build(const double searchRadius, const size_t tableSize)
{
	spaceHash.setup(searchRadius, tableSize);
}

void PhotonTransporter::transport(const float length)
{
	// photon‚ðparticle‚É‚Ô‚Â‚©‚é‚Ü‚Å‚·‚·‚ß‚Ä‚¢‚­
	for (auto p : photons) {
		if (p->isAbserved()) {
			continue;
		}

		p->setPosition(p->getPositionf() + p->getDirection() * length);
	}

	std::random_device seed;
	std::mt19937 mt(seed());

	std::uniform_int_distribution<> dist(0, 10000);

	for (auto p : photons) {
		auto neighbors = spaceHash.findNeighbors(p->getPosition());
		for (auto n : neighbors) {
			if (dist(mt) < 1000) {
//				p->setPosition(n->getPosition());
				p->setAbserved(true);
			}
		}
	}
}
