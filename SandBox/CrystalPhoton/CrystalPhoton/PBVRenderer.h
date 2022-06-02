#pragma once

#include "Crystal/Math/Vector3d.h"
#include "Crystal/Math/Matrix4d.h"
#include "Crystal/Graphics/Buffer1d.h"
#include "Crystal/Graphics/Buffer3d.h"
#include "Crystal/Graphics/Buffer4d.h"
#include "Crystal/Shader/IRenderer.h"
#include "Crystal/Shader/VertexBufferObject.h"
#include "Crystal/Shader/GLObjectFactory.h"
#include "Crystal/Shader/ShaderBuildStatus.h"
#include <string>

namespace Crystal {
	namespace Photon {

struct PBVRBuffer
{
	Graphics::Buffer3d<float> positions;
	Graphics::Buffer1d<float> sizes;
	Graphics::Buffer1d<float> colors;
};

class PBVRenderer : public Shader::IRenderer
{
public:
	struct Buffer
	{

		Shader::VertexBufferObject position;
		Shader::VertexBufferObject size;
		Shader::VertexBufferObject color;
		Math::Matrix4dd projectionMatrix;
		Math::Matrix4dd modelViewMatrix;
		int count = 0;
		int repeatLevel = 10;
		//int currentRepeatLevel = 1;
	};

	PBVRenderer();

	Shader::ShaderBuildStatus build(Shader::GLObjectFactory& factory) override;

	void release(Shader::GLObjectFactory& factory) override;

	void render(const Buffer& buffer);

	std::string getName() const override { return "PBVRRenderer"; }

private:
	std::string getBuiltInGeometryShaderSource() const;

	std::string getBuiltInVertexShaderSource() const;

	std::string getBuiltInFragmentShaderSource() const;

	Shader::ShaderObject* shader;
	Shader::TextureObject* noiseTexture;
};

	}
}