#include "Scene.h"

using namespace Crystal::Math;
using namespace Crystal::Photon;

Scene::Scene()
{
    // Scene: radius, position, color, material

    sph.push_back(SphereObject(1e5, Math::Vector3dd(1e5 + 1, 40.8, 81.6), Math::Vector3dd(0.99, 0.01, 0.01), MaterialType::Matte));   //Right
    sph.push_back(SphereObject(1e5, Math::Vector3dd(-1e5 + 99, 40.8, 81.6), Math::Vector3dd(0.01, 0.01, 0.99), MaterialType::Matte));   //Left
    sph.push_back(SphereObject(1e5, Math::Vector3dd(50, 40.8, 1e5), Math::Vector3dd(0.75, 0.75, 0.75), MaterialType::Matte));   //Back
    sph.push_back(SphereObject(1e5, Math::Vector3dd(50, 40.8, -1e5 + 170), Math::Vector3dd(0.0, 0.0, 0.0), MaterialType::Matte));   //Front
    sph.push_back(SphereObject(1e5, Math::Vector3dd(50, 1e5, 81.6), Math::Vector3dd(0.75, 0.75, 0.75), MaterialType::Matte));   //Bottomm
    sph.push_back(SphereObject(1e5, Math::Vector3dd(50, -1e5 + 81.6, 81.6), Math::Vector3dd(0.75, 0.75, 0.75), MaterialType::Matte));   //Top
    sph.push_back(SphereObject(16.5, Math::Vector3dd(27, 16.5, 47), Math::Vector3dd(0.25, 0.85, 0.25), MaterialType::Mirror));   //Mirror
    sph.push_back(SphereObject(16.5, Math::Vector3dd(73, 16.5, 88), Math::Vector3dd(0.99, 0.99, 0.99), MaterialType::Glass));   //Glass
    sph.push_back(SphereObject(8.5, Math::Vector3dd(50, 8.5, 60), Math::Vector3dd(0.75, 0.75, 0.75), MaterialType::Matte));   //Middle
}

bool Scene::intersect(const Ray3d& r, double& t, int& id)
{
    int n = sph.size();
    auto d = std::numeric_limits<double>::max();
    t = std::numeric_limits<double>::max();
    for (int i = 0; i < n; i++)
    {
        d = sph[i].intersect(r);
        if (d < t)
        {
            t = d;
            id = i;
        }
    }

    return (t < std::numeric_limits<double>::max());
}
