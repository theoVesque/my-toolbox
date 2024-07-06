import React, { useState } from "react";
import axios from "axios";
import config from "../../../config/config";

const TimeConverterForm = () => {
  const [value, setValue] = useState("");
  const [fromUnit, setFromUnit] = useState("second");
  const [toUnit, setToUnit] = useState("minute");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${config.apiUrl}/api/converter/time`, {
        value: parseFloat(value),
        from_unit: fromUnit,
        to_unit: toUnit,
      });
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
            <option value="second">Seconds</option>
            <option value="minute">Minutes</option>
            <option value="hour">Hours</option>
            <option value="day">Days</option>
            <option value="week">Weeks</option>
            <option value="month">Months</option>
            <option value="year">Years</option>
          </select>
        </div>
        <div>
          <label>To Unit:</label>
          <select value={toUnit} onChange={(e) => setToUnit(e.target.value)}>
            <option value="second">Seconds</option>
            <option value="minute">Minutes</option>
            <option value="hour">Hours</option>
            <option value="day">Days</option>
            <option value="week">Weeks</option>
            <option value="month">Months</option>
            <option value="year">Years</option>
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

export default TimeConverterForm;
