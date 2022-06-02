#pragma once

#include "Scene.h"

constexpr double ALPHA = 0.7; // the alpha parameter of PPM

namespace Crystal {
    namespace Photon {

class SpaceHash {
public:
    static unsigned int hash(const int ix, const int iy, const int iz, const Scene& scene);

    static void build_hash_grid(const int w, const int h, Scene& scene);
};

    }
}