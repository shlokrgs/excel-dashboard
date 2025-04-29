import React, { useState } from "react";
import API from "../api/api";

function FilterData({ availableColumns, setFilteredData }) {
  const [filters, setFilters] = useState({});

  const handleChange = (column, value) => {
    setFilters({ ...filters, [column]: value });
  };

  const handleFilter = async () => {
    const res = await API.post("/filter/", filters);
    setFilteredData(res.data.filtered_data_preview);
  };

  return (
    <div>
      {availableColumns.map((col, idx) => (
        <div key={idx}>
          <input placeholder={`Filter ${col}`} onChange={(e) => handleChange(col, e.target.value)} />
        </div>
      ))}
      <button onClick={handleFilter}>Apply Filters</button>
    </div>
  );
}

export default FilterData;
