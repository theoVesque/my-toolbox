import React, { useState } from "react";
import axios from "axios";
import config from "../../../config";

const LengthConverterForm = () => {
  const [value, setValue] = useState("");
  const [fromUnit, setFromUnit] = useState("m");
  const [toUnit, setToUnit] = useState("km");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${config.apiUrl}/api/converter/length`,
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
            <option value="m">Meters</option>
            <option value="km">Kilometers</option>
            <option value="cm">Centimeters</option>
            <option value="mm">Millimeters</option>
            <option value="mile">Miles</option>
            <option value="yard">Yards</option>
            <option value="foot">Feet</option>
            <option value="inch">Inches</option>
          </select>
        </div>
        <div>
          <label>To Unit:</label>
          <select value={toUnit} onChange={(e) => setToUnit(e.target.value)}>
            <option value="m">Meters</option>
            <option value="km">Kilometers</option>
            <option value="cm">Centimeters</option>
            <option value="mm">Millimeters</option>
            <option value="mile">Miles</option>
            <option value="yard">Yards</option>
            <option value="foot">Feet</option>
            <option value="inch">Inches</option>
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

export default LengthConverterForm;
