import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import CalculatorForm from './CalculatorForm';
import * as api from '../services/api';

vi.mock('../services/api');

describe('CalculatorForm', () => {
  test('renders the form and calculates premium', async () => {
    api.calculatePremium.mockResolvedValue({ final_premium: 812.50 });

    render(<CalculatorForm />);

    // Check for initial elements
    expect(screen.getByText('Premium Estimation')).toBeInTheDocument();
    expect(screen.getByLabelText(/NCB Percentage/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Vehicle Multiplier/i)).toBeInTheDocument();

    // Simulate user input
    fireEvent.change(screen.getByLabelText(/NCB Percentage/i), { target: { value: '0.35' } });
    fireEvent.change(screen.getByLabelText(/Vehicle Multiplier/i), { target: { value: '2.5' } });

    // Click the calculate button
    fireEvent.click(screen.getByText('Calculate Premium'));

    // Wait for the premium to be displayed
    await waitFor(() => {
      expect(screen.getByText('812.50')).toBeInTheDocument();
    });

    // Check if the API was called with the correct data
    expect(api.calculatePremium).toHaveBeenCalledWith({
      base_rate: 500,
      ncb_percentage: 0.35,
      vehicle_multiplier: 2.5,
    });
  });
});
