from fastapi import APIRouter

from app.services.instagram_creative import run_pipeline

from app.database import SessionLocal
from app.models.post_model import Post

router = APIRouter()


@router.get("/generate")
def generate():

    creative = run_pipeline()

    db = SessionLocal()

    new_post = Post(
        keyword=creative["keyword"],
        caption=creative["caption"],
        hashtags=" ".join(creative["hashtags"])
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    db.close()

    return {
        "id": new_post.id,
        "keyword": creative["keyword"],
        "caption": creative["caption"],
        "hashtags": creative["hashtags"]
    }

@router.get("/posts")
def list_posts():

    db = SessionLocal()

    posts = db.query(Post).all()

    db.close()

    return posts

@router.get("/posts/{post_id}")
def get_post(post_id: int):

    db = SessionLocal()

    post = db.query(Post).filter(Post.id == post_id).first()

    db.close()

    return post