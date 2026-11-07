import shutil
import os

img_dir = r'D:\Neuromates(website)\assets\images'
mapping = {
    'alzheimers-wearable.jpg': 'page_5_Image-7572533686.jpg',
    'alzheimers-dashboard.jpg': 'page_3_Image-2000805986.jpg',
    'parkinsons-wearable.jpg': 'page_4_Image-9750469207.jpg',
    'parkinsons-dashboard.jpg': 'page_13_Image-6703682664.jpg',
    'epilepsy-headband.jpg': 'page_15_Image-8784015711.jpg',
    'rehab-leg.jpg': 'page_6_Image-8450180107.jpg',
    'rehab-hand.jpg': 'page_7_Image-8659871878.jpg',
    'rehab-face.jpg': 'page_8_Image-5824662338.jpg',
    'rehab-platform.jpg': 'page_12_Image-2708199956.jpg',
    'brain-tech-logo.jpg': 'page_1_Image-7098480789.jpg',
}

for dest, src in mapping.items():
    src_p = os.path.join(img_dir, src)
    dest_p = os.path.join(img_dir, dest)
    if os.path.exists(src_p):
        shutil.copy2(src_p, dest_p)
        print(f"Created friendly alias: {dest}")

