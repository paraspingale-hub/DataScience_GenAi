import tensorflow as tf

# 1. Check TensorFlow Version
print(f"TensorFlow Version: {tf.__version__}")

# 2. Check for GPU (Metal) Access
gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
    print(f"✅ GPU is available: {gpu_devices}")
else:
    print("❌ GPU is NOT available. Using CPU instead.")

# 3. Run a simple calculation
print("\nRunning a quick math test...")
a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
c = tf.matmul(a, b)

print("Calculation Result:")
print(c.numpy())