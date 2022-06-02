#pragma once

#include "CrystalScene/AppBase/IOkCancelView.h"

#include "CrystalScene/AppBase/Sphere3dView.h"
#include "CrystalScene/AppBase/DoubleView.h"

#include "CrystalScene/Scene/World.h"
#include "CrystalScene/AppBase/Canvas.h"

namespace Crystal {
	namespace UI {

class PCSphereView : public UI::IOkCancelView
{
public:
	PCSphereView(const std::string& name, Scene::World* world, Canvas* canvas);

private:
	void onOk();

private:
	Sphere3dView sphereView;
	DoubleView divideLengthView;
};

	}
}