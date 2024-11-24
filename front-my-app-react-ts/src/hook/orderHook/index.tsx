import { useEffect, useState } from "react";

interface UseOrdersParams {
  page: number;
  order_by?: "asc" | "desc";
  order_name?: string;
  start_date?: string;
  end_date?: string;
}

interface UseOrdersReturn {
  ordersList: any[];
  totalPages: number;
  page: number;
  setPage: React.Dispatch<React.SetStateAction<number>>;
  loading: boolean;
  error: string | null;
}

export const useOrders = (
  initialPage: number,
  { order_by, order_name, start_date, end_date }: Partial<UseOrdersParams> = {}
): UseOrdersReturn => {
  const [ordersList, setOrdersList] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [totalPages, setTotalPages] = useState<number>(1);
  const [page, setPage] = useState<number>(initialPage);

  useEffect(() => {
    async function getListOrder() {
      try {
        setLoading(true);
        setError(null);

        const params = new URLSearchParams({ page: page.toString() });
        if (order_by) params.append("order_by", order_by);
        if (order_name) params.append("order_name", order_name);
        if (start_date) params.append("start_date", start_date);
        if (end_date) params.append("end_date", end_date);

        const response = await fetch(
          `http://localhost:5000/orders?${params.toString()}`
        );
        if (!response.ok) {
          throw new Error("Error Server");
        }
        const data = await response.json();
        setOrdersList(data?.orders || []);
        setTotalPages(data?.total_pages || 1);
      } catch (err: any) {
        setError(err.message || "An error occurred");
      } finally {
        setLoading(false);
      }
    }
    getListOrder();
  }, [page, order_by, order_name, start_date, end_date]);

  return { ordersList, totalPages, page, setPage, loading, error };
};
