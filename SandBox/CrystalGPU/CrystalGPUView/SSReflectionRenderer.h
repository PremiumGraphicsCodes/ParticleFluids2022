#pragma once

#include "Crystal/Shader/IRenderer.h"

namespace Crystal {
	namespace Shader {

class SSReflectionRenderer : public IRenderer
{
public:
	SSReflectionRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	std::string getName() const override { return "SSReflectionRenderer"; }

private:
	Shader::ShaderObject* shader;
};

	}
}