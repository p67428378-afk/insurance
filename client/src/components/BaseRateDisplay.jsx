import React from 'react';

const BaseRateDisplay = () => {
  return (
    <div className='bg-gray-100 p-4 rounded-lg flex justify-between items-center'>
      <div>
        <p className='text-xs text-gray-500 uppercase tracking-wider'>Base Rate</p>
        <p className='text-2xl font-bold text-gray-800'>$500</p>
      </div>
      <span className='text-gray-500'>Info</span>
    </div>
  );
};

export default BaseRateDisplay;
