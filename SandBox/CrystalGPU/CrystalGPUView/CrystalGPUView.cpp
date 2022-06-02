#include "CrystalScene/AppBase/Window.h"
#include "CrystalScene/AppBase/FileMenu.h"
#include "CrystalScene/AppBase/CameraMenu.h"
#include "CrystalScene/AppBase/CtrlMenu.h"
#include "CrystalScene/AppBase/ShapeMenu.h"
#include "CrystalScene/AppBase/AppearanceMenu.h"
#include "CrystalScene/AppBase/SceneListPanel.h"
#include "CrystalScene/AppBase/Canvas.h"
#include "CrystalScene/AppBase/ControlPanel.h"

#include "CrystalScene/Scene/World.h"


#include "SSNormalRenderer.h"
#include "SSAbsorptionRenderer.h"
#include "SSThicknessRenderer.h"
#include "ParticleDepthRenderer.h"
#include "SSFluidRenderer.h"
#include "SSReflectionRenderer.h"

#include "CSSampleRenderer.h"

#include <cassert>

using namespace Crystal::Math;
using namespace Crystal::Graphics;
using namespace Crystal::Scene;
using namespace Crystal::UI;

using namespace Crystal::Shader;

int main(int, char**)
{
	World world;
	Canvas canvas;

	Window window("FluidStudio", &world, &canvas);
	if (!window.init()) {
		assert(false);
		return 0;
	}

	auto glFactory = world.getRenderer()->getGLFactory();
	auto renderers = world.getRenderer()->getRenderers();
	std::unique_ptr<SSNormalRenderer> ssNormalRenderer = std::make_unique<SSNormalRenderer>();
	const auto status1 = ssNormalRenderer->build(*glFactory);
	assert(status1.isOk);
	std::unique_ptr<SSAbsorptionRenderer> ssAbsorptionRenderer = std::make_unique<SSAbsorptionRenderer>();
	const auto status2 = ssAbsorptionRenderer->build(*glFactory);
	assert(status2.isOk);
	std::unique_ptr<SSThicknessRenderer> ssThicknessRenderer = std::make_unique<SSThicknessRenderer>();
	const auto status3 = ssThicknessRenderer->build(*glFactory);
	assert(status3.isOk);
	std::unique_ptr<SSReflectionRenderer> ssReflectionRenderer = std::make_unique<SSReflectionRenderer>();
	const auto status4 = ssReflectionRenderer->build(*glFactory);
	assert(status4.isOk);
	std::unique_ptr<ParticleDepthRenderer> pdRenderer = std::make_unique<ParticleDepthRenderer>();
	pdRenderer->build(*glFactory);
	std::unique_ptr<SSFluidRenderer> ssfr = std::make_unique<SSFluidRenderer>();
	ssfr->build(*glFactory);
	renderers->addRenderer(std::move(ssNormalRenderer));
	renderers->addRenderer(std::move(ssAbsorptionRenderer));
	renderers->addRenderer(std::move(ssThicknessRenderer));
	renderers->addRenderer(std::move(pdRenderer));
	renderers->addRenderer(std::move(ssfr));

	std::unique_ptr<CSSampleRenderer> csSampleRenderer = std::make_unique<CSSampleRenderer>();
	const auto status11 = csSampleRenderer->build(*glFactory);
	assert(status11.isOk);
	renderers->addRenderer(std::move(csSampleRenderer));

	auto control = new ControlPanel("Control", &world, &canvas);
	window.add(control);

	window.add(new FileMenu("File", &world, &canvas));
	window.add(new CameraMenu("Camera", &world, &canvas));
	window.add(new CtrlMenu("Ctrl", &world, &canvas));
	window.add(new ShapeMenu("Shape", &world, &canvas, control));
	window.add(new AppearanceMenu("Appearance", &world, &canvas, control));
	//window.add(new CSMenu("ComputeShader", &world, &canvas, control));

	window.add(new SceneListPanel("Scene", &world, &canvas, control));

	window.show();

	return 0;
}

