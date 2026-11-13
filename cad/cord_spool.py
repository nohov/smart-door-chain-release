"""Printable cord spool that screws to the servo's supplied plastic horn."""

from build123d import Align, Cylinder, Pos, Rot


def gen_step():
    flat = (Align.CENTER, Align.CENTER, Align.MIN)
    part = Cylinder(25, 3, align=flat)
    part += Pos(0, 0, 3) * Cylinder(22, 6, align=flat)
    part += Pos(0, 0, 9) * Cylinder(25, 3, align=flat)
    part -= Cylinder(2, 12, align=flat)
    part -= Pos(22, 0, 6) * Rot(Y=90) * Cylinder(1.2, 10)
    assert len(part.solids()) == 1 and part.is_valid
    assert abs(part.bounding_box().size.Z - 12) < 0.01
    return {
        "shape": part,
        "step_output": "../parts/cord_spool.step",
        "export_stl": True,
        "stl_output": "../parts/cord_spool.stl",
    }


if __name__ == "__main__":
    from pathlib import Path
    from build123d import export_step, export_stl

    result = gen_step()
    for key, exporter in (("step_output", export_step), ("stl_output", export_stl)):
        path = (Path(__file__).parent / result[key]).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        exporter(result["shape"], path)
