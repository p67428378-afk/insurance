import React from 'react';

const NCBInput = ({ value, onChange }) => {
  return (
    <div className='space-y-2'>
      <label className='text-sm font-medium text-gray-600' htmlFor='ncb'>NCB Percentage (29% - 50%)</label>
      <div className='relative'>
        <input
          className='w-full h-12 px-4 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 transition-all outline-none bg-white text-gray-800'
          id='ncb'
          type='number'
          step='0.01'
          value={value}
          onChange={onChange}
          placeholder='e.g., 0.35'
        />
        <span className='absolute right-3 top-1/2 -translate-y-1/2 text-sm text-gray-500'>Dec</span>
      </div>
      <p className='text-xs text-gray-500'>Enter decimal value between 0.29 and 0.50</p>
    </div>
  );
};

export default NCBInput;
