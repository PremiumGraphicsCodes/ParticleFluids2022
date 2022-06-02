#pragma once

#include "CrystalScene/Scene/IShaderScene.h"
#include "Crystal/Graphics/Camera.h"
#include "CrystalScene/Scene/PointBuffer.h"
#include "PBVRenderer.h"

namespace Crystal {
	namespace Photon {

class PBVRShaderScene : public Scene::IShaderScene
{
public:
	explicit PBVRShaderScene(const std::string& name);

	bool build(Shader::GLObjectFactory& glFactory) override;

	void release(Shader::GLObjectFactory& glFactory) override;

	void render(const Graphics::Camera& camera) override;

	void send(const Scene::PointBuffer& buffer);

	void setShader(PBVRenderer* shader);

private:
	PBVRenderer* shader;
	PBVRenderer::Buffer rBuffer;
};

	}
}