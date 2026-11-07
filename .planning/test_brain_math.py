import math

def generate_brain_points(count=1600):
    points = []
    # Two hemispheres: side in [-1, 1]
    for i in range(count):
        side = -1 if i % 2 == 0 else 1
        u = (i // 2) / (count // 2)
        # Spherical coords
        theta = math.acos(max(-1.0, min(1.0, 1.0 - 2.0 * u)))
        phi = math.sqrt((count // 2) * math.pi) * theta

        # Ellipsoid base with brain-like proportions:
        # width (X) ~ 1.0, height (Y) ~ 1.0, length (Z) ~ 1.3
        # Brain taper: wider in parietal, narrower at frontal/occipital
        x = side * (0.15 + 0.85 * math.sin(theta) * abs(math.cos(phi)))
        y = math.cos(theta) * 0.95
        z = math.sin(theta) * math.sin(phi) * 1.25

        # Temporal lobe bulge & Cerebellum adjustment
        if y < 0 and z < 0:
            # Cerebellum / brainstem
            x *= 0.75
            y -= 0.15
            z *= 0.9
        elif y < -0.1 and abs(z) < 0.4:
            # Temporal lobes
            x *= 1.15

        # Cortical folds (gyri & sulci)
        fold = (
            math.sin(x * 9.0) * math.cos(y * 8.0) * 0.06 +
            math.sin(y * 12.0) * math.cos(z * 10.0) * 0.05 +
            math.sin(z * 15.0 + x * 7.0) * 0.04
        )
        norm = math.sqrt(x*x + y*y + z*z)
        if norm > 0:
            x += (x / norm) * fold
            y += (y / norm) * fold
            z += (z / norm) * fold

        points.append((round(x, 3), round(y, 3), round(z, 3)))
    return points

pts = generate_brain_points(100)
print(f"Generated {len(pts)} test points. Sample:", pts[:5])

