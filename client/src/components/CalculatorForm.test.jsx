import { render, screen, fireEvent } from '@testing-library/react';
import CalculatorForm from './CalculatorForm';
import { describe, it, expect, vi } from 'vitest';

describe('CalculatorForm', () => {
  it('should call onCalculate with the correct data on submit', () => {
    const onCalculate = vi.fn();
    render(<CalculatorForm onCalculate={onCalculate} />);

    const ncbInput = screen.getByLabelText(/NCB Percentage/i);
    const multiplierInput = screen.getByLabelText(/Vehicle Multiplier/i);
    const calculateButton = screen.getByText(/Calculate Premium/i);

    fireEvent.change(ncbInput, { target: { value: '0.4' } });
    fireEvent.change(multiplierInput, { target: { value: '3.0' } });

    fireEvent.click(calculateButton);

    expect(onCalculate).toHaveBeenCalledWith({
      base_rate: 500,
      ncb_percentage: 0.4,
      vehicle_multiplier: 3.0,
    });
  });
});
