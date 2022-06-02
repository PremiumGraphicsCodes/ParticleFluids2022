#include "SpaceHash.h"

using namespace Crystal::Math;
using namespace Crystal::Photon;


unsigned int SpaceHash::hash(const int ix, const int iy, const int iz, const Scene& scene)
{
    return (unsigned int)(
        (ix * 73856093) ^
        (iy * 19349663) ^
        (iz * 83492791)) % scene.hash_grid.size();
}

void SpaceHash::build_hash_grid
(
    const int w,
    const int h,
    Scene& scene
)
{
    // heuristic for initial radius
    auto size = scene.hpbbox.getLength();
    auto irad = ((size.x + size.y + size.z) / 3.0) / ((w + h) / 2.0) * 2.0;

    // determine hash table size
    // we now find the bounding box of all the measurement points inflated by the initial radius
    scene.hpbbox = Box3dd::createDegeneratedBox();
    auto photon_count = 0;
    for (auto itr = scene.hitpoints.begin(); itr != scene.hitpoints.end(); ++itr)
    {
        auto hp = (*itr);
        hp->r2 = irad * irad;
        hp->n = 0;
        hp->flux = Vector3dd(0,0,0);

        photon_count++;
        scene.hpbbox.add(hp->pos - irad);
        scene.hpbbox.add(hp->pos + irad);
    }

    // make each grid cell two times larger than the initial radius
    scene.hash_s = 1.0 / (irad * 2.0);

    // build the hash table
    scene.hash_grid.resize(photon_count);
    scene.hash_grid.shrink_to_fit();
    for (auto itr = scene.hitpoints.begin(); itr != scene.hitpoints.end(); ++itr)
    {
        auto hp = (*itr);
        auto min = ((hp->pos - irad) - scene.hpbbox.getMin()) * scene.hash_s;
        auto max = ((hp->pos + irad) - scene.hpbbox.getMin()) * scene.hash_s;

        for (int iz = abs(int(min.z)); iz <= abs(int(max.z)); iz++)
        {
            for (int iy = abs(int(min.y)); iy <= abs(int(max.y)); iy++)
            {
                for (int ix = abs(int(min.x)); ix <= abs(int(max.x)); ix++)
                {
                    int hv = hash(ix, iy, iz, scene);
                    scene.hash_grid[hv].push_back(hp);
                }
            }
        }
    }
}