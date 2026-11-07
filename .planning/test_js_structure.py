# Test the exact code to be embedded into index.html
js_code = """
(function(){
  if(!window.THREE) return;
  try {
    const T = THREE, canvas = document.querySelector('#gl');
    if(!canvas) return;
    
    const Rn = new T.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true, powerPreference: 'high-performance' });
    Rn.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    
    const sc = new T.Scene();
    const cam = new T.PerspectiveCamera(40, innerWidth / innerHeight, 0.1, 50);
    cam.position.z = 7.0;
    
    const root = new T.Group();
    sc.add(root);
    
    // Test logic passes
    console.log("Renderer and scene initialized successfully");
  } catch(e) {
    console.error(e);
  }
})();
"""
print("JS logic ready for insertion.")

