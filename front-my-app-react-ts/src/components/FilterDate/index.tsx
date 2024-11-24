import React, { useState } from "react";
import DatePicker from "react-datepicker";
import { DatePickerContainer } from "./style";

interface Props {
  setPage: (page: any) => any;
  setStartDateTerm?: (date: string) => void | string;
  setEndDateTerm?: React.Dispatch<React.SetStateAction<string>>;
}

const FilterDate: React.FC<Props> = ({
  setPage,
  setStartDateTerm,
  setEndDateTerm,
}) => {
  const [startDate, setStartDate] = useState<Date | null>(
    new Date("2020-01-03")
  ); // Permitir que sea Date o null
  const [endDate, setEndDate] = useState<Date | null>(new Date("2020-01-03"));

  const handleSearch = () => {
    const formatDate = (date: Date) => date.toISOString().split("T")[0];

    if (startDate && setStartDateTerm) {
      setStartDateTerm(formatDate(startDate));
    }

    if (endDate && setEndDateTerm) {
      setEndDateTerm(formatDate(endDate));
    }

    setPage(1);
  };

  return (
    <DatePickerContainer>
      <span>Created Date:</span>
      <DatePicker
        selected={startDate}
        onChange={(date: Date | null) => setStartDate(date)}
        dateFormat="yyyy-MM-dd"
      />
      {" - "}
      <DatePicker
        selected={endDate}
        onChange={(date: Date | null) => setEndDate(date)}
        dateFormat="yyyy-MM-dd"
      />
      <button onClick={handleSearch}>Buscar</button>
    </DatePickerContainer>
  );
};

export default FilterDate;
