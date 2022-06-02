#include "RayTracer.h"

#include "SpaceHash.h"

#include <chrono>

using namespace Crystal::Math;
using namespace Crystal::Photon;

void RayTracer::trace_ray(int w, int h, Scene& scene)
{
    auto start = std::chrono::system_clock::now();

    // trace eye rays and store measurement points
    Ray3d cam(
        Math::Vector3dd(50, 48, 295.6),
        normalize(Math::Vector3dd(0, -0.042612, -1))
    );
    auto cx = Math::Vector3dd(w * 0.5135 / h, 0, 0);
    auto cy = normalize(cross(cx, cam.getDirection())) * 0.5135;

    for (int y = 0; y < h; y++)
    {
        fprintf(stdout, "\rHitPointPass %5.2f%%", 100.0 * y / (h - 1));
        for (int x = 0; x < w; x++)
        {
            auto idx = x + y * w;
            auto d = cx * ((x + 0.5) / w - 0.5) + cy * (-(y + 0.5) / h + 0.5) + cam.getDirection();
            trace(Ray3d(cam.getOrigin() + d * 140.0, normalize(d)), 0, Vector3dd(0,0,0), Vector3dd(1, 1, 1), idx, scene);
        }
    }
    fprintf(stdout, "\n");
    auto end = std::chrono::system_clock::now();
    auto dif = end - start;
    fprintf(stdout, "Ray Tracing Pass : %lld(msec)\n", std::chrono::duration_cast<std::chrono::milliseconds>(dif).count());

    start = std::chrono::system_clock::now();

    // build the hash table over the measurement points
    SpaceHash::build_hash_grid(w, h, scene);

    end = std::chrono::system_clock::now();
    dif = end - start;
    fprintf(stdout, "Build Hash Grid : %lld(msec)\n", std::chrono::duration_cast<std::chrono::milliseconds>(dif).count());
}

void RayTracer::trace(const Ray3d& r, int dpt, const Vector3dd& fl, const Vector3dd& adj, int i, Scene& scene)
{
    double t;
    int id;

    dpt++;
    if (!scene.intersect(r, t, id) || (dpt >= 20))
        return;

    auto d3 = dpt * 3;
    const auto& obj = scene.sph[id];
    auto x = r.getOrigin() + r.getDirection() * t, n = normalize(x - obj.sphere.getCenter());
    auto f = obj.color;
    auto nl = (dot(n, r.getDirection()) < 0) ? n : n * -1.0;
    auto p = (f.x > f.y && f.x > f.z) ? f.x : (f.y > f.z) ? f.y : f.z;

    if (obj.type == MaterialType::Matte)
    {
        {
            // eye ray
            // store the measurment point
            auto hp = new HitRecord;
            hp->f = (f * adj);
            hp->pos = x;
            hp->nrm = n;
            hp->idx = i;
            scene.hitpoints.push_back(hp);

            // find the bounding box of all the measurement points
            scene.hpbbox.add(x);
        }

    }
    else if (obj.type == MaterialType::Mirror)
    {
        trace(Ray3d(x, reflect(r.getDirection(), n)), dpt, (f * fl), (f * adj), i, scene);
    }
    else
    {
        Ray3d lr(x, reflect(r.getDirection(), n));
        auto into = glm::dot(n, nl) > 0.0;
        auto nc = 1.0;
        auto nt = 1.5;
        auto nnt = (into) ? nc / nt : nt / nc;
        auto ddn = dot(r.getDirection(), nl);
        auto cos2t = 1 - nnt * nnt * (1 - ddn * ddn);

        // total internal reflection
        if (cos2t < 0)
            return trace(lr, dpt, (f * fl), (f * adj), i, scene);

        auto td = normalize(r.getDirection() * nnt - n * ((into ? 1 : -1) * (ddn * nnt + sqrt(cos2t))));
        auto a = nt - nc;
        auto b = nt + nc;
        auto R0 = a * a / (b * b);
        auto c = 1 - (into ? -ddn : dot(td, n));
        auto Re = R0 + (1 - R0) * c * c * c * c * c;
        auto P = Re;
        Ray3d  rr(x, td);
        auto fa = (f * adj);
        auto ffl = (f * fl);

        {
            // eye ray (trace both rays)
            trace(lr, dpt, ffl, fa * Re, i, scene);
            trace(rr, dpt, ffl, fa * (1.0 - Re), i, scene);
        }
    }
}