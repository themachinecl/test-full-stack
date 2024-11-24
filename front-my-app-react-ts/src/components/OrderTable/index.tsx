import React, { Dispatch, SetStateAction, useState } from "react";
import { StyledTable, TableContainer, TotalAmount } from "./style";

interface Order {
  order_name: string;
  customer_company_name: string;
  customer_name: string;
  order_date: string;
  delivered_amount: number;
  total_amount: number;
}

interface Props {
  orders: Order[];
  setPage: (page: number) => void;
  setOrderByTerm?: Dispatch<SetStateAction<"asc" | "desc">>;
}

const OrderTable: React.FC<Props> = ({ orders, setPage, setOrderByTerm }) => {
  const [orderBy, setOrderBy] = useState<"asc" | "desc">("asc");

  const toggleOrder = () => {
    setOrderBy((prev) => (prev === "asc" ? "desc" : "asc"));
    if (setOrderByTerm) {
      setOrderByTerm(orderBy);
    }
    setPage(1);
  };

  const Total_Amount = Number(
    orders?.reduce(
      (sum, order) =>
        sum +
        (isNaN(order.total_amount)
          ? 0
          : parseFloat(order.total_amount.toString())),
      0
    )
  ).toFixed(2);

  return (
    <>
      <TotalAmount>Total Amount: ${Total_Amount}</TotalAmount>
      <TableContainer>
        <StyledTable>
          <thead>
            <tr>
              <th>Order Name</th>
              <th>Customer Company</th>
              <th>Customer Name</th>
              <th onClick={toggleOrder}>Order Date - {orderBy}</th>
              <th>Delivered Amount</th>
              <th>Total Amount</th>
            </tr>
          </thead>
          <tbody>
            {orders?.map((order: any, index: any) => (
              <tr key={index}>
                <td>{order.order_name}</td>
                <td>{order.customer_company_name}</td>
                <td>{order.customer_name}</td>
                <td>{order.order_date}</td>
                <td>$ {order.delivered_amount}</td>
                <td>$ {isNaN(order.total_amount) ? 0 : order.total_amount}</td>
              </tr>
            ))}
          </tbody>
        </StyledTable>
      </TableContainer>
    </>
  );
};

export default OrderTable;
