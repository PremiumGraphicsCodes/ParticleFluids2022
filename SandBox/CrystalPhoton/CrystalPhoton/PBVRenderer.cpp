#include "PBVRenderer.h"

//#include "CameraShaderScene.h"
#include "Crystal/Shader/ShaderObject.h"
#include "Crystal/Shader/TextureObject.h"
#include "Crystal/Graphics/Image.h"
#include "ImprovedPerlinNoise.h"

#include <sstream>

using namespace Crystal::Math;
using namespace Crystal::Graphics;
using namespace Crystal::Shader;
//using namespace Crystal::Scene;
using namespace Crystal::Photon;

namespace {
	constexpr auto positionLabel = "position";
	constexpr auto colorLabel = "color";
	constexpr auto sizeLabel = "pointSize";
	constexpr auto projectionMatrixLabel = "projectionMatrix";
	constexpr auto modelViewMatrixLabel = "modelviewMatrix";
	constexpr auto fragColorLabel = "fragColor";
	constexpr auto maxRepeatLevelLabel = "maxRepeatLevel";
	constexpr auto currentRepeatLevelLabel = "currentRepeatLevel";
	constexpr auto noiseTextureLabel = "noiseTexture";
}

PBVRenderer::PBVRenderer() :
	shader(nullptr)
{
}

ShaderBuildStatus PBVRenderer::build(GLObjectFactory& factory)
{
	ShaderBuildStatus status;
	status.isOk = true;

	const auto& vsSource = getBuiltInVertexShaderSource();
	const auto& fsSource = getBuiltInFragmentShaderSource();

	ImprovedPerlinNoise noise;
	noise.buildTable();

	Crystal::Graphics::Image image(64,64);
	for (int i = 0; i < 64; ++i) {
		for (int j = 0; j < 64; ++j) {
			const auto r = noise.getNoise(i, j, 0.0);
			const auto g = noise.getNoise(i, j, 1.0);
			const auto b = noise.getNoise(i, j, 2.0);
			const auto a = noise.getNoise(i, j, 3.0);
			Crystal::Graphics::ColorRGBAuc c(r, g, b, 255);
			image.setColor(i, j, c);
		}
	}
	this->noiseTexture = factory.createTextureObject();
	this->noiseTexture->send(image);

	shader = factory.createShaderObject();
	const auto isOk = shader->build(vsSource, fsSource);
	status.log = shader->getLog();
	if (!isOk) {
		status.isOk = false;
		return status;
	}

	shader->findUniformLocation(::projectionMatrixLabel);
	shader->findUniformLocation(::modelViewMatrixLabel);
	shader->findUniformLocation(::maxRepeatLevelLabel);
	shader->findUniformLocation(::currentRepeatLevelLabel);
	shader->findUniformLocation(::noiseTextureLabel);

	shader->findAttribLocation(::positionLabel);
	shader->findAttribLocation(::colorLabel);
	shader->findAttribLocation(::sizeLabel);

	return status;
}

void PBVRenderer::release(GLObjectFactory& factory)
{
	factory.remove(shader);

	//factory.remove()
}

void PBVRenderer::render(const Buffer& buffer)
{
	shader->bind();

	shader->sendUniform(::projectionMatrixLabel, buffer.projectionMatrix);
	shader->sendUniform(::modelViewMatrixLabel, buffer.modelViewMatrix);
	shader->sendUniform(::maxRepeatLevelLabel, buffer.repeatLevel);
	shader->sendUniform(::noiseTextureLabel, *this->noiseTexture, 0);

	shader->sendVertexAttribute3df(::positionLabel, buffer.position);
	shader->sendVertexAttribute4df(::colorLabel, buffer.color);
	shader->sendVertexAttribute1df(::sizeLabel, buffer.size);

	glEnable(GL_BLEND);
	glBlendFunc(GL_ONE, GL_ONE);

	for (int i = 0; i < buffer.repeatLevel; ++i) {
		glClear(GL_DEPTH_BUFFER_BIT);

		shader->sendUniform(::currentRepeatLevelLabel, i);

		shader->enableDepthTest();
		shader->enablePointSprite();

		this->noiseTexture->bind(0);

		shader->drawPoints(buffer.count);

		shader->bindOutput(::fragColorLabel);

		shader->disablePointSprite();
		shader->disableDepthTest();
	}
	glDisable(GL_BLEND);

	this->noiseTexture->unbind();

	shader->unbind();

	assert(GL_NO_ERROR == glGetError());
}

