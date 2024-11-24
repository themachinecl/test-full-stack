import React, { useState } from "react";
import { SearchContainer } from "./style";

interface Props {
  setPage: (page: number) => void;
  setSearchTerm: (term: string) => void; // Función para actualizar el término de búsqueda
}

const Search: React.FC<Props> = ({ setPage, setSearchTerm }) => {
  const [localSearch, setLocalSearch] = useState<string>("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    setLocalSearch(value);
  };

  const handleSearch = () => {
    setPage(1);
    setSearchTerm(localSearch); // Pasar el término al componente principal
  };

  return (
    <SearchContainer>
      <span>Search: </span>
      <input
        type="text"
        placeholder="Search..."
        value={localSearch}
        onChange={handleChange}
      />
      <button onClick={handleSearch}>Buscar</button>
    </SearchContainer>
  );
};

export default Search;
