#include "CSMenu.h"
#include "CrystalScene/AppBase/imgui.h"
#include "CrystalScene/AppBase/ControlPanel.h"

using namespace Crystal::Scene;
using namespace Crystal::UI;

void CSMenu::onShow()
{
	auto model = getWorld();
	auto canvas = getCanvas();

	/*
	const auto& c = name.c_str();
	if (ImGui::BeginMenu(c)) {

		if (ImGui::MenuItem("ComputeShader")) {
			control->setWindow(new CSSampleView("CSSample", model, canvas));
		}

		ImGui::EndMenu();
	}
	*/
}
