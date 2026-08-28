# Headless Mantaflow FLIP smoke test: tiny inflow into a tiny tank, 24 frames, low res.
# Run: ~/tools/blender/blender -b --python sim/blender/smoke_test.py -- /tmp/manta_smoke
# Success: prints SMOKE_TEST_OK with a nonzero baked-cache file count.
import bpy, os, sys

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
cache_dir = argv[0] if argv else "/tmp/manta_smoke"
os.makedirs(cache_dir, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.frame_start, scene.frame_end = 1, 24

# Domain: 20 cm cube centered at origin top half
bpy.ops.mesh.primitive_cube_add(size=1)
dom = bpy.context.active_object
dom.name = "Domain"
dom.scale = (0.1, 0.1, 0.1)
mod = dom.modifiers.new(name="Fluid", type="FLUID")
mod.fluid_type = "DOMAIN"
ds = mod.domain_settings
ds.domain_type = "LIQUID"
ds.resolution_max = 40
ds.use_flip_particles = True
ds.cache_directory = cache_dir
ds.cache_type = "ALL"

# Inflow: small sphere near top with downward initial velocity
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(0, 0, 0.03))
inflow = bpy.context.active_object
inflow.name = "Inflow"
fm = inflow.modifiers.new(name="Fluid", type="FLUID")
fm.fluid_type = "FLOW"
fs = fm.flow_settings
fs.flow_type = "LIQUID"
fs.flow_behavior = "INFLOW"
fs.use_initial_velocity = True
fs.velocity_coord = (0.0, 0.0, -0.5)

bpy.context.view_layer.objects.active = dom
dom.select_set(True)
bpy.ops.fluid.bake_all()

# Count baked cache artifacts
n = 0
for root, _dirs, files in os.walk(cache_dir):
    n += sum(1 for f in files if f.endswith((".uni", ".vdb", ".bobj.gz")))
print(f"baked cache files: {n}")
print("SMOKE_TEST_OK" if n >= 24 else "SMOKE_TEST_FAIL")