std::string PBVRenderer::getBuiltInVertexShaderSource() const
{
	// noise function is from https://gist.github.com/patriciogonzalezvivo/670c22f3966e662d2f83
	std::ostringstream stream;
	stream
		<< "#version 150" << std::endl
		<< "in vec3 position;" << std::endl
		<< "in float pointSize;" << std::endl
		<< "in vec4 color;" << std::endl
		<< "out vec4 vColor;" << std::endl
		<< "uniform mat4 projectionMatrix;" << std::endl
		<< "uniform mat4 modelviewMatrix;" << std::endl
		<< "uniform sampler2D noiseTexture;" << std::endl
		<< "uniform int currentRepeatLevel;" << std::endl
		<< "float rand(float n){return fract(sin(n) * 43758.5453123);}" << std::endl
		<< "void main(void) {" << std::endl
		<< "	vec3 v = texelFetch(noiseTexture, ivec2(int(mod(gl_VertexID, 64)), currentRepeatLevel), 0).rgb;" << std::endl
//		<< "	float random = rand(float(gl_VertexID));" << std::endl
//		<< "	float n1 = random * 1.0;" << std::endl
//		<< "	float n2 = 0.0;" << std::endl //rand(position.y) * 0.1;" << std::endl
//		<< "	float n3 = 0.0;" << std::endl //rand(position.z) * 0.1;" << std::endl
//		<< "	vec3 v = vec3(n1,n2,n3);" << std::endl
		<< "	gl_Position = projectionMatrix * modelviewMatrix * vec4(position + v * 0.5, 1.0);" << std::endl
		<< "	gl_PointSize = pointSize / gl_Position.w;" << std::endl
		<< "	vColor = color;" << std::endl
		<< "}" << std::endl;
	return stream.str();
}

std::string PBVRenderer::getBuiltInFragmentShaderSource() const
{
	std::ostringstream stream;
	stream
		<< "#version 150" << std::endl
		<< "uniform int maxRepeatLevel;" << std::endl
		<< "in vec4 vColor;" << std::endl
		<< "out vec4 fragColor;" << std::endl
		<< "void main(void) {" << std::endl
		<< "	vec2 coord = gl_PointCoord * 2.0 - 1.0;" << std::endl
		<< "	float distSquared = 1.0 - dot(coord, coord);" << std::endl
		<< "	if (distSquared < 0.0) {" << std::endl
		<< "		discard;" << std::endl
		<< "	}" << std::endl
		<< "	fragColor.rgba = vColor / float(maxRepeatLevel);" << std::endl
//		<< "	float random = rand(gl_FragCoord.xy);" << std::endl
//		<< "	fragColor.r = random;"<< std::endl
//		<< "	fragColor.g = random;" << std::endl
//		<< "	fragColor.b = random;" << std::endl
		<< "}" << std::endl;
	return stream.str();
}

std::string PBVRenderer::getBuiltInGeometryShaderSource() const
{

	std::ostringstream stream;
	stream
		<< "#version 330" << std::endl
		//		<< "#extension GL_EXT_gpu_shader4 : enable" << std::endl
		<< "layout(points) in" << std::endl
		<< "layout(points, max_vertices = 1) out;" << std::endl
		<< "in Vertex" << std::endl
		<< "{" << std::endl
		<< "	vec3 position;" << std::endl
		<< "	vec4 color;" << std::endl
		<< "} vertex[];" << std::endl
		<< "uniform mat4 projectionMatrix;" << std::endl
		<< "uniform mat4 modelviewMatrix;" << std::endl
		<< "uniform float pointSize;" << std::endl
		<< "uniform sampler2D noiseTexture;" << std::endl
		<< "uniform int repetitionLevel;" << std::endl
		<< "uniform float particleDiameter;" << std::endl
		<< "out vec4 color;" << std::endl
		<< "void main() {" << std::endl
		<< "for (int i = 0; i < gl_in.length(); i++) {" << std::endl
		<< "	int howMany = int(vertex[i].color.a * 1.0);" << std::endl
		<< "	float random = texelFetch2D(noiseTexture, ivec2(int(mod(gl_PrimitiveIDIn, 100)), repetitionLevel), 0).a;" << std::endl
		<< "	float over = mod(vertex[i].color.a * 1.0, 1.0);" << std::endl
		<< "	if (over > random) {" << std::endl
		<< "		++howMany;" << std::endl
		<< "	}" << std::endl
		<< "	for (int j = 0; j < howMany; j++) {" << std::endl
		<< "		vec3 noiseVector = texelFetch2D(noiseTexture, ivec2(j, repetitionLevel), 0).rgb - vec3(0.5, 0.5, 0.5);" << std::endl
		<< "		noiseVector *= particleDiameter;" << std::endl
		<< "		vec3 position = vertex[i].position + noiseVector;" << std::endl
		<< "		gl_Position = projectionMatrix * modelviewMatrix * vec4(position, 1.0);" << std::endl
		<< "		float dist = length(gl_Position);" << std::endl
		<< "		gl_PointSize = pointSize / dist;" << std::endl
		<< "		color = vertex[i].color;" << std::endl
		<< "		EmitVertex();" << std::endl
		<< "	}" << std::endl
		<< "	EndPrimitive();" << std::endl
		<< "}" << std::endl;
	return stream.str();
}