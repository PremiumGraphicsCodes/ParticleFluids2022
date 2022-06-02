#include "PhotonCloudPresenter.h"

//#include "ParticleSystemScene.h"
#include "PhotonCloudScene.h"
#include "Photon.h"

#include "CrystalScene/Scene/SceneShader.h"
#include "CrystalScene/Scene/PointShaderScene.h"

#include "PBVRShaderScene.h"

using namespace Crystal::Shader;
using namespace Crystal::Scene;
//using namespace Crystal::Graphics;
using namespace Crystal::Photon;

PhotonCloudPresenter::PhotonCloudPresenter(PhotonCloudScene* model) :
	IPhotonCloudPresenter(model),
	view(nullptr),
	model(model)
{
}

void PhotonCloudPresenter::createView(SceneShader* sceneShader)
{
	{
		this->view = new PointShaderScene(model->getName());
		this->view->setShader(sceneShader->getRenderers()->getPointShader());
		this->view->build(*sceneShader->getGLFactory());
		sceneShader->getObjectRenderer()->addScene(this->view);
	}

	updateView();
}

void PhotonCloudPresenter::removeView(SceneShader* sceneShader)
{
	this->view->release(*sceneShader->getGLFactory());
	sceneShader->getObjectRenderer()->removeScene(this->view);
	delete this->view;
}

void PhotonCloudPresenter::updateView()
{
	updateScreenView();
	updateParentIdView();
	updateChildIdView();
}

void PhotonCloudPresenter::updateScreenView()
{
	const auto& ps = model->getPhotons();
	PointBuffer pb;
	for (auto p : ps) {
		pb.add(p->getPosition(), p->getColor(), p->getSize());
	}

	//this->view->setBlend(this->doBlend);
	this->view->send(pb);
	this->view->setVisible(model->isVisible());
}

void PhotonCloudPresenter::updateParentIdView()
{
}

void PhotonCloudPresenter::updateChildIdView()
{
}

PhotonCloudPBVRPresenter::PhotonCloudPBVRPresenter(PhotonCloudScene* model) :
	IPhotonCloudPresenter(model),
	view(nullptr),
	model(model)
{
}

void PhotonCloudPBVRPresenter::createView(SceneShader* sceneShader)
{
	{
		this->view = new PBVRShaderScene(model->getName());
		auto renderer = static_cast<PBVRenderer*>(sceneShader->getRenderers()->findRenderer("PBVRRenderer"));
		this->view->setShader(renderer);
		this->view->build(*sceneShader->getGLFactory());
		sceneShader->getObjectRenderer()->addScene(this->view);
	}

	updateView();
}

void PhotonCloudPBVRPresenter::removeView(SceneShader* sceneShader)
{
	this->view->release(*sceneShader->getGLFactory());
	sceneShader->getObjectRenderer()->removeScene(this->view);
	delete this->view;
}

void PhotonCloudPBVRPresenter::updateView()
{
	updateScreenView();
	updateParentIdView();
	updateChildIdView();
}

void PhotonCloudPBVRPresenter::updateScreenView()
{
	const auto& ps = model->getPhotons();
	PointBuffer pb;
	for (auto p : ps) {
		pb.add(p->getPosition(), p->getColor(), p->getSize());
	}

	//this->view->setBlend(this->doBlend);
	this->view->send(pb);
	this->view->setVisible(model->isVisible());
}

void PhotonCloudPBVRPresenter::updateParentIdView()
{
}

void PhotonCloudPBVRPresenter::updateChildIdView()
{
}
