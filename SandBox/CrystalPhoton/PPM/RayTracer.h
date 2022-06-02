#pragma once

#include "Scene.h"

namespace Crystal {
    namespace Photon {

class RayTracer
{
public:
    void trace_ray(int w, int h, Scene& scene);

private:
    void trace(const Math::Ray3d& r, int dpt, const Math::Vector3dd& fl, const Math::Vector3dd& adj, int i, Scene& scene);
    
};

    }
}