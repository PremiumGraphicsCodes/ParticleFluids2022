#include "Photon.h"

using namespace Crystal::Math;
using namespace Crystal::Graphics;
using namespace Crystal::Photon;

Photon::Photon() :
	Photon(Vector3df(0, 0, 0), Graphics::ColorRGBAf(0, 0, 0, 0), 1.0f)
{};

Photon::Photon(const Vector3df& p, const ColorRGBAf& c, const float size) :
	position(p),
	color(c),
	size(size),
	direction(1, 0, 0),
	_isAbsorbed(false)
{}
