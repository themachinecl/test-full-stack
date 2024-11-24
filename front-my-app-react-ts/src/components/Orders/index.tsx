import React, { useState } from "react";
import "react-datepicker/dist/react-datepicker.css";
import OrderTable from "../OrderTable";
import Search from "../Search";
import FilterDate from "../FilterDate";
import Paginator from "../Paginator";
import { OrderContainer } from "./style";
import { useOrders } from "../../hook/orderHook";

const Orders: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [orderByTerm, setOrderByTerm] = useState<"asc" | "desc">("asc");
  const [startDateTerm, setStartDateTerm] = useState("");
  const [endDateTerm, setEndDateTerm] = useState("");

  const { ordersList, totalPages, page, setPage, loading, error } = useOrders(
    1,
    {
      order_name: searchTerm,
      order_by: orderByTerm,
      start_date: startDateTerm,
      end_date: endDateTerm,
    }
  );

  if (loading) return <h1>...::: Loading :::...</h1>;
  if (error) return <div>Error: {error}</div>;

  return (
    <OrderContainer>
      <h2>Test Full Stack - JPRF</h2>
      <Search setPage={setPage} setSearchTerm={setSearchTerm} />
      <FilterDate
        setPage={setPage}
        setStartDateTerm={setStartDateTerm}
        setEndDateTerm={setEndDateTerm}
      />
      <OrderTable
        orders={ordersList}
        setPage={setPage}
        setOrderByTerm={setOrderByTerm}
      />
      <Paginator setPage={setPage} page={page} totalPages={totalPages} />
    </OrderContainer>
  );
};
export default Orders;
