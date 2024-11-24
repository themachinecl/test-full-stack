import { useEffect, useState } from "react";

interface UseOrdersParams {
  page: number; // Obligatorio
  order_by?: "asc" | "desc"; // Opcional
  order_name?: string; // Opcional
  start_date?: string; // Opcional (Formato: YYYY-MM-DD)
  end_date?: string; // Opcional (Formato: YYYY-MM-DD)
}

interface UseOrdersReturn {
  ordersList: any[]; // Cambia `any` por el tipo específico si lo conoces
  totalPages: number;
  page: number;
  setPage: React.Dispatch<React.SetStateAction<number>>; // Correcto tipo de setPage
  loading: boolean;
  error: string | null;
}

export const useOrders = (
  initialPage: number,
  { order_by, order_name, start_date, end_date }: Partial<UseOrdersParams> = {}
): UseOrdersReturn => {
  const [ordersList, setOrdersList] = useState<any[]>([]); // Lista de órdenes
  const [loading, setLoading] = useState<boolean>(true); // Estado de carga
  const [error, setError] = useState<string | null>(null); // Estado de error
  const [totalPages, setTotalPages] = useState<number>(1); // Total de páginas
  const [page, setPage] = useState<number>(initialPage); // Página actual

  useEffect(() => {
    async function getListOrder() {
      try {
        setLoading(true);
        setError(null); // Reiniciar error antes de una nueva solicitud

        // Construir la URL con parámetros opcionales
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
        setOrdersList(data?.orders || []); // Actualiza la lista de órdenes
        setTotalPages(data?.total_pages || 1); // Actualiza el total de páginas
      } catch (err: any) {
        setError(err.message || "An error occurred");
      } finally {
        setLoading(false); // Finaliza la carga
      }
    }

    getListOrder();
  }, [page, order_by, order_name, start_date, end_date]); // El efecto se dispara cuando cambia cualquier parámetro

  return { ordersList, totalPages, page, setPage, loading, error };
};
