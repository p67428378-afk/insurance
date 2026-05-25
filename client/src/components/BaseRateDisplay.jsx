import React from 'react';

const BaseRateDisplay = () => {
    return (
        <div className='bg-gray-50 p-4 rounded-lg flex justify-between items-center'>
            <div>
                <p className='text-xs text-gray-500 uppercase tracking-wider'>Base Rate</p>
                <p className='text-2xl font-semibold text-gray-800'>$500</p>
            </div>
            <span className='material-symbols-outlined text-gray-400'>info</span>
        </div>
    );
};

export default BaseRateDisplay;
