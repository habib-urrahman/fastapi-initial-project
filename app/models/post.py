from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]

    # Links correctly to the users table
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    #  Now links correctly to the categories table
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    # Relationships
    user: Mapped["User"] = relationship(
        back_populates="posts"
    )

    category: Mapped["Category"] = relationship(
        back_populates="posts"
    )
