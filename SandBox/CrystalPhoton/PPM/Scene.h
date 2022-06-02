#pragma once

#include <list>
#include <vector>
#include <array>

#include "hitrecord.h"
#include "SphereObject.h"

#include "Crystal/Math/Box3d.h"

namespace Crystal {
    namespace Photon {

class Scene {
public:
    Scene();

    std::list<HitRecord*>               hitpoints;
    std::vector<std::list<HitRecord*> > hash_grid;
    double                              hash_s;
    Math::Box3dd hpbbox;

    std::vector<SphereObject> sph;

    bool intersect(const Math::Ray3d& r, double& t, int& id);
};

    }
}