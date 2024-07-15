import React, { useState } from "react";
import LengthConverterForm from "./length";
import TimeConverterForm from "./time";
import MassConverterForm from "./mass";
import SpeedConverterForm from "./speed";

const ConverterApp = () => {
  const [selectedConverter, setSelectedConverter] = useState("");

  const renderConverterForm = () => {
    switch (selectedConverter) {
      case "length":
        return <LengthConverterForm />;
      case "time":
        return <TimeConverterForm />;
      case "mass":
        return <MassConverterForm />;
      case "speed":
        return <SpeedConverterForm />;
      default:
        return null;
    }
  };

  return (
    <div>
      <h1>Unit Converter</h1>
      <div>
        <button onClick={() => setSelectedConverter("length")}>Length</button>
        <button onClick={() => setSelectedConverter("time")}>Time</button>
        <button onClick={() => setSelectedConverter("mass")}>Mass</button>
        <button onClick={() => setSelectedConverter("speed")}>Speed</button>
      </div>
      {renderConverterForm()}
    </div>
  );
};

export default ConverterApp;
