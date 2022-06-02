#pragma once

#include "Crystal/Shader/IRenderer.h"

namespace Crystal {
	namespace Shader {

class SSNormalRenderer : public IRenderer
{
public:
	SSNormalRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	std::string getName() const override { return "SSNormalRenderer"; }

private:
	Shader::ShaderObject* shader;

};
	}
}