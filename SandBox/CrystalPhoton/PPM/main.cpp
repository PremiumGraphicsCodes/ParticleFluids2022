//-------------------------------------------------------------------------------------------
// File : main.cpp
// Desc : expanded smallppm (code is exactly the same as smallppm.cpp but with more comments)
//        Original Code by T.Hachisuka (http://users-cs.au.dk/toshiya/)
//-------------------------------------------------------------------------------------------

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <vector>
#include <chrono>

#include "bitmap.h"
#include "SphereObject.h"
#include "hitrecord.h"

#include "Scene.h"
#include "SpaceHash.h"
#include "PhotonMap.h"
#include "RayTracer.h"

using namespace Crystal::Math;
using namespace Crystal::Photon;


int main(int argc, char **argv) 
{
    auto w = 512;      // 画像の横幅.
    auto h = 512;      // 画像の縦幅.
    auto s = 1000;     // s * 1000 photon paths will be traced
    auto c = new Vector3dd[ w * h ];

    Scene scene;
    scene.hpbbox = Box3dd::createDegeneratedBox();

    RayTracer rayTracer;
    rayTracer.trace_ray(w, h, scene);

    Crystal::Photon::PhotonMap photonMap;
    photonMap.trace_photon( s, scene );
    photonMap.density_estimation( c, s, scene.hitpoints );

    save_to_bmp( "image.bmp", w, h, &c[0].x, 2.2 );

    delete [] c;
    c = nullptr;

    return 0;
}
