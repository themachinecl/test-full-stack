# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class CustomerCompany(Base):
    __tablename__ = 'customer_companies'
    __table_args__ = {'schema': 'public'}

    company_id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".customer_companies_company_id_seq'::regclass)"))
    company_name = Column(String, nullable=False)


class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'public'}

    user_id = Column(String(10), primary_key=True)
    login = Column(String(10), nullable=False)
    password = Column(String(20), nullable=False)
    name = Column(String(20))
    company_id = Column(String(20))
    credit_cards = Column(String(100))


class Delivery(Base):
    __tablename__ = 'deliveries'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".deliveries_id_seq'::regclass)"))
    order_item_id = Column(Numeric(20, 0), nullable=False)
    delivered_quantity = Column(Numeric(20, 0), nullable=False)


class OrderItem(Base):
    __tablename__ = 'order_items'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".order_id_id_seq'::regclass)"))
    order_id = Column(Numeric(20, 0), nullable=False)
    price_per_unit = Column(Float(53))
    quantity = Column(Numeric(20, 0), nullable=False)
    product = Column(String(50))


class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".orders_id_seq'::regclass)"))
    created_at = Column(DateTime(True), nullable=False)
    order_name = Column(String(50), nullable=False)
    customer_id = Column(String(50), nullable=False)
