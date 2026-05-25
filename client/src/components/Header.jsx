import React from 'react';

const Header = () => {
    return (
        <header className='bg-primary text-on-primary fixed w-full shadow-md z-50'>
            <div className='flex justify-between items-center px-4 md:px-8 py-4 w-full'>
                <div className='flex items-center gap-3'>
                    <span className='material-symbols-outlined'>security</span>
                    <h1 className='text-xl md:text-2xl font-semibold tracking-tight'>Vehicle Insurance Premium Calculator</h1>
                </div>
                <div className='flex items-center gap-4'>
                    <button className='material-symbols-outlined hover:bg-primary-container/10 p-2 rounded-full'>help_outline</button>
                </div>
            </div>
        </header>
    );
};

export default Header;
