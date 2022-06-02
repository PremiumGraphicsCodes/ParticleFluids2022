#include "CrystalScene/AppBase/IMenu.h"

namespace Crystal {
	namespace UI {
		class ControlPanel;

class PhotonMenu : public IMenu
{
public:
	PhotonMenu(const std::string& name, Scene::World* world, Canvas* canvas, ControlPanel* control);

	void onShow() override;

private:
	ControlPanel* control;
	/*
	PSGenerationMenu particleSystemMenu;
	WFGenerationMenu wireFrameMenu;
	PMGenerationMenu polygonMeshMenu;
	SolidGenerationMenu solidMenu;
	TransformMenu transformMenu;
	*/
};

	}
}