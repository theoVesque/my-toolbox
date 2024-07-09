import React, { useState } from "react";
import axios from "axios";
import config from "../../../../config";

const MassConverterForm = () => {
  const [value, setValue] = useState("");
  const [fromUnit, setFromUnit] = useState("gram");
  const [toUnit, setToUnit] = useState("kilogram");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${config.apiUrl}/api/converter/mass`, {
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
            <option value="gram">Gram</option>
            <option value="kilogram">Kilogram</option>
            <option value="milligram">Milligram</option>
            <option value="tonne">Ton</option>
            <option value="ounce">Ounce</option>
            <option value="yard">Yards</option>
            <option value="foot">Feet</option>
            <option value="pound">Pound</option>
          </select>
        </div>
        <div>
          <label>To Unit:</label>
          <select value={toUnit} onChange={(e) => setToUnit(e.target.value)}>
            <option value="gram">Gram</option>
            <option value="kilogram">Kilogram</option>
            <option value="milligram">Milligram</option>
            <option value="tonne">Ton</option>
            <option value="ounce">Ounce</option>
            <option value="yard">Yards</option>
            <option value="foot">Feet</option>
            <option value="pound">Pound</option>
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

export default MassConverterForm;
