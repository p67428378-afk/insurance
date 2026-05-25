import React from 'react';

const CalculateButton = ({ onClick }) => {
    return (
        <div className='pt-4'>
            <button
                className='w-full bg-blue-600 text-white font-semibold py-4 rounded-lg shadow-sm hover:bg-blue-700 active:scale-[0.98] transition-all flex justify-center items-center gap-2'
                onClick={onClick}
            >
                <span className='material-symbols-outlined'>account_balance_wallet</span>
                Calculate Premium
            </button>
        </div>
    );
};

export default CalculateButton;
