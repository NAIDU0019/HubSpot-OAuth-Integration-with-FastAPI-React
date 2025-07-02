import { useState } from 'react';
import {
  Box,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
  Paper,
  Chip,
} from '@mui/material';
import axios from 'axios';

const endpointMapping = {
  Notion: 'notion',
  Airtable: 'airtable',
  Hubspot: 'hubspot',
};

export const DataForm = ({ integrationType, credentials }) => {
  const [loadedData, setLoadedData] = useState([]);
  const [error, setError] = useState(null);

  const endpoint = endpointMapping[integrationType];

  const handleLoad = async () => {
    try {
      setError(null);
      const formData = new FormData();
      formData.append('credentials', typeof credentials === 'string' ? credentials : JSON.stringify(credentials));
      const response = await axios.post(`http://localhost:8000/integrations/${endpoint}/load`, formData);
      setLoadedData(response.data || []);
    } catch (e) {
      console.error(e);
      setError(e?.response?.data?.detail || 'Error loading data');
    }
  };

  const handleClear = () => {
    setLoadedData([]);
    setError(null);
  };

  return (
    <Box
      sx={{
        width: '100%',
        mt: 4,
        p: 4,
        borderRadius: '16px',
        background: 'linear-gradient(to right, #e0f7fa, #fce4ec)',
        boxShadow: 3,
      }}
    >
      <Typography variant="h5" sx={{ fontWeight: 'bold', mb: 2, color: '#4a148c' }}>
        🔍 Loaded {integrationType} Data
      </Typography>

      <Box sx={{ mb: 2 }}>
        <Button
          variant="contained"
          color="secondary"
          onClick={handleLoad}
          sx={{ mr: 2, borderRadius: '30px', fontWeight: 'bold' }}
        >
          🚀 Load Data
        </Button>
        <Button
          variant="outlined"
          color="error"
          onClick={handleClear}
          sx={{ borderRadius: '30px', fontWeight: 'bold' }}
        >
          ❌ Clear Data
        </Button>
      </Box>

      {error && (
        <Typography color="error" sx={{ mt: 1 }}>
          ⚠️ {error}
        </Typography>
      )}

      {loadedData.length > 0 ? (
        <TableContainer component={Paper} elevation={4} sx={{ borderRadius: 3 }}>
          <Table>
            <TableHead sx={{ backgroundColor: '#9c27b0' }}>
              <TableRow>
                <TableCell sx={{ color: '#fff', fontWeight: 'bold' }}>🆔 ID</TableCell>
                <TableCell sx={{ color: '#fff', fontWeight: 'bold' }}>👤 Name</TableCell>
                <TableCell sx={{ color: '#fff', fontWeight: 'bold' }}>📧 Email</TableCell>
                <TableCell sx={{ color: '#fff', fontWeight: 'bold' }}>📅 Created At</TableCell>
                <TableCell sx={{ color: '#fff', fontWeight: 'bold' }}>Status</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {loadedData.map((item, index) => (
                <TableRow
                  key={item.id}
                  sx={{
                    backgroundColor: index % 2 === 0 ? '#f3e5f5' : '#ede7f6',
                    '&:hover': { backgroundColor: '#d1c4e9' },
                  }}
                >
                  <TableCell>{item.id}</TableCell>
                  <TableCell>{item.name}</TableCell>
                  <TableCell>{item.email}</TableCell>
                  <TableCell>{item.extra_params?.createdate || '—'}</TableCell>
                  <TableCell>
                    <Chip
                      label="Active"
                      color="success"
                      size="small"
                      sx={{ fontWeight: 'bold' }}
                    />
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      ) : (
        <Typography sx={{ mt: 3, fontStyle: 'italic' }}>No data loaded yet.</Typography>
      )}
    </Box>
  );
};
