#include "PhotonTracerView.h"

using namespace Crystal::Math;
using namespace Crystal::Shape;
using namespace Crystal::Scene;
using namespace Crystal::Graphics;
using namespace Crystal::Photon;
using namespace Crystal::UI;

PhotonTracerView::PhotonTracerView(const std::string& name, World* world, Canvas* canvas) :
	IOkCancelView(name, world, canvas),
	lightView("Light"),
	buildButton("Build"),
	stepButton("Step")
{
	SpotLight light;
	light.setPosition(Vector3df(5.0f, 5.0f, 0.0f));
	lightView.setValue(light);

	add(&lightView);
	add(&buildButton);
	buildButton.setFunction([=]() { onBuild(); });

	add(&stepButton);
	stepButton.setFunction([=]() { onStep(); });

	{
		auto shape = std::make_unique<ParticleSystem<ParticleAttribute>>();
		this->particles = new ParticleSystemScene(getWorld()->getNextSceneId(), "Boundary", std::move(shape));
		auto presenter = particles->getPresenter();
		presenter->createView(getWorld()->getRenderer());
	}

	{
		this->photonCloud = new PhotonCloudScene(getWorld()->getNextSceneId(), "Photon");
		this->photonCloud->getPresenter()->createView(getWorld()->getRenderer());
	}
}

void PhotonTracerView::onBuild()
{
	ParticleAttribute attr;
	attr.color = ColorRGBAf(1, 0, 0, 0);
	attr.size = 10.0f;
	for (int i = 0; i < 10; ++i) {
		particles->getShape()->add(Vector3dd(i, 0, 0), attr);
		particles->getShape()->add(Vector3dd(i, 10, 0), attr);
		particles->getShape()->add(Vector3dd(0, i, 0), attr);
		particles->getShape()->add(Vector3dd(10, i, 0), attr);
	}
	particles->getPresenter()->updateView();

	tracer.build(0.5, particles->getShape()->getSize());

	const auto ps = particles->getShape()->getParticles();
	for (auto p : ps) {
		tracer.add(p);
	}

	auto photons = tracer.generatePhotons(lightView.getValue());
	for (auto p : photons) {
		this->photonCloud->addPhoton(p);
	}
	this->photonCloud->getPresenter()->updateView();
	//tracer.build()
}

void PhotonTracerView::onStep()
{
	tracer.trance(this->photonCloud, 1.0f);
	this->photonCloud->getPresenter()->updateView();
}

void PhotonTracerView::onOk()
{

}
