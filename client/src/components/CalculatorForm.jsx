import React, { useState } from 'react';
import BaseRateDisplay from './BaseRateDisplay';
import NCBInput from './NCBInput';
import VehicleMultiplierInput from './VehicleMultiplierInput';
import CalculateButton from './CalculateButton';
import PremiumDisplay from './PremiumDisplay';
import { calculatePremium } from '../services/api';

const CalculatorForm = () => {
    const [ncb, setNcb] = useState(0.35);
    const [multiplier, setMultiplier] = useState(2.5);
    const [premium, setPremium] = useState(null);
    const [error, setError] = useState('');

    const handleCalculate = async () => {
        try {
            const response = await calculatePremium({ 
                base_rate: 500, 
                ncb_percentage: ncb, 
                vehicle_multiplier: multiplier 
            });
            setPremium(response.final_premium);
            setError('');
        } catch (err) {
            setError('Error calculating premium. Please check your inputs.');
            setPremium(null);
        }
    };

    return (
        <section className='bg-white rounded-xl shadow-md p-8 md:p-12 border border-gray-200'>
            <div className='flex items-center gap-2 mb-8 pb-4 border-b border-gray-200'>
                <span className='material-symbols-outlined text-blue-600'>calculate</span>
                <h3 className='text-lg font-semibold text-gray-800'>Premium Estimation</h3>
            </div>
            <div className='grid grid-cols-1 gap-8'>
                <BaseRateDisplay />
                <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
                    <NCBInput value={ncb} onChange={setNcb} />
                    <VehicleMultiplierInput value={multiplier} onChange={setMultiplier} />
                </div>
                <CalculateButton onClick={handleCalculate} />
                {error && <p className='text-red-500 text-sm mt-4'>{error}</p>}
                {premium !== null && <PremiumDisplay premium={premium} />}
            </div>
        </section>
    );
};

export default CalculatorForm;
