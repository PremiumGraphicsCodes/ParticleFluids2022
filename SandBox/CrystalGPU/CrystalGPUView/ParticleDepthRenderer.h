#pragma once

#include "Crystal/Shader/IRenderer.h"

namespace Crystal {
	namespace Shader {

class ParticleDepthRenderer : public IRenderer
{
public:
	ParticleDepthRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	std::string getName() const override { return "ParticleDepthRenderer"; }

private:
	Shader::ShaderObject* shader;
};

	}
}