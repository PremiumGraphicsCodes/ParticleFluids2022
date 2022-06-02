#include "SSFluidRenderer.h"

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

SSFluidRenderer::SSFluidRenderer() :
	shader(nullptr)
{
}

ShaderBuildStatus SSFluidRenderer::build(GLObjectFactory& factory)
{
	ShaderBuildStatus status;
	status.isOk = true;

	ShaderUnit vs;
	vs.compileFromFile("./GLSL/SSFluid.glvs", ShaderUnit::Stage::VERTEX);

	ShaderUnit fs;
	fs.compileFromFile("./GLSL/SSFluid.glfs", ShaderUnit::Stage::FRAGMENT);

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

void SSFluidRenderer::release(GLObjectFactory& factory)
{
	factory.remove(shader);
}

void SSFluidRenderer::render()
{
	shader->bind();

	/*
	shader->sendUniform(::projectionMatrixLabel, buffer.projectionMatrix);
	shader->sendUniform(::modelViewMatrixLabel, buffer.modelViewMatrix);

	shader->sendVertexAttribute3df(::positionLabel, buffer.position);
	shader->sendVertexAttribute4df(::colorLabel, buffer.color);
	shader->sendVertexAttribute1df(::sizeLabel, buffer.size);

	shader->enableDepthTest();
	shader->enablePointSprite();

	shader->drawPoints(buffer.count);

	shader->bindOutput(::fragColorLabel);

	shader->disablePointSprite();
	shader->disableDepthTest();
	*/

	shader->unbind();

	assert(GL_NO_ERROR == glGetError());
}