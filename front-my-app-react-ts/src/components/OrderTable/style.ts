import styled from "styled-components";

export const TableContainer = styled.div`
  overflow-x: auto;
  margin: 1rem 0;
  border: 1px solid #ddd;
  border-radius: 8px;
`;

export const StyledTable = styled.table`
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;

  thead {
    background-color: #f4f4f4;
  }

  th,
  td {
    text-align: left;
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }

  th {
    cursor: pointer;
  }

  tr:hover {
    background-color: #f9f9f9;
  }

  @media (max-width: 768px) {
    font-size: 0.9rem;

    th,
    td {
      padding: 8px;
    }
  }
`;

export const TotalAmount = styled.h4`
  font-size: 1.2rem;
  margin-bottom: 1rem;
`;