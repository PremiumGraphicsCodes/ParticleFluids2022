#include <random>

#include "MovingPhotonView.h"
#include "Crystal/Math/Tolerance.h"
#include "../CrystalPhoton/Photon.h"

using namespace Crystal::Math;
using namespace Crystal::Shape;
using namespace Crystal::Scene;
using namespace Crystal::Graphics;
using namespace Crystal::Photon;
using namespace Crystal::UI;

namespace {
	// https://tapioca.hatenablog.jp/entry/2017/02/19/015556
	std::vector<Vector3dd> generateVolume()
	{
		std::random_device seed;
		std::mt19937 mt(seed());

		std::uniform_real_distribution<> distZ(-1.0, 1.0);
		std::uniform_real_distribution<> distTheta(0.0, 2.0 * PI);
		std::uniform_real_distribution<> distR(0.0, 1.0);

		std::vector<Vector3dd> positions;
		for (int i = 0; i < 1000; ++i) {
			const auto z = distZ(mt);
			const auto theta = distTheta(mt);
			const auto r = distR(mt);

			const auto rr = std::pow(r, 1.0 / 3.0);
			const auto xx = rr * std::sqrt(1.0 - z * z) * ::cos(theta);
			const auto yy = rr * std::sqrt(1.0 - z * z) * ::sin(theta);
			const auto zz = rr * z;
			positions.emplace_back(xx, yy, zz);
		}
		return positions;
	}
}

MovingPhotonView::MovingPhotonView(const std::string& name, World* world, Canvas* canvas) :
	IOkCancelView(name, world, canvas),
	buildButton("AddVolume"),
	stepButton("Step")
{
	add(&buildButton);
	buildButton.setFunction([=]() { onBuild(); });

	add(&stepButton);
	stepButton.setFunction([=]() { onStep(); });
}

void MovingPhotonView::onBuild()
{
	auto shape = std::make_unique<ParticleSystem<ParticleAttribute>>();
	ParticleAttribute attr;
	attr.color = ColorRGBAf(1, 0, 0, 0);
	attr.size = 10.0f;
	const auto positions = ::generateVolume();
	for (const auto& p : positions) {
		shape->add(p, attr);
	}
	this->particles = new ParticleSystemScene(getWorld()->getNextSceneId(), "Boundary", std::move(shape));
	auto presenter = particles->getPresenter();
	presenter->createView(getWorld()->getRenderer());
	getWorld()->getScenes()->addScene(this->particles);

	this->photonCloud = new PhotonCloudScene(getWorld()->getNextSceneId(), "Photon");
	for (int i = 0; i < 100; ++i) {
		const auto x = 0.01 * i;
		auto photon = new Photon::Photon(Vector3df(x, 1, 0), ColorRGBAf(1.0f, 1.0f, 1.0f, 1.0f), 10.0f);
		photon->setDirection(Vector3df(0, -1, 0));
		this->photonCloud->addPhoton(photon);
	}
	this->photonCloud->getPresenter()->createView(getWorld()->getRenderer());
	getWorld()->getScenes()->addScene(this->photonCloud);

	auto ps = this->particles->getShape()->getIParticles();
	transporter.build(0.1, positions.size());
	for (auto p : ps) {
		transporter.add(p);
	}

	auto photons = this->photonCloud->getPhotons();
	for (auto p : photons) {
		transporter.addPhoton(p);
	}

}

void MovingPhotonView::onStep()
{
	transporter.transport(0.1f);
	this->photonCloud->getPresenter()->updateView();
}

void MovingPhotonView::onOk()
{
	for (int i = 0; i < 100; ++i) {
		transporter.transport(0.1f);
	}
	this->photonCloud->getPresenter()->updateView();
}
