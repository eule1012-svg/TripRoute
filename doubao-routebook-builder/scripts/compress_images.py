#!/usr/bin/env python3
"""批量压缩图片，供 HTML 路书内嵌使用。
用法: python3 compress_images.py <输入目录> [输出目录] [长边px] [quality]
默认: 输入目录(含 jpg/jpeg/png) → 同目录, 长边 760px, quality 52
要求: pip install pillow
"""
import os, sys
from PIL import Image

def compress(src_dir, out_dir=None, max_side=760, quality=52):
    if out_dir is None:
        out_dir = src_dir
    os.makedirs(out_dir, exist_ok=True)
    total_before = total_after = 0
    exts = (".jpg", ".jpeg", ".png")
    for fn in sorted(os.listdir(src_dir)):
        if not fn.lower().endswith(exts):
            continue
        src = os.path.join(src_dir, fn)
        dst = os.path.join(out_dir, fn)
        if src == dst:
            # 输出到临时再覆盖，避免边读边写
            tmp = dst + ".tmp"
        else:
            tmp = dst
        im = Image.open(src)
        im = im.convert("RGB")
        w, h = im.size
        if max(w, h) > max_side:
            scale = max_side / max(w, h)
            im = im.resize((round(w*scale), round(h*scale)), Image.LANCZOS)
        before = os.path.getsize(src)
        im.save(tmp, "JPEG", quality=quality, optimize=True)
        after = os.path.getsize(tmp)
        os.replace(tmp, dst)
        total_before += before
        total_after += after
        print(f"{fn}: {w}x{h} -> {im.size}, {before/1024:.0f}KB -> {after/1024:.0f}KB")
    print(f"\n合计: {total_before/1024/1024:.2f}MB -> {total_after/1024/1024:.2f}MB")

if __name__ == "__main__":
    args = sys.argv[1:]
    src = args[0] if len(args) > 0 else "."
    out = args[1] if len(args) > 1 else None
    side = int(args[2]) if len(args) > 2 else 760
    q = int(args[3]) if len(args) > 3 else 52
    compress(src, out, side, q)
