import React, { useState } from "react";
import API from "../api/api";

function FileUpload({ setFilesUploaded }) {
  const [selectedFiles, setSelectedFiles] = useState([]);

  const handleFileChange = (e) => {
    setSelectedFiles(e.target.files);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    for (let file of selectedFiles) {
      formData.append("files", file);
    }
    await API.post("/upload/", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    setFilesUploaded(true);
    alert("Files Uploaded Successfully");
  };

  return (
    <div>
      <input type="file" multiple onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload Files</button>
    </div>
  );
}

export default FileUpload;
