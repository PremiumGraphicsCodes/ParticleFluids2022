#include "SSThicknessRenderer.h"

//#include "CameraShaderScene.h"

using namespace Crystal::Math;
//using namespace Crystal::Graphics;
using namespace Crystal::Shader;
//using namespace Crystal::Scene;

namespace {
	constexpr auto positionLabel = "position";
	constexpr auto normalLabel = "normal";
	constexpr auto projectionMatrixLabel = "projectionMatrix";
	constexpr auto modelViewMatrixLabel = "modelviewMatrix";
	constexpr auto fragColorLabel = "fragColor";
}

SSThicknessRenderer::SSThicknessRenderer() :
	shader(nullptr)
{
}

ShaderBuildStatus SSThicknessRenderer::build(GLObjectFactory& factory)
{
	ShaderBuildStatus status;
	status.isOk = true;

	ShaderUnit vs;
	vs.compileFromFile("./GLSL/SSThickness.glvs", ShaderUnit::Stage::VERTEX);

	ShaderUnit fs;
	fs.compileFromFile("./GLSL/SSThickness.glfs", ShaderUnit::Stage::FRAGMENT);

	shader = factory.createShaderObject();
	const auto isOk = shader->link({ vs, fs });
	status.log = shader->getLog();
	if (!isOk) {
		status.isOk = false;
		return status;
	}
	/*
	shader->findUniformLocation(::projectionMatrixLabel);
	shader->findUniformLocation(::modelViewMatrixLabel);

	shader->findAttribLocation(::positionLabel);
	shader->findAttribLocation(::normalLabel);
	shader->findAttribLocation(::colorLabel);
	shader->findAttribLocation(::sizeLabel);
	*/

	return status;
}

void SSThicknessRenderer::release(GLObjectFactory& factory)
{
	factory.remove(shader);
}

void SSThicknessRenderer::render()
{
	shader->bind();

	shader->unbind();

	assert(GL_NO_ERROR == glGetError());
}