import React from 'react';

const VehicleMultiplierInput = ({ value, onChange }) => {
    return (
        <div className='space-y-2'>
            <label className='text-sm font-medium text-gray-600' htmlFor='multiplier'>Vehicle Multiplier (1.6x - 9.8x)</label>
            <div className='relative'>
                <input
                    className='w-full h-11 px-4 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 transition-all outline-none bg-white text-gray-800'
                    id='multiplier'
                    placeholder='e.g., 2.5'
                    step='0.1'
                    type='number'
                    value={value}
                    onChange={(e) => onChange(parseFloat(e.target.value))}
                />
                <span className='absolute right-3 top-1/2 -translate-y-1/2 text-sm text-gray-500'>x</span>
            </div>
            <p className='text-xs text-gray-500'>Risk factor based on vehicle model</p>
        </div>
    );
};

export default VehicleMultiplierInput;
