import logging
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from dataclasses import dataclass
from typing import Tuple

# ==========================================
# 1. Configuration & Logging Setup
# ==========================================
@dataclass
class ModelConfig:
    """Hyperparameters and configuration for the Deep Learning model."""
    input_dim: int = 30
    hidden_dim: int = 64
    output_dim: int = 1
    learning_rate: float = 0.001
    batch_size: int = 32
    epochs: int = 50
    test_size: float = 0.2
    random_state: int = 42

# Set up a professional logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# ==========================================
# 2. Data Pipeline (Custom Dataset)
# ==========================================
class TabularDataset(Dataset):
    """Custom PyTorch Dataset for tabular data."""
    def __init__(self, features: torch.Tensor, labels: torch.Tensor):
        self.features = features
        self.labels = labels

    def __len__(self) -> int:
        return len(self.features)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.features[idx], self.labels[idx]

def prepare_data(config: ModelConfig) -> Tuple[DataLoader, DataLoader]:
    """Loads, scales, and splits the dataset into PyTorch DataLoaders."""
    logger.info("Loading and preprocessing dataset...")
    data = load_breast_cancer()
    X, y = data.data, data.target

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.test_size, random_state=config.random_state
    )

    # Standardize features (Crucial for Neural Networks)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Convert to PyTorch Tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

    # Create DataLoaders
    train_loader = DataLoader(
        TabularDataset(X_train_tensor, y_train_tensor), 
        batch_size=config.batch_size, 
        shuffle=True
    )
    test_loader = DataLoader(
        TabularDataset(X_test_tensor, y_test_tensor), 
        batch_size=config.batch_size, 
        shuffle=False
    )
    
    logger.info(f"Data ready. Train size: {len(X_train)}, Test size: {len(X_test)}")
    return train_loader, test_loader

# ==========================================
# 3. Model Architecture
# ==========================================
class DeepNeuralNet(nn.Module):
    """A standard Multi-Layer Perceptron (MLP) for binary classification."""
    def __init__(self, config: ModelConfig):
        super(DeepNeuralNet, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(config.input_dim, config.hidden_dim),
            nn.ReLU(),
            nn.BatchNorm1d(config.hidden_dim),
            nn.Dropout(0.3),
            
            nn.Linear(config.hidden_dim, config.hidden_dim // 2),
            nn.ReLU(),
            nn.BatchNorm1d(config.hidden_dim // 2),
            nn.Dropout(0.3),
            
            nn.Linear(config.hidden_dim // 2, config.output_dim),
            nn.Sigmoid() # Outputs probability between 0 and 1
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)

# ==========================================
# 4. Training Engine
# ==========================================
class Trainer:
    """Handles the training and evaluation loop for the model."""
    def __init__(self, model: nn.Module, train_loader: DataLoader, test_loader: DataLoader, config: ModelConfig):
        self.model = model
        self.train_loader = train_loader
        self.test_loader = test_loader
        self.config = config
        
        # Binary Cross Entropy Loss for binary classification
        self.criterion = nn.BCELoss() 
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.config.learning_rate)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def train(self):
        """Executes the training loop."""
        logger.info(f"Starting training on device: {self.device}")
        
        for epoch in range(self.config.epochs):
            self.model.train()
            total_loss = 0.0
            
            for batch_X, batch_y in self.train_loader:
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)
                
                # Forward pass
                predictions = self.model(batch_X)
                loss = self.criterion(predictions, batch_y)
                
                # Backward pass and optimization
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                
                total_loss += loss.item()
                
            avg_loss = total_loss / len(self.train_loader)
            
            # Log progress every 10 epochs
            if (epoch + 1) % 10 == 0:
                logger.info(f"Epoch [{epoch + 1}/{self.config.epochs}] - Loss: {avg_loss:.4f}")

    def evaluate(self):
        """Evaluates model performance on the test set."""
        logger.info("Starting evaluation...")
        self.model.eval()
        correct = 0
        total = 0
        
        with torch.no_grad(): # Disable gradient tracking for evaluation
            for batch_X, batch_y in self.test_loader:
                batch_X, batch_y = batch_X.to(self.device), batch_y.to(self.device)
                
                outputs = self.model(batch_X)
                predicted = (outputs > 0.5).float() # Convert probabilities to 0 or 1
                
                total += batch_y.size(0)
                correct += (predicted == batch_y).sum().item()
                
        accuracy = (correct / total) * 100
        logger.info(f"Evaluation Complete. Test Accuracy: {accuracy:.2f}%")

# ==========================================
# 5. Execution Block
# ==========================================
if __name__ == "__main__":
    # 1. Initialize config
    config = ModelConfig()
    
    # 2. Prepare data
    train_loader, test_loader = prepare_data(config)
    
    # 3. Initialize model
    model = DeepNeuralNet(config)
    
    # 4. Train and Evaluate
    trainer = Trainer(model, train_loader, test_loader, config)
    trainer.train()
    trainer.evaluate()