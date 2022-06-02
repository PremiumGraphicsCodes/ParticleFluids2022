#pragma once

#include "Crystal/Shader/IRenderer.h"

namespace Crystal {
	namespace Shader {

class SSAbsorptionRenderer : public IRenderer
{
public:
	SSAbsorptionRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	//void render(const Buffer& buffer);

	//void renderBlend(const Buffer& buffer);

	std::string getName() const override { return "SSAbsorptionRenderer"; }

private:
	Shader::ShaderObject* shader;

};
	}
}