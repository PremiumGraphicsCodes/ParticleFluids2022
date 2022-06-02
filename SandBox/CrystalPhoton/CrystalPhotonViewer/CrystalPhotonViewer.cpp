#include "CrystalScene/AppBase/Window.h"
#include "CrystalScene/AppBase/FileMenu.h"
#include "CrystalScene/AppBase/CameraMenu.h"
#include "CrystalScene/AppBase/MaskMenu.h"
#include "CrystalScene/AppBase/CtrlMenu.h"
#include "CrystalScene/AppBase/ScreenMenu.h"
#include "CrystalScene/AppBase/ShapeMenu.h"
#include "CrystalScene/AppBase/AppearanceMenu.h"
#include "CrystalScene/AppBase/SelectionMenu.h"
#include "CrystalScene/AppBase/SceneListPanel.h"
#include "CrystalScene/AppBase/ControlPanel.h"
#include "CrystalScene/AppBase/Canvas.h"

#include "../CrystalPhoton/PBVRenderer.h"

#include "PhotonMenu.h"

//#include "../../Crystal/Scene/World.h"

using namespace Crystal::Math;
using namespace Crystal::Graphics;
using namespace Crystal::Scene;
using namespace Crystal::UI;

using namespace Crystal::Photon;

#include <iostream>

int main(int, char**)
{
	World world;
	Canvas canvas;

	Window window("CrystalViewer", &world, &canvas);
	if (!window.init()) {
		assert(false);
		return 0;
	}

	auto pbvrRenderer = std::make_unique<PBVRenderer>();
	pbvrRenderer->build(*world.getRenderer()->getGLFactory());
	world.getRenderer()->getRenderers()->addRenderer(std::move(pbvrRenderer));

	auto control = new ControlPanel("Control", &world, &canvas);
	window.add(control);

	window.add(new FileMenu("File", &world, &canvas));
	window.add(new CameraMenu("Camera", &world, &canvas));
	window.add(new MaskMenu("Mask", &world, &canvas));
	window.add(new CtrlMenu("Ctrl", &world, &canvas));
	window.add(new ScreenMenu("Screen", &world, &canvas));
	window.add(new ShapeMenu("Shape", &world, &canvas, control));
	window.add(new AppearanceMenu("Appearance", &world, &canvas, control));
	window.add(new SelectionMenu("Selection", &world, &canvas, control));
	window.add(new PhotonMenu("Photon", &world, &canvas, control));

	window.add(new SceneListPanel("SceneList", &world, &canvas, control));

	window.show();

	return 0;
}