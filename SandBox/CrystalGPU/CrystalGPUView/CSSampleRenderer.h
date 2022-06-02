#pragma once

#include "CrystalScene/AppBase/IOkCancelView.h"

namespace Crystal {
	namespace Shader {

// Compute Shader sample.
class CSSampleRenderer : public IRenderer
{
public:
	CSSampleRenderer();

	ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render();

	std::string getName() const override { return "CSSampleRenderer"; }

private:
	Shader::ShaderObject* shader;
	GLuint ssbo;
	int num = 100;
};


	}
}