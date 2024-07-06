import React, { useState } from "react";
import axios from "axios";
import config from "../../../config/config";

const SpeedConverterForm = () => {
  const [value, setValue] = useState("");
  const [fromUnit, setFromUnit] = useState("m/s");
  const [toUnit, setToUnit] = useState("km/h");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${config.apiUrl}/api/converter/speed`,
        {
          value: parseFloat(value),
          from_unit: fromUnit,
          to_unit: toUnit,
        }
      );
      setResult(response.data.converted_value);
    } catch (error) {
      console.error("There was an error!", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Value:</label>
          <input
            type="number"
            value={value}
            onChange={(e) => setValue(e.target.value)}
          />
        </div>
        <div>
          <label>From Unit:</label>
          <select
            value={fromUnit}
            onChange={(e) => setFromUnit(e.target.value)}
          >
            <option value="m/s">m/s</option>
            <option value="km/h">km/h</option>
            <option value="mph">mph</option>
            <option value="knot">knot</option>
          </select>
        </div>
        <div>
          <label>To Unit:</label>
          <select value={toUnit} onChange={(e) => setToUnit(e.target.value)}>
            <option value="m/s">m/s</option>
            <option value="km/h">km/h</option>
            <option value="mph">mph</option>
            <option value="knot">knot</option>
          </select>
        </div>
        <button type="submit">Convert</button>
      </form>
      {result !== null && (
        <div>
          <p>Converted Value: {result}</p>
        </div>
      )}
    </div>
  );
};

export default SpeedConverterForm;
