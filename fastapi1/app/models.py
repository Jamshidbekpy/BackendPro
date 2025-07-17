from sqlalchemy import ForeignKey, Integer, String, Boolean, Table, Column, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base, TimestampMixin

# Many-to-many connector table for Book and Tag
Books_Tags = Table(
    "books_tags",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    books: Mapped[list["UserBook"]] = relationship("UserBook", back_populates="user")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="user")

    def __str__(self):
        return self.username


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="category")

    def __str__(self):
        return self.name


class Publisher(Base, TimestampMixin):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    logo: Mapped[str] = mapped_column(String(255), nullable=False)
    website: Mapped[str] = mapped_column(String(255), nullable=False)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="publisher")

    def __str__(self):
        return self.name


class Author(Base, TimestampMixin):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str] = mapped_column(String(255), nullable=True)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")

    def __str__(self):
        return self.full_name


class Book(Base, TimestampMixin):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    isbn: Mapped[str] = mapped_column(String(13), nullable=False, unique=True)
    cover: Mapped[str] = mapped_column(String(255), nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    publisher_id: Mapped[int] = mapped_column(ForeignKey("publishers.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    category: Mapped[Category] = relationship("Category", back_populates="books")
    publisher: Mapped[Publisher] = relationship("Publisher", back_populates="books")
    author: Mapped[Author] = relationship("Author", back_populates="books")

    tags: Mapped[list["Tag"]] = relationship(
        secondary=Books_Tags, back_populates="books"
    )

    user_books: Mapped[list["UserBook"]] = relationship(
        "UserBook", back_populates="book"
    )
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="book")
    
    category: Mapped[Category] = relationship("Category", back_populates="books")
    author: Mapped[Author] = relationship("Author", back_populates="books")
    publisher: Mapped[Publisher] = relationship("Publisher", back_populates="books")

    def __str__(self):
        return self.name


class UserBook(Base):
    __tablename__ = "user_books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    current_page: Mapped[int] = mapped_column(Integer, default=0)
    started_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    finished_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped[User] = relationship("User", back_populates="books")
    book: Mapped[Book] = relationship("Book", back_populates="user_books")


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    reply_to: Mapped[int] = mapped_column(
        Integer, ForeignKey("comments.id"), nullable=True
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped[User] = relationship("User", back_populates="comments")
    book: Mapped[Book] = relationship("Book", back_populates="comments")


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    books: Mapped[list[Book]] = relationship(
        secondary=Books_Tags, back_populates="tags"
    )
    
    
    
    
    
    
