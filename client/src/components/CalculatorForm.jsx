import React, { useState } from 'react';
import BaseRateDisplay from './BaseRateDisplay';
import NCBInput from './NCBInput';
import VehicleMultiplierInput from './VehicleMultiplierInput';
import CalculateButton from './CalculateButton';

const CalculatorForm = ({ onCalculate }) => {
  const [ncb, setNcb] = useState(0.35);
  const [multiplier, setMultiplier] = useState(2.5);

  const handleSubmit = (e) => {
    e.preventDefault();
    onCalculate({ 
      base_rate: 500, 
      ncb_percentage: parseFloat(ncb),
      vehicle_multiplier: parseFloat(multiplier) 
    });
  };

  return (
    <form onSubmit={handleSubmit} className='grid grid-cols-1 gap-8'>
      <BaseRateDisplay />
      <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
        <NCBInput value={ncb} onChange={(e) => setNcb(e.target.value)} />
        <VehicleMultiplierInput value={multiplier} onChange={(e) => setMultiplier(e.target.value)} />
      </div>
      <div className='pt-4'>
        <CalculateButton />
      </div>
    </form>
  );
};

export default CalculatorForm;
