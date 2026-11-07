from PIL import Image

# 1. From ecosystem-architecture-live.jpg (587 x 325)
eco = Image.open(r"D:\Neuromates(website)\assets\images\ecosystem-architecture-live.jpg")
# Patient is top center ~ (200, 30, 380, 160)
patient_crop = eco.crop((215, 35, 335, 155)).resize((160, 160), Image.Resampling.LANCZOS)
patient_crop.save(r"D:\Neuromates(website)\assets\images\person-1.jpg", quality=92)

# Caretaker is right ~ (400, 115, 510, 225)
caretaker_crop = eco.crop((405, 120, 505, 220)).resize((160, 160), Image.Resampling.LANCZOS)
caretaker_crop.save(r"D:\Neuromates(website)\assets\images\person-2.jpg", quality=92)

# Doctor is bottom center ~ (210, 220, 320, 320)
doctor_crop = eco.crop((210, 220, 310, 320)).resize((160, 160), Image.Resampling.LANCZOS)
doctor_crop.save(r"D:\Neuromates(website)\assets\images\person-3.jpg", quality=92)

# Admin is left ~ (25, 120, 125, 220)
admin_crop = eco.crop((25, 120, 125, 220)).resize((160, 160), Image.Resampling.LANCZOS)
admin_crop.save(r"D:\Neuromates(website)\assets\images\person-4.jpg", quality=92)

# 2. From page_5_Image-7572533686.jpg (Caregiver & elderly patient in park)
p5 = Image.open(r"D:\Neuromates(website)\assets\images\page_5_Image-7572533686.jpg")
w5, h5 = p5.size
# Crop elderly lady
lady_crop = p5.crop((int(w5*0.62), int(h5*0.35), int(w5*0.82), int(h5*0.65))).resize((160, 160), Image.Resampling.LANCZOS)
lady_crop.save(r"D:\Neuromates(website)\assets\images\person-5.jpg", quality=92)

# Crop smiling daughter
daughter_crop = p5.crop((int(w5*0.78), int(h5*0.35), int(w5*0.96), int(h5*0.65))).resize((160, 160), Image.Resampling.LANCZOS)
daughter_crop.save(r"D:\Neuromates(website)\assets\images\person-6.jpg", quality=92)

print("Generated person-1 through person-6 avatar photos successfully!")

