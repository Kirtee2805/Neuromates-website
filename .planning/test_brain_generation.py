import math
import json

def build_brain():
    node_count = 2200
    nodes = []
    
    # Generate left and right hemisphere cortex nodes
    for i in range(node_count):
        side = -1.0 if (i % 2 == 0) else 1.0
        # Fibonacci spiral on hemisphere
        u = (i // 2) / (node_count // 2)
        theta = math.acos(max(-1.0, min(1.0, 1.0 - 2.0 * u)))
        phi = math.sqrt((node_count // 2) * math.pi) * theta

        # Brain dimensions: X = lateral, Y = vertical, Z = anterior-posterior
        # Width ~ 1.05, Height ~ 0.95, Length ~ 1.35
        # Interhemispheric fissure: base gap 0.12 + lateral curvature
        cos_phi = abs(math.cos(phi))
        sin_theta = math.sin(theta)
        
        rx = 0.12 + 0.88 * sin_theta * cos_phi
        ry = math.cos(theta) * 0.95
        rz = sin_theta * math.sin(phi) * 1.35
        
        x = side * rx
        y = ry
        z = rz

        # Anatomical shaping:
        # Cerebellum & brainstem (posterior lower)
        if y < -0.1 and z < -0.2:
            x *= 0.72
            y -= 0.12
            z *= 0.88
        # Temporal lobes (middle lower lateral bulge)
        elif y < 0.0 and abs(z) < 0.45:
            x *= 1.18
            y *= 0.95
        # Frontal lobe (anterior top rounded)
        elif z > 0.4:
            y *= 1.05
            x *= 0.96

        # Cortical folds (sulci & gyri)
        fold = (
            math.sin(x * 8.5) * math.cos(y * 7.5) * 0.055 +
            math.sin(y * 11.0) * math.cos(z * 9.5) * 0.045 +
            math.sin(z * 13.0 + x * 6.0) * 0.035
        )
        
        # Pull slightly inward at fissure
        if abs(x) < 0.2:
            fold -= (0.2 - abs(x)) * 0.25

        mag = math.sqrt(x*x + y*y + z*z)
        if mag > 0:
            x += (x / mag) * fold
            y += (y / mag) * fold
            z += (z / mag) * fold

        nodes.append({"x": round(x, 3), "y": round(y, 3), "z": round(z, 3), "side": side})

    # Find neighbor connections for synaptic axon web
    edges = []
    max_d2 = 0.22 * 0.22
    min_d2 = 0.04 * 0.04
    
    # Spatial binning or step sampling for efficiency
    for i in range(len(nodes)):
        connected = 0
        p1 = nodes[i]
        # check neighboring nodes in list
        for j in range(i + 1, min(i + 35, len(nodes))):
            p2 = nodes[j]
            dx = p1["x"] - p2["x"]
            dy = p1["y"] - p2["y"]
            dz = p1["z"] - p2["z"]
            d2 = dx*dx + dy*dy + dz*dz
            if min_d2 <= d2 <= max_d2:
                edges.append((i, j))
                connected += 1
                if connected >= 3:
                    break
                    
    print(f"Generated {len(nodes)} cortex nodes and {len(edges)} axon edges.")

build_brain()

