import React, { useState } from "react";
import Plot from "react-plotly.js";

function ChartVisualizer({ filteredData }) {
  const [xAxis, setXAxis] = useState("");
  const [yAxis, setYAxis] = useState("");

  const plotData = filteredData.map((row) => ({
    x: row[xAxis],
    y: row[yAxis],
  }));

  return (
    <div>
      <input placeholder="X-Axis Column" onChange={(e) => setXAxis(e.target.value)} />
      <input placeholder="Y-Axis Column" onChange={(e) => setYAxis(e.target.value)} />
      <Plot
        data={[
          {
            x: plotData.map(p => p.x),
            y: plotData.map(p => p.y),
            type: "bar",
          },
          {
            x: plotData.map(p => p.x),
            y: plotData.map(p => p.y),
            type: "scatter",
            mode: "lines+markers",
          },
          {
            labels: plotData.map(p => p.x),
            values: plotData.map(p => p.y),
            type: "pie",
          }
        ]}
        layout={{ width: 800, height: 600, title: "Dynamic Chart" }}
      />
    </div>
  );
}

export default ChartVisualizer;
