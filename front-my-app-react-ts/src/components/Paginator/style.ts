import styled from "styled-components";

export const PaginatorContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding: 0.5rem;
  background-color: #f8f9fa; /* Color de fondo suave */
  border: 1px solid #dee2e6; /* Borde gris claro */
  border-radius: 5px;
`;

export const PageInfo = styled.span`
  font-size: 1rem;
  font-weight: 500;
  color: #495057; /* Gris oscuro */
`;

export const PaginatorButton = styled.button`
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff;
  background-color: #007bff; /* Azul Bootstrap */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #0056b3; /* Azul oscuro al pasar el mouse */
  }

  &:disabled {
    background-color: #6c757d; /* Gris cuando está deshabilitado */
    cursor: not-allowed;
  }
`;