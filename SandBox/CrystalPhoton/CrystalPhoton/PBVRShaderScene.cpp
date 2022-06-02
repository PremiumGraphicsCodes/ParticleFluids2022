#include "PBVRShaderScene.h"

//#include "PBVR.h"

using namespace Crystal::Graphics;
using namespace Crystal::Shader;
using namespace Crystal::Scene;
using namespace Crystal::Photon;

PBVRShaderScene::PBVRShaderScene(const std::string& name) :
	IShaderScene(name),
	shader(nullptr)
{}

bool PBVRShaderScene::build(GLObjectFactory& glFactory)
{
	rBuffer.position.build();
	rBuffer.size.build();
	rBuffer.color.build();

	return true;
}

void PBVRShaderScene::release(GLObjectFactory& glFactory)
{
	rBuffer.position.release();
	rBuffer.size.release();
	rBuffer.color.release();

	//vao.release();
}

void PBVRShaderScene::send(const PointBuffer& buffer)
{
	const auto& positions = buffer.getPosition().get();
	const auto& colors = buffer.getColor().get();
	const auto& sizes = buffer.getSize().get();

	if (positions.empty()) {
		return;
	}

	// TODO : 乱数テーブルを送っておく．
	rBuffer.position.send(positions);
	rBuffer.size.send(sizes);
	rBuffer.color.send(colors);
	//vao.unbind();

	rBuffer.count = static_cast<int>(positions.size() / 3);
	//	rBuffer.matrix = buffer.getMatrix();
}

void PBVRShaderScene::render(const Graphics::Camera& camera)
{
	if (!isVisible()) {
		return;
	}

	rBuffer.modelViewMatrix = camera.getModelViewMatrix();
	rBuffer.projectionMatrix = camera.getProjectionMatrix();

	shader->render(rBuffer);
}

void PBVRShaderScene::setShader(PBVRenderer* shader)
{
	this->shader = shader;
}
