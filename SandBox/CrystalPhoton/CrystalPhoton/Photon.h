#pragma once

#include "Crystal/Shape/IParticle.h"
#include "Crystal/Graphics/ColorRGBA.h"

namespace Crystal {
	namespace Photon {

class Photon : Shape::IParticle
{
public:
	Photon();

	Photon(const Math::Vector3df& p, const Graphics::ColorRGBAf& c, const float size);

	virtual Math::Vector3dd getPosition() const { return position; }

	Math::Vector3df getPositionf() const { return position; }

	void setPosition(const Math::Vector3df& p) { this->position = p; }

	Graphics::ColorRGBAf getColor() const { return color; }

	float getSize() const { return size; }

	void setDirection(const Math::Vector3df& dir) { this->direction = dir; }

	Math::Vector3df getDirection() const { return direction; }

	bool isAbserved() const { return _isAbsorbed; }

	void setAbserved(const bool b) { this->_isAbsorbed = b; }

private:
	Math::Vector3df position;
	Math::Vector3df direction;
	Graphics::ColorRGBAf color;
	float size;
	bool _isAbsorbed;
};
	}
}