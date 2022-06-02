//References:
//http://pybind11.readthedocs.io/en/stable/classes.html
//https://qiita.com/ignis_fatuus/items/c7523c0fe2bc2f415d50
//https://qiita.com/exy81/items/e309df7e33d4ff20a91a#_reference-c8a52580111447fade09
//http://pybind11.readthedocs.io/en/stable/advanced/classes.html#operator-overloading
//http://pybind11.readthedocs.io/en/stable/classes.html#overloaded-methods

#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // vector—p
#include <pybind11/operators.h>//operator
#include "Crystal/Math/Vector3d.h"
#include "Crystal/Math/Triangle3d.h"

#include "CrystalScene/Scene/World.h"
#include "CrystalScene/Command/CommandFactory.h"
#include "CrystalSpace/CrystalSpaceCommand/SpaceCommandFactory.h"
#include "CrystalPhysics/CrystalPhysicsCommand/PhysicsCommandFactory.h"
//#include "../../CrystalVDB/VDBCommand/VDBCommandFactory.h"

using namespace Crystal::Math;

namespace {

    class Vector3dfVector
    {
    public:
        std::vector<Vector3df> values;

        Vector3dfVector()
        {}

        explicit Vector3dfVector(const std::vector<Vector3df>& vs) :
            values(vs)
        {}

        void add(Vector3df v) { this->values.push_back(v); }

        //    Vector3dd get(const int index) { return this->values[i]; }
    };

    class Vector3ddVector
    {
    public:
        Vector3ddVector()
        {}

        explicit Vector3ddVector(const std::vector<Vector3dd>& vs) :
            values(vs)
        {}

        std::vector<Vector3dd> values;

        void add(Vector3dd v) { this->values.push_back(v); }

        //    Vector3dd get(const int index) { return this->values[i]; }
    };

    class Triangle3ddVector
    {
    public:
        Triangle3ddVector()
        {}

        explicit Triangle3ddVector(const std::vector<Triangle3d>& vs) :
            values(vs)
        {}

        std::vector<Triangle3d> values;

        void add(Triangle3d v) { this->values.push_back(v); }
    };

    Crystal::Command::CommandFactory sceneCommandFactory;
    Crystal::Space::SpaceCommandFactory spaceCommandFactory;
    Crystal::Physics::PhysicsCommandFactory physicsCommandFactory;
    //Crystal::VDB::VDBCommandFactory vdbCommandFactory;
    std::unique_ptr<Crystal::Command::ICommand> command;

    void createSceneCommand(const std::string& commandName) {
        command = sceneCommandFactory.createCommand(commandName);
    }

    void createSpaceCommand(const std::string& commandName) {
        command = spaceCommandFactory.create(commandName);
    }

    void createPhysicsCommand(const std::string& commandName) {
        command = physicsCommandFactory.create(commandName);
//        command->execute(&world);
    }

    /*
    void createVDBCommand(const std::string& commandName) {
        command = vdbCommandFactory.createCommand(commandName);
    }
    */

    template<typename T>
    void setArg(const std::string& name, T value) {
        command->setArg(name, value);
    }

    void setArgVector3dfVector(const std::string& name, const Vector3dfVector& vv) {
        command->setArg(name, vv.values);
    }

    void setArgVector3ddVector(const std::string& name, const Vector3ddVector& vv) {
        command->setArg(name, vv.values);
    }

    void setArgTriangle3ddVector(const std::string& name, const Triangle3ddVector& tv) {
        command->setArg(name, tv.values);
    }

    /*
    template<typename T>
    void setArg<T>(const std::string& name, const T& value)
    {

    }
    */

    bool executeCommand(Crystal::Scene::World& world) {
        return command->execute(&world);
    }
    /*
    void setArg(const std::string& name, const std::string& value) {
        command->setArg(name, value);
    }
    */
    template<typename T>
    T getResult(const std::string& name)
    {
        return std::any_cast<T>( command->getResult(name));
    }

    /*
    std::vector<int> getResultIntVector(const std::string& name)
    {
        return std::any_cast<std::vector<int>>(command->getResult(name));
    }

    std::vector<bool> getResultBoolVector(const std::string& name)
    {
        return std::any_cast<std::vector<bool>>(command->getResult(name));
    }
    */

    Vector3dfVector getResultVector3dfVector(const std::string& name)
    {
        const auto vv = std::any_cast<std::vector<Vector3df>>(command->getResult(name));
        return Vector3dfVector(vv);
    }

    Vector3ddVector getResultVector3ddVector(const std::string& name)
    {
        const auto vv = std::any_cast<std::vector<Vector3dd>>(command->getResult(name));
        return Vector3ddVector(vv);
    }

    Triangle3ddVector getResultTriangle3ddVector(const std::string& name)
    {
        const auto tv = std::any_cast<std::vector<Triangle3d>>(command->getResult(name));
        return Triangle3ddVector(tv);
    }
}


