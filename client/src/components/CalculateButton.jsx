import React from 'react';

const CalculateButton = () => {
  return (
    <button
      type='submit'
      className='w-full bg-blue-600 text-white font-semibold py-4 rounded-lg shadow-sm hover:bg-blue-700 active:scale-[0.98] transition-all flex justify-center items-center gap-2'
    >
      Calculate Premium
    </button>
  );
};

export default CalculateButton;
