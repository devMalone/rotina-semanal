"""
PWA Asset Generator - Antigravity Dev Standards
Gera automaticamente manifest.json e conjunto completo de icones PNG (180, 192, 512, favicon)
para instalacao de Progressive Web Apps no Android, iOS e Desktop.
"""

import os
import sys
import json
import argparse
from PIL import Image, ImageDraw, ImageFont

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join([c*2 for c in hex_str])
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def create_base_icon(size, bg_color_hex, accent_color_hex, symbol_char, logo_path=None):
    """Cria uma imagem mestre em alta resolução com cantos arredondados sutis ou canvas sólido."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    bg_rgb = hex_to_rgb(bg_color_hex)
    accent_rgb = hex_to_rgb(accent_color_hex)
    
    # Fundo com cantos arredondados modernos
    radius = int(size * 0.22)
    draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=bg_rgb)
    
    # Se uma imagem de logo foi fornecida, redimensiona e centraliza
    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert('RGBA')
            max_inner = int(size * 0.65)
            logo.thumbnail((max_inner, max_inner), Image.Resampling.LANCZOS)
            offset_x = (size - logo.width) // 2
            offset_y = (size - logo.height) // 2
            img.paste(logo, (offset_x, offset_y), logo)
            return img
        except Exception as e:
            print(f"[Aviso] Falha ao processar imagem de logo ({e}). Usando gerador tipografico.", file=sys.stderr)
            
    # Caso contrário, desenha um emblema geométrico sofisticado
    # Circulo sutil interno
    inner_pad = int(size * 0.12)
    circle_box = [inner_pad, inner_pad, size - inner_pad, size - inner_pad]
    inner_bg = (
        min(255, bg_rgb[0] + 15),
        min(255, bg_rgb[1] + 18),
        min(255, bg_rgb[2] + 25),
        255
    )
    draw.ellipse(circle_box, fill=inner_bg, outline=accent_rgb, width=max(2, int(size * 0.025)))
    
    # Glifo ou símbolo central
    char_to_draw = symbol_char.upper() if symbol_char else "A"
    
    # Tenta carregar uma fonte elegante do sistema (Segoe UI, Arial, Roboto)
    font = None
    font_size = int(size * 0.45)
    candidate_fonts = [
        "C:\\Windows\\Fonts\\segoeuib.ttf",
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    ]
    for fp in candidate_fonts:
        if os.path.exists(fp):
            try:
                font = ImageFont.truetype(fp, font_size)
                break
            except Exception:
                continue
                
    if font is None:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), char_to_draw, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    # Desenho centralizado compensando a baseline
    x = (size - w) / 2 - bbox[0]
    y = (size - h) / 2 - bbox[1]
    draw.text((x, y), char_to_draw, fill=accent_rgb, font=font)
    
    return img

def generate_pwa(name, short_name, theme_color, bg_color, accent_color, symbol, output_dir, logo_path=None):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Gerar imagem mestre de 1024x1024
    master_icon = create_base_icon(1024, bg_color, accent_color, symbol, logo_path)
    
    # 2. Gerar variantes
    sizes = {
        'icon-512.png': 512,
        'icon-192.png': 192,
        'apple-touch-icon.png': 180,
        'favicon.png': 64
    }
    
    generated_files = []
    for filename, s in sizes.items():
        resized = master_icon.resize((s, s), Image.Resampling.LANCZOS)
        path = os.path.join(output_dir, filename)
        resized.save(path, 'PNG', optimize=True)
        generated_files.append(filename)
        print(f"✓ Gerado: {filename} ({s}x{s}px)")
        
    # 3. Gerar manifest.json
    manifest_data = {
        "name": name,
        "short_name": short_name,
        "description": f"Aplicacao web progressiva {name}.",
        "start_url": "./index.html",
        "display": "standalone",
        "orientation": "portrait-primary",
        "background_color": bg_color,
        "theme_color": theme_color,
        "lang": "pt-BR",
        "icons": [
            {
                "src": "icon-192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any"
            },
            {
                "src": "icon-512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any"
            },
            {
                "src": "icon-512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "maskable"
            }
        ]
    }
    
    manifest_path = os.path.join(output_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
        
    print(f"✓ Gerado: manifest.json")
    
    print("\n--- Snippet para o <head> do seu index.html ---")
    print(f"""<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="{theme_color}">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{short_name}">
""")

def main():
    parser = argparse.ArgumentParser(description="PWA Asset Generator - Antigravity")
    parser.add_argument("--name", default="Minha Aplicacao", help="Nome completo do PWA")
    parser.add_argument("--short-name", default="App", help="Nome curto do app para a tela inicial")
    parser.add_argument("--theme-color", default="#0f172a", help="Cor do tema (hex, ex: #0f172a)")
    parser.add_argument("--bg-color", default="#0f172a", help="Cor de fundo (hex, ex: #0f172a)")
    parser.add_argument("--accent-color", default="#6366f1", help="Cor de destaque (hex, ex: #6366f1)")
    parser.add_argument("--symbol", default="", help="Letra ou caractere simbolo (ex: 'R', 'P')")
    parser.add_argument("--logo", default=None, help="Caminho opcional para arquivo de logo")
    parser.add_argument("--output-dir", default=".", help="Diretório de destino")
    
    args = parser.parse_args()
    sym = args.symbol if args.symbol else (args.short_name[0] if args.short_name else "A")
    generate_pwa(args.name, args.short_name, args.theme_color, args.bg_color, args.accent_color, sym, args.output_dir, args.logo)

if __name__ == "__main__":
    main()
