#pragma once

#include "Crystal/Shader/IRenderer.h"

namespace Crystal {
	namespace Shader {

class SSThicknessRenderer : public IRenderer
{
public:
	SSThicknessRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	std::string getName() const override { return "SSThicknessRenderer"; }

private:
	Shader::ShaderObject* shader;

};

	}
}