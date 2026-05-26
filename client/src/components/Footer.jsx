import React from 'react';

const Footer = () => {
  return (
    <footer className='bg-gray-800 text-white mt-auto'>
      <div className='flex flex-col md:flex-row justify-between items-center px-4 md:px-8 py-8 w-full gap-6'>
        <div className='flex items-center gap-2'>
          <p className='text-sm font-semibold'>© 2026 Vehicle Insurance. All rights reserved.</p>
        </div>
        <nav className='flex gap-8'>
          <a className='text-sm text-gray-400 hover:text-blue-300 transition-colors' href='#'>Privacy Policy</a>
          <a className='text-sm text-gray-400 hover:text-blue-300 transition-colors' href='#'>Terms of Service</a>
          <a className='text-sm text-gray-400 hover:text-blue-300 transition-colors' href='#'>Contact Support</a>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;
