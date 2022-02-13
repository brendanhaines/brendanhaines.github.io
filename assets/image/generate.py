from PIL import Image
from pathlib import Path

image_ext = ["jpg", "png"]

dir_avatar = Path(__file__).parent
orig = [f for f in dir_avatar.iterdir() if f.stem == "avatar_orig" and f.suffix[1:] in image_ext]
if len(orig) == 0:
    raise FileNotFoundError(f'Could not find file named "avatar_orig.[{"|".join(image_ext)}]"')
elif len(orig) > 1:
    raise ValueError(f"Ambiguous source image. Found {', '.join([p.name for p in orig])}")

with Image.open(orig[0]) as im:
    if im.size[0] != im.size[1]:
        s = min(im.size)
        left = (im.size[0] - s)/2
        top = (im.size[1] - s)/2
        right = (im.size[0] + s)/2
        bottom = (im.size[1] + s)/2
        im = im.crop((left, top, right, bottom))

    im.resize([min(im.size[0], 70)] * 2).save(dir_avatar / "avatar.png")

    for s in [16, 32, 57, 60, 70, 72, 76, 96, 114, 120, 128, 144, 150, 152, 180, 192, 310, 384, 512]:
        im.resize([min(im.size[0], s)] * 2).save(dir_avatar / f"favicon-{s}x{s}.png")