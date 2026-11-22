from PIL import Image

map_img = Image.open("tourist_map.png").convert("RGB")
qr_img = Image.open("giveaway.png").convert("L")

# Resize QR
qr_img.thumbnail((500, 500))

r, g, b = map_img.split()

blue = b.load()
qr = qr_img.load()

# QR dimensions come from the Image object
qr_width, qr_height = qr_img.size

# Position QR in bottom-right
x0 = map_img.width - qr_width - 100
y0 = map_img.height - qr_height - 100

for y in range(qr_height):
    for x in range(qr_width):
        px = x0 + x
        py = y0 + y

        if qr[x, y] < 128:
            # Set blue-channel LSB to 0
            blue[px, py] &= 0xFE
        else:
            # Set blue-channel LSB to 1
            blue[px, py] |= 0x01

result = Image.merge("RGB", (r, g, b))
result.save("india_tourist_map.png")

print("Created india_tourist_map.png")
print(f"QR size: {qr_width}x{qr_height}")
print(f"Position: {x0},{y0}")
