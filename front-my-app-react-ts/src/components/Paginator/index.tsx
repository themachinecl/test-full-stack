import React from "react";
import { PageInfo, PaginatorButton, PaginatorContainer } from "./style";

interface Props {
  setPage: (page: any) => any;
  page: number;
  totalPages: number;
}

const Paginator: React.FC<Props> = ({ setPage, page, totalPages }) => {
  const handleNextPage = () => {
    if (page < totalPages) {
      setPage((prev: any) => prev + 1);
    }
  };

  const handlePreviousPage = () => {
    if (page > 1) {
      setPage((prev: any) => prev - 1);
    }
  };
  return (
    <>
      <PaginatorContainer>
        <PaginatorButton onClick={handlePreviousPage} disabled={page === 1}>
          {"<"}
        </PaginatorButton>
        <PageInfo>{`Page ${page} / ${totalPages}`}</PageInfo>
        <PaginatorButton
          onClick={handleNextPage}
          disabled={page === totalPages}
        >
          {">"}
        </PaginatorButton>
      </PaginatorContainer>
    </>
  );
};

export default Paginator;
