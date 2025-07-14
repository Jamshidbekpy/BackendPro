from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    
    orders = relationship("Order", back_populates="user")
    
class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    order_items = relationship("OrderItem", back_populates="product")
    
class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    created_at: Mapped[int] = mapped_column(Integer)
    
    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

    
class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
