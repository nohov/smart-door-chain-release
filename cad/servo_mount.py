"""Printable wall mount for a TowerPro MG996R servo."""

from build123d import Align, Box, Cylinder, Pos


def gen_step():
    flat = (Align.CENTER, Align.CENTER, Align.MIN)
    plate = Box(92, 62, 4, align=flat)
    sleeve = Pos(0, 0, 4) * (
        Box(60, 28.7, 26.8, align=flat)
        - Box(41.7, 20.7, 26.8, align=flat)
    )
    part = plate + sleeve
    for x in (-39, 39):
        for y in (-24, 24):
            part -= Pos(x, y, 0) * Cylinder(2.1, 4, align=flat)
    part -= Pos(-25.5, 0, 4) * Box(11, 12, 9, align=flat)
    assert len(part.solids()) == 1 and part.is_valid
    assert abs(part.bounding_box().size.Z - 30.8) < 0.01
    return {
        "shape": part,
        "step_output": "../parts/servo_mount.step",
        "export_stl": True,
        "stl_output": "../parts/servo_mount.stl",
    }


if __name__ == "__main__":
    from pathlib import Path
    from build123d import export_step, export_stl

    result = gen_step()
    for key, exporter in (("step_output", export_step), ("stl_output", export_stl)):
        path = (Path(__file__).parent / result[key]).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        exporter(result["shape"], path)
