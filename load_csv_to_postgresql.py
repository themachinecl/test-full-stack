from flask import Flask, jsonify, request
from sqlalchemy import func
from models import db, Order, Customer, CustomerCompany, Delivery, OrderItem  # Importa tus modelos
from pytz import timezone

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

@app.route('/orders', methods=['GET'])
def get_orders():
    """Obtiene la lista de órdenes con información detallada y paginación."""
    melbourne_tz = 'Australia/Melbourne'

    # Parámetros de paginación
    page = request.args.get('page', default=1, type=int)  # Página actual
    per_page = 5  # Elementos por página

    # Consulta actualizada basada en el modelo proporcionado
    query = db.session.query(
        Order.order_name.label('order_name'),
        CustomerCompany.company_name.label('customer_company_name'),
        Customer.name.label('customer_name'),
        func.timezone(melbourne_tz, Order.created_at).label('order_date'),  # Fecha en Melbourne TZ
        func.coalesce(func.sum(Delivery.delivered_quantity), 0).label('delivered_amount'),  # Usa 0 si no hay entregas
        func.sum(OrderItem.price_per_unit * OrderItem.quantity).label('total_amount')  # Total calculado
    ).join(Customer, Customer.user_id == Order.customer_id) \
     .join(CustomerCompany, CustomerCompany.company_id == Customer.company_id) \
     .outerjoin(OrderItem, OrderItem.order_id == Order.id) \
     .outerjoin(Delivery, Delivery.order_item_id == OrderItem.id) \
     .group_by(Order.id, CustomerCompany.company_name, Customer.name)

    # Paginación
    paginated_orders = query.paginate(page=page, per_page=per_page, error_out=False)

    # Formatear el resultado como JSON
    result = {
        "page": paginated_orders.page,
        "per_page": paginated_orders.per_page,
        "total_pages": paginated_orders.pages,
        "total_items": paginated_orders.total,
        "orders": [
            {
                "order_name": order.order_name,
                "customer_company_name": order.customer_company_name,
                "customer_name": order.customer_name,
                "order_date": order.order_date.strftime('%b %d, %I:%M %p').replace(" 0", " ").replace(", 0", " ") if order.order_date else None,
                "delivered_amount": "-" if order.delivered_amount == 0 else str(order.delivered_amount),
                "total_amount": str(order.total_amount) if order.total_amount else "0.00"
            }
            for order in paginated_orders.items
        ]
    }

    return jsonify(result), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True)
