import React from 'react';

const Header = () => {
  return (
    <header className='bg-blue-600 text-white fixed w-full top-0 shadow-md z-50'>
      <div className='flex justify-between items-center px-4 md:px-8 py-4 w-full'>
        <div className='flex items-center gap-3'>
          <h1 className='text-xl md:text-2xl font-bold tracking-tight'>Vehicle Insurance Premium Calculator</h1>
        </div>
        <div className='flex items-center gap-4'>
          <button className='hover:bg-blue-700 transition-colors p-2 rounded-full active:scale-95 transition-transform'>
            Help
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
