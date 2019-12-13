import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

import MapChart from "./components/Map/Map.js";

function App() {
  return (
    <div>
      <MapChart />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
