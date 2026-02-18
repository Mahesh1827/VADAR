mkdir -p models
cd models

git clone https://github.com/facebookresearch/sam2.git && cd sam2
pip install -e .
cd checkpoints && \
./download_ckpts.sh && \
cd ../..

pip install 'git+https://github.com/apple/ml-depth-pro.git'
cd ..

pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121 --force-reinstall

pip install -r requirements.txt