namespace py = pybind11;
PYBIND11_MODULE(CrystalPLI, m) {
//    m.doc() = "";

    py::class_<Crystal::Scene::World>(m, "World")
        .def(py::init());

    py::class_<Vector2df>(m, "Vector2df")
        .def(py::init<float, float>())
        .def_readwrite("x", &Vector2df::x)
        .def_readwrite("y", &Vector2df::y);

    py::class_<Vector3df>(m, "Vector3df")
        .def(py::init<float, float, float>())
        .def_readwrite("x", &Vector3df::x)
        .def_readwrite("y", &Vector3df::y)
        .def_readwrite("z", &Vector3df::z);

    py::class_<Vector3dd>(m, "Vector3dd")
        .def(py::init<double, double, double>())
        .def_readwrite("x", &Vector3dd::x)
        .def_readwrite("y", &Vector3dd::y)
        .def_readwrite("z", &Vector3dd::z);

    py::class_<Box3df>(m, "Box3df")
        .def(py::init<>())
        .def(py::init<Vector3df, Vector3df>())
        .def_property_readonly("min", &Box3df::getMin)
        .def_property_readonly("max", &Box3df::getMax);

    py::class_<Box3dd>(m, "Box3dd")
        .def(py::init<>())
        .def(py::init<Vector3dd, Vector3dd>())
        .def_property_readonly("min", &Box3dd::getMin)
        .def_property_readonly("max", &Box3dd::getMax);

    py::class_<Vector3dfVector>(m, "Vector3dfVector")
        .def(py::init<>())
        .def("add", &Vector3dfVector::add)
        .def_readwrite("values", &Vector3dfVector::values);

    py::class_<Vector3ddVector>(m, "Vector3ddVector")
        .def(py::init<>())
        .def("add", &Vector3ddVector::add)
        .def_readwrite("values", &Vector3ddVector::values);
    //    .def_readwrite("add", &std::vector<Vector3df>::push_back);

    py::class_<Triangle3d>(m, "Triangle3dd")
        .def(py::init<Vector3dd, Vector3dd, Vector3dd>())
        .def_property_readonly("v0", &Triangle3d::getV0)
        .def_property_readonly("v1", &Triangle3d::getV1)
        .def_property_readonly("v2", &Triangle3d::getV2);

    py::class_<Triangle3ddVector>(m, "Triangle3ddVector")
        .def(py::init<>())
        .def("add", &Triangle3ddVector::add)
        .def_readwrite("values", &Triangle3ddVector::values);

    py::class_<Crystal::Graphics::ColorRGBAf>(m, "ColorRGBAf")
        .def(py::init<>())
        .def(py::init<float, float, float, float>())
        .def_readwrite("r", &Crystal::Graphics::ColorRGBAf::r)
        .def_readwrite("g", &Crystal::Graphics::ColorRGBAf::g)
        .def_readwrite("b", &Crystal::Graphics::ColorRGBAf::b)
        .def_readwrite("a", &Crystal::Graphics::ColorRGBAf::a);

    m.def("create_scene_command", &createSceneCommand);
    m.def("create_space_command", &createSpaceCommand);
    m.def("create_physics_command", &createPhysicsCommand);
    m.def("execute_command", &executeCommand);
    m.def("set_arg_bool", &setArg<bool>);
    m.def("set_arg_bool_vector", &setArg<std::vector<bool>>);
    m.def("set_arg_int", &setArg<int>);
    m.def("set_arg_int_vector", &setArg<std::vector<int>>);
    m.def("set_arg_float", &setArg<float>);
    m.def("set_arg_float_vector", &setArg<std::vector<float>>);
    m.def("set_arg_double", &setArg<double>);
    m.def("set_arg_double_vector", &setArg<std::vector<double>>);
    m.def("set_arg_string", &setArg<std::string>);
    m.def("set_arg_vector3df", &setArg<Vector3df>);
    m.def("set_arg_vector3dd", &setArg<Vector3dd>);
    m.def("set_arg_box3df", &setArg<Box3df>);
    m.def("set_arg_box3dd", &setArg<Box3dd>);
    m.def("set_arg_triangle3dd", &setArg<Triangle3d>);
    m.def("set_arg_triangle3dd_vector", &setArgTriangle3ddVector);
    m.def("set_arg_vector3df_vector", &setArgVector3dfVector);
    m.def("set_arg_vector3dd_vector", &setArgVector3ddVector);
    m.def("set_arg_color4f", setArg<Crystal::Graphics::ColorRGBAf>);
    m.def("get_result_int", &getResult<int>);
    m.def("get_result_string", &getResult<std::string>);
    m.def("get_result_box3dd", &getResult<Box3dd>);
    m.def("get_result_int_vector", &getResult<std::vector<int>>);
    m.def("get_result_bool_vector", &getResult<std::vector<bool>>);
    m.def("get_result_vector3df_vector", getResultVector3dfVector);
    m.def("get_result_vector3dd_vector", getResultVector3ddVector);
    m.def("get_result_triangle3dd_vector", getResultTriangle3ddVector);
    //m.def("call", &call);
}