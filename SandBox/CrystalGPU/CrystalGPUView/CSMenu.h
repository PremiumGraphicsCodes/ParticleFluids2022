#pragma once

#include "CrystalScene/AppBase/IMenu.h"

namespace Crystal {
	namespace UI {
		class ControlPanel;

class CSMenu : public IMenu
{
public:
	CSMenu(const std::string& name, Scene::World* model, Canvas* canvas, ControlPanel* control) :
		IMenu(name, model, canvas),
		control(control)
	{}

	virtual void onShow() override;

private:
	ControlPanel* control;
};

	}
}