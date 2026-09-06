#!/usr/bin/env python3
"""
extract_colors.py — Extração de Paleta de Cores & Mapping para Design System Antigravity

Recebe o caminho de uma imagem de logo (PNG, JPG, WEBP) e gera um relatório JSON 
contendo as cores dominantes, valores HEX/RGB/HSL, e o mapeamento automático para 
os tokens de CSS do Design System do ecossistema Antigravity.
"""

import sys
import json
import os
import math
import warnings
from PIL import Image

# Suppress Pillow deprecation warnings in stdout JSON output
warnings.filterwarnings("ignore", category=DeprecationWarning)

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}".upper()

def rgb_to_hsl(r, g, b):
    r_n, g_n, b_n = r / 255.0, g / 255.0, b / 255.0
    max_c = max(r_n, g_n, b_n)
    min_c = min(r_n, g_n, b_n)
    l = (max_c + min_c) / 2.0

    if max_c == min_c:
        h = s = 0.0
    else:
        d = max_c - min_c
        s = d / (2.0 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r_n:
            h = (g_n - b_n) / d + (6.0 if g_n < b_n else 0.0)
        elif max_c == g_n:
            h = (b_n - r_n) / d + 2.0
        else:
            h = (r_n - g_n) / d + 4.0
        h /= 6.0

    return round(h * 360), round(s * 100), round(l * 100)

def color_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def extract_logo_colors(image_path, num_colors=6):
    if not os.path.exists(image_path):
        return {"error": f"Arquivo não encontrado: {image_path}"}

    try:
        img = Image.open(image_path).convert("RGBA")
    except Exception as e:
        return {"error": f"Erro ao abrir imagem: {str(e)}"}

    # Resize for faster processing while maintaining proportions
    img.thumbnail((300, 300))

    pixels = list(img.getdata())

    # Filter out transparent pixels
    valid_pixels = []
    has_alpha = False

    for r, g, b, a in pixels:
        if a < 30:  # Transparent or semi-transparent
            has_alpha = True
            continue
        valid_pixels.append((r, g, b))

    if not valid_pixels:
        return {"error": "A imagem não contém pixels visíveis."}

    # Create RGB image for quantization
    rgb_img = Image.new("RGB", (len(valid_pixels), 1))
    rgb_img.putdata(valid_pixels)

    # Quantize to find key palette
    method = getattr(Image, 'MEDIANCUT', 0)
    quantized = rgb_img.quantize(colors=num_colors * 2, method=method)
    palette = quantized.getpalette()[:num_colors * 2 * 3]
    color_counts = quantized.getcolors()

    if not color_counts:
        return {"error": "Não foi possível quantizar as cores da imagem."}

    # Sort colors by frequency descending
    sorted_counts = sorted(color_counts, key=lambda x: x[0], reverse=True)

    extracted = []
    total_valid = len(valid_pixels)

    for count, idx in sorted_counts:
        r = palette[idx * 3]
        g = palette[idx * 3 + 1]
        b = palette[idx * 3 + 2]

        # Check for near-duplicates
        is_duplicate = False
        for ext in extracted:
            if color_distance((r, g, b), ext["rgb"]) < 25:
                ext["count"] += count
                ext["percentage"] = round((ext["count"] / total_valid) * 100, 1)
                is_duplicate = True
                break

        if not is_duplicate:
            h, s, l = rgb_to_hsl(r, g, b)
            extracted.append({
                "hex": rgb_to_hex(r, g, b),
                "rgb": [r, g, b],
                "hsl": [h, s, l],
                "count": count,
                "percentage": round((count / total_valid) * 100, 1)
            })

    extracted = sorted(extracted, key=lambda x: x["count"], reverse=True)[:num_colors]

    tokens, suggested_theme = generate_design_tokens(extracted, has_alpha)

    return {
        "status": "success",
        "image_path": image_path,
        "total_pixels_analyzed": total_valid,
        "extracted_palette": extracted,
        "suggested_theme": suggested_theme,
        "tokens": tokens
    }

def generate_design_tokens(extracted, has_alpha):
    if not extracted:
        return {}, "Tema Claro Quente"

    # Saturated vs Neutrals
    saturated = [c for c in extracted if c["hsl"][1] >= 15]
    neutrals = [c for c in extracted if c["hsl"][1] < 15]

    primary_accent = saturated[0] if saturated else extracted[0]
    secondary_accent = saturated[1] if len(saturated) > 1 else (extracted[1] if len(extracted) > 1 else primary_accent)

    r, g, b = primary_accent["rgb"]
    h, s, l = primary_accent["hsl"]

    hover_l = max(5, l - 10) if l > 20 else min(95, l + 15)
    hover_hex = hsl_to_hex(h, s, hover_l)

    soft_rgba = f"rgba({r}, {g}, {b}, 0.12)"

    dark_neutrals = [c for c in neutrals if c["hsl"][2] < 25]
    if dark_neutrals and dark_neutrals[0]["percentage"] > 40:
        suggested_theme = "Tema Escuro Premium"
        bg_primary = "#0F0F0F"
        bg_secondary = "#1A1A1A"
        text_dark = "#F5F5F0"
        text_muted = "#888880"
    elif h >= 15 and h <= 45 and s > 30:
        if l < 40:
            suggested_theme = "Tema Barbearia/Masculino"
            bg_primary = "#F8F6F3"
            bg_secondary = "#EFEBE4"
            text_dark = "#1C1A18"
            text_muted = "#6B5F52"
        else:
            suggested_theme = "Tema Alimentação/Padaria"
            bg_primary = "#FFFEF9"
            bg_secondary = "#FFF8F0"
            text_dark = "#2A1F14"
            text_muted = "#7A6352"
    else:
        suggested_theme = "Tema Claro Quente (Padrão)"
        bg_primary = "#FDFBF7"
        bg_secondary = "#F5F1EB"
        text_dark = "#2C2825"
        text_muted = "#7A6F68"

    tokens = {
        "--accent": primary_accent["hex"],
        "--accent-hover": hover_hex,
        "--accent-soft": soft_rgba,
        "--accent-secondary": secondary_accent["hex"],
        "--bg-primary": bg_primary,
        "--bg-secondary": bg_secondary,
        "--text-dark": text_dark,
        "--text-muted": text_muted,
        "--border": f"rgba({r}, {g}, {b}, 0.15)"
    }

    return tokens, suggested_theme

def hsl_to_hex(h, s, l):
    h_n = h / 360.0
    s_n = s / 100.0
    l_n = l / 100.0

    if s_n == 0:
        r = g = b = l_n
    else:
        def hue2rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p

        q = l_n * (1 + s_n) if l_n < 0.5 else l_n + s_n - l_n * s_n
        p = 2 * l_n - q
        r = hue2rgb(p, q, h_n + 1/3)
        g = hue2rgb(p, q, h_n)
        b = hue2rgb(p, q, h_n - 1/3)

    return rgb_to_hex(round(r * 255), round(g * 255), round(b * 255))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Uso: python extract_colors.py <caminho_da_imagem>"
        }, indent=2, ensure_ascii=False))
        sys.exit(1)

    path = sys.argv[1]
    result = extract_logo_colors(path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
