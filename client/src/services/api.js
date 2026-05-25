import axios from 'axios';

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json'
    }
});

export const calculatePremium = async (data) => {
    try {
        const response = await apiClient.post('/api/v1/premium/calculate', data);
        return response.data;
    } catch (error) {
        console.error("Error calculating premium:", error);
        throw error;
    }
};

export const createPolicy = async (data) => {
    try {
        const response = await apiClient.post('/api/v1/policies', data);
        return response.data;
    } catch (error) {
        console.error("Error creating policy:", error);
        throw error;
    }
};

export const getPolicy = async (policyId) => {
    try {
        const response = await apiClient.get(`/api/v1/policies/${policyId}`);
        return response.data;
    } catch (error) {
        console.error(`Error fetching policy ${policyId}:`, error);
        throw error;
    }
};
