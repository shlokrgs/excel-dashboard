import React from "react";
import API from "../api/api";

function DownloadButton() {
  const handleDownload = async () => {
    const response = await API.get("/download/", { responseType: "blob" });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "filtered_data.xlsx");
    document.body.appendChild(link);
    link.click();
  };

  return <button onClick={handleDownload}>Download Filtered Excel</button>;
}

export default DownloadButton;
