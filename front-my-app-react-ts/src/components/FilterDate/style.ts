import styled from "styled-components";

import "react-datepicker/dist/react-datepicker.css"; 
export const Container = styled.div`
  padding: 1rem;
`;

export const DatePickerContainer = styled.div`
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;

  span {
    font-size: 1rem;
    font-weight: 500;
  }

  .react-datepicker-wrapper {
    width: auto; 
  }

  .react-datepicker__input-container input {
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
    width: 120px;
  }

  button {
    padding: 0.5rem 1rem;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 4px;
    cursor: pointer;

    &:hover {
      background-color: #0056b3;
    }
  }
`;
