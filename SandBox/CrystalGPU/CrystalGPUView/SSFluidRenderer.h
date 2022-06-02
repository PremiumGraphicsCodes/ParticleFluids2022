#pragma once

#include "Crystal/Shader/IRenderer.h"

namespace Crystal {
	namespace Shader {

class SSFluidRenderer : public IRenderer
{
public:
	SSFluidRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	std::string getName() const override { return "SSFluidRenderer"; }

private:
	Shader::ShaderObject* shader;

};

	}
}