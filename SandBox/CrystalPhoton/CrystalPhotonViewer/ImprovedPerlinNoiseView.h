#pragma once

#include "CrystalScene/AppBase/IOkCancelView.h"

#include "CrystalScene/Scene/World.h"
#include "CrystalScene/AppBase/Canvas.h"
#include "CrystalScene/AppBase/ImageView.h"

namespace Crystal {
	namespace UI {

class ImprovedPerlinNoiseView : public UI::IOkCancelView
{
public:
	ImprovedPerlinNoiseView(const std::string& name, Scene::World* world, Canvas* canvas);

private:
	void onBuild();

	void onOk() override;

private:
	Button buildButton;
	ImageView imageView;
};

	}
}