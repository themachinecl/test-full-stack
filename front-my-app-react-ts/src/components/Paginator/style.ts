import styled from "styled-components";

export const PaginatorContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding: 0.5rem;
  background-color: #f8f9fa; 
  border: 1px solid #dee2e6; 
  border-radius: 5px;
`;

export const PageInfo = styled.span`
  font-size: 1rem;
  font-weight: 500;
  color: #495057; 
`;

export const PaginatorButton = styled.button`
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff;
  background-color: #007bff; 
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #0056b3; 
  }

  &:disabled {
    background-color: #6c757d; 
    cursor: not-allowed;
  }
`;