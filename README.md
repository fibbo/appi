# APPI - Intermediate Python Course

This is my try at contributing to APPI

# Capstone Project (`tiny_raytracer`)

The idea of the capstone project is based on tinyraytracer, a 256 line C++ ray-tracer - rewritten in Python [tinyraytracer](https://github.com/ssloy/tinyraytracer).

It uses a scene description of materials, spheres and lights and uses this scene to render an image based on the law of physics (diffuse light, ambient light, reflection, refraction).

The key class is the `Vector` class. Even though there is no heritance involved it shows many of the overload methods like `__add__`, `__sub__`.

Implementing the `Vector` functions is the primary exercise of the first course. Once all unit tests (contained in `test_vector.py`) succeed it should be safe to continue.

Inheritance can be shown in a smaller side example.

The web part will be achieved by providing a screen description as text file online. The students will need to get the description and parse it to create the scene objects.

The plan is to provide later a second scene description in JSON which allows then for easier parsing.

## chapters

Contains a folder for each chapter for this course. Each subfolder contains at least a `README.md`. Other files might be example source code related to the chapter.

## src (tbd)

This folder will contain Python source files. Potentially with subfolders like `examples` for particular examples.



## Powerpoint

The presentation is shared here: https://1drv.ms/p/s!AlQXFUn0ctPihfpVTOoC7x7xzudaPA?e=rvk7Mc

## TODO
* Add json scene description
* Add json scene parser