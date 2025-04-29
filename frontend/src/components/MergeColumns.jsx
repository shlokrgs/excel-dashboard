import React, { useState } from "react";
import API from "../api/api";

function MergeColumns({ setAvailableColumns }) {
  const [mergeKeys, setMergeKeys] = useState([{ left: "", right: "" }]);

  const handleChange = (index, side, value) => {
    const keys = [...mergeKeys];
    keys[index][side] = value;
    setMergeKeys(keys);
  };

  const handleAddKey = () => {
    setMergeKeys([...mergeKeys, { left: "", right: "" }]);
  };

  const handleMerge = async () => {
    const selectedColumns = {
      left: mergeKeys.map((k) => k.left),
      right: mergeKeys.map((k) => k.right),
    };
    const res = await API.post("/merge/", selectedColumns);
    setAvailableColumns(res.data.columns);
    alert("Files Merged Successfully");
  };

  return (
    <div>
      {mergeKeys.map((key, index) => (
        <div key={index}>
          <input placeholder="Left Column" value={key.left} onChange={(e) => handleChange(index, "left", e.target.value)} />
          <input placeholder="Right Column" value={key.right} onChange={(e) => handleChange(index, "right", e.target.value)} />
        </div>
      ))}
      <button onClick={handleAddKey}>Add More Merge Keys</button>
      <button onClick={handleMerge}>Merge Files</button>
    </div>
  );
}

export default MergeColumns;
