from sqlalchemy.orm import Session
from schemas.user import ProfileCreate
from db.models.profile import Profile

def create_profile(profile:ProfileCreate,db:Session, key):
    print(key)
    profile = Profile(
        picture = profile.picture,
        profile_id = key
        )
    print(profile.profile_id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile