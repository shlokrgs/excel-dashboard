import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import MergeColumns from "./components/MergeColumns";
import FilterData from "./components/FilterData";
import DownloadButton from "./components/DownloadButton";
import ChartVisualizer from "./components/ChartVisualizer";

function App() {
  const [filesUploaded, setFilesUploaded] = useState(false);
  const [availableColumns, setAvailableColumns] = useState([]);
  const [filteredData, setFilteredData] = useState([]);

  return (
    <div className="App">
      <h1>Excel Dashboard</h1>
      <FileUpload setFilesUploaded={setFilesUploaded} />
      {filesUploaded && (
        <>
          <MergeColumns setAvailableColumns={setAvailableColumns} />
          <FilterData availableColumns={availableColumns} setFilteredData={setFilteredData} />
          <DownloadButton />
          <ChartVisualizer filteredData={filteredData} />
        </>
      )}
    </div>
  );
}

export default App;
