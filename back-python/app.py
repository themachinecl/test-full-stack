from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Order, Customer, CustomerCompany, Delivery, OrderItem  # Importa tus modelos
from pytz import timezone
from sqlalchemy import func, cast, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)

@app.route('/orders', methods=['GET'])
def get_orders():
    """Obtiene la lista de órdenes con información detallada, paginación, filtros de fechas, búsqueda y ordenamiento."""
    melbourne_tz = 'Australia/Melbourne'

    page = request.args.get('page', default=1, type=int)  
    per_page = request.args.get('per_page', default=5, type=int)  
    offset = (page - 1) * per_page 

    start_date = request.args.get('start_date')  
    end_date = request.args.get('end_date') 
    order_name = request.args.get('order_name')  
    order_by = request.args.get('order_by', default='asc', type=str).lower() 

    query = db.session.query(
        Order.order_name.label('order_name'),
        CustomerCompany.company_name.label('customer_company_name'),
        Customer.name.label('customer_name'),
        func.timezone(melbourne_tz, Order.created_at).label('order_date'),  # Fecha en Melbourne TZ
        func.coalesce(func.sum(Delivery.delivered_quantity), 0).label('delivered_amount'),  # Usa 0 si no hay entregas
        func.coalesce(func.sum(cast(func.coalesce(OrderItem.price_per_unit, 0) * func.coalesce(OrderItem.quantity, 0), Float)), 0).label('total_amount')
    ).join(Customer, Customer.user_id == Order.customer_id) \
     .join(CustomerCompany, CustomerCompany.company_id == Customer.company_id) \
     .outerjoin(OrderItem, OrderItem.order_id == Order.id) \
     .outerjoin(Delivery, Delivery.order_item_id == OrderItem.id)

    if start_date:
        query = query.filter(func.timezone(melbourne_tz, Order.created_at) >= start_date)
    if end_date:
        query = query.filter(func.timezone(melbourne_tz, Order.created_at) <= end_date)
  
    if order_name:
        query = query.filter(Order.order_name.ilike(f"%{order_name}%"))
  
    if order_by == 'asc':
        query = query.order_by(func.timezone(melbourne_tz, Order.created_at).asc())
    elif order_by == 'desc':
        query = query.order_by(func.timezone(melbourne_tz, Order.created_at).desc())

 
    query = query.group_by(Order.id, CustomerCompany.company_name, Customer.name) \
                 .limit(per_page) \
                 .offset(offset)


    total_items_query = db.session.query(func.count(Order.id))
    if start_date:
        total_items_query = total_items_query.filter(func.timezone(melbourne_tz, Order.created_at) >= start_date)
    if end_date:
        total_items_query = total_items_query.filter(func.timezone(melbourne_tz, Order.created_at) <= end_date)
    if order_name:
        total_items_query = total_items_query.filter(Order.order_name.ilike(f"%{order_name}%"))
    total_items = total_items_query.scalar()

    total_pages = (total_items + per_page - 1) 

    #Result
    orders = query.all()
    result = {
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "total_items": total_items,
        "orders": [
            {
                "order_name": order.order_name,
                "customer_company_name": order.customer_company_name,
                "customer_name": order.customer_name,
                "order_date": order.order_date.strftime('%b %d, %I:%M %p').replace(" 0", " ").replace(", 0", " ") if order.order_date else None,
                "delivered_amount": "-" if order.delivered_amount == 0 else str(order.delivered_amount),
                "total_amount": str(order.total_amount)  
            }
            for order in orders
        ]
    }

    return jsonify(result), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
