import unittest
from unittest.mock import patch, MagicMock
from modules import ADXDataRetriever 

class TestCreateConnection(unittest.TestCase):

    @patch('modules.KustoClient') 
    @patch('modules.KustoConnectionStringBuilder.with_aad_application_key_authentication')  
    def test_create_connection_success(self, mock_auth, mock_client):
        # Arrange
        mock_auth.return_value = 'connection_string'
        instance = ADXDataRetriever()  
        instance.cluster = 'cluster'
        instance.client_id = 'client_id'
        instance.client_secret = 'client_secret'
        instance.authority_id = 'authority_id'

        # Act
        instance.create_connection()

        # Assert
        mock_auth.assert_called_once_with('cluster', 'client_id', 'client_secret', 'authority_id')
        mock_client.assert_called_once_with('connection_string')
        self.assertIsNotNone(instance.client)

    @patch('modules.KustoClient')  
    @patch('modules.KustoConnectionStringBuilder.with_aad_application_key_authentication')  
    def test_create_connection_failure(self, mock_auth, mock_client):
        # Arrange
        mock_auth.side_effect = Exception("Failed to authenticate")
        instance = ADXDataRetriever()  
        instance.cluster = 'cluster'
        instance.client_id = 'client_id'
        instance.client_secret = 'client_secret'
        instance.authority_id = 'authority_id'

        # Act
        with self.assertRaises(Exception) as context:
            instance.create_connection()

        # Assert
        self.assertTrue('Failed to create connection with error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

