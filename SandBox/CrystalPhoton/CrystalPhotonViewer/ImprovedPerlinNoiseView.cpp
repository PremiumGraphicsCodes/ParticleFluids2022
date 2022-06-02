#include "ImprovedPerlinNoiseView.h"

#include "../CrystalPhoton/ImprovedPerlinNoise.h"

using namespace Crystal::Graphics;
using namespace Crystal::Scene;
using namespace Crystal::UI;
using namespace Crystal::Photon;

ImprovedPerlinNoiseView::ImprovedPerlinNoiseView(const std::string& name, World* world, Canvas* canvas) :
	IOkCancelView(name, world, canvas),
	buildButton("Build"),
	imageView("Image")
{
	add(&buildButton);
	buildButton.setFunction([=]() { onBuild(); });

	add(&imageView);
	//add(&stepButton);
	//stepButton.setFunction([=]() { onStep(); });
}

void ImprovedPerlinNoiseView::onBuild()
{
	Image image(64,64);
	ImprovedPerlinNoise noise;
	noise.buildTable();
	for (int i = 0; i < 64; ++i) {
		for (int j = 0; j < 64; ++j) {
			const auto u = (double)i; // / 64.0;
			const auto v = (double)j; // / 64.0;
			const auto n = noise.getNoise(u, v, 0.0);
			ColorRGBAuc c(n,n,n,n);
			image.setColor(i, j, c);
		}
	}
	imageView.setValue(image);
}

void ImprovedPerlinNoiseView::onOk()
{

}

//add(&buildButton);
//buildButton.setFunction([=]() { onBuild(); });
