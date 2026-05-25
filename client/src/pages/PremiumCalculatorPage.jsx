import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import CalculatorForm from '../components/CalculatorForm';

const PremiumCalculatorPage = () => {
    return (
        <div className='flex flex-col min-h-screen'>
            <Header />
            <main className='flex-grow pt-24 pb-12 flex flex-col items-center px-4 md:px-8'>
                <div className='w-full max-w-4xl mb-8'>
                    <div className='relative h-48 w-full rounded-xl overflow-hidden shadow-sm mb-8'>
                        <img
                            className='w-full h-full object-cover'
                            src='https://lh3.googleusercontent.com/aida-public/AB6AXuA1HIbWg08s-nuxufyqTTE0PgwMUPQsq_zJeD5G0eq-rA5__VQ7t_v8On2GIqgx4KROGmFWB5BAWwQ_zMHshT9dUgqNTJeCjPUW7DXTRKynQ1DyBSPo2yeFTK7kKRUQua3OxHb_9JV9xHEWlNuP9nr2lovOh2ft-QtszlRPY2wwyCjAhmHZQSdusu-CSIdHWqvMNeoBVVl-p5w7dHzd0iT42zWSg3SnsIItzVOG2inp9L4_pv0tmYTplyCuKsgtXwUD2sgrH6Et8A'
                            alt="A sleek modern SUV driving along a winding coastal highway during the golden hour sunset."
                        />
                        <div className='absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-8'>
                            <h2 className='text-white text-2xl md:text-4xl font-bold'>Get Your Quote in Seconds</h2>
                        </div>
                    </div>
                    <CalculatorForm />
                </div>
                <div className='w-full max-w-4xl grid grid-cols-1 md:grid-cols-3 gap-6 mt-8'>
                    <div className='bg-gray-100 p-6 rounded-lg text-center'>
                        <span className='material-symbols-outlined text-blue-600 text-3xl mb-3'>verified</span>
                        <h4 className='font-semibold text-gray-800 mb-1'>Secure Calculations</h4>
                        <p className='text-sm text-gray-600'>Industry standard encryption for all data.</p>
                    </div>
                    <div className='bg-gray-100 p-6 rounded-lg text-center'>
                        <span className='material-symbols-outlined text-blue-600 text-3xl mb-3'>speed</span>
                        <h4 className='font-semibold text-gray-800 mb-1'>Instant Results</h4>
                        <p className='text-sm text-gray-600'>Get your estimates in real-time instantly.</p>
                    </div>
                    <div className='bg-gray-100 p-6 rounded-lg text-center'>
                        <span className='material-symbols-outlined text-blue-600 text-3xl mb-3'>support_agent</span>
                        <h4 className='font-semibold text-gray-800 mb-1'>Expert Support</h4>
                        <p className='text-sm text-gray-600'>Connect with agents for detailed policy info.</p>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default PremiumCalculatorPage;
