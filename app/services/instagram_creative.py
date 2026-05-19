"""
instagram_creative.py
---------------------
Protótipo do pipeline de criação de conteúdo para Instagram.
"""

# ---------------------------------------------------------------------------
# MÓDULO 1 — TRENDING
# ---------------------------------------------------------------------------

def fetch_trending_keywords(geo: str = "BR", top_n: int = 10) -> list[dict]:

    return [
        {"keyword": "Academia", "score": 95}
    ]


# ---------------------------------------------------------------------------
# MÓDULO 2 — GERAÇÃO DE CONTEÚDO
# ---------------------------------------------------------------------------

def generate_caption_and_prompt(keyword: str, **kwargs) -> dict:

    return {
        "caption": f"🔥 Confira novidades sobre {keyword}!",
        "hashtags": ["#fitness", "#gym", "#trend"],
        "image_prompt": f"Imagem moderna sobre {keyword}"
    }


# ---------------------------------------------------------------------------
# MÓDULO 3 — GERAÇÃO DE IMAGEM
# ---------------------------------------------------------------------------

def generate_image(image_prompt: str, **kwargs) -> bytes:

    return b"fake_image_bytes"


# ---------------------------------------------------------------------------
# PIPELINE PRINCIPAL
# ---------------------------------------------------------------------------

def run_pipeline(geo: str = "BR") -> dict:

    # 1. Busca a trend mais alta
    trends = fetch_trending_keywords(geo=geo)

    keyword = trends[0]["keyword"]

    # 2. Gera legenda e prompt
    content = generate_caption_and_prompt(keyword)

    # 3. Gera imagem
    image_bytes = generate_image(content["image_prompt"])

    # 4. Retorna resultado final
    return {
        "keyword": keyword,
        "caption": content["caption"],
        "hashtags": content["hashtags"],
        "full_caption": content["caption"] + "\n\n" + " ".join(content["hashtags"]),
        "image": image_bytes,
    }


# ---------------------------------------------------------------------------
# TESTE
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    creative = run_pipeline(geo="BR")

    print("KEYWORD:", creative["keyword"])
    print("LEGENDA:", creative["full_caption"])
    print("IMAGEM:", len(creative["image"]), "bytes")