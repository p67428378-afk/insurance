import React from 'react';

const PremiumDisplay = ({ premium }) => {
    return (
        <div className='mt-4 p-8 bg-blue-50 border border-blue-200 rounded-xl text-center transition-all animate-in fade-in zoom-in duration-500'>
            <p className='text-sm text-blue-600 mb-2 uppercase tracking-widest'>Calculated Premium</p>
            <div className='flex items-center justify-center gap-1'>
                <span className='text-4xl font-bold text-blue-600'>$</span>
                <span className='text-4xl font-bold text-blue-600'>{premium.toFixed(2)}</span>
            </div>
            <p className='mt-4 text-sm text-gray-600 max-w-sm mx-auto'>
                This is an estimated monthly premium based on the provided risk factors and base rates.
            </p>
        </div>
    );
};

export default PremiumDisplay;
