import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import CalculatorForm from '../components/CalculatorForm';
import PremiumDisplay from '../components/PremiumDisplay';
import { calculatePremium } from '../services/api';

const PremiumCalculatorPage = () => {
  const [premium, setPremium] = useState(null);
  const [error, setError] = useState(null);

  const handleCalculate = async (data) => {
    try {
      const result = await calculatePremium(data);
      setPremium(result.final_premium);
      setError(null);
    } catch (err) {
      setError('Failed to calculate premium');
      setPremium(null);
    }
  };

  return (
    <div className='flex flex-col min-h-screen'>
      <Header />
      <main className='flex-grow pt-24 pb-12 flex flex-col items-center px-4 md:px-8'>
        <div className='w-full max-w-4xl mb-8'>
          <div className='relative h-48 w-full rounded-xl overflow-hidden shadow-sm mb-8'>
            <img
              className='w-full h-full object-cover'
              src='https://lh3.googleusercontent.com/aida-public/AB6AXuA1HIbWg08s-nuxufyqTTE0PgwMUPQsq_zJeD5G0eq-rA5__VQ7t_v8On2GIqgx4KROGmFWB5BAWwQ_zMHshT9dUgqNTJeCjPUW7DXTRKynQ1DyBSPo2yeFTK7kKRUQua3OxHb_9JV9xHEWlNuP9nr2lovOh2ft-QtszlRPY2wwyCjAhmHZQSdusu-CSIdHWqvMNeoBVVl-p5w7dHzd0iT42zWSg3SnsIItzVOG2inp9L4_pv0tmYTplyCuKsgtXwUD2sgrH6Et8A'
              alt='A sleek modern SUV driving along a winding coastal highway during the golden hour sunset.'
            />
            <div className='absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-8'>
              <h2 className='text-white text-2xl md:text-4xl font-bold'>Get Your Quote in Seconds</h2>
            </div>
          </div>
          <section className='bg-white rounded-xl shadow-md p-8 md:p-12 border'>
            <CalculatorForm onCalculate={handleCalculate} />
            {premium && <PremiumDisplay premium={premium} />}
            {error && <p className='mt-4 text-red-500'>{error}</p>}
          </section>
        </div>
        <div className='w-full max-w-4xl grid grid-cols-1 md:grid-cols-3 gap-6 mt-8'>
          <div className='bg-gray-100 p-6 rounded-lg text-center'>
            <h4 className='font-semibold text-lg mb-1'>Secure Calculations</h4>
            <p className='text-sm text-gray-600'>Industry standard encryption for all data.</p>
          </div>
          <div className='bg-gray-100 p-6 rounded-lg text-center'>
            <h4 className='font-semibold text-lg mb-1'>Instant Results</h4>
            <p className='text-sm text-gray-600'>Get your estimates in real-time instantly.</p>
          </div>
          <div className='bg-gray-100 p-6 rounded-lg text-center'>
            <h4 className='font-semibold text-lg mb-1'>Expert Support</h4>
            <p className='text-sm text-gray-600'>Connect with agents for detailed policy info.</p>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default PremiumCalculatorPage;
