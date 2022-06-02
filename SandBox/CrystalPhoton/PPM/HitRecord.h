#pragma once

#include "Crystal/Math/Vector3d.h"

namespace Crystal {
    namespace Photon {

struct HitRecord
{
    Crystal::Math::Vector3dd         pos;
    Crystal::Math::Vector3dd         nrm;
    Crystal::Math::Vector3dd         flux;
    Crystal::Math::Vector3dd         f;
    double          r2;
    unsigned int    n;
    int             idx;
};

    }
}
