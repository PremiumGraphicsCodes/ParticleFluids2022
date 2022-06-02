#pragma once

#include "Crystal/Math/Vector3d.h"
#include "Crystal/Math/Sphere3d.h"
#include "Crystal/Math/Ray3d.h"

////////////////////////////////////////////////////////////////////////////////
// MaterialType
////////////////////////////////////////////////////////////////////////////////
enum MaterialType
{
    Matte = 0,  // Diffuse
    Mirror,     // Specular
    Glass,      // Refract
};


struct SphereObject
{
    Crystal::Math::Vector3dd         color;
    MaterialType    type;
    Crystal::Math::Sphere3dd sphere;

    SphereObject( double r, Crystal::Math::Vector3dd pos, Crystal::Math::Vector3dd col, MaterialType mat )
    : sphere( pos, r )
    , color ( col )
    , type  ( mat )
    { /* DO_NOTHING */ }

    double intersect(const Crystal::Math::Ray3d& ray) const;

private:
};