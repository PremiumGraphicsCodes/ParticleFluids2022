#include "CSSampleRenderer.h"

#include "Crystal/Graphics/ColorRGBA.h"
//#include "../Scene/ParticleSystemScene.h"

#include "Crystal/Shader/ShaderUnit.h"

#include <random>
#include <iostream>

using namespace Crystal::Math;
using namespace Crystal::Graphics;
using namespace Crystal::Shader;
using namespace Crystal::Scene;
using namespace Crystal::UI;


// see https://kakashibata.hatenablog.jp/entry/2020/08/31/001306
namespace {

	const char* compute_shader_source = R"(
#version 430

uniform int element_size;

layout(std430, binding = 3) buffer layout_dst
{
    float dst[];
};

layout(local_size_x = 256, local_size_y = 1, local_size_z = 1) in;

void main() {
    uint index = gl_GlobalInvocationID.x;
    if (index >= element_size) { return; }

    dst[index] = mix(0.0, 3.141592653589, float(index) / element_size);
}
)";
}

CSSampleRenderer::CSSampleRenderer()
{
};

ShaderBuildStatus CSSampleRenderer::build(GLObjectFactory& factory)
{
    ShaderBuildStatus status;
    status.isOk = true;

    ShaderUnit computeShader;
    const auto isOk = computeShader.compile(compute_shader_source, ShaderUnit::Stage::COMPUTE);
    assert(isOk == true);

    shader = factory.createShaderObject();
    shader->link({ computeShader });

    status.log = shader->getLog();
    if (!isOk) {
        status.isOk = false;
        return status;
    }

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }



    // create buffer
    shader->findUniformLocation("element_size");
    glGenBuffers(1, &ssbo);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, ssbo);
    glBufferData(GL_SHADER_STORAGE_BUFFER, num * sizeof(float), nullptr, GL_DYNAMIC_COPY);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }
    return status;
}

void CSSampleRenderer::release(GLObjectFactory& factory)
{
    /*
    glDeleteBuffers(1, &ssbo);
    shader.clear();

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }
    */
}

void CSSampleRenderer::render()
{


 //   glUseProgram(shader.getID());
    shader->bind();

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }

    shader->sendUniform("element_size", num);

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }

    //glUniform1ui(uniform_element_size, num);
    glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 3, ssbo);

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }


    glDispatchCompute(num / 256 + 1, 1, 1);

    shader->unbind();

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }

    std::vector<float> data(num);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, ssbo);
    glGetBufferSubData(GL_SHADER_STORAGE_BUFFER, 0, num * sizeof(float), data.data());
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);

    for (auto v : data) { std::cout << v << '\n'; }

    {
        const auto error = glGetError();
        assert(GL_NO_ERROR == error);
    }


}